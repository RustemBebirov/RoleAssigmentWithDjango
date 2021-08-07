from django.urls import path
from django.urls import path, re_path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('customer/',views.customer,name='customer'),
    path('editor/',views.editor,name='editor'),


    path('customer/add/', views.createCustomer, name='customer-add'),
    path('update_customer/<str:pk>/', views.updateCustomer, name="customer-update"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="customer-delete"),
    # path('customer/add/', views.CustomerCreateView.as_view(), name='customer-add'),
    # path('customer/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer-update'),
    # path('customer/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),
    
    path('editor/add/', views.createEditor, name='editor-add'),
    path('update_editor/<str:pk>/', views.updateEditor, name="editor-update"),
    path('update_admin/<str:pk>/', views.updateAdmin, name="admin-update"),
    path('delete_editor/<str:pk>/', views.deleteEditor, name="editor-delete"),
    
]
