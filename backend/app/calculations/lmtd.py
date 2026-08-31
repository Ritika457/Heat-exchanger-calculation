import math

def calculate_lmtd(T1, T2, t1, t2):

    numerator = (T1 - t2) - (T2 - t1)

    denominator = math.log(
        (T1 - t2) /
        (T2 - t1)
    )

    return numerator / denominator


def corrected_lmtd(lmtd, ft):

    return lmtd * ft