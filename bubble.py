# Сортировка пузырьком O(n^2) 
def bubble_sort(vec):
        for i in range(len(vec)-1,0,-1):
            for j in range(i):
                if vec[j] >= vec[j+1]:
                    vec[j], vec[j+1] = vec[j+1], vec[j]