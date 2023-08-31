import datetime
from sgp4.earth_gravity import wgs84
from sgp4.io import twoline2rv
import pyproj
# Read TLE data from the file
tle_file_path = '30sate.txt'
with open(tle_file_path, 'r') as tle_file:
    tle_lines = tle_file.readlines()

# Initialize a list to store satellite objects
satellites = []

# Iterate through TLE sets (3 lines per set)
for i in range(0, len(tle_lines), 3):
    line1 = tle_lines[i + 1].strip()
    line2 = tle_lines[i + 2].strip()
    satellite = twoline2rv(line1, line2, wgs84)
    satellites.append(satellite)

# Define time range and interval
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(days=1)
time_interval = datetime.timedelta(minutes=1)

# Print header
print("Time, L(x), L(y), L(z), V(x), V(y), V(z)")

# Propagate and print satellite positions
current_time = start_time
while current_time <= end_time:
    output = current_time.strftime('%Y-%m-%d %H:%M:%S')
    for satellite in satellites:
        position, velocity = satellite.propagate(
            current_time.year,
            current_time.month,
            current_time.day,
            current_time.hour,
            current_time.minute,
            current_time.second
        )
        output += f", {position[0]:.4f}, {position[1]:.4f}, {position[2]:.4f}, {velocity[0]:.4f}, {velocity[1]:.4f}, {velocity[2]:.4f}"
    print(output)
    current_time += time_interval




