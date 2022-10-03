from knox import views as knox_views
from .views import loginAPI
from django.urls import path

app_name='accounts'
urlpatterns = [
    path('login/', loginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]