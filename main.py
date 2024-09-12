

def guess(mixn,maxn):
    '''
    if mixn == maxn:
        return mixn
    if mixn > maxn:
        mixn , maxn = maxn , mixn
    number = maxn - mixn + 1
    if number%2 == 0:
        return int(number//2)
    else:
        return int((number+1)//2)
    '''
    if mixn == maxn:
        return mixn
    if mixn > maxn:
        mixn , maxn = maxn , mixn
    number = maxn - mixn + 1
    if number%2 == 0:
        return int(number//2)
    else:
        return int((number+1)//2)

def replace(minn,maxn,guess,result):#booln:1.guess<key:True 2.guess>key:False
    if result=='ok':
        return guess,maxn
    if result:
        minn=guess
        pass
    else:
        maxn=guess
        pass
    return minn,maxn
def check(guess):
    key=10
    if key>guess:
        return True
    elif key<guess:
        return False
    else:
        return 0

minn=1
maxn=100
key=10


i=0
print(guess(1,2))
'''
while minn!=maxn:
    guessn = median(minn,maxn)
    if guessn<key:
        result=True
    elif guessn<key:
        result=False
    else:
        minn=median(minn,maxn)
        maxn=minn
        result = minn
    print(f'当前范围:最小值:{minn}最大值:{maxn}猜测值:{guessn}结果:{result}')
    minn , maxn = replace(minn,maxn,guessn,result)
print(f'最终结果:{minn}')
'''