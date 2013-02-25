Transformer
===========

Transformer is not a robot. Transformer wrangles messy CSV-like files so you don't have to.

The idea is simple: You write an ORM-like schema for your data files, and transformer does the rest.

You can also describe different transformations, like, parsing and fiddling with date formats or applying regex replacements. Transformer comes with a small set of these already, but writing your own is as easy as writing a python callable. Combining and aggregating data from different columns is also possible.

Transformer is alpha for all purposes except the ones I use it for, which is why documentation is scarce. The code is fairly well annotated and clear, and your starting point should be the example in the examples/ directory.

Questions, comments, pull requests welcome. Good luck!
