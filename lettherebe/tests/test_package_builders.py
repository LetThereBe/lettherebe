import pytest
from lettherebe import package_languages as pl


def test_python_package_builder():
    outdict = pl.set_up_python_package("myname",
                                       "test@gmail.com", 
                                       "gitname", 
                                       "myproj", 
                                       "This is a test project",  
                                       "BSD",
                                       "0.1.0")
    assert len(outdict)>0


def test_cpp_package_builder():
    outdict = pl.set_up_cpp_package("myproj",
                                    "MIT")
    assert len(outdict)>0
