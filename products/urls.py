from django.urls import path
from products.apps import ProductsConfig
from products.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    VersionDetailView, VersionDeleteView

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductListView.as_view, name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path("version_detail/<int:pk>/", VersionDetailView.as_view(), name="version_detail"),
    path("version_delete/<int:pk>/", VersionDeleteView.as_view(), name="version_delete"),
]
