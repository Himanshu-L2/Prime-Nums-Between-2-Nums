start = int(input('Please enter the starting number : '))
end = int(input('Please enter last number : '))


for i in range (start , end+1):
    flag= 0
    for a in range(2, i):
        if ((i % a) == 0):
            flag = 1
            break

    if(flag!=1):
        print(i)