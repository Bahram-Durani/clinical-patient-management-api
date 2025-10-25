# Importing FastAPI (this is the main framework we use to build APIs)
from fastapi import FastAPI, Path, HTTPException, Query  

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



@app.get('/patient/{patient_id}')   # GET endpoint → e.g. /patient/P001
def view_patient(
    patient_id: str = Path(..., description='Patient ID in DB', example='P001')  # path param with description + example
):
    data = load_data()  # Load all patients

    if patient_id in data:  # If patient exists
        return data[patient_id]  # Return their info

    raise HTTPException(status_code=404, detail="Patient not found")


@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='Sort by: height, weight, or bmi'),
    order: str = Query('asc', description='Sort order: asc or desc')  # default = asc
):
    valid_fields = ['height', 'weight', 'bmi']  # allowed sort fields

    if sort_by not in valid_fields:  # validate field name
        raise HTTPException(status_code=400, detail=f'Invalid field. Choose from {valid_fields}')

    if order not in ['asc', 'desc']:  # validate order
        raise HTTPException(status_code=400, detail='Invalid order. Use asc or desc')

    data = load_data()  # load data

    sort_order = True if order == 'desc' else False  # True = reverse sorting

    # sort list of patients by the given key
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data  # return sorted results



