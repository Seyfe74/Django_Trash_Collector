from customers.models import Customer
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Employee
from datetime import date
from django.apps import apps
import calendar




# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request,):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    user = request.user
    Customer = apps.get_model('customers.Customer')
    # logged_in_employee = Employee.objects.get(user=user)
    employee_zip =Employee.zip_code()
    today = date.today()
    day_of_week = (calendar.day_name[today.weekday()])
    # not_suspended = Customer.suspend_status (= False)
    all_customer = Customer.objects.filter(zip_code=employee_zip, weekly_pickup_day=day_of_week) | Customer.objects.filter(zip_code=employee_zip, one_time_pickup=today,suspend_start=today, suspend_end=today) or Customer.objects.filter(zip_code=employee_zip,suspend_start=today, suspend_end=today)
    context = {
            'all_customer': all_customer
        }
    return render(request, 'employees/index.html', {'all_customer' : all_customer},context)
    
   



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
