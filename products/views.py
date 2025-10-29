from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product
from django.core.paginator import Paginator

def product_list_view(request):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'object_list': page_obj.object_list,
        'total_count': products.count(),
    }
    return render(request, "products/product_list.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/products/')

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def dynamic_look_up(request, id):
    obj = get_object_or_404(Product, id = id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoestNotExist:
        raise Http404
    
    context = {
        "object" : obj
    }
    return render (request, "products/product_detail.html",context)

def render_initial_data(request):
    initial_data = {
        'username':"My good",
        'description' :"this"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance =obj)
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/products/')
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
    
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id = id)
    if request.method == 'POST':
        obj.delete()

    context = {
        "object": obj
    }
    return render (request, "products/product_delete.html", context)