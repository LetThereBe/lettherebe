import os

from .registry import repository_host


class Repository(object):
    """
    Unified object to represent repositories
    """

    def add_directory_to_repo(local_path, remote_path, message):
        raise NotImplementedError()

    def instructions_to_get_repo(self):
        raise NotImplementedError()


GITHUB_EPILOGUE = """
Your repository has been set up! You can see it in all its glory at:

    {html_url}

If you want to get it locally, you will need to make sure you have git installed,
then you will be able to clone it with:

    git clone {clone_url}

Enjoy!
"""


class GitHubRepository(Repository):

    def __init__(self, repo):
        self._repo = repo

    def add_directory_to_repo(self, local_path, remote_path, message):
        """
        Add a new file to a new branch in a GitHub repo
        """

        from github import InputGitTreeElement

        commit = self._repo.get_branch('master').commit
        git_commit = self._repo.get_git_commit(commit.sha)

        tree_input = []

        # List files
        for root, dirnames, filenames in os.walk(local_path):
            for filename in filenames:

                full_path = os.path.join(root, filename)
                repo_path = os.path.relpath(full_path, local_path)

                with open(full_path, 'r') as f:
                    content = f.read()

                blob = self._repo.create_git_blob(content=content, encoding='utf-8')
                tree_input.append(InputGitTreeElement(os.path.normpath(os.path.join(remote_path, repo_path)),
                                                      "100644", "blob", sha=blob.sha))

        # We make a new tree, commit, and branch
        tree = self._repo.create_git_tree(tree=tree_input)
        commit = self._repo.create_git_commit(tree=tree, message=message, parents=[git_commit])
        master = self._repo.get_git_ref('heads/master')
        master.edit(commit.sha)

    def instructions_to_get_repo(self):
        return GITHUB_EPILOGUE.strip().format(html_url=self._repo.html_url,
                                              clone_url=self._repo.clone_url)


@repository_host('github')
def set_up_github_repo(login_or_token, password, name, description):
    """
    Set up an empty GitHub repository

    Parameters
    ----------
    login_or_token : str
        What is your GitHub username?
    password : str
        what is your GitHub password?
    name : str
        What is the repository name?
    description : str
        Can you provide a one-line description for the package?
    """
    import github
    gh = github.Github(login_or_token=login_or_token,
                       password=password)
    user = gh.get_user()
    repo = user.create_repo(name, description=description, auto_init=True)
    return GitHubRepository(repo)
