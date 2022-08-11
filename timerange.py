import helpers as h
from dataclasses import dataclass, field
from datetime import datetime


@dataclass()
class TimeRange:
    start_time: str
    end_time: str

    def __setattr__(self, name, value):
        if name in ["start_time", "end_time"]:
            try:
                datetime.strptime(value, "%H:%M")
                super(TimeRange, self).__setattr__(name, value)
            except TypeError:
                return

        elif name in ["start_minutes", "end_minutes", "range_minutes"]:
            super(TimeRange, self).__setattr__(name, value)

        else:
            raise ValueError

    start_minutes: int = field(init=False, repr=False)
    end_minutes: int = field(init=False, repr=False)
    range_minutes: range = field(init=False, repr=False)

    def __post_init__(self):
        self.start_minutes = h.timerange_to_minutes(self.start_time)
        self.end_minutes = h.timerange_to_minutes(self.end_time)
        self.range_minutes = range(self.start_minutes, self.end_minutes, 1)
