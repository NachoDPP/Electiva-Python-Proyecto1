from datetime import time


def TryParseInt(value):
    """Permite convertir un valor a numérico si es posible"""
    try:
        intValue = int(value)
        return intValue
    except ValueError:
        return None


def TryParseTime(hours: int, mins: int, segs: int):
    """Permite convertir un valor a time si es posible"""
    try:
        timeValue = time(hours, mins, segs)
        return timeValue
    except Exception:
        return None
