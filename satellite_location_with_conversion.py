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




def ecef_to_lla(pos_x, pos_y, pos_z):
    ecef = pyproj.Proj(proj="geocent", ellps="WGS84", datum="WGS84")
    lla = pyproj.Proj(proj="latlong", ellps="WGS84", datum="WGS84")
    lon, lat, alt = pyproj.transform(ecef, lla, pos_x, pos_y, pos_z, radians=False)
    return lat, lon, alt

# Read TLE data and create satellite objects

# Define time range and interval
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(days=1)
time_interval = datetime.timedelta(minutes=1)

# Print header
print("Time, Latitude, Longitude, Altitude")

# Propagate, convert, and print satellite positions
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
        lat, lon, alt = ecef_to_lla(position[0], position[1], position[2])
        output += f", {lat:.4f}, {lon:.4f}, {alt:.4f}"
    print(output)
    current_time += time_interval




