from geopy.distance import geodesic
# Read TLE data from the file
tle_file_path = '30sate.txt'
with open(tle_file_path, 'r') as tle_file:
    tle_lines = tle_file.readlines()
    
# Sample list of points in (latitude, longitude) format
points = [
    (16.66673, 103.58196),  # Example point 1
    (69.74973, -120.64459),  # Example point 2
    (-21.09096, -119.71009),  # Example point 3
    (-31.32309, -147.79778),  # Example point 4
    # Add more points as needed
]

# User-defined rectangle coordinates
rectangle_coords = [
    (16.66673, 103.58196),  # Top-left corner
    (69.74973, 103.58196),  # Top-right corner
    (69.74973, -120.64459),  # Bottom-right corner
    (16.66673, -120.64459),  # Bottom-left corner
]

# Function to check if a point is within the rectangle
def is_point_in_rectangle(point, rectangle_coords):
    lat, lon = point
    min_lat = min(rectangle_coords[0][0], rectangle_coords[1][0])
    max_lat = max(rectangle_coords[0][0], rectangle_coords[2][0])
    min_lon = min(rectangle_coords[0][1], rectangle_coords[3][1])
    max_lon = max(rectangle_coords[1][1], rectangle_coords[2][1])
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon

# Filter points within the specified rectangle
points_in_rectangle = [point for point in points if is_point_in_rectangle(point, rectangle_coords)]

# Print the points within the rectangle
for i, point in enumerate(points_in_rectangle, start=1):
    print(f"Point {i}: Latitude: {point[0]}, Longitude: {point[1]}")
