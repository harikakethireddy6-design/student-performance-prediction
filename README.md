# Student Performance Prediction

## Overview
This project builds a simple machine learning system to predict whether a student will pass or fail based on academic and behavioral indicators such as study hours, attendance, prior marks, and assignment scores. The model uses a supervised learning approach and is implemented as a command-line application.

The goal is to demonstrate a complete data science workflow from dataset loading and preprocessing to model training, evaluation, and real-time prediction.

## Problem Statement
Student performance depends on multiple factors, and many institutions want a quick way to estimate whether a student is likely to succeed. This project models that prediction problem using a binary classification approach where:

- 0 = Fail
- 1 = Pass

## Objectives
- Prepare and inspect a student dataset.
- Train a classification model using supervised learning.
- Evaluate the model with standard metrics.
- Accept new input values from the terminal and predict pass/fail outcome.
- Provide an easy-to-run project structure for academic assignments and demos.

## Tech Stack
- Python 3.9+
- Pandas
- scikit-learn
- Logistic Regression
- Command-line interface (CLI)

## Model Used
The project uses Logistic Regression because the target is binary. It is simple to train, fast to run, and suitable for small tabular datasets.

## Dataset
The dataset is stored in the data folder as student_data.csv. It contains the following columns:

- study_hours
- attendance
- previous_marks
- assignments
- passed

### Feature Description
- study_hours: Daily study hours
- attendance: Attendance percentage
- previous_marks: Marks obtained in previous exams
- assignments: Assignment score
- passed: Binary target variable for pass/fail prediction

## Project Structure
```text
student-performance-prediction/
├── data/
│   └── student_data.csv
├── src/
│   └── main.py
├── .gitignore
├── README.md
├── requirements.txt
├── PROJECT_REPORT.docx
├── SUBMISSION_CHECKLIST.txt
├── sample_input.txt
└── .venv/
```

## Requirements
The project depends on:

- Python 3.9 or newer
- pip
- pandas
- scikit-learn

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Setup Instructions
### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Project
From the project root, run:

```bash
python src/main.py
```

You can also point to a custom dataset path:

```bash
python src/main.py --data data/student_data.csv
```

## How the Program Works
The script performs the following steps:

1. Loads the dataset.
2. Validates that all required columns exist.
3. Splits the data into training and testing sets.
4. Trains a Logistic Regression model.
5. Evaluates the model using accuracy, confusion matrix, and classification report.
6. Prompts the user to enter a student's details.
7. Predicts whether the student will pass or fail.

## Example Input
```text
Study hours per day (1-10): 7
Attendance percentage (0-100): 85
Previous marks (0-100): 75
Assignment score (0-100): 80
```

## Example Output
```text
Student Performance Prediction Using Machine Learning
------------------------------------------------------
Records: 80
Test accuracy: 68.75%

Confusion Matrix:
[[3 4]
 [1 8]]

Classification Report:
              precision    recall  f1-score   support

        Fail       0.75      0.43      0.55         7
        Pass       0.67      0.89      0.76         9

    accuracy                           0.69        16

Enter student details
Study hours per day (1-10): 7
Attendance percentage (0-100): 85
Previous marks (0-100): 75
Assignment score (0-100): 80

Prediction: PASS
Model confidence for predicted class: 99.33%
```

## Important Notes
- The dataset is synthetic and intended for learning and coursework.
- Real student outcomes depend on more variables than the four features used here.
- The model is not suitable for high-stakes decisions without additional validation.
- Accuracy may vary based on train/test splits and dataset size.

## Limitations
- Small dataset size
- Synthetic data rather than real institutional records
- No advanced hyperparameter tuning
- No cross-validation or feature engineering beyond the basic setup

## Future Improvements
- Add cross-validation
- Try multiple algorithms such as Decision Tree, Random Forest, or SVM
- Tune model parameters for better accuracy
- Add visual charts and model insight reports
- Deploy as a web or API service

## Academic/Project Use
This project is suitable for:
- ML coursework
- beginner-level classification demonstrations
- prediction app prototypes
- educational assignments involving logistic regression

## Author Information
Add the following before formal submission:

- Student Name
- Register Number
- Course Name
- Institution Name
- Department or Major

## Project Status
The project is currently working and has been validated in a Python environment with the required dependencies installed.
