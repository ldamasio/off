from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('products/', views.ItemList.as_view(), name='view_all_items'),
    path('products/<int:pk>/', views.ViewItem.as_view(), name='view_items'),
    path('products/<int:pk>/', views.update_items, name='update-items'),
    path('products/<int:pk>/', views.delete_items, name='delete-items'),
]
