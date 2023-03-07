# app.py

# Import the Flask module
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the index page
@app.route("/")
def index():
    with open("toBeRead.txt", "r") as f:
        content = f.read()
    return content

# Start the Flask application if this file is being executed as the main script
if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")