from .views import ProductListView , ProductDetail, CategoryDetail, CategoryListView, FileDetail, FileListView
from django.urls import path

urlpatterns = [

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('products/<int:product_id>/files/', FileListView.as_view(), name='file-list'),
    path('products/<int:product_id>/files/<int:pk>/', FileDetail.as_view(), name='file-detail')
]