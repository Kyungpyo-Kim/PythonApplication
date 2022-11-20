next_char = {
    "A": "E",
    "E": "I",
    "I": "O",
    "O": "U",
    "U": None
}

def solution(word):

    def get_next_word(cur_word):
        if len(cur_word) < 5:
            next_word = cur_word + 'A'
            return next_word
        
        if next_char[cur_word[-1]]:
            next_word = cur_word[:-1] + next_char[cur_word[-1]]
            return next_word
        
        while cur_word[-1] == 'U':
            cur_word = cur_word[:-1]
        
        return cur_word[:-1] + next_char[cur_word[-1]]
    
    cnt = 1
    cur_word = "A"
    while cur_word != word:
        cur_word = get_next_word(cur_word)
        cnt += 1
    return cnt

if __name__ == "__main__":
    print(solution("AAAAE"), 6)
    print(solution("AAAE"), 10)
    print(solution("I"), 1563)
    print(solution("EIO"), 1189)