class enum(object):
    """Just plug in a dict to give a mapping of strings to other values."""

    def __init__(self, enumdict=None):
        self.enum_dict = enumdict

    def run(self, val):
        if not self.enum_dict:
            self.enum_dict.get(val, None)
