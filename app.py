from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'lrtrans-secret-key-2025'  # Change in production

# ====================
# ROUTES
# ====================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quote')
def quote():
    return render_template('quote.html')

@app.route('/submit-quote', methods=['POST'])
def submit_quote():
    try:
        company = request.form['company'].strip()
        email = request.form['email'].strip()
        phone = request.form['phone'].strip()
        service = request.form['service']
        message = request.form.get('message', '').strip()

        # Simple validation
        if not company or not email or not phone:
            flash("Please fill in all required fields.", "danger")
            return redirect(url_for('quote'))

        # In real app: Save to DB, send email, etc.
        # For now: Just show success
        flash(
            f"Quote request received! We'll contact {company} at {email} within 1 hour.",
            "success"
        )
        return redirect(url_for('home'))

    except Exception as e:
        flash("Something went wrong. Please try again.", "danger")
        return redirect(url_for('quote'))


# Optional: About, Services, Contact pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# ====================
# ERROR HANDLING
# ====================

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


# ====================
# RUN APP
# ====================

if __name__ == '__main__':
    app.run(debug=True)