from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .models import Book, Borrow, Return
from .pagination import CustomPageNumberPagination
from .serializers import BookSerializer, BorrowSerializer, ReturnSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CustomPageNumberPagination


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data["user"] = request.user.id

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
        except ValueError as e:  # Handle 'No copies available' error
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ReturnViewSet(viewsets.ModelViewSet):
    queryset = Return.objects.all()
    serializer_class = ReturnSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        borrow_id = mutable_data.get("borrow")

        try:
            borrow = Borrow.objects.get(
                id=borrow_id, user=request.user, returned=False)
        except Borrow.DoesNotExist:
            return Response({"error": "Invalid borrow record or book already returned."},
                            status=status.HTTP_400_BAD_REQUEST)

        borrow.returned = True
        borrow.book.available_copies += 1
        borrow.book.save()
        borrow.save()

        mutable_data["borrow"] = borrow.id

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
