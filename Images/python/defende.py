import math
import pandas as pd

# Function to calculate Euclidean distance between two coordinates
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Function to find the 5 nearest base coordinates for each input coordinate
def find_5_nearest_for_each(input_coords, base_coords, n=5):
    all_nearest_coords = []
    for input_coord in input_coords:
        distances = [(base_coord, euclidean_distance(input_coord, base_coord)) for base_coord in base_coords]
        # Sort the distances and take the top 5 nearest coordinates
        distances.sort(key=lambda x: x[1])
        nearest_coords = [coord for coord, dist in distances[:n]]
        all_nearest_coords.append(nearest_coords)
    return all_nearest_coords

# Function to load coordinates from an Excel file
def load_coordinates_from_excel(file_path):
    df = pd.read_excel(file_path)
    # Assuming the coordinates are in columns 'X' and 'Y'
    return list(zip(df['X'], df['Y']))

# Function to save results to Excel
def save_results_to_excel(input_coords, all_nearest_coords, output_file):
    # Create columns for nearest coordinates for each input
    data = {
        'Input X': [coord[0] for coord in input_coords],
        'Input Y': [coord[1] for coord in input_coords],
    }
    
    # Add 5 nearest coordinates to the DataFrame
    for i in range(5):
        data[f'Nearest {i+1} X'] = [nearest[i][0] for nearest in all_nearest_coords]
        data[f'Nearest {i+1} Y'] = [nearest[i][1] for nearest in all_nearest_coords]

    # Save DataFrame to Excel
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

# Main logic
def main(input_file, base_file, output_file):
    # Load input coordinates and base coordinates from Excel files
    input_coords = load_coordinates_from_excel(input_file)
    base_coords = load_coordinates_from_excel(base_file)
    
    # Find the 5 nearest base coordinates for each input coordinate
    all_nearest_coords = find_5_nearest_for_each(input_coords, base_coords)
    
    # Save the results to an Excel file
    save_results_to_excel(input_coords, all_nearest_coords, output_file)

# Example usage
if __name__ == "__main__":
    input_file = '/data/input_coordinates.xlsx'  # Path to the input coordinates Excel file
    base_file = '/data/base_coordinates.xlsx'    # Path to the base coordinates Excel file
    output_file = '/data/output_nearest_coords.xlsx'  # Path to save the output Excel file
    # Update these paths to the correct location of your Excel files
##    input_file = 'D:/0_Adobe/md/1_bac/Images/python/input_coordinates.xlsx'  # Full path to input file
##    base_file = 'D:/0_Adobe/md/1_bac/Images/python/base_coordinates.xlsx'    # Full path to base file
##    output_file = 'D:/0_Adobe/md/1_bac/Images/python/output_nearest_coords.xlsx'  # Output file path

    main(input_file, base_file, output_file)

    
    main(input_file, base_file, output_file)
