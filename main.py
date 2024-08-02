import smtplib
my_mail = "kumar.samyak018@gmail.com"
passcode = "SamyakKumar@200418"
mail_content = "Subject: Trip on this weekend?\n\nHey Buddy, how are you? Iss weekend pe Goa plan kare?"
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Start TLS encryption
        connection.login(user=my_mail, password=passcode)
        connection.sendmail(from_addr=my_mail, to_addrs="kumar.samyak018@gmail.com", msg=mail_content)
        print("Email sent successfully.")
except Exception as e:
    print("Something went wrong while sending the email:", e)
