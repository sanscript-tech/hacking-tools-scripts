n=int(input("Enter no of rows and coulomn of sudoku problem : "))
print("Please enter a ",n,"x",n,"Matrix")
matrix = [[0 for i in range(9)] for j in range(9)]
for i in range(0,n):
    for j in range(0,n):
        matrix[i][j] = int(input())


def solve(matrix):
    find = find_empty(matrix)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(matrix, i, (row, col)):
            matrix[row][col] = i

            if solve(matrix):
                return True

            matrix[row][col] = 0

    return False


def valid(matrix, num, pos):
    # Check row
    for i in range(len(matrix[0])):
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(matrix)):
        if matrix[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if matrix[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(matrix):
    for i in range(len(matrix)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(matrix[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(matrix[i][j])
            else:
                print(str(matrix[i][j]) + " ", end="")


def find_empty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return (i, j)  # row, col

    return None
print("The entered Matrix for sudoku solver is : ")
print("")
print_board(matrix)
solve(matrix)
print("")
print("***********************************************")
print("")
print("The output is : ")
print("")
print_board(matrix)
