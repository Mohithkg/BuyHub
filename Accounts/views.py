from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import auth
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Carts.models import CartItem, Cart
from Carts.views import _cart_id
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name,email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Successful.')
            return redirect('register')
    else:
        form = RegistrationForm()
    context={
        'form': form,
    }
    return render(request,'accounts/register.html', context)



def login(request):
    if request.method=="POST":
        email= request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)
                    # Getting product variation by cart id
                    product_variation=[]
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))

                    #Get the cart items from the user to access his product variation
                    cart_item = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)

                    for pr in product_variation:
                        if pr in ex_var_list:
                            index= ex_var_list.index(pr)
                            item_id=id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity +=1
                            item.user = user
                            item.save()

                        else:
                            cart_item= CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()

            except:
                pass

            auth.login(request, user)
            #messages.success(request, "You are now logged in.")
            return redirect('dashboard')

        else:
            messages.error(request, "Invalid login Credentials")
            return redirect('login')

    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,"You are logged out.")
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def forgotPassword(request):
    return render(request, 'accounts/forgotPassword.html')