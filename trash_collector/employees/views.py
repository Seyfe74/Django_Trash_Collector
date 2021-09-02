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


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers

    user = request.user
    try:
       logged_in_employee = Employee.objects.get(user=user)
    except:
        employee = apps.get_model('employees.employee')
        return render(request, 'employees/create.html')
    print(user)
    return render(request, 'employees/index.html')




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


def details(request):
        user = request.user
        single_employee = Employee.objects.get(user=user )
        zip = single_employee.zip_code
        today = date.today()
        day_of_week = (calendar.day_name[today.weekday()])
        
        # pday = "Monday"
        cus_info = Customer.objects.filter( zip_code=zip)  or Customer.objects.filter(zip_code=zip,suspend_start=today,suspend_status = False) 

        
        context = {
            'cus_info': cus_info
            
        }
        return render(request, 'employees/details.html', context)
