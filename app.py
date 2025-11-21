from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# A secret key is required for flashing messages (important for production!)
app.secret_key = 'your_super_secret_key' 

# --- Routes ---

@app.route('/')
def index():
    """Renders the main portfolio page."""
    # Context data for the template (your personal info)
    my_info = {
        'name': 'A. Developer',
        'title': 'Full Stack Developer | Python Enthusiast',
        'bio': 'Passionate about building scalable web applications and exploring new technologies. Specializing in Python/Flask and modern frontend frameworks.',
        'skills': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'SQL']
    }
    return render_template('index.html', info=my_info)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handles the contact form submission."""
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # --- Real-World Action (Simulated) ---
        # In a real application, you would:
        # 1. Validate the data (check if fields are empty, email is valid, etc.)
        # 2. Save the data to a database OR
        # 3. Send an email to yourself with the contact info (using a library like Flask-Mail)
        
        # Simulate successful submission
        print(f"New message from {name} ({email}): {message}") 
        
        # Flash a success message
        flash(f'Thank you, {name}! Your message has been sent.', 'success')
        
        # Redirect to avoid form re-submission upon refresh
        return redirect(url_for('contact'))

    # For GET requests, render the contact form page
    return render_template('contact.html')

# --- Run the App ---
if __name__ == '__main__':
    # Debug mode is great for development, turn off for production!
    app.run(debug=True)
