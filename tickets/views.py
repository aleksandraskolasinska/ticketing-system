from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse

from .models import Ticket
from .forms import TicketForm

# Create your views here.

# class IndexView(generic.ListView):
#     template_name = 'tickets/index.html'
#     context_object_name = 'latest_tickets_list'

def index(request):
    tickets = Ticket.objects.order_by('publication_date')[:5]
    context = {'tickets': tickets}
    return render(request, 'index.html', context)

def ticketView(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'ticketView.html', {'ticket':ticket})

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.assignee = request.user
            # ticket.created_by = request.user
            ticket.save()
            return HttpResponseRedirect(reverse('ticketsapp:ticketView', args=(ticket.id,)))
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})