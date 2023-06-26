def get_missing_number(A,K):
    left=0
    right=len(A)-1
    while left<=right:
        middle=left+((right-left)//2)
        missing_number=A[middle]-middle-A[0]
        if missing_number<K:
            left=middle+1 
        else:
            right=middle-1
    return A[0]+left+K-1

N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
print(get_missing_number(A,K))