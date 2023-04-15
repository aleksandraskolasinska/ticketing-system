from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

import datetime

from .models import Ticket

# Create your tests here.

class TicketModelTests(TestCase):

    def test_was_published_with_future_date(self):
        """
        was _published recently() returns False for tickets whose publication_date is in the future
        """
        time = timezone.now() + datetime.timedelta(30)
        future_ticket = Ticket(publication_date=time)
        self.assertIs(future_ticket.was_published_recently(), False)

    def test_was_published_with_recent_date(self):
        """
        was _published recently() returns True for tickets whose publication_date is in the recent past (within 7 days)
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_ticket = Ticket(publication_date=time)
        self.assertIs(recent_ticket.was_published_recently(), True)

    def test_was_published_old_date(self):
        """
        was _published recently() returns False for tickets whose publication_date is in the recent past (within 7 days)
        """
        time = timezone.now() - datetime.timedelta(days=7, seconds=1)
        old_ticket = Ticket(publication_date=time)
        self.assertIs(old_ticket.was_published_recently(), False)

def createTicket(title, ticket_content):
    """
    Create a ticket
    """
    return Ticket.objects.create(title=title, ticket_content=ticket_content)


class TicketWithMissingData(TestCase):

    def test_ticket_correct_ticket(self):
        """
        Ticket with added title and content returns True for checking if valid.
        """
        ticket = createTicket(title='title', ticket_content='aaa')
        self.assertTrue(ticket.is_valid())
