from almostSorted import almostSorted

if __name__ == '__main__':
    
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    almostSorted(arr)