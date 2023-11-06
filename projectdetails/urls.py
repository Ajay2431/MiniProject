from django.urls import path

from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('add/', views.ProjectCreateView.as_view(), name='project_add'),
    path('<uuid:uuid>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('<uuid:uuid>/del/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('<uuid:uuid>/coedit/', views.ProjectCoordinatorUpdateView.as_view(), name='project_coedit'),
]   
