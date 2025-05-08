from pydantic import BaseModel

class FormData(BaseModel):
    partname=str
    hr_qty=int
    qty_price=int
    