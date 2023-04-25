from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks_index, name='tasks_index'),

    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),

#    path('search/', views.task_search, name='task_search'),

    path('priority/new/', views.priority_new, name='priority_new'),
]

