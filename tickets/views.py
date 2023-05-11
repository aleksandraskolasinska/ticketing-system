from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse

from .models import Ticket
from .forms import TicketForm, SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

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