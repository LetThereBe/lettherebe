from .registry import package_language


@package_language('python')
def set_up_python_package(name, tests=True, directory='.'):
    """
    Set up a basic Python package

    Parameters
    ----------
    name : str
        What is the package name?
    tests : bool, optional
        Should tests be included?
    directory : str, optional
        Which directory should the files be written to?
    """
    pass
