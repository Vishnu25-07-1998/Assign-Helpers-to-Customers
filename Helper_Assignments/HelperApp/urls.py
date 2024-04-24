from django.urls import path
from . import views

urlpatterns = [  

    path('', views.home, name='home'),        
    path('AddHelper/', views.AddHelper, name='AddHelper'),
    path('HelperDetails/', views.HelperDetails, name='HelperDetails'),

    path('AddCustomer/', views.AddCustomer, name='AddCustomer'),
    path('CustomerDetails/', views.CustomerDetails, name='CustomerDetails'),

    path('AssignHelper/', views.AssignHelper, name='AssignHelper'),
    path('assigned-helper/<str:customer_name>/<str:helper_name>/<str:skill>/', views.AssignedHelper, name='assigned_helper'),

    
]