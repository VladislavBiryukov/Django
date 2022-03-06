import random

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Contact, Product, ProductCategory


def main(request):
    title = "главная"
    products = Product.objects.filter(is_active=True, category__is_active=True)[:3]
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)





def products(request, pk=None, page=1):
    title = "продукты"
    links_menu = ProductCategory.objects.filter(is_active=True)


            category = {"pk": 0, "name": "все"}
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by("price")
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                "price"
            )

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            "title": title,
            "links_menu": links_menu,
            "category": category,
            "products": products_paginator,
            "media_url": settings.MEDIA_URL,

    content = {
        "title": title,
        "links_menu": links_menu,
        "same_products": same_products,
        "media_url": settings.MEDIA_URL,

        "hot_product": hot_product,
    }
    return render(request, "mainapp/products.html", content)


def product(request, pk):
    title = "продукты"
    content = {
        "title": title,
        "links_menu": ProductCategory.objects.filter(is_active=True),
        "product": get_object_or_404(Product, pk=pk),

        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/product.html", content)


def contact(request):
    title = "о нас"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
