from accounts.models import  Customer
from django.shortcuts import redirect, render
from .froms import CustomerForm, Login
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .decorators import allowed_users, unauthenticated_user,admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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

@unauthenticated_user
def logout(request):
    django_logout(request)
    messages.success(request,'You logged out')
    return redirect(reverse_lazy('accounts:login'))

@login_required(login_url='accounts:login')
def home(request):
    return render(request, 'accounts/dashboard.html')


def customer(request):
    customers= Customer.objects.all()
    context={
        'customers':customers

    }

    return render(request,'accounts/customer.html',context)

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'accounts/create.html'
    success_url = '/customer'

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.teacher = self.request.user
    #     obj.save()        
    #     return http.HttpResponseRedirect(self.get_success_url())

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'accounts/create.html'
    success_url = '/customer'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'accounts/delete.html'
    success_url = '/customer'