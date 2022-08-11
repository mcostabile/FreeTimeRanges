from timerange import TimeRange
from mate import Mate


def main():
    mate = Mate("mate")
    mate.add_busy_range(TimeRange(start_time="09:00", end_time="13:00"))

    Mate.show_available_time()


if __name__ == __name__:
    main()
