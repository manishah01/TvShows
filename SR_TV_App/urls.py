from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new',views.show_form),
    path('shows/add', views.add_show),
    path('shows/<int:id>',views.this_show),
    path('shows/<int:id>/edit', views.update_show_form),
    path('shows/<int:id>/update', views.submit_update),
    path('shows/delete/<int:id>',views.delete_show),
]