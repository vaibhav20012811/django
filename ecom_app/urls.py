from django.urls import path
from ecom_app import views

urlpatterns = [
    path("", views.EcomUserAPIView.as_view(), name="ecom_user"),
]
