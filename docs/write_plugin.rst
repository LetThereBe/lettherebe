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

The questions for the command-line and website are taken from the docstring,
which should be in NumpyDoc format. Default values can be specified by using
keyword arguments. It is important that this function returns a Repository
subclass, but otherwise you can do anything you like in the function. All the
rest will be taken care of by the ``lettherebe`` package!

Package templates for different languages
-----------------------------------------

To add support for a 'best practice template' for a new language, you will need
to define a function as follows::

    from lettherebe.registry import package_language

    @package_language('fortran66')
    def set_up_fortran66_package(tests=True):
        """
        Set up a basic Python package

        Parameters
        ----------
        tests : bool, optional
            Should tests be included?
        """
        directory = tempfile.mkdtemp()
        # populate directory here
        return directory

The use of ``tests`` as the argument is just an example, and you can put any
number of arguments/options. The function should write the generated files
to a local temporary directory and return the path to this directory. The rest
of the package will then automatically sync those generated files to the
remote repository.
