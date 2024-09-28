from django.urls import path, include

urlpatterns = [
    path("v1/ecom_user/", include('ecom_app.urls'), name="ecom_app"),
]
