from .registry import package_language


@package_language('python')
def set_up_python_package(tests=True):
    """
    Set up a basic Python package

    Parameters
    ----------
    tests : bool, optional
        Should tests be included?
    """
    pass
