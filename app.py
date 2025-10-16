# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
# import smtplib
# from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # ✅ Option 1: Save message to messages.txt
        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

        # ✅ Option 2: Send message via email (commented out for safety)
        """
        msg = EmailMessage()
        msg['Subject'] = f"New Contact Form Submission from {name}"
        msg['From'] = email
        msg['To'] = "vishal.bhadarge@tataconsultingengineers.com"
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")

        with smtplib.SMTP('smtp.yourserver.com', 587) as server:
            server.starttls()
            server.login('your_username', 'your_password')
            server.send_message(msg)
        """

        return f"Thank you, {name}. We received your message."

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)