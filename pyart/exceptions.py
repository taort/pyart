"""
pyart.exceptions
================

Custom Py-ART exceptions.

.. autosummary::
    :toctree: generated/

    MissingOptionalDependency
    DepreciatedAttribute
    DepreciatedFunctionName
    _depreciated_alias

"""

import warnings


class MissingOptionalDependency(Exception):
    """ Exception raised when a optional depency is needed by not found. """
    pass


class DepreciatedAttribute(DeprecationWarning):
    """ Warning catagory for an attribute which has been renamed/moved.  """
    pass


class DepreciatedFunctionName(DeprecationWarning):
    """ Warning catagory for a function which has been renamed/moved. """
    pass


def _depreciated_alias(func, old_name, new_name):
    """

    A function for creating an alias to a renamed or moved function.

    Parameters
    ----------
    func : func
        The function which has been renamed or moved.
    old_name, new_name : str
        Name of the function before and after it was moved or renamed
        (with namespace if changed).

    Returns
    -------
    wrapper : func
        A wrapper version of func, which issues a DepreciatedFunctionName
        warning when the called.

    """
    def wrapper(*args, **kwargs):
        warnings.warn(
            ("{0} has been depreciated and will be removed in future " +
             "versions of Py-ART, pleases use {1}. ").format(
                old_name, new_name), category=DepreciatedFunctionName)
        return func(*args, **kwargs)
    return wrapper
