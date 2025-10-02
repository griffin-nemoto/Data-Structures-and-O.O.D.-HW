# main.py
import weather_analysis
def weather_analyze(file_path):
    '''Parameter: text file containing weather data
       Output: Dictionary of various labeled weather statistics using weather_analysis module
    '''
    weather = dict()
    data = weather_analysis.read_weather_data(file_path)
    #Assigns dictionary with all values from read_weather_data
    weather['average_temperature'] = weather_analysis.calculate_average_temperature(data)
    weather['total_rainfall'] = weather_analysis.calculate_total_rainfall(data)
    weather['highest_temperature'] = dict()
    weather['highest_temperature']['date']= weather_analysis.find_highest_temperature(data)[0]
    weather['highest_temperature']['temperature']= weather_analysis.find_highest_temperature(data)[1]
    weather['lowest_temperature'] = dict()
    weather['lowest_temperature']['date']= weather_analysis.find_lowest_temperature(data)[0]
    weather['lowest_temperature']['temperature']= weather_analysis.find_lowest_temperature(data)[1]
    weather['most_rainfall'] = dict()
    weather['most_rainfall']['date']= weather_analysis.find_day_with_most_rainfall(data)[0]
    weather['most_rainfall']['temperature']= weather_analysis.find_day_with_most_rainfall(data)[1]
    return weather


if __name__ == "__main__":
    
    results = weather_analyze("hw1_starter/weather_data.txt") #or the path to the file
    print(results)
