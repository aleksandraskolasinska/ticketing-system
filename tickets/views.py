from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required


from .models import Ticket
from .forms import TicketForm, SignUpForm, UsernameUpdateForm, PasswordUpdateForm, EmailUpdateForm, FirstNameUpdateForm, LastNameUpdateForm


# Create your views here.

# class IndexView(generic.ListView):
#     template_name = 'tickets/index.html'
#     context_object_name = 'latest_tickets_list'

def index(request):
    tickets = Ticket.objects.order_by('publication_date')[:5]
    context = {'tickets': tickets}
    return render(request, 'index.html', context)

def home(request):
    tickets = Ticket.objects.order_by('publication_date')[:5]
    context = {'tickets': tickets}
    return render(request, 'home.html', context)

def ticketView(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'ticketView.html', {'ticket':ticket})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            # ticket.assignee = request.user
            # ticket.created_by = request.user
            # ticket.save()
            ticket.save(user=request.user)
            return HttpResponseRedirect(reverse('ticketsapp:ticketView', args=(ticket.id,)))
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})

class LoginView(LoginView):
    template_name = 'registration/login.html'

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})




#

@login_required
def account_details_view(request):
    user = request.user
    return render(request, 'edit_acc/account_details.html', {'user': user})

@login_required
def username_update_view(request):
    if request.method == 'POST':
        form = UsernameUpdateForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            user = request.user
            user.username = new_username
            user.save()
            return redirect('ticketsapp:account_details')
    else:
        form = UsernameUpdateForm()
    
    return render(request, 'edit_acc/username_update.html', {'form': form})

@login_required
def password_update_view(request):
    if request.method == 'POST':
        form = PasswordUpdateForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            user = request.user
            if user.check_password(current_password) and new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Update session with new password
                return redirect('ticketsapp:account_details')
            else:
                form.add_error('confirm_password', 'Passwords do not match.')
    else:
        form = PasswordUpdateForm()
    
    return render(request, 'edit_acc/password_update.html', {'form': form})

@login_required
def email_update_view(request):
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            user = request.user
            user.email = new_email
            user.save()
            return redirect('ticketsapp:account_details')
    else:
        form = EmailUpdateForm(initial={'new_email': request.user.email})
    
    return render(request, 'edit_acc/email_update.html', {'form': form})

@login_required
def first_name_update_view(request):
    if request.method == 'POST':
        form = FirstNameUpdateForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['new_first_name']
            user = request.user
            user.first_name = new_first_name
            user.save()
            return redirect('ticketsapp:account_details')
    else:
        form = FirstNameUpdateForm(initial={'new_first_name': request.user.first_name})
    
    return render(request, 'edit_acc/first_name_update.html', {'form': form})

@login_required
def last_name_update_view(request):
    if request.method == 'POST':
        form = LastNameUpdateForm(request.POST)
        if form.is_valid():
            new_last_name = form.cleaned_data['new_last_name']
            user = request.user
            user.last_name = new_last_name
            user.save()
            return redirect('ticketsapp:account_details')
    else:
        form = LastNameUpdateForm(initial={'new_last_name': request.user.last_name})
    
    return render(request, 'edit_acc/last_name_update.html', {'form': form})

