A tiny FastAPI service to read patient records from a local patients.json file and expose simple endpoints to view, fetch by ID, and sort patients.

Features

	•	GET / — health/welcome.
	•	GET /about — short description.
	•	GET /view — return all patients.
	•	GET /patient/{patient_id} — return a single patient (404 if not found).
	•	GET /sort?sort_by=height|weight|bmi&order=asc|desc — sorted list of patients.

Auto docs:

	•	Swagger UI: http://127.0.0.1:8000/docs
	•	ReDoc: http://127.0.0.1:8000/redoc

Requirements

	•	Python 3.9+
	•	Packages: fastapi, uvicorn
