from timerange import TimeRange
from dataclasses import dataclass, field
from typing import ClassVar
from custom_list import CustomList
import helpers as h


@dataclass()
class Mate:
    name: str
    busy_time_ranges: list[TimeRange] = field(default_factory=list, repr=False)
    all_busy_minutes_range: ClassVar[list] = []

    def add_busy_range(self, obj: TimeRange):
        self.busy_time_ranges.append(obj)
        # Add the minutes range object to the class attribute
        Mate.all_busy_minutes_range.append(obj.range_minutes)

    @staticmethod
    def show_available_time():
        available_minutes = CustomList(range(1440))
        for m in available_minutes[:]:
            for r in Mate.all_busy_minutes_range:
                if m in r:
                    available_minutes.remove_if_exist(m)

        print(f"Available time windows to meet for all the mates:")
        for tr in h.prettify_available_minutes(available_minutes):
            print(f"\U00002705  {tr}")
