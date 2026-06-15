# Number of rows for the triangle
rows = 5

# Loop for each row
for i in range(1, rows + 1):
    # Print leading spaces to center the triangle
    print(' ' * (rows - i), end='')
    
    # Print numbers in the current row
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # Move to the next line after each row
    print()

