from pydantic import BaseModel


class LineItem(BaseModel):
    name: str
    quantity: float
    price: float


class Receipt(BaseModel):
    store: str
    date: str
    line_items: list[LineItem]
    total: float
