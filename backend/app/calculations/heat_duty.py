def calculate_qs(flow, cp, t1, t2):
    """
    Shell Side Heat Duty
    """
    return (flow * cp * (t1 - t2)) / 1000000


def calculate_qt(flow, cp, t1, t2):
    """
    Tube Side Heat Duty
    """
    return (flow * cp * (t2 - t1)) / 1000000