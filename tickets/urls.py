from django.urls import path

from . import views

app_name='ticketsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ticket_id>', views.ticketView, name='ticketView'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]