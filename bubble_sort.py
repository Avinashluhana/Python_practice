list = [4,3,1,5,5,6,7,2]

def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

sort(list)
print(list)
