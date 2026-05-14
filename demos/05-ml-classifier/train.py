"""
A tiny text classifier on the 20 newsgroups corpus.
Scaffolded by Claude Code in ~10 minutes.

Pipeline:
    raw text  →  TF-IDF (1-2grams, sublinear)  →  Linear SVM
    test set accuracy reported + confusion matrix saved.
"""

from pathlib import Path
import json

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.pipeline import Pipeline

HERE = Path(__file__).parent
OUT = HERE / "results.json"

# Four well-separated topics — fast to train, easy to beat baseline.
CATEGORIES = [
    "rec.sport.hockey",
    "sci.space",
    "talk.politics.guns",
    "comp.graphics",
]


def main():
    print(f"  Loading 20-newsgroups subset ({len(CATEGORIES)} topics)...")
    train = fetch_20newsgroups(
        subset="train", categories=CATEGORIES,
        remove=("headers", "footers", "quotes"), random_state=42,
    )
    test = fetch_20newsgroups(
        subset="test", categories=CATEGORIES,
        remove=("headers", "footers", "quotes"), random_state=42,
    )
    print(f"  Train: {len(train.data)} docs  ·  Test: {len(test.data)} docs")
    print(f"  Classes: {', '.join(c.split('.')[-1] for c in train.target_names)}")
    print()

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.9,
                                  sublinear_tf=True, stop_words="english")),
        ("clf", LinearSVC(C=1.0)),
    ])

    print("  Training...")
    model.fit(train.data, train.target)

    preds = model.predict(test.data)
    acc = accuracy_score(test.target, preds)
    cm = confusion_matrix(test.target, preds).tolist()

    print()
    print(f"  Test accuracy:  {acc:.3f}")
    print()
    print("  Confusion matrix (rows = actual, columns = predicted):")
    labels = [c.split(".")[-1][:8] for c in train.target_names]
    header = "             " + "  ".join(f"{l:>8}" for l in labels)
    print(header)
    for i, row in enumerate(cm):
        print(f"  {labels[i]:>10}  " + "  ".join(f"{v:>8}" for v in row))
    print()
    print("  Per-class report:")
    report = classification_report(test.target, preds, target_names=train.target_names)
    for line in report.splitlines():
        print(f"    {line}")

    OUT.write_text(json.dumps({
        "accuracy": round(acc, 4),
        "confusion_matrix": cm,
        "labels": train.target_names,
        "n_train": len(train.data),
        "n_test": len(test.data),
    }, indent=2))
    print()
    print(f"  Saved metrics to {OUT.name}")


if __name__ == "__main__":
    main()
