from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import ProductDetailView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name


urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    # path('product/<int:pk>/', views.product, name='product')
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
]
