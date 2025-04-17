from rest_framework import viewsets, permissions
from rest_framework.request import Request

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django_ratelimit.decorators import ratelimit


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

    # Limit to 5 requests per minute
    @method_decorator(ratelimit(key="ip", rate="5/s", block=True))
    @method_decorator(cache_page(60 * 15, key_prefix="book_list"))
    def list(self, request: Request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Limit to 5 requests per minute
    @method_decorator(ratelimit(key="ip", rate="3/s", block=True))
    @method_decorator(cache_page(60 * 15, key_prefix="book_detail"))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(ratelimit(key='ip', rate='2/s', block=True))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


def ratelimit_exceeded_view(request, exception=None):
    return JsonResponse({"detail": "Rate limit exceeded"})
