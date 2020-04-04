
pos= 0
list = [3,5,62,4,5]

sear = 62

def search(list,n):
    for i in range(len(list)):
        if list[i]==n:

            globals()['pos'] = i
            print("found at postion",pos+1)
            break


    else:
            print("Not found")

search(list,sear)