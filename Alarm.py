import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

class Alarm:

    # method to send a message "alarm" though gmail
    def send_alarm(to_add, sub, content):
        # Create an SMTP object and connect to the Gmail server
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.ehlo()  # Say 'hello' to the server
        smtp_object.starttls()  # Start the TLS connection

        # Retrieve email and app password from environment variables
        email = os.getenv("EMAIL_SEND")
        App_pass = os.getenv("APP_PASS")

        # Login to the email account using the provided credentials
        smtp_object.login(email, App_pass)

        # Send the alarm message to each recipient in the 'to_add' (address) list
        for address in to_add:
            msg = "Subject: " + sub + '\n' + content
            smtp_object.sendmail(email, address, msg)

        # Close the SMTP connection
        smtp_object.quit()

# print(os.getenv("EMAIL_SEND"),os.getenv("APP_PASS"))