from django.urls import path
from .apps import CatalogConfig
from .views import ProductDetailView, ProductListView, contacts
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
]
