def save_matrix(file_name):
    matrix = []
    row_length = None
    with open(file_name, "r") as file:
        for line in file:
            matrix_row = line.strip().split()
            try:
                numbers  = [int(x) for x in matrix_row]
            except ValueError:
                raise ValueError("Linia nu este alcatuita doar din numere.")
            if row_length is None:
                row_length = len(numbers)
                if row_length<2:
                    raise ValueError("Matricea nu se afla intr-o forma valida(numarul de coloane>=2)")
            elif len(numbers) != row_length :
                raise ValueError("Matricea introdusa este invalida.")
            matrix.append(numbers)
        
    if len(matrix) < 2:
        raise ValueError("Matricea nu se afla intr-o forma valida (numarul de linii >= 2)")
    return matrix

def write_matrix(file_name, matrix):
    with open(file_name, "w") as file:
        for row in matrix :
            line = " ".join(str(x) for x in row)
            file.write(line + "\n")

try:
    matrix = save_matrix("initial_matrix.txt")
    write_matrix("final_matrix.txt", matrix)
    print("Matrice introdusa cu succes in 'final_matrix.txt'.")
except ValueError as er:
    print("Eroare ", er)
    