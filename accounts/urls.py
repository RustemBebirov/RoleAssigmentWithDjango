from django.urls import path
from . import views

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
    path('delete_editor/<str:pk>/', views.deleteEditor, name="editor-delete"),
    # path('editor/add/', views.EditorCreateView.as_view(), name='editor-add'),
    # path('editor/<int:pk>/', views.EditorUpdateView.as_view(), name='editor-update'),
    # path('editor/<int:pk>/delete/', views.EditorDeleteView.as_view(), name='editor-delete')
]
