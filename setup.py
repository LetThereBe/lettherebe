from setuptools import setup

entry_points = """
[console_scripts]
lettherebe = lettherebe.main:main
"""

setup(
    version='0.0.2',
    url="https://github.com/LetThereBe/lettherebe",
    name="lettherebe",
    description='LetThereBe Python library and command-line scripts',
    packages=['lettherebe'],
    install_requires=['requests', 'pygithub', 'click', 'colorama', 'cookiecutter', 'sphinx', 'numpydoc'],
    license='BSD',
    author="Mayeul d'Avezac, Ilektra Christidi, Alice Harpole, David Perez Suarez, Thomas Robitaille, Sinan Shi",
    author_email="thomas.robitaille@gmail.com",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points=entry_points
)
