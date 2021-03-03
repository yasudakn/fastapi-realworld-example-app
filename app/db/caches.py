
def key_builder(func, *args, **kwargs):
    ordered_kwargs = sorted(kwargs.items())
    return '{0}{1}({2}){3}'.format(
        (func.__module__ + "." or ""),
        func.__name__,
        str(','.join(
            '.'.join((x.__class__.__module__, x.__class__.__name__))
                for x in args[0:])
                    if 0 < len(args) else ""),
        str(ordered_kwargs)
    )