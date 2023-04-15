from django.urls import path

from . import views

app_name='ticketsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ticket_id>', views.ticketView, name='ticketView'),
]