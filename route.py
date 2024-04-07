import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kastu0308",
    database="dbms"
)
cursor = conn.cursor()

iata = input("Enter the IATA code: ")

cursor.execute(f"SELECT airports.*, countries.* FROM airports JOIN countries ON airports.country_code = countries.code WHERE airports.iata='{iata}'")
data = cursor.fetchone()

if data:
    print("Data:")
    print(data)
else:
    print("No data found for the given IATA code.")

conn.close()