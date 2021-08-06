from django import http
from django.forms.forms import Form
from django.http.response import HttpResponse
from accounts.models import  Customer
from django.shortcuts import redirect, render
from .froms import ChangeEmail, CustomerForm, Login, UserForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .decorators import allowed_users, unauthenticated_user,admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.encoding import force_text 
from accounts.tasks import send_confirmation_mail 
from accounts.tools.tokens import account_activation_token 
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
# Create your views here.

@unauthenticated_user
def login(request):
    form = Login(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if user:
            django_login(request,user)
            messages.success(request,'You logged in successfuly')
            return redirect(reverse_lazy('accounts:home'))
        else:
            messages.error(request,'The information you entered is valid')

    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)   


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('accounts:login'))



@login_required(login_url='accounts:login')
def home(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='accounts:login')
def customer(request):
    if request.user.read == True:

        customers= Customer.objects.all()
        context={
            'customers':customers

        }

        return render(request,'accounts/customer.html',context)
    else:
        return HttpResponse("<p>You are note permissions</p>")


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def createCustomer(request):
    form=CustomerForm()
    if request.user.create == True:
	    if request.method == 'POST':
		    form = CustomerForm(request.POST, request.FILES)
		    if form.is_valid():
			    form.save()
			    return redirect('/customer')
	    context = {'form':form}
	    return render(request, 'accounts/create.html', context)
    else:
        return HttpResponse("<p>You are note permissions</p>")

@login_required(login_url='login')  
def updateCustomer(request, pk):
    if request.user.update == True:

        customer = Customer.objects.get(id=pk)
        form = CustomerForm(instance=customer)
        if request.method == 'POST':
            form = CustomerForm(request.POST, request.FILES, instance=customer)
            if form.is_valid():
                form.save()
                return redirect('/customer')

        context = {'form':form}
        return render(request, 'accounts/create.html', context)
    else:
        return HttpResponse("<p>You are note permissions</p>")


@login_required(login_url='login')
def deleteCustomer(request, pk):
    if request.user.delete == True:
        customer = Customer.objects.get(id=pk)
        if request.method == "POST":
            customer.delete()
            return redirect('/customer')
        return render(request, 'accounts/delete.html')
    else:
        return HttpResponse("<p>You are note permissions</p>")


# editor
@login_required(login_url='accounts:login')
def editor(request):
    editors= User.objects.filter(is_superuser = False).all
    context={
        'editors':editors
    }
    return render(request,'accounts/editor.html',context)


@login_required(login_url='login')
def createEditor(request):
    form=UserForm()
    if request.user.is_superuser == True:
	    form=UserForm()
	    if request.method == 'POST':
		    form = UserForm(request.POST)
		    if form.is_valid():
			    form.save()
			    return redirect('/editor')
	    context = {'form':form}
	    return render(request, 'accounts/create.html', context)

@login_required(login_url='login')
def updateEditor(request, pk):
    if request.user.is_superuser == True:

        editor = User.objects.get(id=pk)
        form = UserForm(instance=editor)
        if request.method == 'POST':
            form = UserForm(request.POST,request.FILES, instance=editor)
            if form.is_valid():
                form.save()
                return redirect('/editor')

        context = {'form':form}
        return render(request, 'accounts/create.html', context)


@login_required(login_url='login')
def deleteEditor(request, pk):
    if request.user.is_superuser == True:
        editor = User.objects.get(id=pk)
        if request.method == "POST":
            editor.delete()
            return redirect('/editor')
        return render(request, 'accounts/delete.html')


def updateAdmin(request,pk):

    user = User.objects.get(id=pk)
    form = UserForm(instance = user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance = user)
        if form.is_valid():
            email  = request.POST.get('email')
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST'] 
            send_confirmation_mail(user_id=user.id, site_address=site_address) 
            messages.success(request, 'Siz ugurla deyisiklik elediniz')        
            return redirect('/')

    context = {
        'form':form,
    }
    return render(request, 'accounts/create.html', context)



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64)) 
        user = User.objects.get(pk=uid) 
    except:
        (TypeError, ValueError, OverflowError, User.DoesNotExist) 
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.save()
        messages.success(request, 'Email is changed')
        return redirect(reverse_lazy('accounts:home'))

    elif user:
        messages.error(request, 'Email is not activated. May be is already activated')
        return redirect(reverse_lazy('accounts:home'))

    else:
        messages.error(request, 'Email is not activated')
        return redirect(reverse_lazy('accounts:home'))