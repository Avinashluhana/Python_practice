pos = -1
list=[1,3,5,6,7,8]
sear = 6

hi=len(list)-1
low=0


while low <= hi:

        mid = (hi + low) // 2

        if list[mid] == sear:
            globals()['pos'] =  mid
            print("found", pos)
            break
        else:
            if list[mid]<sear:
                low=mid+1
            else:
                hi=mid-1
