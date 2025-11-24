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
