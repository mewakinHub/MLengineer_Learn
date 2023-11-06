import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Extract components of the date and time
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second

# Create a specific date and time
specific_datetime = datetime.datetime(2023, 10, 31, 15, 30, 0)

# Format a datetime object as a string
formatted_date = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Parse a string into a datetime object
parsed_date = datetime.datetime.strptime('2023-10-31 15:30:00', '%Y-%m-%d %H:%M:%S')

# Calculate the difference between two datetimes
time_difference = specific_datetime - current_datetime

# Perform various date and time calculations using timedelta

# For more advanced operations, you can use the datetime.timedelta class.

# Print the results
print("Current Date and Time:", current_datetime)
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)
print("Specific Date and Time:", specific_datetime)
print("Formatted Date:", formatted_date)
print("Parsed Date:", parsed_date)
print("Time Difference:", time_difference)
