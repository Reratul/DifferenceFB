import csv


# Function to calculate u for backward difference
def u_cal_backward(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp


# Function to calculate factorial
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# Function to read input from a .txt file
def get_input_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        # Read number of data points
        n = int(lines[0].strip())

        # Read x values
        x = list(map(float, lines[1].strip().split()))

        # Read y values
        y = list(map(float, lines[2].strip().split()))

        # Read the value to interpolate at
        value = float(lines[3].strip())

    return n, x, y, value


# Function to interpolate a value using backward difference
def backward_difference_interpolation(n, x, y, value):
    # y[][] is used for difference table
    # with y[][0] used for input
    y_table = [[0 for i in range(n)] for j in range(n)]

    # Initializing the difference table
    for i in range(n):
        y_table[i][0] = y[i]

    # Calculating the backward difference table
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y_table[j][i] = y_table[j][i - 1] - y_table[j - 1][i - 1]

    # Prepare data for CSV file
    table_data = []
    header = ["x"] + [f"y{i}" for i in range(n)]
    table_data.append(header)

    for i in range(n):
        row = [x[i]] + y_table[i][:i + 1]
        table_data.append(row)

    # Value to interpolate at
    u = (value - x[n - 1]) / (x[1] - x[0])
    sum_val = y_table[n - 1][0]

    # Newton's backward interpolation formula
    for i in range(1, n):
        sum_val += (u_cal_backward(u, i) * y_table[n - 1][i]) / fact(i)

    # Append the interpolated value to the table
    table_data.append([f"Interpolated Value at {value}", round(sum_val, 6)])

    # Save the table to a CSV file
    csv_file_path = "BackwardDifference_output.csv"
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table_data)

    return csv_file_path, sum_val


# Driver code
filename = input("Enter the input file name (with .txt extension): ")

# Read input data from the file
n, x, y, value = get_input_from_file(filename)

# Perform interpolation using backward difference
csv_file_path, interpolated_value = backward_difference_interpolation(n, x, y, value)

print(f"The interpolated value at {value} is {interpolated_value}")
print(f"The output has been saved to {csv_file_path}")
