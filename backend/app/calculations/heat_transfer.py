def calculate_u_shell(qs, adeltln):
   return (qs * 1000000) / adeltln


def calculate_u_tube(qt, adeltln):
   return (qt * 1000000) / adeltln


def approach_temperature(T1, t2):
    return T1 - t2


def calculate_adeltln(area, corrected_lmtd):
    return area * corrected_lmtd