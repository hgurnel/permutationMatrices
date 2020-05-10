# CONSTANTS

N_MIN = 1
N_MAX = 100
MAT_MIN_SIZE = 0 
MAT_MAX_SIZE = 10000 

# ----- USER INPUT -----  

input_list = []
N_str = input()
try:
    N = int(N_str)
except ValueError:
    print("ERROR")

input_list.append(N)

for i in range(int(N)):
    M_str = input()
    try:
        M = int(M_str)
    except ValueError:
        print("ERROR")
    input_list.append(M)
    for j in range(M):
        elem_str = input()
        try:
            elem = int(elem_str)
        except ValueError:
            print("ERROR")
        input_list.append(elem)

# print(input_list)

# ----- FIND IF MATRICES ARE PERMUTATIONS -----

def isPowerOfTwo(n):
    # & = binary operator, so it considers the bin representations of n and n-1
    return n > 0 and ((n & (n - 1)) == 0)


def isRowDuplicate(elem, setOfElems):    
    if elem in setOfElems:
        return True
    else:
        setOfElems.add(elem)         
        return False
    
def isRowCorrect(num, mat_size):
    mat_conditions = mat_size > MAT_MIN_SIZE and mat_size < MAT_MAX_SIZE
    try: 
        if mat_conditions and num < 2**mat_size:
            if (num == 1 or isPowerOfTwo(num)):
                return True
            else:
                return False
        else:
            raise Exception("ERROR")
    except ValueError:
            print("ERROR")


def areTheyPermutationMatrices(line):
    N = line[0]
    
    if N > N_MIN and N < N_MAX:
        M = line[1]
        id_M = 1
        id_first_row = id_M + 1
        id_last_row = id_first_row + (M - 1)
        
        # Empty set to detect duplicates among the rows of each matrix
        rows_set = set()
        
        for matrix in range(N):
            output = 1 
            # Make range() stop at (id_last_row + 1) to loop until id_last_row
            for id in range(id_first_row, id_last_row + 1):
                row = line[id]
                # The moment a wrong row is encountered, the loop is stopped
                if not isRowCorrect(row, M):
                    output = 0
                    break
                else:
                    if isRowDuplicate(row, rows_set):
                        output = 0
                        break
            
            print(output)
            
            if(matrix != N-1): 
                # Reset data before moving to the next matrix
                rows_set = set()
                M = line[id_last_row + 1]
                id_M = id_last_row + 1
                id_first_row = id_M + 1
                id_last_row = id_first_row + (M - 1)
    else:
        print("ERROR")


areTheyPermutationMatrices(input_list)