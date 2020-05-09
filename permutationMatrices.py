# CONSTANTS

N_MIN = 1
N_MAX = 100
MAT_MIN_SIZE = 0 
MAT_MAX_SIZE = 10000 

# ----- USER INPUT -----  

# print("Enter positive integers")
input_list = input().split()

try:
    input_list = list(map(int, input_list))
except ValueError:
    print("ERROR")

# print(input_list)

# ----- FIND IF MATRICES ARE PERMUTATIONS -----

def isPowerOfTwo(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
              
    return True


def isRowDuplicate(elem, setOfElems):    
    if elem in setOfElems:
        return True
    else:
        setOfElems.add(elem)         
        return False
 
    
def isRowCorrect(num, mat_size):
    mat_conditions = mat_size > MAT_MIN_SIZE and mat_size < MAT_MAX_SIZE    
    if mat_conditions and num < 2**mat_size:
        if (num == 1 or isPowerOfTwo(num)):
            return True
        else:
            return False
    else:
        return False

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
            for id in range(id_first_row, id_last_row):
                row = line[id]
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