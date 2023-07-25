def solution(phone_book):
    answer = True
    
    # 카운트 갯수 저장항 딕셔너리
    phone_count = {}
    
    # 모든 앞자리 경우의 수를 카운트
    for base in phone_book:
        for i in range(1, len(base)+1):
            phone_number = base[:i]
            phone_count[phone_number] = phone_count.get(phone_number, 0) + 1
            
    # 해당 번호를 앞자리로 가지고 있는 번호의 갯수
    for phone in phone_book:
        if phone_count[phone] > 1:
            return False
    return answer