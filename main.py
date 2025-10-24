# Importing FastAPI (this is the main framework we use to build APIs)
from fastapi import FastAPI

# Importing json so we can read data from patients.json
import json

# Creating an app object — this starts the FastAPI engine
app = FastAPI(title="Patient Management System API")


# ---------- Helper function to load patient data ----------

def load_data():
    
    with open('patients.json', 'r') as f:    # Open the patients.json file in read mode
        data = json.load(f)  # Convert JSON text into a Python dict
    return data  # Return all patient records


# ---------- Home Route ----------
# When someone visits the ROOT URL ( / ), run this function
@app.get("/")
def hello():
    # Send a simple welcome message (JSON response)
    return {"message": "Patient Management System API"}


# ---------- About Route ----------
# If someone opens: http://127.0.0.1:8000/about
@app.get("/about")
def about():
    # Short description of what this hospital API does
    return {"message": "A fully functional API to manage your patient records"}


# ---------- View Route ----------
# If someone opens: http://127.0.0.1:8000/view
@app.get("/view")
def view():
    # Load patient data from the JSON file
    data = load_data()
    # Return the full dataset as-is
    return data
