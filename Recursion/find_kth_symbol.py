# PS: We are given two number K and N where we have to generate grammer where N is number of step and
# K it position of a symbol in Nth step, N starts at 0 and first it generate 0. Also 0 will generate 01 in next step
# and 1 will generate 10 in next step. So
# N =0 => 0, N=1 => 01, N=2 => 0110, N=3 => 01101001 . So if N=3 and  k=6 , it should return 0
# ( 1st position started at k=1 which is 0)

def find_kth_symbol(N, K):
    # Base condition
    if N == 1:
        return 0

    mid = 2**(N-2)
    if K <= mid:
        return 1 if find_kth_symbol(N-1, K) else 0
    else:
        return 0 if find_kth_symbol(N-1, K-mid) else 1

N=4
K=9
res = find_kth_symbol(N,K)
print(res)