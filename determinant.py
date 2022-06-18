def delete(word, i):
    if i == 0:
        return word[1:]
    elif i == len(word):
        return word[:len(word)-1]
    else:
        return word[:i] + word[(i+1):]

def permutation(word):
    if len(word) == 1:
        return [word]
    ret = []
    for i in range(len(word)):
        for temp in permutation(delete(word, i)):
            ret.append(word[i] + temp)
    return ret

def symmetric_group(dim):
    word = ""
    for i in range(dim):
        word += str(i)
    return permutation(word)

def inversion(word):
    word_to_list = [int(c) for c in word]
    ret = 0
    for i in range(len(word_to_list)):
        for j in range(i, len(word_to_list)):
            if word_to_list[i] > word_to_list[j]:
                 ret += 1
    return ret

def sign(word):
    return 1 if inversion(word) % 2 == 0 else -1

def determinant(matrix):
    if len(matrix) != len(matrix[1]):
        raise TypeError("For square matrices only.")
    dim = len(matrix)
    Sym = symmetric_group(dim)
    det = 0
    for word in Sym:
        p = [int(c) for c in word]
        s = sign(word)
        term = 1
        for j in range(dim):
            term *= matrix[p[j]][j]
        term *= s
        det += term
    return det

if __name__ == "__main__":

    matrix = [[2, 2], [2, 2]]
    print(determinant(matrix))