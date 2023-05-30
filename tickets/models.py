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
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="%(app_label)s_%(class)s_created_tickets")#limit_choices_to={'is_staff': True}
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_assigned_tickets")
    status = models.CharField(max_length=20, choices=TicketStatus.choices, default=TicketStatus.to_do)
    publication_date = models.DateTimeField('date published', auto_now_add = True)
    update_date = models.DateTimeField('date of update', auto_now = True)
    ticket_content = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk is None:
            #Set created_by only if new ticket
            self.created_by = kwargs.pop('user', None)
        super().save(*args, **kwargs)
    
    def get_replies(self):
        return TicketReply.objects.filter(ticket=self)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.publication_date <= now

class TicketReply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

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
