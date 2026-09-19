import argparse
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

FEATURES = ["study_hours", "attendance", "previous_marks", "assignments"]
TARGET = "passed"


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    data = pd.read_csv(path)
    required = FEATURES + [TARGET]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return data


def train_model(data: pd.DataFrame):
    X = data[FEATURES]
    y = data[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return model, X_test, y_test, predictions, accuracy


def predict_student(model):
    print("\nEnter student details")
    study = float(input("Study hours per day (1-10): "))
    attendance = float(input("Attendance percentage (0-100): "))
    previous = float(input("Previous marks (0-100): "))
    assignments = float(input("Assignment score (0-100): "))

    sample = pd.DataFrame(
        [[study, attendance, previous, assignments]],
        columns=FEATURES
    )
    prediction = int(model.predict(sample)[0])
    probability = float(model.predict_proba(sample)[0][prediction])

    result = "PASS" if prediction == 1 else "FAIL"
    print(f"\nPrediction: {result}")
    print(f"Model confidence for predicted class: {probability * 100:.2f}%")


def main():
    parser = argparse.ArgumentParser(
        description="Student Performance Prediction using Logistic Regression"
    )
    parser.add_argument(
        "--data",
        default="data/student_data.csv",
        help="Path to the CSV dataset"
    )
    args = parser.parse_args()

    data = load_data(Path(args.data))
    print("Student Performance Prediction Using Machine Learning")
    print("------------------------------------------------------")
    print(f"Records: {len(data)}")

    model, X_test, y_test, predictions, accuracy = train_model(data)

    print(f"Test accuracy: {accuracy * 100:.2f}%")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification Report:")
    print(classification_report(
        y_test, predictions, target_names=["Fail", "Pass"], zero_division=0
    ))

    predict_student(model)


if __name__ == "__main__":
    main()
