from django.shortcuts import redirect, render,get_object_or_404
from .models import Products,CartModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    trend = False
    offer = False
    count_ = 0
    all_products = Products.objects.all()

    # Cart count for authenticated users
    if request.user.is_authenticated:
        count_ = CartModel.objects.filter(host=request.user).count()

    # Category list preparation from all products
    cat = list(set(product.p_category for product in all_products))

    # Search query
    if 'q' in request.GET:
        q = request.GET['q']
        all_products = Products.objects.filter(
            Q(p_name__icontains=q) |
            Q(p_desc__icontains=q) |
            Q(p_category__icontains=q)
        )
        if not all_products:
            messages.warning(request, 'No Match Found !!')

    # Trending filter
    elif 't' in request.GET:
        trend = True
        all_products = Products.objects.filter(p_trending=1)

    # Offer filter
    elif 'offer' in request.GET:
        offer = True
        all_products = Products.objects.filter(p_offer=1)

    # Category filter
    elif 'cat_form' in request.GET:
        cat_form = request.GET['cat_form']
        all_products = Products.objects.filter(p_category=cat_form.lower())

    return render(request, 'home.html', {
        'count_': count_,
        'all_products': all_products,
        'trend': trend,
        'offer': offer,
        'cat': cat
    })

@login_required(login_url='login_')
def cart(request):
    cart_nav=True

    cart_data=CartModel.objects.filter(host=request.user)

    Totalpay=0
    for i in cart_data:
        # print(i.totalamount)
        Totalpay+=i.totalamount
    # print(Totalpay)

  
    messages.add_message(request,messages.SUCCESS,'login successfully done !! welcome to shopsphere')

    return render(request,'cart.html',{'cart_nav':cart_nav,'cart_data':cart_data,'Totalpay':Totalpay})

@login_required(login_url='login_')
def addtocart(request, pk):
    product = get_object_or_404(Products, id=pk)

    try:
        cart_item = CartModel.objects.get(p_name=product.p_name, host=request.user)
        cart_item.p_quatity += 1
        cart_item.totalamount += product.p_price
        cart_item.save()
    except CartModel.DoesNotExist:
        CartModel.objects.create(
            p_category=product.p_category,
            p_name=product.p_name,
            p_desc=product.p_desc,
            p_price=product.p_price,
            totalamount=product.p_price,
            host=request.user
        )

    return render(request, 'addtocart.html', {'product': product})



def removecartitem(request,pk):

    item=CartModel.objects.get(id=pk)
    item.delete()
    return redirect('cart')


def support(request):


    return render(request,'support.html')