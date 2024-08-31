def ft_filter(function, iterable):

    """
    Args:
        function: a function that returns a boolean
        iterable: an iterable lie sets, lists, tuples etc.
    Returns:
        type: same as iterable
        value: iterable with item for which function(item) is true

        When None used as first argument,
        all elemts that gives True if converted to boolean are extracted

    """

    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
