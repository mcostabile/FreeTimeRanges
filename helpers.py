def timerange_to_minutes(timerange_str):
    '''
    Return amount of minutes for timerange in format HH:MM
    :param timerange_str:
    :return:
    '''
    hour = int(timerange_str.split(":")[0])
    minutes = int(timerange_str.split(":")[1])
    time_in_minutes = hour * 60 + minutes

    return time_in_minutes


def minutes_to_timerange_str(m):
    '''
    Return a timerange string in format of HH:MM for the given integer
    :param timerange_str:
    :return:
    m = 90 -> 01:30
    '''
    hour = m // 60
    hour_str = f"{hour:02d}"
    minutes = m % 60
    minutes_str = f"{minutes:02d}"

    return f"{hour_str}:{minutes_str}"


def prettify_available_minutes(l: list):
    grouped_list = []
    list_resettable = []
    for element in l:
        if list_resettable == []:
            list_resettable.append(element)
            continue
        if list_resettable[-1] + 1 == element:
            list_resettable.append(element)
        else:
            grouped_list.append(list_resettable[:])
            list_resettable.clear()
            list_resettable.append(element)
    grouped_list.append(list_resettable)

    time_ranges = []
    for group in grouped_list:
        start_time = minutes_to_timerange_str(m=group[0])
        end_time = minutes_to_timerange_str(m=group[-1])
        time_range_str = f"{start_time} - {end_time}"
        time_ranges.append(time_range_str)

    return time_ranges
