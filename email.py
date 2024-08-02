import smtplib
from email.message import EmailMessage
from email.policy import SMTP
def create_email(sender, recipient, subject, body):
    # Create an EmailMessage object
    msg = EmailMessage(policy=SMTP)
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)
    return msg

def send_email(smtp_server, smtp_port, username, password, msg):
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
    # Define email details
    sender_email = "kumar.samyak018@gmail.com"
    recipient_email = "kumar.samyak018@gmail.com"
    subject = "Tour planning"
    body = "Lets plan a trip to goa on this coming weekend"
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    username = "kumar.samyak018@gmail.com"
    password = "SamyakKumar@200418"  
    email_msg = create_email(sender_email, recipient_email, subject, body)
    send_email(smtp_server, smtp_port, username, password, email_msg)
