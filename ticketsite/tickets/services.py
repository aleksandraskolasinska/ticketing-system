from django.shortcuts import get_object_or_404
from .models import Ticket

def get_ticket_list():
    tickets = Ticket.objects.all().order_by('-publication_date')
    return tickets

def get_ticket_list():
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return ticket

