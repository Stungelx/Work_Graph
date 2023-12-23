from datetime import datetime, timedelta


def working_days(days: int, work_days: int, rest_days: int, start_date: datetime) ->list:
    day_of_work = ([start_date])
    current_date = start_date
    left_of_work_day = work_days-1
    left_of_rest_day = rest_days
    for i in range(1, days):
        current_date += timedelta(days=1)
        if left_of_work_day > 0:
            day_of_work.append(current_date)
            left_of_work_day -= 1
        elif left_of_rest_day > 0:
            left_of_rest_day -= 1
        else:
            left_of_work_day = work_days-1
            left_of_rest_day = rest_days
            day_of_work.append(current_date)

    return (day_of_work)

print(working_days(14, 5, 2, datetime(2020, 1, 30)))