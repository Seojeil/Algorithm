import sys

def is_uniform(video):
    """전체 블록이 모두 같은 값인지 확인"""
    if not video or not video[0]:
        return True
    
    first_char = video[0][0]
    for row in video:
        for char in row:
            if char != first_char:
                return False
    return True

def divide_video(video):
    """영상을 4개 블록으로 분할 (왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래)"""
    n = len(video)
    half = n // 2
    
    # 왼쪽 위
    top_left = [row[:half] for row in video[:half]]
    # 오른쪽 위  
    top_right = [row[half:] for row in video[:half]]
    # 왼쪽 아래
    bottom_left = [row[:half] for row in video[half:]]
    # 오른쪽 아래
    bottom_right = [row[half:] for row in video[half:]]
    
    return [top_left, top_right, bottom_left, bottom_right]

def compress(video):
    """쿼드 트리 압축"""
    # 모든 픽셀이 같은 값인지 확인
    if is_uniform(video):
        return video[0][0]
    
    # 4개 영역으로 분할하고 각각 압축
    result = "("
    blocks = divide_video(video)
    
    for block in blocks:
        result += compress(block)
    
    result += ")"
    return result

# 입력 처리
N = int(input())
video = []
for _ in range(N):
    video.append(input().strip())

# 압축 실행
print(compress(video))