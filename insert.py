def insertion_sort(vec):
     for i in range(1, len(vec)):
        j = i - 1
        element_next = vec[i]
        while (vec[j] > element_next) & (j >= 0):
            vec[j+1]=vec[j]
            j = j - 1
            print(vec)
        vec[j+1] = element_next