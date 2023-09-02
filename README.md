# Satellite Tracking and Filtering
# Project Overview 

This project is a Python program for tracking the positions of satellites using Two-Line Element Sets (TLEs),
converting the positions to latitude, longitude, and altitude (LLA) format, 
and filtering the satellite data based on user-defined geographic regions.
The code is optimized for performance to handle a large number of satellites efficiently.

# How to Run the Code:
1. Clone the Git repository to your local machine:
      git clone <repository-url>
      
2. Navigate to the project directory:
     cd satellite_pro
   
3. Install the required dependencies using pip:
    pip install -r requirements.txt
   
4. Prepare your TLE data file (e.g., 30sats.txt) containing satellite TLE sets.
   
5. Run the main program with the following command, providing the TLE data file path and specifying the rectangular region coordinates:
     python main.py --tle-file <tle-file-path> --lat1 <lat1> --lon1 <lon1> --lat2 <lat2> --lon2 <lon2>
     Replace <tle-file-path>, <lat1>, <lon1>, <lat2>, and <lon2> with your specific values.

# Dependencies
    sgp4: Used for satellite position calculations.
    pyproj: Used for coordinate transformations.
    
# Code Structure:

1. satellite_location.py: This code structure includes functions for parsing TLE data, calculating satellite positions, and converting coordinates to LLA format.
  The if __name__ == "__main__": block demonstrates example usage of these functions. 
  Replace "tle_data.txt" with your actual TLE data file and adjust the start_time, end_time, and interval_minutes as needed.

2. The code you provided is split into two parts: the first part calculates and prints satellite positions in ECEF (Earth-Centered,Earth-Fixed) coordinates along with velocities,while the second part converts these coordinates to latitude, longitude, and altitude (LLA) format and prints them.  Both parts share the same code for readin TLE data and defining the time range and interval. This code first calculates and prints satellite positions in ECEF coordinates along with velocities, and then it defines a function ecef_to_lla to convert these ECEF coordinates to LLA format and prints them.Both parts share the same TLE data loading, time range, and interval definitions.

3.In this section, we'll demonstrate how to use Python with the `geopy` library to filter a list of points based on whether they fall within a user-defined rectangle. 
 This can be useful for spatial analysis and geospatial applications. Before you begin, ensure you have the `geopy` library installed. You can install it using pip:
    
      pip install geopy


# Additional Details
1 This code is designed to process satellite data in the TLE format. Ensure that your TLE data file is correctly formatted.

2 The rectangular region for filtering should be defined by specifying two latitude and longitude coordinates (lat1, lon1, lat2, lon2), representing the top-left and bottom-right corners of the region, respectively.

3 Feel free to customize the code and adapt it to your specific requirements or integrate it into a larger system.


and Thank you
