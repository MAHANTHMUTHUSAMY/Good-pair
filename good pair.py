def good_pair(array,value):
    n = len(array)
    l=0
    for i in range(n):
        for j in range(i+1,n):
            if i != j and array[i] + array[j] == value:
                l+=1
    print(l)
array = list(map(int,input('A=').split()))
value = int(input('B='))
good_pair(array,value)