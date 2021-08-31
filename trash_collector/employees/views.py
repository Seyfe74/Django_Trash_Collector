from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Employee


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    #Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


def create(request):
    if request.method =="POST":
       name = request.POST.get("name")
       user = request.user
       new_cust = Employee(name=name, user = user)
       new_cust.save()
       return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')
