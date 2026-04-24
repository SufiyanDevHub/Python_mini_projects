def mean(*l):

    total = 0
    #sum of the list
    for i in l:
        total+=i

    # calculation of mean

    return total/len(l)





l = [1,2,3,4,5,6]
print(mean(*l))