from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import BookViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path('api/token/', views.obtain_auth_token),
    path("", RedirectView.as_view(url="/api/", permanent=True)),
]
