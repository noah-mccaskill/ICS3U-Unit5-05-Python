#!/usr/bin/env python3

# Created by Noah McCaskill
# Created June 2022
# This program properly formats a canadian postal address with user input.


def address_format(
    name, street_number, street_info, city, province, postal_code, apartment_number=None
):
    # this function formats a postal address

    # process
    if apartment_number is not None:
        postal_address = (
            name.upper()
            + "\n"
            + apartment_number.upper()
            + "-"
            + street_number.upper()
            + " "
            + street_info.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + "  "
            + postal_code.upper()
        )
    else:
        postal_address = (
            name.upper()
            + "\n"
            + street_number.upper()
            + " "
            + street_info.upper()
            + "\n"
            + city.upper()
            + " "
            + province.upper()
            + "  "
            + postal_code.upper()
        )

    return postal_address


def main():
    # this function gets input, calls a function, gives output
    print("This program formats a mailing address using your information.")
    print("")

    apartment_number = None

    # input
    name = input("Enter your full name: ")
    ask_apartment = input("Do you live in an apartment? (y/n): ")
    if ask_apartment.upper() == "Y" or ask_apartment.upper() == "YES":
        apartment_number = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_info = input("Enter your street name and type (ex. Main St): ")
    city = input("Enter your city: ")
    province = input("Enter your province (abbreviated, ex. ON): ")
    postal_code = input("Enter your postal code: ")

    try:
        # will skip to exception if numbers are not integers
        if apartment_number is not None:
            apartment_check = int(apartment_number)
        street_check = int(street_number)

        # function calls
        if apartment_number is not None:
            postal_address = address_format(
                name,
                street_number,
                street_info,
                city,
                province,
                postal_code,
                apartment_number,
            )
        else:
            postal_address = address_format(
                name,
                street_number,
                street_info,
                city,
                province,
                postal_code,
            )

        # output
        print("")
        print(postal_address)

    except Exception:
        print(
            "\nYour information is invalid. "
            "Please verify it is accurate and resubmit."
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
