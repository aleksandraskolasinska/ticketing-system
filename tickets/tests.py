from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

import datetime

from .models import Ticket

# Create your tests here.

class TicketPublishDateTests(TestCase):

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

class TicketContentTests(TestCase):
    def setUp(self):
        """
        Assign user and assignee to a ticket"
        """
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.ticket = Ticket.objects.create(title='Test Ticket', ticket_content='This is a test ticket', created_by=self.user1, assignee=self.user2)

    def test_ticket_str(self):
        """
        Returns True if previously created ticket title was correct
        """
        self.assertEqual(str(self.ticket), 'Test Ticket')

    def test_ticket_status_new(self):
        """
        Returns True, if the beginning status equals to "to do"
        """
        self.assertEqual(self.ticket.status, 'to_do')

    def test_ticket_status_closed(self):
        """
        Returns True, if the status changed to done as set.
        """
        self.ticket.status = 'done'
        self.assertEqual(self.ticket.status, 'done')

class CreateTicketViewTests(TestCase):
    def setUp(self):
        """
        Create user
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_ticket_view(self):
        """
        Return True if creating ticket successful
        """
        url = reverse('create_ticket')
        response = self.client.post(url, {'title': 'Test Ticket', 'ticket_content': 'This is a test ticket'})
        self.assertEqual(response.status_code, 302)

        tickets = Ticket.objects.all()
        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0].title, 'Test Ticket')
        self.assertEqual(tickets[0].description, 'This is a test ticket')
        self.assertEqual(tickets[0].created_by, self.user)

