import pytest
from lettherebe import package_languages as pl


def test_git_downloader():
    txt = pl.downloadtemplate('https://raw.githubusercontent.com/audreyr/cookiecutter-pypackage/master/cookiecutter.json')
    assert type(txt) is str
    assert len(txt) > 0


def test_python_package_builder():
    outloc = pl.set_up_python_package("myname",
                                      "test@gmail.com", 
                                      "gitname", 
                                      "mypyproj", 
                                      "This is a test project",  
                                      "BSD",
                                      "0.1.0")
    assert outloc.find('mypyproj') > 0


def test_cpp_package_builder():
    outloc = pl.set_up_cpp_package("mycppproj",
                                   "MIT")
    assert outloc.find('mycppproj')
