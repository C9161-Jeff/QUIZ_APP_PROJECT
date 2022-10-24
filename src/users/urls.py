from django.urls import path
from .views import RegisterSerializer, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register")
]