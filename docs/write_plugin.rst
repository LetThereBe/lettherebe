Writing a plugin
================

**LetThereBe** is designed to be extensible and customisable so that it can be
**tailored to other services or programming languages, and users can write
**plugins. Any code below can be either added to a config.py file in the
directory from where you are running the ``lettherebe`` command, or you can
add them to the main package via There are three main components that can be extended:

Repository hosting providers
----------------------------

At the moment we have provided support for GitHub, but other services such as
BitBucket or GitLab could be added. To do this, you need to define a function
that sets up a repo on the given service. The basic structure of the code to do
this is::

    from lettherebe.registry import repository_host, Repository


    class MyRepository(Repository):

        def add_directory_to_repo(local_path, remote_path, message):
            # Code here that knows how to put the directory at local_path into
            # the repository, in a sub-directory given by remote_path. The
            # message argument gives the commit message.

        def instructions_to_get_repo(self):
            # This should return a string with instructions on how to access
            # the repository and how to clone.

    @repository_host('name-of-service')
    def set_up_repo(argument1, argument2=False):
        """
        Set up an empty repository on a repository host

        Parameters
        ----------
        argument1 : str
            What is the value of argument1?
        argument2 : bool, optional
            What about the value of argument2?
        """
        # create repo here then return class to provide abstract interface
        return MyRepository(...)

It is important that this function returns a Repository subclass, but otherwise
you can do anything you like in the function. All the rest will be taken care of
by the ``lettherebe`` package!
