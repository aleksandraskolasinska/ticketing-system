from django.db import models
import datetime

from django.utils import timezone
from django.contrib.auth.models import User, Permission

# Create your models here.

class TicketStatus(models.TextChoices):
    to_do = 'To do'
    in_progress = 'In progress'
    done = 'Done'


class Ticket(models.Model):
    title = models.CharField(max_length=150)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)#, related_name=staff)#limit_choices_to={'is_staff': True}
    # submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name=basic_user)
    status = models.CharField(max_length=20, choices=TicketStatus.choices, default=TicketStatus.to_do)
    publication_date = models.DateTimeField('date published', auto_now_add = True)
    update_date = models.DateTimeField('date of update', auto_now = True)
    ticket_content = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.publication_date <= now

class TicketAssign(models.Model):

    def get_assigned_tickets(self, user):
        return self.filter(assigned_to=user)

    def assign_ticket():
        self.assigned_to = user
        self.status = TicketStatus.to_do
        self.save() 

    def close_ticket():
        self.status = TicketStatus.done
        self.save()
