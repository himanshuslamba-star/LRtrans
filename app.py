from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# All Other Pages
@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/services')
def services():
    return render_template('Services.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/quote')
def quote():
    return render_template('Quote.html')

@app.route('/test')
def test():
    return render_template('Test.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)