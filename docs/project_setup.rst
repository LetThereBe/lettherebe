Setting up a project
====================

Information on how to get started setting up a new project using ``LetThereBe``.

Before setting up your project, you will need a `GitHub <https://github.com>`_ account. If you do not currently have one, you will need to register.

To begin setting up a project using ``LetThereBe``, navigate to the project directory and enter the command

::

    lettherebe quickstart [--options]

where ``options`` are optional options for your project (see below).

This will then take you through the set up of your project with a set of prompts. The first prompt will ask you for the details of your GitHub account - if you have not got one, you will be directed to register for one. Next, you will be asked for the name of the project, then ``LetThereBe`` will then provide a series of prompts about the specifics of your project. If all the default options are chosen, your project will end up with:

- a `GitHub <https://github.com>`_ repository
- an **MIT License**
- simple example **tests** to be executed using  ``py.test``
- **continuous integration** of these tests using `Travis CI <https://travis-ci.org>`_
- **code coverage** provided by `Codecov <https://codecov.io>`_
- **documentation** with  `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ which will be automatically built on `ReadTheDocs <https://readthedocs.org>`_


Advanced Setup
--------------

If you choose not to use the default options, you will then be prompted to provide answers to a series of questions which will allow you to customise these settings. Alternatively, you will have the ability to provide a configuration file describing the settings you would like to use, making it easy to reuse settings from other projects. **Insert information about config file here**.

The initial project setup command can also be modified using the following options as an alternative to passing these when prompted by the wizard.

--project=name          name of project
--service=service       version control service to use
--language=language      sets the project language (e.g. ``python``, ``julia``, ``R``...)
--license=license           sets the project license (e.g. MIT, BSD,....
--CI=provider           sets which continuous integration provider to use, e.g. Travis CI, CircleCI,...
--docs=package          sets which package to use to build the documentation, e.g. Sphinx, Doxygen...

``LetThereBe`` can also be used to set up each of the above components separately. To do this, first navigate to the project directory, then execute one of the following commands

::

    lettherebe docs [-options]

If no options are passed, this will set up sphinx documentation which is then automatically built on ReadTheDocs. Alternatively, the following options can be passed:

-sphinx         documentation is set up using Sphinx
-doxygen        documentation is set up using Doxygen
-readthedocs    documentation hosted and built online in ReadTheDocs
-offline        documentation built locally only (not connected to ReadTheDocs)

::

    lettherebe tests [-options]

If there are no options passed and the project language has been set to ``python``, this will set up some simple tests that can be run using ``py.test`` and will connected to a ``travis.ci`` project so that they are executed when changes to the code are pushed to the GitHub repository. The following options are possible:

-travis         sets up continuous integration using ``travis.ci``
-circle         sets up continuous integration using ``Circle CI``
