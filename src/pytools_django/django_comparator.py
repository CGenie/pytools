# Compare same 2 Django model instances

from django.db import models


def compare(a, b):
    ret = {}

    for x in dir(a):
        try:
            ax = getattr(a, x)
            bx = getattr(b, x)
        except AttributeError:
            continue

        equal = True

        if not callable(ax):
            if isinstance(ax, models.Model):
                if ax.pk != bx.pk:
                    equal = False
            elif ax != bx:
                equal = False

        if not equal:
            ret[x] = (ax, bx)

    return ret
