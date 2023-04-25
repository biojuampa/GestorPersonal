from django.urls import path
from . import views


urlpatterns = [
    path('', views.agenda_index, name='agenda_index'),
    
    path('contact/new/', views.contact_new, name='contact_new'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/<int:pk>/remove/', views.contact_remove, name='contact_remove'),
    path('contact/search/', views.contact_search, name='contact_search'),
    
    path('zipcode/new/', views.zipcode_new, name='zipcode_new'),
    path('zipcode/<int:pk>/', views.zipcode_new, name='zipcode_detail'),
    path('zipcode/<int:pk>/edit/', views.zipcode_new, name='zipcode_edit'),
    
    path('location/new/', views.location_new, name='location_new'),
    path('job/new/', views.job_new, name='job_new'),
    path('group/new/', views.group_new, name='group_new'),
]

