# Instructions:
# 1. **Remove the TODO comment and pass statement** once you’ve completed the function implementation.
#    - The TODO and pass are placeholders indicating that the function is not yet complete.
#    - Once the function is implemented, these should be removed to keep the code clean.
# 
# 2. **Best Coding Practices**:
#    - In professional programming, finalizing the code means removing unnecessary placeholders.
#    - This ensures your code is ready for review, testing, and does not contain clutter.
# 
# 3. **Adding Docstrings**:
#    - After removing TODO and pass, add a **docstring** for each function.
#    - The docstring should explain the function’s purpose, parameters, and expected output.
#    - Proper documentation improves code readability and helps with debugging and maintenance.

def read_weather_data(file_path: str):
    ''' Reads weather data and returns list of tuples containing data from each line
    Parameter: text file containing weather data
    Returns: list of tuples containing weather data separated by date
    '''
    weatherList =[]
    weatherFile = open(file_path,'r')
    lines = weatherFile.read().splitlines()
    for line in lines:
        #filler list to assign correct types to data
        hold = []
        strings = line.split(',')
        hold.append(strings[0])
        hold.append(float(strings[1]))
        hold.append(float(strings[2]))
        weatherList.append(tuple(hold))
    weatherFile.close()
    return weatherList
def calculate_average_temperature(weather_data):
    '''Uses list of weather data to return average temperature
    Parameters: list of weather data
    Returns: float representing average temperature
    '''
    sum=0
    for tup in weather_data:
        sum += tup[1]
    return sum/len(weather_data)
def calculate_total_rainfall(weather_data):
    '''Calculates and returns total rainfall from list of weather data
    Parameters: list of weather data
    Returns: float representing total rainfall'''
    sum =0
    for tup in weather_data:
        sum+=tup[2]
    return sum

def find_highest_temperature(weather_data):
    '''returns highest temperature and date from list of weather data
    Parameters: list containing weather data
    Returns: tuple containing date and temperature of day with highest temp'''
    hi = weather_data[0][1]
    index=0
    for i in range(len(weather_data)):
        if weather_data[i][1]>hi:
            hi = weather_data[i][1]
            index=i     
    return weather_data[index][0],hi
    

def find_lowest_temperature(weather_data):
    '''returns lowest temperature and date from list of weather data
    Parameters: list containing weather data
    Returns: tuple containing date and temperature of day with lowest temp'''
    lo = weather_data[0][1]
    index=0
    for i in range(len(weather_data)):
        if weather_data[i][1]<lo:
            lo = weather_data[i][1]
            index=i     
    return weather_data[index][0],lo

def find_day_with_most_rainfall(weather_data):
    '''returns highest rainfall and date from list of weather data
    Parameters: list containing weather data
    Returns: tuple containing date and temperature of day with highest rainfall'''
    hi = weather_data[0][2]
    index=0
    for i in range(len(weather_data)):
        if weather_data[i][2]>hi:
            hi = weather_data[i][2]
            index=i     
    return weather_data[index][0],hi

