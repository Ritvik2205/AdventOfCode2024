
def txt_to_list(file_path):
    with open(file_path, "r") as file:        
        list = [str(line) for line in file]

    return list

# do a matrix search for the word 'XMAS' horizontally, vertically, diagonally, written backwards, and overlapping other words
def search_matrix(matrix, word):
    word = word.upper()
    row = len(matrix)
    col = len(matrix[0]) - 1
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]
    result = 0
    
    for i in range(row):
        for j in range(col):
            for d in directions:
                x, y = i, j
                for k in range(len(word)):
                    if 0 <= x < row and 0 <= y < col and matrix[x][y] == word[k]:
                        x += d[0]
                        y += d[1]
                    else:
                        break
                else:
                    result += 1
    
    return result

def search_cross_mas(matrix, word):
    # count the pair of words 'MAS' forming a cross in either direction
    word = word.upper()
    row = len(matrix)
    col = len(matrix[0])
    result = 0
    
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            if matrix[i][j] == 'A':
                if ((matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and
                     matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S') or
                    (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and
                     matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M') or
                    (matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S' and
                     matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M') or
                    (matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M' and
                     matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S')):
                    result += 1
    
    return result

def main():
    list = txt_to_list("input.txt")


def main():
    list = txt_to_list("input.txt")

    result = search_cross_mas(list, "XMAS")
    print(result)


if __name__ == "__main__":
    main()