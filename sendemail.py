import sendgrid
from sendgrid.helpers.mail import Mail
from listen import listen

def send_email(api_key, sender_email, recipient_email, subject, body):
    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=subject,
        plain_text_content=body
    )
    response = sg.send(message)
    if response.status_code == 202:
        return True
    else:
        return False



