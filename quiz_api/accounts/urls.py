from knox import views as knox_views
from .views import LoginAPI

from quiz_api.views import ScoreListCreate, ScoreRetreiveUpdateDestroy
from django.urls import path

app_name='accounts'
urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
]