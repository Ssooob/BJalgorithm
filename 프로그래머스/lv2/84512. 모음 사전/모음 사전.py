from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i): # 1에서 5개까지 모든 조합을 구함
            words.append(''.join(list(c))) # 하나의 단어로 

    words.sort() # 정렬
    # 그 이후 index를 사용하여 찾기 
    return words.index(word) + 1