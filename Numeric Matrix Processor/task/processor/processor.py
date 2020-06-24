from math import floor
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING


def main():
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    action = int(input('Your choice: '))

    if action == 1:
        rc_matrix1, matrix1 = read_matrix()
        rc_matrix2, matrix2 = read_matrix()
        if rc_matrix1 == rc_matrix2:
            print('The result is:')
            add(matrix1, matrix2, rc_matrix1[0], rc_matrix1[1])
        else:
            print('The operation cannot be performed.')
    elif action == 2:
        rc_matrix1, matrix1 = read_matrix()
        scalar = Decimal(input('Enter constant: '))
        print('The result is:')
        print_matrix(mult_by_constant(matrix1, scalar))
    elif action == 3:
        rc_matrix1, matrix1 = read_matrix()
        rc_matrix2, matrix2 = read_matrix()
        if rc_matrix1[1] == rc_matrix2[0]:
            print('The result is:')
            print_matrix(mult(matrix1, matrix2, rc_matrix1[0], rc_matrix2[1]))
        else:
            print('The operation cannot be performed.')
    elif action == 4:
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        tr_type = int(input('Your choice: '))
        rc_matrix1, matrix1 = read_matrix()
        print_matrix(transpose(matrix1, rc_matrix1, tr_type))
    elif action == 5:
        rc_matrix1, matrix1 = read_matrix()
        print('The result is:')
        print(det_matrix(matrix1))
    elif action == 6:
        rc_matrix1, matrix1 = read_matrix()
        print('The result is:')
        if det_matrix(matrix1) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            print_matrix(inverse_matrix(matrix1, rc_matrix1))
    elif action == 0:
        return 0


def add(matrix1, matrix2, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(matrix1[i][j] + matrix2[i][j], end=' ')
        print()


def mult_by_constant(matrix1, scalar):
    new_matrix = []
    for el in matrix1:
        temp = []
        for x in el:
            temp.append(x * scalar)
        new_matrix.append(temp)
    return new_matrix


def mult(matrix1, matrix2, rows, columns):
    C = [[0 for row in range(columns)] for col in range(rows)]
    new_matrix = []
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                C[i][j] += matrix1[i][k] * matrix2[k][j]
            temp.append(C[i][j])
        new_matrix.append(temp)
    return new_matrix


def transpose(matrix1, rc_matrix1, tr_type=1):
    new_matrix = []
    if tr_type == 1:
        for i in range(rc_matrix1[1]):
            temp = []
            for j in range(rc_matrix1[0]):
                temp.append(matrix1[j][i])
            new_matrix.append(temp)
        return new_matrix
    elif tr_type == 2:
        for i in range(rc_matrix1[1] - 1, -1, -1):
            temp = []
            for j in range(rc_matrix1[0] - 1, -1, -1):
                temp.append(matrix1[j][i])
            new_matrix.append(temp)
    elif tr_type == 3:
        for i in range(rc_matrix1[0]):
            temp = []
            for j in range(rc_matrix1[1]):
                temp.append(matrix1[i][rc_matrix1[1] - j - 1])
            new_matrix.append(temp)
    elif tr_type == 4:
        for i in range(rc_matrix1[0]):
            temp = []
            for j in range(rc_matrix1[1]):
                temp.append(matrix1[rc_matrix1[0] - i - 1][j])
            new_matrix.append(temp)
    return new_matrix


def read_matrix():
    rc_matrix1 = tuple(map(int, input('Enter size of first matrix: ').strip().split()))
    print('Enter first matrix:')
    matrix1 = []
    for _ in range(rc_matrix1[0]):
        matrix1.append(list(map(Decimal, input().strip().split())))
    return rc_matrix1, matrix1


def det_matrix(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    cof_matrix = matrix_with_cofactors(matrix)
    det = 0
    for j in range(len(matrix[0])):
        det += matrix[0][j] * cof_matrix[0][j]
    return det


def matrix_for_cofactor(matrix, i, j):
    new_matrix = []
    for ii in range(len(matrix)):
        temp = []
        if ii != i:
            for jj in range(len(matrix[0])):
                if jj != j:
                    temp.append(matrix[ii][jj])
            new_matrix.append(temp)
    return new_matrix


def cofactor(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    cof = 0
    for j in range(len(matrix[0])):
        cof += matrix[0][j] * (-1) ** j * cofactor(matrix_for_cofactor(matrix, 0, j))
    return cof


def matrix_with_cofactors(matrix1):
    if len(matrix1) == 1:
        return matrix1
    new_matrix = []
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix1[0])):
            temp.append(cofactor(matrix_for_cofactor(matrix1, i, j)) * (-1) ** (i + j))
        new_matrix.append(temp)
    return new_matrix


def inverse_matrix(matrix, rc_matrix):
    return mult_by_constant(
        transpose(
            matrix_with_cofactors(
                matrix
            ),
            rc_matrix
        ),
        1 / det_matrix(
            matrix
        )
    )


def print_matrix(matrix):
    for line in matrix:
        for el in line:
            el = spec_round(el)

            # if len(el) >= 5:
            #     print('{0:>5}'.format(el), end='')
            if el == '0':
                print('{0:>5} '.format(str(0)), end='')
            else:
                print('{1}{0:<5}'.format(' ' + el, ' ' * (2 - el.find('.'))), end='')
            # else:
            #     print(' {0:>4}'.format(el), end='')
        print()


def spec_round(element):
    if element.quantize(Decimal("1.00"), ROUND_CEILING) == 0 \
            or element == 0 \
            or element.quantize(Decimal("1.00"), ROUND_FLOOR) == 0:
        return '0'
    if element < 0:
        return str(element.quantize(Decimal("1.00"), ROUND_CEILING)).rstrip('0').rstrip('.')
    return str(element.quantize(Decimal("1.00"), ROUND_FLOOR)).rstrip('0').rstrip('.')


while True:
    if main() == 0:
        break
    print()
