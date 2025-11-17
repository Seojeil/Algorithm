import sys

while True:
    try:
        line = sys.stdin.readline()
        
        if not line:
            break
            
        A, B = map(int, line.split())
        
        print(A + B)
        
    except:
        break