word = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
reverse_word = dict(map(reversed, word.items()))

def solution(s):
    result = ''
    english = ''
    eng_word = word.values()

    for i in s:
        if i.isdigit():
            result += i
        else:
            english += i
            if english in eng_word:
                result += str(reverse_word[english])
                english = ''
    return (int(result))
