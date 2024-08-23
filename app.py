from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

# Database Configuration - Update these values with your GCP MySQL instance details
username = "root"
password = "password1"
hostname = "34.41.207.237" 
databasename = "comments"

# Construct the SQLAlchemy Database URI
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define the Comment model
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# Route for the Contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        # Render the contact.html template with all comments
        return render_template("contact.html", comments=Comment.query.all())

    # Handle POST request (form submission)
    content = request.form.get("contents")
    if content:
        comment = Comment(content=content)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('contact'))

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Run the application
if __name__ == '__main__':
    # Ensure the app is accessible externally and on port 5000
    app.run(host='0.0.0.0', port=5000)
