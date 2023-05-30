from django.urls import path

from . import views

app_name='ticketsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ticket_id>', views.ticketView, name='ticketView'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    # path('account/edit', views.account_edit_view, name='account_edit'),
    path('account/', views.account_details_view, name='account_details'),
    path('account/username/update/', views.username_update_view, name='username_update'),
    path('account/password/update/', views.password_update_view, name='password_update'),
    path('account/email/update/', views.email_update_view, name='email_update'),
    path('account/first_name/update/', views.first_name_update_view, name='first_name_update'),
    path('account/last_name/update/', views.last_name_update_view, name='last_name_update'),


]