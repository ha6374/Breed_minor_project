# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from app.core.config import settings


# def send_reset_email(to_email: str, reset_link: str):
#     """
#     Send password reset email using Gmail SMTP.
#     """

#     smtp_server = settings.EMAIL_HOST
#     smtp_port = int(settings.EMAIL_PORT)
#     sender_email = settings.EMAIL_USERNAME
#     sender_password = settings.EMAIL_PASSWORD

#     subject = "Reset Your Password - Pashudhan AI"
#     message = f"""
# Hi,

# Click the link below to reset your password:

# {reset_link}

# If you did not request this, you can ignore this email.

# Regards,
# Pashudhan AI Team
# """

#     try:
#         # Create the email
#         msg = MIMEMultipart()
#         msg["From"] = sender_email
#         msg["To"] = to_email
#         msg["Subject"] = subject

#         msg.attach(MIMEText(message, "plain"))

#         # Connect to Gmail SMTP
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.starttls()  # encryption
#         server.login(sender_email, sender_password)

#         # Send email
#         server.sendmail(sender_email, to_email, msg.as_string())
#         server.quit()

#         print(f"📩 Email sent to: {to_email}")
#         print(f"🔗 Reset link: {reset_link}")

#     except Exception as e:
#         print("❌ Email sending failed:", e)

import requests
from app.core.config import settings

RESEND_URL = "https://api.resend.com/emails"


def send_reset_email(to_email: str, reset_link: str):
    headers = {
        "Authorization": f"Bearer {settings.RESEND_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "from": settings.EMAIL_FROM,
        "to": [to_email],
        "subject": "Reset Your Password - Pashudhan AI",
        "html": f"""
        <p>Hi,</p>
        <p>Click the link below to reset your password:</p>
        <p><a href="{reset_link}">{reset_link}</a></p>
        <p>If you did not request this, you can ignore this email.</p>
        <br>
        <p><b>Pashudhan AI Team</b></p>
        """
    }

    response = requests.post(RESEND_URL, headers=headers, json=payload)

    if response.status_code not in (200, 201):
        raise Exception(f"Resend error: {response.text}")
