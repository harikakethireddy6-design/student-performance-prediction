# Commit History

This file documents the project development history and key milestone changes for the Student Performance Prediction project.

## Initial Project Setup
- Created the project structure for a student performance prediction system.
- Added the dataset folder and the main prediction script.
- Added the Python requirements file for machine learning dependencies.
- Initialized the project documentation and submission-related files.

## Dataset Preparation
- Added synthetic student performance dataset in CSV format.
- Included fields for study_hours, attendance, previous_marks, assignments, and passed.
- Ensured the dataset is compatible with a binary classification workflow.

## Model Implementation
- Implemented data loading and validation logic.
- Added train/test splitting with stratification.
- Trained a Logistic Regression model using the selected features.
- Calculated accuracy, confusion matrix, and classification report.

## Prediction Workflow
- Added CLI-based student input prompts.
- Implemented prediction logic for pass/fail outcomes.
- Added probability output for the predicted class.
- Designed the script to run directly from the terminal.

## Environment Setup and Validation
- Installed required Python dependencies.
- Created and configured a virtual environment for project execution.
- Resolved Windows-specific dependency import issue caused by SciPy native library blocking.
- Verified the project runs successfully and produces model output.

## Documentation and Submission Support
- Added README documentation with setup instructions, project goals, and execution steps.
- Added supporting project files for academic submission.
- Kept the project focused on a beginner-friendly machine learning workflow.

## Current Project Status
- Project is functional and executable.
- The model predicts pass/fail based on student metrics.
- Documentation and working project files are in place for submission or further extension.

## Notes
This project is intended for academic or demonstration use. It is not a production-grade system and should be extended with real-world data and validation before use in critical decisions.
