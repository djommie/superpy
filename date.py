import datetime


def get_date():
    with open('./data/date.txt', 'r') as file:
        for line in file:
            return line


def print_date():
    date = ''
    with open('./data/date.txt', 'r') as file:
        for line in file:
            date = line
    print(f'The current system date is: {date}')


def set_date_today():
    # Get today's date and write it to the txt file
    today = str(datetime.date.today())
    with open('./data/date.txt', 'w') as file:
        file.write(today)
    print(f'The date is now sate to the date of today: {today}')


def advance_date():
    # advance the date by given number of days
    try:
        days = int(input(
            'Please tell me how many days you would like to travel into the future: '))
        today = datetime.datetime.strptime(get_date(), '%Y-%m-%d').date()
        new_date = today + datetime.timedelta(days=days)
        with open('./data/date.txt', 'w') as file:
            file.write(str(new_date))
            print(f'The new date is now {new_date}.')
    except ValueError:
        print('Error: Please try again and enter a valid number.')
