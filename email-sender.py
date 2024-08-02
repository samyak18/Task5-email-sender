import argparse
import smtplib
from email.message import EmailMessage
def send_email(smtp_server, smtp_port, username, password, to_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Tour planning"
    msg["From"] = "kumar.samyak018@gmail.com"
    msg["To"] =  "kumar.samyak018@gmail.com"
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)
            server.send_message(msg)
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Error: {e}")
def main():
    parser = argparse.ArgumentParser(description="Send an email via CLI")
    parser.add_argument("--smtp_server smtp.gmail.com", required=True, help="smtp.gmail.com")
    parser.add_argument("--smtp_port 465", type=int, required=True, help="465")
    parser.add_argument("--username kumar.samyak018@gmail.com", required=True, help="kumar.samyak018@gmail.com")
    parser.add_argument("--password kumar.samyak018@gmail.com", required=True, help="SamyakKumar@200418")
    parser.add_argument("--to_email kumar.samyak018@gmail.com", required=True, help="kumar.samyak018@gmail.com")
    parser.add_argument("--subject Tour planning", required=True, help="Tour planning")
    parser.add_argument("--body Let us plan a tour to goa on coming week end.", required=True, help="Let us plan a tour to goa on coming week end.")
    args = parser.parse_args()
    send_email(
        smtp_server=args.smtp_server,
        smtp_port=args.smtp_port,
        username=args.username,
        password=args.password,
        to_email=args.to_email,
        subject=args.subject,
        body=args.body
    )
if __name__ == "__main__":
    main()