# Generated by Django 4.1.7 on 2023-03-30 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('ticket_content', models.TextField()),
                ('status', models.CharField(choices=[('To do', 'To Do'), ('In progress', 'In Progress'), ('Done', 'Done')], default='To do', max_length=20)),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date of update')),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
