from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from .models import Ticket, TicketAssign, TicketReply


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'assignee', 'created_by', 'status', 'publication_date', 'update_date')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:
            form.base_fields['assignee'].disabled = True
            form.base_fields['status'].disabled = True
        return form

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