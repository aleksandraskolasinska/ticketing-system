from django.contrib import admin
from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'

# Register your models here.
admin.site.register(Ticket, TicketAdmin)