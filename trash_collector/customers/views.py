from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

 
 

# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        pass

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

    print(user)
    return render(request, 'customers/index.html')


def create(request):
    if request.method =="POST":
       name = request.POST.get("name")
       user = request.user
       new_cust = Customer(name=name, user = user)
       new_cust.save()
       return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')

def detail(request, customer_id):
        single_customer = Customer.objects.get(pk=customer_id)
        context = {
            'single_customer': single_customer
        }
        return(request, 'customers/detail.html', context)


def change_pickup_date(request):
    if request.method =="POST":
       weekly_pickup_day = request.POST.get("weekly_pickup_day")
       user = request.user
       new_p_date = Customer(name = weekly_pickup_day, user = user)
       new_p_date.save()
       return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/update.html')


def suspend_account(request):
    pass

def account_info(request):
    pass


# delete view for details
def delete(request, customer_id):
    single_customer = Customer.objects.get(pk=customer_id)
    context = {
        'single_customer': single_customer
    }

  
    obj = get_object_or_404(Customer, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "customers/delete_view.html", context)
