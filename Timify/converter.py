class TimeConverter(object):
    def __init__(self, millisecond: int = 0, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, months: int = 0,
                 years: int = 0):

        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.days = days
        self.months = months
        self.years = years
        self.millisecond = millisecond

    def to_seconds(self) -> float:
        """
        Formulas: year to seconds           : (value * 3.154e+7)
                  months to seconds         : (value * 2.628e+6)
                  days to seconds           : (value * 86400)
                  hours to seconds          : (value * 3600)
                  minutes to seconds        : (value * 60)
                  milliseconds to seconds   : (value / 1000)
        """

        total_seconds = sum([
            (self.years * 3.154e+7),
            (self.months * 2.628e+6),
            (self.days * 86400),
            (self.hours * 3600),
            (self.minutes * 60),
            self.seconds,
            (self.millisecond / 1000)
        ])

        return total_seconds

    def to_milliseconds(self) -> float:
        return self.to_seconds() * 1000

    def to_minutes(self) -> float:
        return self.to_seconds() / 60

    def to_hours(self) -> float:
        return self.to_minutes() / 60

    def to_days(self) -> float:
        return self.to_hours() / 24

    def to_months(self) -> float:
        return self.to_days() / 30

    def to_years(self) -> float:
        return self.to_months() / 12
