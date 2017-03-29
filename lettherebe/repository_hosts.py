from .registry import repository_host


@repository_host('github')
def set_up_github_repo(name):
    """
    Set up an empty GitHub repository

    Parameters
    ----------
    name : str
        What is the repository name?
    """
    pass
