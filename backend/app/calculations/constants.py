import math

def calculate_a(r, s):
    numerator = math.sqrt((r * r) + 1)
    denominator = 2 * (r - 1)

    return (numerator / denominator) * math.log(
        (1 - s) / (1 - (r * s))
    )#verified


def calculate_b(r, s):

    return (
        (2 / s)
        - 1
        - r
        + ((2 / s) * math.sqrt((1 - s) * (1 - r * s)))
        + math.sqrt((r * r) + 1)
    )#verified


def calculate_c(r, s):

    return (
        (2 / s)
        - 1
        - r
        + ((2 / s) * math.sqrt((1 - s) * (1 - r * s)))
        - math.sqrt((r * r) + 1)
    )#verified


def calculate_ft(a, b, c):
    return a / math.log(b / c)#verified

def calculate_r(T1, T2, t1, t2):
    return (T1 - T2) / (t2 - t1)#verified


def calculate_s(T1, t1, t2):
    return (t2 - t1) / (T1 - t1)#verified