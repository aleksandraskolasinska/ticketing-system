from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from .models import Ticket, TicketAssign


class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'

class TicketStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_assigned_tickets(self):
        return TicketAssign.objects.get_assigned_tickets(self.user)

    def respond_to_ticket(self, ticket, message):
        ticket.status = TicketStatus.to_do
        ticket.save()
        Ticket.objects.create(ticket=ticket, user=self.user, message=self.message)


# Register your models here.
admin.site.register(Ticket, TicketAdmin)