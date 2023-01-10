import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    x= datetime.fromisoformat(iso_string)
    formatted_date=(x.strftime("%A %d %B %Y"))
    
    


    return formatted_date
    pass


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    # temp = float(input("Enter temperature in Fahrenheit: "))
    # celsius = (temp - 32) * 5/9

    # print(f"{temp} in Fahrenheit is equal to {celsius} in Celsius")

    # celsius_1 = float(input("Temperature value in degree Celsius: " ))
    celsius = round((float(temp_in_farenheit) - 32)  / 1.8,1)

    
    return celsius
    

    pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """         
    
    mean = sum([float(x) for x in weather_data])/len([float(x) for x in weather_data])

    return mean

    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    
    with open (csv_file) as x: 
    
        reader= csv.reader(x)
        
        final_list = []
        count=0
        for line in reader:
            if len(line) ==0:
                continue
            if count==0:
                count=count+1
                continue
            new_line=[line[0], int(line[1]), int(line[2])]
            final_list.append(new_line)
        
        
    return final_list



def find_min(weather_data): 
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
#why does this work?
    if len(weather_data)==0:
        return ()
    
    weather_min = min(weather_data)
    index= 0
    indexmin=index
    for number in weather_data:
        if number==weather_min:
            indexmin=index 
        index=index+1
        
    
    return (float(weather_min), indexmin)
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data)==0:
        return ()
    print(weather_data)
    weather_max= max(weather_data)

    print(weather_max)
    
    index= 0
    index2=index
    for number in weather_data:
        if number==weather_max:
            index2=index 
        index= index+1
    print(index)
    
    return (float(weather_max), index2)

    
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    list_max_temps=[]
    list_min_temps= []

    for item in weather_data:

        list_max_temps.append(item[2])
        list_min_temps.append(item[1])

   
    max_temp_data= find_max(list_max_temps)
    max_temp=max_temp_data [0]
    max_temp_in_c= convert_f_to_c(max_temp)
    max_temp_formatted = format_temperature(max_temp_in_c)
    max_temp_date = convert_date(weather_data[max_temp_data [1]][0]) 
    num_days= len(weather_data)
    avg_low= format_temperature(convert_f_to_c(calculate_mean(list_min_temps)))
    avg_high= format_temperature(convert_f_to_c(calculate_mean(list_max_temps)))
    


    min_temp_data= find_min (list_min_temps)
    min_temp= min_temp_data [0]
    min_temp_in_c= convert_f_to_c (min_temp)
    min_temp_formatted= format_temperature(min_temp_in_c)
    min_temp_date= convert_date(weather_data[min_temp_data [1]][0]) 
    # print(min_temp_date)

    summary= (f"{num_days} Day Overview\n  The lowest temperature will be {min_temp_formatted}, and will occur on {min_temp_date}.\n  The highest temperature will be {max_temp_formatted}, and will occur on {max_temp_date}.\n  The average low this week is {avg_low}.\n  The average high this week is {avg_high}.\n")
    
    print(summary)
    return summary 
# generate_summary(load_data_from_csv("/Users/chandinithirumalai/Documents/GitHub/she-codes-exercises-chandinithirumalai/test-project/she-codes-python-weather-project-chandinithirumalai/tests/data/example_one.csv"))


pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """



    summary=""
    for i in weather_data:
        human_readable_date= convert_date(i[0])
        min_temp_in_c = convert_f_to_c(i[1])
        min_temp_formatted = format_temperature(min_temp_in_c)
        max_temp_in_c= convert_f_to_c(i[2])
        max_temp_formatted= format_temperature(max_temp_in_c)
        summary = summary + "---- " + human_readable_date + " ----\n  Minimum Temperature: " + min_temp_formatted + "\n  Maximum Temperature: " + max_temp_formatted + "\n\n"
    return summary


    
    pass
