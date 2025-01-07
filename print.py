def print_pascals_triangle(rows):
    for i in range(rows):
        # Generate each row of Pascal's Triangle
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)

        # Print the row with proper spacing
        print(" " * (rows - i), end="")
        print(" ".join(map(str, row)))

        # Store the current row as the previous row for the next iteration
        prev_row = row


# Input for number of rows
num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))

print_pascals_triangle(num_rows)
