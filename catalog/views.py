from django.shortcuts import render

from catalog.models import Product, Version
from django.views.generic import DetailView


def index(request):
    product_list = Product.objects.all()
    context_prod = {
        'object_list_prod': product_list
    }
    return render(request, 'catalog/index.html', context_prod)


def contacts(request):
    return render(request, 'catalog/contacts.html')


# def product(request):
#     product_list = Product.objects.all()
#     context_prod = {
#         'object_list_prod': product_list
#     }
#     return render(request, 'catalog/product.html', context_prod)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Version.objects.filter(product=self.kwargs['pk'])
        return context
