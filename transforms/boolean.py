
class boolean(object):
    """
    Common boolean values:
    True    False
    t       f
    true    false
    y       n
    yes     no
    on      off
    1       0
    """

    true  = [True, "t", "true", "y", "yes", "on", "1", 1]
    false = [False, "f", "false", "n", "no", "off", "0", 0]

    def __init__(self, invert=False):
        """
        invert will return the opposite of the parsed value.
        """
        self.invert = invert

    def run(self, val):
        if isinstance(val, basestring):
            processed = val.strip().lower()
        if processed in boolean.true:
            return True != self.invert
        elif processed in boolean.false:
            return False != self.invert
        else:
            return None
