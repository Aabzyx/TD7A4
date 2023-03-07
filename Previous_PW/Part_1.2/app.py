# app.py

# Import the Flask module
from flask import Flask

# Import the PyMongo module to interact with MongoDB
from pymongo import MongoClient

# Create a Flask application instance
app = Flask(__name__)

# Connect to the MongoDB container
# We use the hostname "mongodb" to connect to the MongoDB container
# as it will be automatically resolved to the IP address of the container
# within the Docker network
client = MongoClient("mongodb://mongodb:27017/")

# Get a reference to the test_database
db = client.test_database

# Get a reference to the test_collection
collection = db.test_collection

# Let's insert some datatest in the DB
users = [{'name': 'Jon Smith', 'age': 54}, {'name': 'Mc Flurry', 'age': 30}]
collection.insert_many(users)

# Define the route for the index page
@app.route("/")
def index():
    # Fetch a single document from the test_collection
    data = collection.find_one()
    
    with open("toBeRead.txt", "r") as f:
        content = f.read()

    # Return the fetched data as a string
    return str(data) + "\n" + content

# Start the Flask application if this file is being executed as the main script
if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")
