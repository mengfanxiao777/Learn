def MAX(arrays,n):
    sum1=0;maxs=arrays[0]
    for i in arrays:
        if sum1<0:
            sum1=i
        else:
            sum1+=i
        if sum1>=maxs:
            maxs=sum1
    sum2=0;mins=arrays[0];alls=0
    for i in arrays:
        alls+=i
        if sum2<=0:
            sum2+=i
        if sum2>0:
            sum2=0
        if sum2<mins:
            mins=sum2
    return max(maxs,alls-mins)

if __name__ == '__main__':
    n=int(input("Please input the length of the array\n"))
    array=[]
    for i in range(n):
        num=int(input())
        array.append(num)
    print('最大子数组和为',MAX(array,n))
