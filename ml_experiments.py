# ml_experiments.py
"""
Simple ML experiments for the Mood Machine lab.

This file uses a "real" machine learning library (scikit-learn)
to train a tiny text classifier on the same SAMPLE_POSTS and
TRUE_LABELS that you use with the rule based model.
"""

from typing import List, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from dataset import SAMPLE_POSTS, TRUE_LABELS


def train_ml_model(
    texts: List[str],
    labels: List[str],
) -> Tuple[TfidfVectorizer, LogisticRegression]:
    """
    Train a simple text classifier using TF-IDF features
    and logistic regression.

    This keeps the original structure of the project, but
    uses a more realistic ML setup for a tiny dataset.
    """
    if len(texts) != len(labels):
        raise ValueError(
            "texts and labels must be the same length. "
            "Check SAMPLE_POSTS and TRUE_LABELS in dataset.py."
        )

    if not texts:
        raise ValueError("No training data provided. Add examples in dataset.py.")

    X_train, X_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.3,
        random_state=42,
    )

    vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
    )
    model.fit(X_train_vec, y_train)

    X_test_vec = vectorizer.transform(X_test)
    preds = model.predict(X_test_vec)

    print("=== ML Model Evaluation on Test Set ===")
    for text, true_label, pred_label in zip(X_test, y_test, preds):
        print(f'"{text}" -> predicted={pred_label}, true={true_label}')

    accuracy = accuracy_score(y_test, preds)
    print(f"\nAccuracy on this dataset: {accuracy:.2f}")
    return vectorizer, model


def evaluate_on_dataset(
    texts: List[str],
    labels: List[str],
    vectorizer: TfidfVectorizer,
    model: LogisticRegression,
) -> float:
    """
    Evaluate the trained model on a labeled dataset.

    Prints each text with its predicted label and the true label,
    then returns the overall accuracy as a float between 0 and 1.
    """
    if len(texts) != len(labels):
        raise ValueError(
            "texts and labels must be the same length. "
            "Check your dataset."
        )

    X = vectorizer.transform(texts)
    preds = model.predict(X)

    print("=== ML Model Evaluation on Dataset ===")
    for text, true_label, pred_label in zip(texts, labels, preds):
        print(f'"{text}" -> predicted={pred_label}, true={true_label}')

    accuracy = accuracy_score(labels, preds)
    print(f"\nAccuracy on this dataset: {accuracy:.2f}")
    return accuracy


def predict_single_text(
    text: str,
    vectorizer: TfidfVectorizer,
    model: LogisticRegression,
) -> str:
    """
    Predict the mood label for a single text string using
    the trained ML model.
    """
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    return pred


def run_interactive_loop(
    vectorizer: TfidfVectorizer,
    model: LogisticRegression,
) -> None:
    """
    Let the user type their own sentences and see the ML model's
    predicted mood label.

    Type 'quit' or press Enter on an empty line to exit.
    """
    print("\n=== Interactive Mood Machine (ML model) ===")
    print("Type a sentence to analyze its mood.")
    print("Type 'quit' or press Enter on an empty line to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input == "" or user_input.lower() == "quit":
            print("Goodbye from the ML Mood Machine.")
            break

        label = predict_single_text(user_input, vectorizer, model)
        print(f"ML model: {label}")


if __name__ == "__main__":
    print("Training an ML model on SAMPLE_POSTS and TRUE_LABELS from dataset.py...")
    print("Make sure you have added enough labeled examples before running this.\n")

    vectorizer, model = train_ml_model(SAMPLE_POSTS, TRUE_LABELS)

    # Optional: evaluate on the full dataset as a sanity check
    # evaluate_on_dataset(SAMPLE_POSTS, TRUE_LABELS, vectorizer, model)

    run_interactive_loop(vectorizer, model)

    print("\nTip: Compare these predictions with the rule based model")
    print("by running `python main.py`. Notice where they fail in")
    print("similar ways and where they fail in different ways.")