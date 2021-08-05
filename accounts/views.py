from django import http
from accounts.models import  Customer
from django.shortcuts import redirect, render
from .froms import CustomerForm, Login, UserForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .decorators import allowed_users, unauthenticated_user,admin_only
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import HttpResponse, request
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

@login_required(login_url='login')
def deleteCustomer(request, pk):
    if request.user.delete == True:
        customer = Customer.objects.get(id=pk)
        if request.method == "POST":
            customer.delete()
            return redirect('/customer')
        return render(request, 'accounts/delete.html')



# class CustomerCreateView(LoginRequiredMixin,CreateView):

#     model = Customer
#     form_class = CustomerForm
#     template_name = 'accounts/create.html'
#     success_url = '/customer'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["is_super"] = self.request.user.is_superuser
#         return context


# class CustomerUpdateView(UpdateView):
#     model = Customer
#     form_class = CustomerForm
#     template_name = 'accounts/create.html'
#     success_url = '/customer'

    
#         # def form_valid(self, form):
#         #     obj = form.save(commit=False)
#         #     obj.save()        
#         #     return http.HttpResponseRedirect(self.get_success_url())


# class CustomerDeleteView(DeleteView):
#     model = Customer
#     template_name = 'accounts/delete.html'
#     success_url = '/customer'

#     def form_valid(self, form):

#         if request.user.delete == True:
#             obj = form.save(commit=False)
#             obj.save()        
#             return http.HttpResponseRedirect(self.get_success_url())


@login_required(login_url='accounts:login')
def editor(request):

    editors= User.objects.filter(is_superuser = False).all
    context={
        'editors':editors
    }
    return render(request,'accounts/editor.html',context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def createEditor(request):
    form=UserForm()
    if request.user.is_superuser == True:
	    form=UserForm()
	    if request.method == 'POST':
		    form = UserForm(request.POST)
		    if form.is_valid():
			    form.save()
			    return redirect('/edtior')
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

# class EditorCreateView(CreateView):
#     model = User
#     form_class = UserForm
#     template_name = 'accounts/create.html'
#     success_url = '/editor'

#     # def form_valid(self, form):
#     #     obj = form.save(commit=False)
#     #     obj.teacher = self.request.user
#     #     obj.save()        
#     #     return http.HttpResponseRedirect(self.get_success_url())


# class EditorUpdateView(UpdateView):
#     model = User
#     form_class = UserForm
#     template_name = 'accounts/create.html'
#     success_url = '/editor'


# class EditorDeleteView(DeleteView):
#     model = User
#     template_name = 'accounts/delete.html'
#     success_url = '/editor'