from django.urls import path
from . import views 

urlpatterns = [
    
    path('hello/', views.hello_world),
    path('about/', views.about_page),
    path('', views.home_page),
    path('all-employee', views.all_employee),
    path('remove-employee', views.remove_employee),
    path('add-employee', views.add_employee),
    path('filter-employee', views.filter_employee),
]

