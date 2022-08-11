# Available Meet Time

This project takes in Mate object with the busy time ranges and list the time windows available to meet between mates.

## To execute the project:

Execute `python3 main.py`

## ADD Mates and Times

Just create a new Mate object in the main.py file and use the add_busy_range method like in the example below:

    mate = Mate("mate")
    mate.add_busy_range(TimeRange(start_time="HH:MM", end_time="HH:MM"))

## Screenshot of this project.

![Bill](https://raw.githubusercontent.com/mcostabile/FreeTimeRanges/main/example.png)
