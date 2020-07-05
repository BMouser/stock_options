import argparse
import csv
from datetime import timedelta, datetime, date
import json
from dateutil import relativedelta, rrule
from dateutil.parser import parse


def months_between(start_date, end_date):
    return (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


def print_schedule(schedule):
    for month, money in schedule.items():
        print(f'{month} - {money:.2f}')


def minimum(grants):
    schedule = {}
    current_month = date.today().replace(day=1)
    for grant in grants:
        remaining_months = months_between(current_month, grant['expire'])
        total = grant['quantity'] * grant['strike_price']
        average = total / remaining_months
        print(average)
        for dt in rrule.rrule(rrule.MONTHLY, dtstart=current_month, until=grant['expire']):
            dt = dt.strftime("%m-%d-%Y")
            schedule[dt] = schedule.get(dt, 0.0) + average
    print_schedule(schedule)


def calculate(input_file):
    grants = []
    csv_file = csv.DictReader(open(input_file))
    for row in csv_file:
        row['quantity'] = int(row['quantity'])
        row['strike_price'] = float(row['strike_price'])
        row["start"] = parse(row["start"])
        row["expire"] = row["start"].replace(year=row["start"].year + 10)
        grants.append(row)

    minimum(grants)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", help="The csv with stock option information")
    args = parser.parse_args()

    calculate(args.input_file)
