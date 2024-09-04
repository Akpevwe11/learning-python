class Date(object):
    def __init__(self, year = 0, month = 0, day = 0):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return cls(year, month, day)

    @staticmethod
    def is_date_valid(date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        return month <= 12 and day <= 31

date1 = Date.from_string('2020-10-10')
print(date1.year, date1.month, date1.day)
print(Date.is_date_valid('2020-10-10'))