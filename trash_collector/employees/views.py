from customers.models import Customer
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Employee
from datetime import date
from django.apps import apps

today = date.today()
print("", today)


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request,):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    logged_in_employee = Employee.objects.get(user=request.user)
    same_zip = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
    not_suspended = Customer.objects.filter(suspend_status=False)
    pickup_date = Customer.objects.filter(weekly_pickup_day = today)
    context= {
        "same_zip":same_zip,
        "not_suspended":not_suspended,
        "pickup_date":pickup_date
    }
    return render(request, 'employees/index.html',context)


def create(request):
    if request.method =="POST":
       name = request.POST.get("name")
       user = request.user
       zip_code = request.POST.get('zip_code')
       new_employee = Employee(name=name,zip_code=zip_code, user = user)
       new_employee.save()
       return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')
