def minion_game(string):
    # your code goes here
    Kevin_score=0
    Stuart_score=0
    Vowel="AEIOU"
    for i in range (len(string)):
        if s[i] in Vowel:
            Kevin_score+=len(string)-i
        else:
            Stuart_score+=len(string)-i
    if Stuart_score>Kevin_score:
        print("Stuart "+str(Stuart_score))

    elif Stuart_score<Kevin_score:
        print("Kevin "+str(Kevin_score))
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)