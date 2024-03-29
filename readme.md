# Table of contents

- [About the project - overview](#ticketing-system)
- [Installation and set up](#instalation)
- [Usage and features](#usage-and-features)

    - [user site](#user-site)
    - [admin site](#admin-site)

- [User manual](#user-manual)
- [Administrator manual](#administrator-manual)

# Ticketing system

Practice project for a ticketing system using Django and database in postgres. Allows users to create an account, edit their account data, submit tickets and view their tickets and their current status.

# Installation

This project uses Docker. By default the development server runs on
- http://127.0.0.1:8000/

To run the app follow the commands listed below:

 ## Using Docker Compose

```bash
docker compose up -d
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

## Create superuser to login
To create an admin account run:

```bash
docker compose exec -it web python manage.py createsuperuser
```
and follow the terminal instructions.

## Take the server down
To take the app down run:

```bash
docker compose down
```

Note: docker compose is configured to use docker volume. This will persist between `docker up` and `docker down` commands. 

In case the database needs to be deleted:
```bash
docker compose down --volumes my_db_data
```


# Usage and features

## User site

- Users can submit support tickets providing a title and a description of the problem

- They can see an overview of all the tickets they have submited and their status including the information whenever a staff member has been assigned to their ticket

- Users can add comments to their tickets 


## Admin site

- Staff can assign themselves to tickets, change their statuses and resolve the issues

- Staff can see the history of all created tickets including their updates, replies and changes made

# User manual

## Getting started

To start using the app, you need to be logged in. Main page will greet new users with a prompt to create an account or log in.

To create a new account you will need to provide a username, a valid email address and pick a password. It is later possible (but not required) to add first and last name via edit account option located in the account details tab.

![image](/readme_files/getting_started.png)

## Dashboard

Logged in users on the header of the app should see main options such as:
- Home: redirects to main page.
- Create a ticket: moves to create ticket form.
- View tickets: allows to see sumbitted tickets.
- Account:  lets the user see the account details and edit them as well as log out.

![image](/readme_files/dashboard.png)


## Submitting a ticket

To create a ticket simply go to `create a ticket` located on the dashboard and fill in the title as well as the description.

![image](/readme_files/create_ticket.png)

## Tracking tickets

Tickets can be tracked via the `View sumbited tickets` tab visible on the dashboard. To see details as well as add more information 

![image](/readme_files/tracking_tickets.png)

## Details and replies with staff

Viewing the details of a submited ticket allows to exchange replies with staff.

![image](/readme_files/ticket_replies.png)

# Administrator manual

## Accessing the admin panel

If the user has the staff status then after being logged in they will be able to visit

- http://127.0.0.1:8000/admin

and see a redirection to the panel in the Account tab on the dashboard

![image](/readme_files/admin_panel.png)

## Admin panel

In the tickets category in the admin panel, staff will be able to see all tickets, their statuses and when they were last updated.

![image](/readme_files/admin_panel_view.png)