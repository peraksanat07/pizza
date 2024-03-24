import sqlite3
import csv

# Connect to SQLite database (creates new database if not exists)
conn = sqlite3.connect('pizza_shop.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create PizzaTypes table
cur.execute('''CREATE TABLE PizzaTypes (
                pizza_id INTEGER PRIMARY KEY,
                pizza_name TEXT)''')

# Create Bases table
cur.execute('''CREATE TABLE Bases (
                base_id INTEGER PRIMARY KEY,
                base_name TEXT)''')

# Create Toppings table
cur.execute('''CREATE TABLE Toppings (
                topping_id INTEGER PRIMARY KEY,
                topping_name TEXT)''')

# Create PizzaComposition table
cur.execute('''CREATE TABLE PizzaComposition (
                composition_id INTEGER PRIMARY KEY,
                pizza_id INTEGER,
                base_id INTEGER,
                topping_id INTEGER,
                FOREIGN KEY (pizza_id) REFERENCES PizzaTypes(pizza_id),
                FOREIGN KEY (base_id) REFERENCES Bases(base_id),
                FOREIGN KEY (topping_id) REFERENCES Toppings(topping_id))''')

# Read data from CSV files and insert into tables
def read_csv_and_insert(file_path, table_name):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            cur.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(row))})", row)

# Import data into PizzaTypes table
read_csv_and_insert('pizza_types.csv', 'PizzaTypes')

# Import data into Bases table
read_csv_and_insert('bases.csv', 'Bases')

# Import data into Toppings table
read_csv_and_insert('toppings.csv', 'Toppings')

# Import data into PizzaComposition table
read_csv_and_insert('pizza_composition.csv', 'PizzaComposition')

# Commit changes and close connection
conn.commit()
conn.close()