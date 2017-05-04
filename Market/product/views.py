from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Collection
from django.http import Http404
from rest_framework import routers, serializers, viewsets
from .serializers import ProductSerializer, CollectionSerializer
from .forms import ProductAddForm

# Create your views here.


def retrieve_product(request, title):
    queryset = get_object_or_404(Product, title=title)
    template = 'Retrieve_Product.html'
    context = {
        'queryset': queryset,
        'user': request.user,
        'title': 'Retrieve',
    }

    return render(request, template, context)


def create_product(request):

    form = ProductAddForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.User = request.user
        instance.save()
        return redirect('/admin')

    template = 'Create_Product.html'
    context = {
        'form': form,
        'user': request.user,
        'title': 'Create',
    }

    return render(request, template, context)


class CollectionViewSet(viewsets.ModelViewSet):

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def collection_view(request):

    name = request.user
    product = Product.objects.all()
    template = "Products.html"
    context = {
        'object': product,
        'username': name,
        'message': 'Hello'

    }

    return render(request, template, context)


def detail_view(request, object_id=None):

    name = request.user
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        'object': product,
        'username': name,
        'message': 'Hello'

    }

    return render(request, template, context)


def list_view(request):
    product = Product.objects.all()
    template = "list_view.html"
    context = {
        "product": product,
    }

    return render(request, template, context)

#def register(request):

