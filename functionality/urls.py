from django.urls import path
from . import views

urlpatterns = [
    path('user/stats/', views.user_stats, name='user-stats'),
    path('questions/filter/', views.filter_questions, name='filter-questions'),
]
