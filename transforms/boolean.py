
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

    def run(self, val):
        if val in boolean.true:
            return True
        elif val in boolean.false:
            return False
        else:
            return None
