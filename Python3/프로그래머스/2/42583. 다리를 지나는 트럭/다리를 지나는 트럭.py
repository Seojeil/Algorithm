from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = 0 # 걸린 시간
    bridge = [0] * bridge_length # 다리
    bridge = deque(bridge)
    current_weight = 0 # 다리에 올라간 트럭의 무게
    
    while truck_weights: # 순서대로 트럭 진입(트럭이 모두 진입할때까지)
        second += 1 # 시간 흐름
        current_weight -= bridge[0] # 다리의 첫칸에 있는 무게 제거
        bridge.popleft() # 다리의 첫칸 제거
        
        if current_weight + truck_weights[0] <= weight: # 다리의 무게제한 검사
            bridge.append(truck_weights[0]) # 다리에 트럭 진입
            current_weight += truck_weights[0] # 트럭의 무게 추가
            truck_weights.pop(0) # 가장 앞의 트럭 진입
        else:
            bridge.append(0) # 무게제한에 걸릴 경우 트럭을 진입시키지 않음
        # print(bridge)
        
    return second + bridge_length