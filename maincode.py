import csv
import random

def poll_ultrasonic():
 
    #SIMULATES DATA FROM ULTRASONIC MIC
    return random.randint(10, 100)

# Create a CSV file and write the data
csv_filename = "sensor_data.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Sunlight Level', 'Water Level', 'Watering Duration', 'Sunlight Duration', 'Nutrients', 'Ultrasonic Values']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
  
    #SIMULATING USER INPUT
    # Loop 1000 times to generate 1000 rows of data
    for _ in range(1000):
        # Generate random values for user inputs
        sunlight_level = random.uniform(0, 100)  # Random sunlight level between 0 and 100
        water_level = random.uniform(0, 100)  # Random water level between 0 and 100
        watering_duration = random.randint(10, 300)  # Random duration of watering between 10 and 300 seconds
        sunlight_duration = random.randint(10, 300)  # Random duration of sunlight exposure between 10 and 300 seconds
        nutrients_array = [random.uniform(0, 10) for _ in range(5)]  # Generate 5 random nutrient values between 0 and 10

        # Collect ultrasonic mic values
        ultrasonic_values = []
        for _ in range(5):  # Assuming 5 instances, you can adjust as needed
            ultrasonic_values.append(poll_ultrasonic())

        # Write the row to the CSV file
        writer.writerow({
            'Sunlight Level': sunlight_level,
            'Water Level': water_level,
            'Watering Duration': watering_duration,
            'Sunlight Duration': sunlight_duration,
            'Nutrients': nutrients_array,
            'Ultrasonic Values': ultrasonic_values
        })

print(f"CSV file '{csv_filename}' has been generated with 1000 rows of random sensor data.")
