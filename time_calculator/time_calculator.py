def add_time(start, duration, day=False):
    """
    Args: takes two required args and one optional parameter
        start: a start time in the 12-hour clock format (ending in AM or PM)
        duration: a duration time that indicates the number of hours and minutes
        (optional): a starting day of the week -- case sensitive
    """

    week = ''
    week_day = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    ]

    start_time = start
    final_time = duration
    time_list = start_time.split(':')
    am_pm_time = time_list[-1][-2:]

    # ## START TIME FUNCTION ## #
    if am_pm_time == "PM":
        hours = 12 + int(time_list[0])
    else:
        hours = int(time_list[0])

    minutes = int(time_list[1][:2])

    # ## DURATION FUNCTION ## #
    dur = duration.split(':')

    if am_pm_time == 'PM':
        new_hours = hours + dur - 12
        mins = int(dur[-1])
        new_dur = mins + dur

        if new_dur >= 24:
            try:
                count_day = int(new_hours // 24)
                try:
                    week = week_day[week_day.index(week.title()) + count_day]
                except IOError:
                    week = week_day[week_day.index(week.title()) + count_day]
            except IOError:
                new_hours = new_hours % 24

        if mins >= 60:
            new_hours += mins // 60
            mins = mins % 60
        if mins <= 9:
            mins = str(0) + str(mins % 60)
        if new_hours > 12:
            am_pm_time = 'AM'
            new_hours += 12
        else:
            am_pm_time = 'PM'
        if week_day == '':
            "{}:{} {}".format(new_hours, mins, am_pm_time)

        new_time = "{}:{} {}{} {} {}".format(
            new_hours,
            mins, am_pm_time, ',' if am_pm_time != '' else "",
            week.title(), ('(' + str(count_day) + ' days later' + ')')
            if count_day >= 1 else '')

        return new_time

    if week_day:
        new_time = start_time + final_time + week_day
    else:
        new_time = start_time + final_time

    return new_time
