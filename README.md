Transformer
===========

Transformer is not a robot. Transformer wrangles messy CSV-like files so you don't have to. The idea is simple: You write an ORM-like schema for your data files, and transformer does the rest.

Say you pulled a 30-column CSV file from data.gov, like the absentee voting dataset:

https://explore.data.gov/dataset/2008-Uniformed-and-Overseas-Citizens-Absentee-Voti/2tan-w4es

Say also that you just want a few columns. Instead of counting column numbers one by one and writing ugly code to extract them in certain ways, just write a schema:

```python

from transformer import Document, Schema, Column, transforms
import string

class AbsenteeSchema(Schema):

    transform=transforms.number.string_to_integer()

    Name = Column("JurisName", transform=string.capwords)
    A1 = Column("A1", transform=lambda x: x/1000, title="A1 count in thousands")
    City = Column("Location 1")
    State = Column("Location 2")

    _ordering = [Name, A1, City, State]

with open("exported.csv", "r") as f:
    doc = Document(f)
    AbsenteeSchema.transform(doc)

```

As above, you can also describe different transformations, like, parsing and fiddling with date formats or applying regex replacements. Transformer comes with a small set of these already, but writing your own is as easy as writing a python callable. Combining and aggregating data from different columns is also possible.

Different CSV dialects are supported as in the python `csv` module.

Transformer is alpha for all purposes except the ones I use it for, which is why documentation is scarce. The code is fairly well annotated and clear, and your starting point should be the example in the examples/ directory.

Questions, comments, pull requests welcome. Good luck!
