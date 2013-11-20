# Compare same 2 Django model instances


def compare(a, b):
    ret = {}

    for x in dir(a):
        try:
            ax = getattr(a, x)
            bx = getattr(b, x)
        except AttributeError:
            continue

        if not callable(ax) and ax != bx:
            ret[x] = (ax, bx)

    return ret
