import decimal

class string_to_decimal(object):
    def run(self, val):
        return decimal.Decimal(val)

class string_to_integer(object):
    def run(self, val):
        return int(float(val)) #TODO: this sucks

class string_to_float(object):
    def run(self, val):
        return float(val)
