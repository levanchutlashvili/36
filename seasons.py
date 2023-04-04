from datetime import datetime
import inflect


def main():
    birth_date = input("Please enter your date of birth in YYYY-MM-DD format: ")

    try:
        age_in_minutes = calculate_age_in_minutes(birth_date)
        age_in_words = minutes_to_words(age_in_minutes)
        print("You are", age_in_words, "old.")
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")


def minutes_to_words(minutes):
    p = inflect.engine()
    hours = minutes // 60
    remaining_minutes = minutes % 60

    if hours == 0:
        return p.number_to_words(minutes) + " minutes"
    else:
        return p.number_to_words(hours) + " hours " + p.number_to_words(remaining_minutes) + " minutes"


def calculate_age_in_minutes(birth_date):
    birth_datetime = datetime.strptime(birth_date, "%Y-%m-%d")
    today_datetime = datetime.today()
    minutes_difference = round((today_datetime - birth_datetime).total_seconds() / 60)
    return minutes_difference


if __name__ == "__main__":
    main()