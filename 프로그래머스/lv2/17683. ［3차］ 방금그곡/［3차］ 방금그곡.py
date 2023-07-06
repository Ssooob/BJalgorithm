def replace_code(cc):
    cc = cc.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    return cc

def solution(m, musicinfos):
    res = []

    for musicinfo in musicinfos: # 구분자로 분리하여 각각 저장
        info = musicinfo.split(',')
        start = info[0].split(':')
        end = info[1].split(':')
        
        # 재생 시간 구하기고, 네오가 기억한 멜로디로 바꾸고
        time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1]) 
        code = replace_code(info[3])
        # 재생 시간만큼의 코드 구하기
        code = code * (time // len(code)) + code[:time%len(code)]
        
        # 네오가 기억하는 멜로디가 구한 코드에 포함되는지 확인 
        if replace_code(m) in code:
            res.append([info[2], time])

    if len(res) == 0:
        return "(None)" # 후보군에 없을 시 '(None)' 반환
    
    else:
        res = sorted(res, key = lambda x: (-x[1])) # 재생된 시간과, 입력된 순서 기준으로 정렬
        return res[0][0] 
