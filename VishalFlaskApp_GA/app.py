
from flask import Flask, render_template, request

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

        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}\n"
                "---\n"
            )

        return f"Thank you, {name}. We received your message."

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
