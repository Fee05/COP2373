import sqlite3
import random
import matplotlib.pyplot as plt


def setup_database(initials):
    """
    Creates the database called population_TM.db and
    populates the initial 2025 data for 10 Florida cities.
    """
    db_name = f"population_{initials}.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Reset table for fresh testing runs
    cursor.execute("DROP TABLE IF EXISTS population")

    # Create the population table
    cursor.execute('''
        CREATE TABLE population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')

    # Initial data for 10 Florida cities for the year 2025
    cities_data = [
        ('Miami', 2025, 455000),
        ('Tampa', 2025, 403000),
        ('Orlando', 2025, 320000),
        ('Jacksonville', 2025, 980000),
        ('North Port', 2025, 85000),
        ('Tallahassee', 2025, 202000),
        ('Fort Lauderdale', 2025, 185000),
        ('Sarasota', 2025, 57000),
        ('Pensacola', 2025, 54000),
        ('Gainesville', 2025, 145000)
    ]

    cursor.executemany("INSERT INTO population VALUES (?, ?, ?)", cities_data)
    conn.commit()
    conn.close()
    return db_name


def simulate_growth(db_name):
    """
    Simulates population growth and decline for 20 years
    at random rates and inserts the results into the DB.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Pull the 2025 starting numbers
    cursor.execute("SELECT city, population FROM population WHERE year = 2025")
    initial_rows = cursor.fetchall()

    for city, start_pop in initial_rows:
        current_pop = start_pop
        data_to_insert = []

        # Calculate for years 2026 through 2045
        for year in range(2026, 2046):
            # Random rate between -2% (decline) and +5% (growth)
            rate = random.uniform(-0.02, 0.05)
            current_pop = int(current_pop * (1 + rate))
            data_to_insert.append((city, year, current_pop))

        cursor.executemany("INSERT INTO population VALUES (?, ?, ?)", data_to_insert)

    conn.commit()
    conn.close()


def display_population_chart(db_name):
    """
    Displays the list of cities, asks for user input,
    and plots the population trends using matplotlib.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Retrieve unique cities for the user menu
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    print("\n--- Florida Population Projection Tool ---")
    print("Available Cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    user_input = input("\nEnter the city name exactly as shown above: ").strip()

    if user_input in cities:
        cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (user_input,))
        results = cursor.fetchall()

        years = [row[0] for row in results]
        counts = [row[1] for row in results]

        # Plotting logic
        plt.figure(figsize=(12, 6))
        plt.plot(years, counts, marker='s', color='green', linewidth=2)
        plt.title(f"20-Year Population Projection: {user_input}")
        plt.xlabel("Year")
        plt.ylabel("Total Population")
        plt.xticks(range(2025, 2046, 2))
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()
    else:
        print(f"Error: '{user_input}' is not in the database. Please check spelling.")

    conn.close()


# Main Entry Point
if __name__ == "__main__":
    # Your Initials: TM
    initials_id = "TM"

    # Execute functions in order
    db_path = setup_database(initials_id)
    simulate_growth(db_path)
    display_population_chart(db_path)