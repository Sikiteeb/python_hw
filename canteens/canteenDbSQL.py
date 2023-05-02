import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('diners.db')
c = conn.cursor()

# Create the PROVIDER and CANTEEN tables
c.execute('''
CREATE TABLE IF NOT EXISTS provider (
    id INTEGER PRIMARY KEY,
    provider_name TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS canteen (
    id INTEGER PRIMARY KEY,
    provider_id INTEGER,
    name TEXT,
    location TEXT,
    time_open TEXT,
    time_closed TEXT,
    FOREIGN KEY (provider_id) REFERENCES provider (id)
)
''')

# Insert the providers and canteens
c.execute("INSERT INTO provider (id, provider_name) VALUES (1, 'Rahva Toit')")
c.execute("INSERT INTO provider (id, provider_name) VALUES (2, 'Baltic Restaurants Estonia AS')")
c.execute("INSERT INTO provider (id, provider_name) VALUES (3, 'TTÜ Sport OÜ')")
c.execute("INSERT INTO provider (id, provider_name) VALUES (4, 'Bitt OÜ')")

canteens = [
    (1, 1, 'Economics- and social science building canteen', 'Akadeemia tee 3, SOC-building', '8:30', '18:30'),
    (2, 1, 'Library canteen', 'Akadeemia tee 1/Ehitajate tee 7', '8:30', '19:00'),
    (3, 2, 'Main building Deli cafe', 'Ehitajate tee 5, U01 building', '9:00', '16:30'),
    (4, 2, 'Main building Daily lunch restaurant', 'Ehitajate tee 5, U01 building', '9:00', '16:30'),
    (5, 1, 'U06 building canteen', '', '9:00', '16:00'),
    (6, 2, 'Natural Science building canteen', 'Akadeemia tee 15, SCI building', '9:00', '16:00'),
    (7, 2, 'ICT building canteen', 'Raja 15/Mäepealse 1', '9:00', '16:00'),
    (8, 3, 'Sports building canteen', 'Männiliiva 7, S01 building', '11:00', '20:00'),
]

# Insert canteens
c.executemany("INSERT INTO canteen (id, provider_id, name, location, time_open, time_closed) VALUES (?, ?, ?, ?, ?, ?)",
              canteens)

# Insert IT College canteen separately
c.execute(
    "INSERT INTO canteen (id, provider_id, name, location, time_open, time_closed) VALUES (9, 4, 'bitStop KOHVIK', "
    "'IT College, Raja 4c', '9:30', '16:00')")

# Query for canteens open from 09:00 to 16:20
canteens_open_9_to_1620 = c.execute(
    "SELECT * FROM canteen WHERE time_open <= '9:00' AND time_closed >= '16:20'").fetchall()

# Query for canteens serviced by Baltic Restaurants Estonia AS
canteens_baltic_restaurants = c.execute(
    "SELECT * FROM canteen WHERE provider_id = (SELECT id FROM provider WHERE provider_name = 'Baltic Restaurants "
    "Estonia AS')").fetchall()

# Close the connection

conn.commit()
conn.close()

# Display the queried results

print("Canteens open from 09:00 to 16:20:")
for canteen in canteens_open_9_to_1620:
    print(canteen)

print("\nCanteens serviced by Baltic Restaurants Estonia AS:")
for canteen in canteens_baltic_restaurants:
    print(canteen)
