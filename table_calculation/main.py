def calculate_table_to_file():
    # this function uses numbers 1 to 10 and multiplies them diagonally
    # creating a table in calculation_table.txt file

    with open('calculation_table.txt', 'w') as file:
        for i in range(1, 11):
            line = ''
            for j in range(1, 11):
                line += str(i * j) + ' '
            line += '\n'
            file.write(line)
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_table_to_file()
