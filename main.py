

def guess(mixn,maxn):#这个函数用于根据给定的范围猜测数字
    if mixn == maxn:
        return mixn
    if mixn > maxn:
        mixn , maxn = maxn , mixn
    number = maxn - mixn + 1
    if number%2 == 0:
        result = int(number//2)+mixn-1
    else:
        result = int((number+1)//2)+mixn-1
    return result


def replace(mixn,maxn,guess,result):#这个函数用于更新猜测范围
    '''
    输出结果为 最小值，最大值
    '''
    if result == 2:
        return mixn,guess-1
    elif result == 1:
        return guess+1,maxn


def check(guess_number):#这个函数用于检查猜测结果
    '''
    输出逻辑:
    猜测结果>key,返回1
    猜测结果<key,返回2
    猜测结果=key,返回0
    '''
    key=10
    if key>guess_number:
        return 1
    elif key<guess_number:
        return 2
    else:
        return 0

def main():
    mixn = 1
    maxn = 100
    while True:
        guess_number = guess(mixn,maxn)
        result = check(guess_number)
        if result == 0:
            break
        mixn,maxn = replace(mixn,maxn,guess_number,result)
    print(f'猜测完成,结果:{guess_number}')
main()


        


