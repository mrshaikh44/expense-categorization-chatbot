# expense-categorization-chatbot
A rule-based expense categorization chatbot using Python &amp; Flask

---

# `expense-categorization-chatbot/README.md`

```markdown
# Expense Categorization Chatbot

## Description
A lightweight chatbot that categorizes expense texts into categories like `Food`, `Transport`, `Shopping`, `Bills`, etc. Useful as a backend demo for expense management apps. This repo includes a minimal Flask API and a simple rule-based classifier. Can be extended with ML models.

## Features
- Accepts natural-language transaction descriptions.
- Returns a category and confidence score (rule-based).
- Simple REST API for integration with frontend apps.

## Tech Stack
- Python 3.x
- Flask (API)
- Optional: scikit-learn / nltk for ML improvements

## Minimal Flask + Rule-based Example
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

CATEGORIES = {
    "food": ["restaurant", "cafe", "diner", "pizza", "burger", "coffee"],
    "transport": ["uber", "ola", "bus", "train", "taxi", "flight"],
    "shopping": ["amazon", "flipkart", "store", "mall"],
    "bills": ["electricity", "water", "internet", "bill", "rent"]
}

def categorize(text):
    t = text.lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in t:
                return {"category": cat, "confidence": 0.9}
    return {"category": "others", "confidence": 0.5}

@app.route("/categorize", methods=["POST"])
def api_categorize():
    data = request.json or {}
    text = data.get("text","")
    if not text:
        return jsonify({"error":"text required"}), 400
    return jsonify(categorize(text))

if __name__ == "__main__":
    app.run(debug=True)
