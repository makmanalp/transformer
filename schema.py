
class Schema(object):

    _ordering = []

    @staticmethod
    def transform(document):
        if hasattr(document, "header"):
            document.reader.next()
        for line in document.reader:
            print line

