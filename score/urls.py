from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('score/', views.score_view, name='score-view'),
    path('history/', views.history_view),
    path('history/<int:id>', views.historyItem_view, name='history-item'),
    path('post-data/', views.post_data, name='post-data'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('update-score/', views.update_score, name='update-score'),
    path('export-report/', views.export_report, name='export-report'),
]
