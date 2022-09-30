from django.shortcuts import render,redirect

# Create your views here.
from .models import ProductsData
def index(request):
    products=ProductsData.objects.all()
    return render(request,'index.html', {'products':products})
def add_products(request):
    if request.method=="GET":
        return render(request,'add_products.html')
    else:
        ProductsData(
        product_name=request.POST.get('pname'),
        product_details=request.POST.get('pdetails'),
        product_price=request.POST.get('pprice'),
        product_loc=request.POST.get('plocation')
        ).save()
        return redirect('index')
def update_product(request,id):
    product=ProductsData.objects.get(id=id)
    if request.method=="GET":
        return render(request,'update_product.html',{'product':product})
    else:
        product.product_name=request.POST.get('pname')
        product.product_details=request.POST.get('pdetails')
        product.product_price=request.POST.get('pprice')
        product.product_loc=request.POST.get('plocation')
        product.save()
        return redirect('index')

def delete_product(request,id):
    product=ProductsData.objects.get(id=id)
    product.delete()
    return redirect('index')
