from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

from django.urls import path
from . import views

app_name = 'customers'
urlpatterns =[
    path('', views.index, name='index'),
    path('<int:customer_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('edit/<int:customer_id>/', views.edit, name='edit'),
    path('delete/<int:customer_id>', views.delete, name='delete')
]
