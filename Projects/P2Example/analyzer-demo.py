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
    print("1. View individual entry")
    print("2. View data by filter/sort")
    print("3. Perform statistical analysis")
    print("4. Export analysis to file")
    print("5. Exit")

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

    for key, value in analysis.items():
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


def view_entry(data):
    
    # View an individual data entry based on user input.
    
    try:
        index = int(input(f"Enter the entry index (0 to {len(data) - 1}): "))
        print(json.dumps(data[index], indent=4))
    except (IndexError, ValueError):
        print("Invalid index! Please try again.")


def interactive_mode(data):
    
    # Run the interactive menu for the user.
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_entry(data)
        elif choice == "2":
            filter_data(data)
        elif choice == "3":
            analysis = analyze_data(data)
        elif choice == "4":
            if 'analysis' in locals():
                export_analysis(analysis)
            else:
                print("Perform analysis first!")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


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
        sys.exit() 

    if user_args.analyze:
        # Here I will separate the two function calls for data analysis, to better see the steps.
        analysis_result = analyze_data(data)
        export_analysis(analysis_result)
    else:
        # If the user did not use the --analyze argument, we use the interactive mode
        interactive_mode(data)
        