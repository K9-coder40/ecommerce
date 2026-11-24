from django.shortcuts import redirect, render
from .forms import ProductForm,RegisterForm
from django.shortcuts import get_object_or_404, redirect,render
from .models import Product
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products':products})
#r-read-fetch records from db
@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff,login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'admin-dashboard.html', {'products': products})
#crud-c-create-add a record
@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff,login_url='login')
def add_product(request):
  if request.method=='POST':
    Form=ProductForm(request.POST,request.FILES)
    if Form.is_valid():
      Form.save()
      return redirect('products')
  else:
      Form=ProductForm()
  return render(request, 'add_product.html', {'form':Form})

#r-reading an existing record

#d-deleting an existing record
@user_passes_test(lambda u: u.is_staff,login_url='login')
@login_required(login_url='login')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products')

#u-update an existing record
@user_passes_test(lambda u: u.is_staff,login_url='login')
@login_required(login_url='login')
def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'add_product.html', {'form': form})

# register user
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# login and logout user
def _style_auth_form(form):
    for field in form.fields.values():
        existing = field.widget.attrs.get('class', '')
        if 'form-control' not in existing:
            field.widget.attrs['class'] = f"{existing} form-control".strip()
    return form
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        _style_auth_form(form)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('products')
            else:
                return redirect('user_dashboard')

            
            
    else:
        form = _style_auth_form(AuthenticationForm())
    return render(request, 'login.html', {'form': form})
@login_required(login_url='login')

def user_dashboard(request):
    products = Product.objects.all()
    return render(request, 'users/user_dashboard.html',{'products':products})

def logout_user(request):
    logout(request)
    return redirect('login')

  