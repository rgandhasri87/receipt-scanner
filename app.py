from flask import Flask, jsonify, request

# actual receipt data model yet to be decided.
# This is just for a mock response
MOCK_RECEIPT = {
    "store": "Mock Grocery",
    "date": "2026-09-24",
    "line_items": [
        {"name": "ORG BANANAS", "quantity": 1, "price": 1.99},
        {"name": "WHOLE MILK 1GAL", "quantity": 1, "price": 3.49},
        {"name": "EGGS LG 12CT", "quantity": 2, "price": 2.79},
    ],
    "total": 10.06,
}


def create_app():
    app = Flask(__name__)

    @app.post("/receipts")
    def create_receipt():
        image = request.files.get("image")
        if image is None or image.filename == "":
            return jsonify(error="missing 'image' file field"), 400
        return jsonify(MOCK_RECEIPT), 200

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
