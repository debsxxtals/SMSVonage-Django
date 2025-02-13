# SMSVonage-Django

# SMS Messaging Django Application from Group 1

# Overview
This Django application allows administrators to send SMS messages directly from the Django Admin interface. It uses an SMS gateway API which is Vonage to handle message delivery efficiently.

# Features
    SMS sending functionality integrated into the Django Admin panel.
    Allows administrators to specify recipients and customize message content.
    Built-in error handling for invalid inputs or failed SMS delivery.

# How It Works
The application adds a model in the Django Admin for SMS messages.
When an admin user creates an SMS entry, a signal triggers a function to send the message using the SMS gateway API.
The gateway handles delivery, and the status is logged in the Admin interface for reference.
    
# Usage
    Log in to the Django Admin panel at http://127.0.0.1:8000/admin/.
    Navigate to the SMS Messages section.
    Click Add SMS Message.
    Fill out the form with:
        Name of the recipient
        Their score
    Save the form to send the SMS. The system will automatically deliver the message through the configured SMS gateway.

# Requirements
Python 3.8+
Django 4.0+
An SMS gateway account (Vonage).
