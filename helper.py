def days_to_units(num_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_days} days are {num_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_days} days are {num_days * 24 * 60} {conversion_unit}"
    else:
        return "unsupported unit"


def validate(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a zero")
        else:
            print("You entered negative number")
    except ValueError:
        print("Your input is not a valid number")


user_input_message = "Enter a num of days and conversion unit: \n"
