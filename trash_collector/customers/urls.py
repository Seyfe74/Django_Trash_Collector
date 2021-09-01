from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

from django.urls import path
from . import views

app_name = 'customers'
urlpatterns =[
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('new/', views.create, name='create'),
    path('delete/<int:customer_id>', views.delete, name='delete'),
    path('weekly/', views.weekly, name='weekly'),
    path('suspend/', views.suspend, name='suspend')
    
]
