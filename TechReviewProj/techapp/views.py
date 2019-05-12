from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TechType, TechProduct, TechReview
 from .forms import TechProductForm, TechReviewForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'techapp/index.html')

def getTypes(request):
    product_list=TechProduct.objects.all()
    return render(request, 'techapp/types.html', {'product_list': product_list} )

def getProducts(request):
    product_list=TechProduct.objects.all()
    return render(request, 'techapp/products.html', {'product_list': product_list} )

def productdetail(request, id):
    prod=get_object_or_404(Product, pk=id)
    reviewcount=TechReview.objects.filter(product=id).count
    reviews=TechReview.objects.filter(product=id)
    context={
        'prod' : prod,
        'reviewcount' : reviewcount,
        'reviews' : reviews,
    }
    return render(request, 'techapp/productdetail.html', context=context)

def producttechapp(request, prod_id):
    prodreviews=TechReview.objects.filter(product=prod_id)
    return render(request, 'techapp/productreview.html', {'prodtechapp': prodreveiws})
'''
@login_required
def newProduct(request):
    form=TechProductForm

    if request.method=='POST':
        form=TechProductForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=TechProductForm()
    else:
        form=TechProductForm()
    return render(request, 'techapp/newproduct.html', {'form': form})

@login_required
def newReview(request):
    form=TechReviewForm

    if request.method=='POST':
        form=TechReviewForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=TechReviewForm()
    else:
        form=TechReviewForm()
    return render(request, 'techapp/newreview.html', {'form': form})

def logoutmessage(request):
    return render(request, 'techapp/logoutmessage.html')

def loginmessage(request):
    return render(request, 'techapp/loginmessage.html')
    '''
