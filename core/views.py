from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status

from django.utils.timezone import now

from datetime import timedelta

from .models import Book
from .serializers import BookSerializer
from .pagination import CustomPageNumberPagination


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
        

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-published_date")
    serializer_class = BookSerializer
    lookup_field = "slug"
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CustomPageNumberPagination

