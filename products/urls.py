from django.urls import path 
from .views import *

app_name = 'product'
urlpatterns = [
    path('', product_list_view, name = 'product-list'),
    path('create/', product_create_view, name = 'product-list'),
    path('<int:id>/', dynamic_look_up, name = 'product-detail'),
    path('<int:id>/delete/', product_delete_view, name = 'product-delete'),
    path('<int:id>/update/', product_update_view, name = 'product-update')
]
