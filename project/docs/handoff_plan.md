# Handoff Plan

- **Deployment path:**  
  The project is prepared and tested locally in `project/`. The prediction model is saved to `model/model.pkl`, the Flask API is defined in `app.py`, and the full analytical workflow is maintained in `notebooks/project_pipeline.ipynb`.

- **Environment setup:**  
  A new user should clone the repository, create the Python environment using `requirements.txt`, and confirm that `.env.example` has been copied to `.env` with the correct local data path settings before running the project.

- **Starting the API:**  
  From the `project/` directory, start the prediction service with:
  ```bash
  python app.py