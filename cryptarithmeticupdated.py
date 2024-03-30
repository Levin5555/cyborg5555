from itertools import permutations

def cryptarithmetic(puzzle):
    words = puzzle.split()
    token = set(''.join(words))  # Changed to ''.join(words)
    permutation = permutations('0123456789', len(token))
    
    for perm in permutation:
        letter_to_num = dict(zip(token, perm))
        if '0' in letter_to_num.values() and any(letter in words[-1] for letter, digit in letter_to_num.items() if digit == '0'):
            continue  # Skip permutations with leading zeros
        
        word_join = [''.join(letter_to_num[letter] for letter in word) for word in words]
        if int(word_join[0]) + int(word_join[1]) == int(word_join[2]):
            return letter_to_num
        
    return None    

if __name__ == '__main__':
    puzzle = input("Enter a cryptarithmetic puzzle: ").strip()
    
    solution = cryptarithmetic(puzzle)
    if solution:
        print("Solution found:")
        for letter, digit in solution.items():
            print(f"{letter} = {digit}")
    else:
        print("No solution found")
