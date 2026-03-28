import csv


def create_grades_file():
    """Prompts user for student data and writes it to grades.csv."""
    try:
        num_students = int(input("How many students do you want to enter? "))

        # Open file using 'with' keyword for automatic closing
        with open('grades.csv', mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

            for i in range(num_students):
                print(f"\nEntering data for student #{i + 1}:")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")

                # Get exam grades as integers
                exam1 = int(input("Exam 1 Grade: "))
                exam2 = int(input("Exam 2 Grade: "))
                exam3 = int(input("Exam 3 Grade: "))

                # Write student record to CSV
                writer.writerow([first_name, last_name, exam1, exam2, exam3])

        print("\nFile 'grades.csv' has been created successfully.")

    except ValueError:
        print("Error: Please enter valid numbers for student counts and grades.")


def read_and_display_grades():
    """Reads grades.csv and displays data in a formatted table."""
    print("\n" + "-" * 60)
    print(f"{'First Name':<15} {'Last Name':<15} {'Ex 1':<8} {'Ex 2':<8} {'Ex 3':<8}")
    print("-" * 60)

    try:
        with open('grades.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                # Unpack the row for easy formatting
                fname, lname, e1, e2, e3 = row
                # Format using f-strings with alignment (Chapter 5 style)
                print(f"{fname:<15} {lname:<15} {e1:<8} {e2:<8} {e3:<8}")

    except FileNotFoundError:
        print("Error: grades.csv file not found.")


def main():
    """Controls the program flow."""
    create_grades_file()
    read_and_display_grades()


if __name__ == "__main__":
    main()