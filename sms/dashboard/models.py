from django.db import models
from django.conf import settings
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse
import vonage

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Fetch credentials from environment variables
        api_key = "8b9fe520"
        api_secret = "O5hLzzfFspCUgrjF"
        
        
        # Initialize the Vonage client
        client = Vonage(Auth(api_key=api_key, api_secret=api_secret))

        # Construct the message text based on the score
        if self.score >= 70:
            text = f"Congratulations {self.name}, your score is {self.score}."
        else:
            text = f"Sorry {self.name}, your score is {self.score}. Try again."

        # Create the SmsMessage object
        message = SmsMessage(
            to="639943755758",
            from_="Vonage APIs",
            text=text,
        )

        # Send the SMS
        response: SmsResponse = client.sms.send(message)

        
         # Access the response correctly
        if response.messages[0].status == "0":
            print("Message sent successfully.")
        else:
            error_text = response.messages[0].error_text
            print(f"Message failed with error: {error_text}")

        # Call the parent class's save method
        super().save(*args, **kwargs)
