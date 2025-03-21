from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path, include

from .views import BookViewSet, BorrowViewSet, ReturnViewSet


router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"borrows", BorrowViewSet)
router.register(r"returns", ReturnViewSet)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", obtain_auth_token),
    path("api/", include(router.urls)),
]
