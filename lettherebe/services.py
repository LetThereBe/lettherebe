from .registry import service


@service('readthedocs')
def set_up_readthedocs(repository):
    """
    Set up readthedocs for the repository

    Parameters
    ----------
    repository : str
        What is the repository name?
    """
    pass


@service('travis')
def set_up_travis(repository):
    """
    Set up Travis for the repository

    Parameters
    ----------
    repository : str
        What is the repository name?
    """
    pass

