import time

class format_to_format(object):

    def __init__(self, from_format="", to_format=None):
        self.from_format = from_format
        self.to_format = to_format

    def run(self, val):
        time_tuple = time.strptime(val, self.from_format)
        if not self.to_format:
            return time.mktime(time_tuple)
        else:
            return time.strftime(self.to_format, time_tuple)
