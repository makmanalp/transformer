from transformer import Document, Schema, Column, transforms

class NewSchema(Schema):

    Name        = Column("B")
    Date        = Column(0, transform=transforms.date.format_to_format("%Y%m%d", "%m-%d-%Y"))
    Addr        = Column("D")
    PriceData   = Column("C", transform=transforms.number.string_to_integer(), title="Price Data")

    _ordering = [Name, Date, Addr, PriceData]

with open("test/sample_old.tsv", "r") as f:
    old_doc  = Document(f)
    NewSchema.transform(old_doc)
