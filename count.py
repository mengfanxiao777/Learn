import random
Str_array=[]
def Practices(num):
    for i in range(num):
        a1 = random.randint(1, 100)
        a2 = random.randint(1, 100)
        a3 = random.randint(1, 100)
        ch=[['+','-'],['*','/']]
        strs=str(a1)+ch[a1%2][a2%2]+str(a2)+ch[a2%2][a3%2]+str(a3)+'='
        RM_DUP(strs)

def RM_DUP(strs):
    if strs not in Str_array:
        Str_array.append(strs)
        print(strs)

if __name__=="__main__":
    num=int(input("Please input the num\n"))
    Practices(num)

