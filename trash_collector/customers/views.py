from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
# The following line will get the logged-in in user (if there is one) within any view function
    all_customers = Customer.objects.all()
    context = {
        'all customers': all_customers
    }
    return render(request,'customers/index.html',context)

def detail(request, customer_id):
        single_customer = Customer.objects.get(pk=customer_id)
        context = {
            'single_customer': single_customer
        }
        return(request, 'customers/detail.html', context)
# try:
#     # This line inside the 'try' will return the customer record of the logged-in user if one exists
#     # logged_in_customer = Customer.objects.get(user=user)
    
# except:
   
   
   
   
    # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip code')
        balance  = request.POST.get('balance')
        one_time_pickup = request.POST.get('one-time-pickup')
        weekly_pickup_day = request.POST.get('weekly pickup day')
        suspend_start = request.POST.get('suspend_start')
        suspend_end = request.POST.get('suspend_end')
        suspend_status = request.POST.get('suspend_status')
        pickup_status = request.POST.get('pickup_status')
        new_user = Customer(name=name,address=address, zip_code=zip_code, balance=balance, one_time_pickup=one_time_pickup, weekly_pickup_day=weekly_pickup_day,suspend_start=suspend_start,suspend_end=suspend_end,suspend_status=suspend_status,pickup_status=pickup_status )
        new_user.save
        

    else:
        return render(request, 'customers/create.html')



# It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

# print(user)
# return render(request, 'customers/index.html', context)
