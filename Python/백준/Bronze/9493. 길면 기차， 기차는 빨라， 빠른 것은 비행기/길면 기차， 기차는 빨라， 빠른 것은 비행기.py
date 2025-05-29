import sys

input = sys.stdin.readline

while True:
    M, A, B = map(int, input().split())
    
    if M == 0 and A == 0 and B == 0:
        break
    
    # 시간 차이를 분 단위로 계산
    time_diff_minutes = M * (1/A - 1/B) * 60
    
    # 시, 분, 초로 분리
    hours = int(time_diff_minutes // 60)
    remaining_minutes = time_diff_minutes - (hours * 60)  # 남은 분
    minutes = int(remaining_minutes)
    remaining_seconds = (remaining_minutes - minutes) * 60  # 소수 부분을 초로
    seconds = round(remaining_seconds)
    
    # 반올림으로 인한 초 오버플로우 처리
    if seconds == 60:
        seconds = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
    
    # 문자열 포맷팅
    hours_str = str(hours)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)
    
    print(f"{hours_str}:{minutes_str}:{seconds_str}")