from timerange import TimeRange
from mate import Mate


def main():
    m1 = Mate("mate1")
    m1.add_busy_range(TimeRange(start_time="08:00", end_time="14:00"))
    m2 = Mate("mate2")
    m2.add_busy_range(TimeRange(start_time="10:00", end_time="17:00"))
    m3 = Mate("mate3")
    m3.add_busy_range(TimeRange(start_time="20:00", end_time="23:00"))

    Mate.show_available_time()


if __name__ == __name__:
    main()
