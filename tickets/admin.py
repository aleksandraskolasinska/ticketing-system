from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from .models import Ticket, TicketAssign, TicketReply

class TicketReplyInline(admin.StackedInline):
    model = TicketReply
    extra = 0

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'assignee', 'created_by', 'status', 'publication_date', 'update_date')
    inlines = [TicketReplyInline]
    readonly_fields = ['created_by', 'status', 'publication_date', 'update_date']


    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
  
    def get_readonly_fields(self, request, obj=None):
        if obj:
            # Check if the user is staff/admin
            if request.user.is_staff or request.user.is_superuser:
                return self.readonly_fields + ['ticket_content']
        return self.readonly_fields
    
class TicketReplyAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'user', 'timestamp']
    readonly_fields = ['user', 'timestamp']

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.user != request.user:
            # If the logged-in user is not the author of the reply, make the 'message' field read-only
            return self.readonly_fields + ['message']
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        if obj and obj.user != request.user:
            return False
        return super().has_change_permission(request, obj)
    

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

    def has_change_permission(self, request, obj=None):
        if obj and obj.user != request.user:
            return False
        return super().has_change_permission(request, obj)


# Register your models here.
admin.site.register(Ticket, TicketAdmin) 
admin.site.register(TicketReply, TicketReplyAdmin)