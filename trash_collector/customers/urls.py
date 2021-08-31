from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('change/', views.change_pickup_date, name="change_pickup_date"),
    path('suspend/', views.suspend_account, name="suspend_account"),
    path('account/', views.account_info, name="account_info")
]
