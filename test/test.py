from transformer import Document, Schema, Column
import csv

class NewSchema(Schema):

    Name        = Column("B")
    Date        = Column(1, transform=transforms.date.format_to_format())
    Addr        = Column("D")
    PriceData   = Column("C", transform=transforms.number.string_to_decimal(), title="Price Data")

    _ordering = [Name, Date, Addr, PriceData]

with open("sample_old.txt", "r") as f:
    old_doc  = Document(csv.reader(f))
    NewSchema.transform(old_doc)
