from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r"projects", ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/register/", RegisterView.as_view(), name="auth_register"),
    path("auth/login/", LoginView.as_view(), name="auth_login"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
