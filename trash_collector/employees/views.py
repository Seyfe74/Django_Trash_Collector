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
Customer = apps.get_model('customers.Customer')
    user = request.user
    try:
        logged_in_employee = Employee.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('employees:create'))
    print(user)
    
    #TODO: moved the "todays pickup" to the index render so the pickups render right away in the index page
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    Customer = apps.get_model('customers.Customer')
    today = date.today()
    string_weekday = calendar.day_name[today.weekday()]
    customers = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
    customer = []
    for pick_ups in customers:
        if (pick_ups.one_time_pickup == today or pick_ups.weekly_pickup == string_weekday) and logged_in_employee.zip_code == pick_ups.zip_code and (pick_ups.suspend_start < today and  today >= pick_ups.suspend_end or pick_ups.suspend_start > today and  today <= pick_ups.suspend_end) and pick_ups.suspend_start != '2000-01-01':
            customer.append(pick_ups)
    context = {
        'customer' : customer
        }
    return render(request, 'employees/index.html', context)



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
    
    def filter(request, day_of_week):
    user = request.user
    logged_in_employee = Employee.objects.get(user=user)
    # is the above necessary? 
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.filter(weekly_pickup = day_of_week)
    customer = []
    for filter_day in customers:
        customer.append(filter_day)
    context = {
        'customer' : customer
    }
    return render(request, 'employees/filter.html', context)

def charge_customer (request, charge, cust_id):
    Customer = apps.get_model('customers.Customer')
    charged_customer = Customer.objects.get(pk = cust_id)
    if request.method == 'POST':
        charged_customer.balance += charge
        charged_customer.save()
        return HttpResponseRedirect(reverse('employees:todays_pickups'))
    else:
        context = {
            'charged_customer' : charged_customer
        }
        return render(request, 'employees/charge_customer.html', context)
