def convert_to_float(input_row):
    output_row = []
    for i in input_row:
        output_row.append(float(i))
    return output_row

def two_d_deep_copy(src_array):
    dest_array = []
    for i in range(0,len(src_array)):
        sub_ra = []
        for j in range(0,len(src_array[i])):y
            sub_ra.append(src_array[i][j])
        dest_array.append(sub_ra)
    return dest_array

def matrix_multiply(matrix1, matrix2):
    # Get the dimensions of the matrices
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    # Check if the matrices can be multiplied
    if cols1 != rows2:
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Initialize the result matrix with zeros
    result_matrix = [[0] * cols2 for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

def find_inverse(matrix):
    try:
        # Check if the matrix is 2x2
        if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
            raise ValueError("Input matrix must be a 2x2 matrix")

        # Get matrix elements
        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

        # Calculate the determinant
        determinant = a * d - b * c

        # Check if the matrix is invertible
        if determinant == 0:
            raise ValueError("Matrix is not invertible")

        # Calculate the inverse
        inverse_matrix = [[d/determinant, -b/determinant], [-c/determinant, a/determinant]]

        return inverse_matrix

    except Exception as e:
        return "Error: "+str(e)
print("Computes B-matrix based on A and b_1,b_2 cols")
print("Enter values for A matrix comma separated")
a_first = convert_to_float((input()).split(","))
a_second = convert_to_float((input()).split(","))
print("Enter values for b (P) matrix comma separated")
p_first = convert_to_float((input()).split(","))
p_second = convert_to_float((input()).split(","))
print("Applying formula P^-1*D*P")
a_mtrx = []
a_mtrx.append(a_first)
a_mtrx.append(a_second)
p_mtrx = []
p_mtrx.append(p_first)
p_mtrx.append(p_second)
p_inv_mtrx = find_inverse(p_mtrx)
res1 = matrix_multiply(p_inv_mtrx,a_mtrx)
res2 = matrix_multiply(res1,p_mtrx)
print("Result:")
print(res2)
