from .views import RegisterAPI
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('account/',include('accounts.urls',namespace='accounts')),
]
