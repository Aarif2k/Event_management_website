# Event_management_website

Overview
Event Management System is a web application built with Django designed to streamline the process of organizing and managing events. It provides features for event creation, registration, and management, making it easier for organizers and attendees to interact and participate in events.

Features
Event Creation and Management: Organizers can create and manage events, including setting dates and descriptions.
User Registration and Login: Attendees can register and log in to the event registrations.
Event Registration: Users can register for events, view event details.
Admin Panel: A comprehensive admin panel for managing users, events, and registrations.

Technologies Used
Backend:
Django: Web framework for building the application.
MySQL: Database for storing event and user data.
Frontend:
HTML, CSS, JavaScript: Core technologies for the user interface.
Bootstrap/Django Crispy Forms: For styling and rendering forms (optional, based on your choice).



Installation
Prerequisites
asgiref==3.8.1
crispy-bootstrap5==2024.2
Django==5.0.7
django-crispy-forms==2.2
mysqlclient==2.2.4
pillow==10.4.0
sqlparse==0.5.0
tzdata==2024.1
Virtual Environment (recommended)

Setup Instructions
Clone the Repository:

git clone https://github.com/Aarif2k/Event_management_website.git
cd event-management-system
Create and Activate a Virtual Environment:

python -m venv venv
venv\Scripts\activate
Install Dependencies:

pip install -r requirements.txt
Configure Database:

Update the DATABASES setting in settings.py with your MySQL credentials.

Apply migrations:
python manage.py migrate

Create a Superuser:
python manage.py createsuperuser

Run the Development Server:
python manage.py runserver

Access the Website:
Open your web browser and go to http://127.0.0.1:8000/ to view the website.

Usage
Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/ using the superuser credentials you created. Here you can manage events, users, and registrations.

User Interface
Event Creation: Organizers can create and manage events from the admin panel or a dedicated interface.
Registration: Users can browse events, register for events.
