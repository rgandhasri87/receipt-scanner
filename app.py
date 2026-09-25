from fastapi import FastAPI, UploadFile

from models import LineItem, Receipt

MOCK_RECEIPT = Receipt(
    store="Mock Grocery",
    date="2026-01-01",
    line_items=[
        LineItem(name="ORG BANANAS", quantity=1, price=1.99),
        LineItem(name="WHOLE MILK 1GAL", quantity=1, price=3.49),
        LineItem(name="EGGS LG 12CT", quantity=2, price=2.79),
    ],
    total=10.06,
)

app = FastAPI(title="Receipt Scanner")


@app.post("/receipts")
async def create_receipt(image: UploadFile) -> Receipt:
    return MOCK_RECEIPT
