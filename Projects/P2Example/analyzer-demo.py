import argparse
import json
import statistics 
from datetime import datetime

# Load my data
def load_data(filepath):

    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return None


# Main menu display for the interactive requirement
def display_menu():
    print("\nWeather Analysis Menu:")
    print("1. Perform statistical analysis")
    print("2. Export analysis to a file")
    print("3. Exit")

# Perform some analysis on our data
def analyze_data(data):

    # Here Im going to create some variables that will hold lists of values from my data set.
    # i.e., a list of the minimum daily temps, the max daily temps, etc. 

    # For every entry in my data set, append the value of whatever is in "tmin" to my tmin_values list
    tmin_values = [entry['tmin'] for entry in data]
    tmax_values = [entry['tmax'] for entry in data]
    prcp_values = [entry['prcp'] for entry in data]
    snow_values = [entry['snow'] for entry in data]
    
    analysis = {
        "Average Min Temperature": statistics.mean(tmin_values),
        "Average Max Temperature": statistics.mean(tmax_values),
        "Total Precipitation": sum(prcp_values),
        "Maximum Recorded Snowfall": max(snow_values)
    }

    for key, value in analysis.items()
        if isinstance(value, float):
            print(f"{key}: {value:.2f}") # Formatting any decimals to 2 places... just for sanity reasons.
        else:
            print(f"{key}: {value}")

    return analysis


# Export that analysis to a file
def export_analysis(analysis): # Taking in an analysis dictionary... formatted like we did in the method above

    filename = f"analysis_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

    with open(filename, 'w') as file:
        for key, value in analysis.items():
            if isinstance(value, float):
                file.write(f"{key}: {value:.2f}\n") # Formatting any decimals to 2 places... just for sanity reasons.
            else:
                file.write(f"{key}: {value}\n")
    
    print(f"Analysis exported to {filename}.")


def interactive_mode(data):

    # While loop to handle the user menu loop, until the user chooses to exit.

    while True:
        display_menu()
        
        # The menu prompts the user for a choice, we then store it to check against to
        # determine what functions if any to run.
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            analyze_data(data)
        elif user_choice == "2":
            # If the user chooses to export the analysis, we call export_analysis, and we give it a 
            # call to analyze_data... analyze_data runs, and its analysis return dictionary is immediately
            # sent to export_analysis, satisfying the call
            export_analysis(analyze_data(data))
        elif user_choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

    if __name__ == "__main__":

        # Creating my parser
        parser = argparse.ArgumentParser(description="Weather Data Analysis App")

        # Adding arguments
        parser.add_argument("--filepath", required=True, help="Path to the JSON data file.")
        parser.add_argument("--analyze", action="store_true", help="Perform and export statistical analysis to a file directly. Bypasses interactive mode.")

        user_args = parser.parse_args()

        # Load our data
        data = load_data(user_args.filepath)

        # If data is not loaded, just exit. It didn't work.
        if not data:
            return 

        if args.analyze:
            # Here I will separate the two function calls for data analysis, to better see the steps.
            analysis_result = analyze_data(data)
            export_analysis(analysis_result)
        else:
            # If the user did not use the --analyze argument, we use the interactive mode
            interactive_mode(data)
        