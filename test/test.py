from transformer import Document, Schema

class NewSchema(Schema):

    Name        = Column(source=Ref(title="B"))
    Date        = Column(source=Ref(index=1), transform=transforms.date.format_to_format())
    Addr        = Column(source=Ref(title="D"))
    PriceData   = Column(source=Ref(title="C"), transform=transforms.number.string_to_decimal(), title="Price Data")

    _ordering = [Name, Date, Addr, PriceData]

with open("sample_old.txt", "r") as f:
    old_doc  = Document(f)
    NewSchema.transform(old_doc)

