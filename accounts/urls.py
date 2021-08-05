from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('customer',views.customer,name='customer'),

    path('course/add/', views.CustomerCreateView.as_view(), name='customer-add'),
    path('customer/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete')
    
]
