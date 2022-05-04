def fact(n):
    if n==1:
        return  n
    else:
        return n*fact(n-1)

def pal(x):
    x1=x[::1]
    if x1==x:
        return 'palindrome'
    else:
        return 'not palindrome'