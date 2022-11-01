from django.urls import path
from . import views
urlpatterns = [
    path('', views.score_view),
    path('history/', views.history_view),
    path('history/<int:id>', views.historyItem_view, name='history-item'),
    path('login/', views.Login.as_view(), name='login')
]
