def median(l):
    l.sort()
    n = len(l)

    #for odd case
    if n%2== 1:
        return l[n//2]
    else:
        mid1 = l[n//2-1]
        mid2 = l[n//2]
        return ((mid1 + mid2 )/ 2)

        

l = list(map(int,input("Enter numbers seperated by space: ").split()))
print(f"Median = {median(l)}")