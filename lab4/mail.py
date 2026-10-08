import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email server details (for example, Gmail's SMTP)
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "getlead.tech@gmail.com"  # Replace with your email address
sender_password = "uslcjgervkhmijdk"     # Replace with your email password or app-specific password
receiver_email = "cb13123@auca.kg"  # Replace with the recipient's email





subject = "SecureBank — Action Required: Verify Your Card"
 
body = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SecureBank Email</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f0f2f5; }
    .container {
      max-width: 600px;
      margin: 0 auto;
      background-color: #ffffff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .header {
      display: flex;
      align-items: center;
      padding-bottom: 20px;
      border-bottom: 2px solid #003087;
    }
    .header h2 { margin: 0; font-size: 22px; color: #003087; }
    .button {
      display: inline-block;
      background-color: #003087;
      color: white;
      text-decoration: none;
      padding: 12px 24px;
      border-radius: 5px;
      font-size: 16px;
      text-align: center;
      border: none;
    }
    .footer {
      text-align: center;
      margin-top: 20px;
      font-size: 12px;
      color: #888;
      border-top: 1px solid #eee;
      padding-top: 14px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h2>🏦 SecureBank</h2>
    </div>
    <p style="font-size: 16px; color: #333; margin-top: 20px;">
      <strong>Important: Your debit card requires verification.</strong>
    </p>
    <p style="font-size: 15px; color: #555;">
      We detected unusual activity on your account. To protect your funds,
      please verify your card details within 24 hours or your card will be temporarily suspended.
    </p>
    <p style="font-size: 15px; color: #555;">Click the link below to verify:</p>
    <p style="font-size: 15px;">
      <a href="http://localhost:8080/bank">http://localhost:8080/bank</a>
    </p>
    <div class="footer">
      <p>If you did not request this, please contact us at support@securebank.com</p>
      <p>SecureBank Inc., 100 Finance Street, New York, NY 10001</p>
    </div>
  </div>
</body>
</html>
"""
 
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "html"))
 
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()