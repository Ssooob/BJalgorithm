def solution(number, k):
    Falg = True
    answer = []
    cnt = 0 
    for n in number:
        while answer and k > 0 and answer[-1] < n :
            answer.pop()
            k -= 1
        answer.append(n)
    if len(answer) != len(number)-k:
        answer = answer[:len(number)-k] 

    return ''.join(answer)