x = [10, 20, 30, 40, 50, 60]


def mean(x):
    mean = (sum(x) / len(x))
    return mean


def median(x):
    x.sort()
    q = len(x) // 2
    if len(x) % 2 != 0:
        return x[q]
    elif len(x) % 2 == 0:
        return (x[q - 1] + x[q]) / 2
        return median


def mode(x):
    counter = 0
    num = x[0]
    for i in x:
        curr_frequency = x.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
        if len(set(x)) == len(x):
            return 'there is no mode'
    return num


def dev(x):
    for i in x:
        x.append(i - mean(x))
    return dev

