def solution(participant, completion):
    answer = ''
    for p in participant:
        
        # 해당 단어가 목록에 있는지 확인
        if not p in completion:
            # 없다면 answer에 넣기
            answer = p
        # 있다면 중복 방지를 위해 목록에서 제거
        else:
            completion.remove(p)
    return answer