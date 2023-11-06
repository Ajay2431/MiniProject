from django.urls import path

from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', views.SeminarListView.as_view(), name='seminar_list'),
    #path('c/', views.SeminarCoordinatorListView.as_view(), name='seminar_colist'),
    path('add/', views.SeminarCreateView.as_view(), name='seminar_add'),
    path('<uuid:uuid>/edit/', views.SeminarUpdateView.as_view(), name='seminar_edit'),
    path('<uuid:uuid>/del/', views.SeminarDeleteView.as_view(), name='seminar_delete'),
    #path('<uuid:uuid>/coedit/', views.SeminarCoordinatorUpdateView.as_view(), name='seminar_coedit'),
]   
