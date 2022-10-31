def get_mean(x):
    return (sum(x) / len(x))
def get_median(x):
    x.sort()
    q=len(x)//2
    if len(x)%2!=0:
        return x[q]
    elif len(x)%2==0:
        return (x[q-1]+x[q])/2
    return median
def get_dev(x,get_mean):
    return [i-get_mean(x) for i in x]
def my_abs(i):
    if i<0:
        return -i
    else:
        return i
def get_absolute(x):
    return [my_abs(i) for i in x]
def get_square(x):
        return [i**2 for i in x]
def get_var(x):
    return sum(x)/len(x)
def SD(x):
    return (x)**0.5
x=[10,20,30,40,50]
print(get_dev(x,get_mean))
x=get_dev(x,get_mean)
print(get_absolute(x))
x=get_absolute(x)
print(get_square(x))
x=get_square(x)
print(get_var(x))
x=get_var(x)
print(SD(x))
















