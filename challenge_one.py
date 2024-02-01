"""
@filename challenge_one.py
@author abbybrown
@date 01/31/24

    A coding challenge that allows the user to look up Montana license plate county numbers
    and gain details about the county seat and county(ies) corresponding with the number.
"""
FILE_NAME = "MontanaCounties.csv"


def file_to_dictionary(filename):
    my_dict = {}
    try:
        with open(filename, 'r') as file:
            # skip the first line of column headers
            next(file)
            for line in file:
                data = line.strip().split(',')
                key = int(data[-1])
                values = data[0:2]
                my_dict[key] = values

        return my_dict

    except FileNotFoundError:
        print(f"I'm sorry, {filename} does not exist.")

    except ValueError:
        print(f"I'm sorry, the key in your new dictionary had an improper numeric entry.")


def do_the_search(my_dict, num):
    for plate, values in my_dict.items():
        if num == plate:
            return values
    return False


if __name__ == "__main__":
    running = True
    counties = file_to_dictionary(FILE_NAME)
    while running:
        try:
            print("\n* * * License Plate Search * * * ")
            user_input = int(input("Please enter a number for lookup or 0 to quit > "))
            search_results = do_the_search(counties, user_input)
            if user_input != 0:
                if search_results:
                    print(f"License plate number {user_input} details:")
                    print(f"County: {search_results[0]}")
                    print(f"County Seat: {search_results[1]}")
                else:
                    print("We do not have that number in our registry! Please try again.")
            else:
                print("Thank you for using our lookup services. Goodbye!")
                break

        except ValueError:
            print("I'm sorry, that is not a valid integer. Please try again...")
            continue
