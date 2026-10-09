import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    a = [0] + [int(x) for x in input_data[1 : n + 1]]
    b = [0] + [int(x) for x in input_data[n + 1 : 2 * n + 1]]
    
    total_stock = 0
    cnt = 0
    x = [0] * (n + 1)
    
    pq = []
    
    for i in range(1, n + 1):
        total_stock += a[i]
        
        if total_stock >= b[i]:
            total_stock -= b[i]
            cnt += 1
            x[i] = 1
            heapq.heappush(pq, (-b[i], i))
            
        elif pq:
            max_cost = -pq[0][0]
            max_idx = pq[0][1]
            
            if max_cost > b[i]:
                heapq.heappop(pq)
                total_stock = total_stock + max_cost - b[i]
                x[max_idx] = 0
                x[i] = 1
                heapq.heappush(pq, (-b[i], i))
                
    print(cnt)
    
    chosen_days = [str(i) for i in range(1, n + 1) if x[i] == 1]
    print(" ".join(chosen_days))

if __name__ == "__main__":
    solve()