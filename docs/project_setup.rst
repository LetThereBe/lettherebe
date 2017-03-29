Setting up a project
====================

Information on how to get started setting up a new project using ``LetThereBe``.

To begin setting up a project using ``LetThereBe``, navigate to the project directory and enter the command

::

    lettherebe project "PROJECTNAME"

where ``PROJECTNAME`` is the name of your project.

This will then take you through the set up of your project with a set of prompts. The first prompt will ask if you wish to use the default options: in this case, ``LetThereBe`` will do the rest of the work for you and set up a ``python`` project with:

- a `GitHub <https://github.com>`_ repository
- an **MIT License**
- simple example **tests** to be executed using  ``py.test``
- **continuous integration** of these tests using `Travis CI <https://travis-ci.org>`_
- **documentation** with  `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ which will be automatically built on `ReadTheDocs <https://readthedocs.org>`_
