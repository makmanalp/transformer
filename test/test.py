
from transformer import Document, Schema


import csv

class NewSchema(Schema):

    Name        = Column(source="B")
    Date        = Column(source=1, transform=transforms.date.format_to_format())
    Addr        = Column(source="D")
    PriceData   = Column(source="C", transform=transforms.number.string_to_decimal(), title="Price Data")

    _ordering = [Name, Date, Addr, PriceData]

with open("sample_old.txt", "r") as f:
    old_doc  = Document(csv.reader(f))
    NewSchema.transform(old_doc)
