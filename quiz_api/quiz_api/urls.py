from .views import RegisterAPI, ScoreDetailRetreiveUpdateDestroy
from django.contrib import admin
from django.urls import path, include
from quiz_api.views import ScoreListCreate, ScoreRetreiveUpdateDestroy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('account/',include('accounts.urls',namespace='accounts')),
    #add and get score api url
    path('api/listcreate/score/',ScoreListCreate.as_view(), name='score-create'),
    #crud score by id
    path('api/update/score/<int:id>/', ScoreRetreiveUpdateDestroy.as_view(), name='score-update'),
    #crud player by id
    path('api/update/score/player/<int:player>/', ScoreDetailRetreiveUpdateDestroy.as_view(), name='detail-update'),
]
