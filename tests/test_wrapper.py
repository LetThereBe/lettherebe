import pytest
import os
import shutil
#import projskeleton
from lettherebe import ccwrapper


def test_git_downloader():
    txt = ccwrapper.downloadtemplate('https://raw.githubusercontent.com/audreyr/cookiecutter-pypackage/master/cookiecutter.json')
    assert type(txt) is str
    assert len(txt) > 0
#    shutil.rmtree("for_test", ignore_errors=True)
#    testrepo = "https://github.com/sinanshi/for_test"
#    projskeleton.downloadtemplate(testrepo)
#    shutil.rmtree("for_test", ignore_errors=True)

def test_projskeleton():
    pjn = ccwrapper.projskeleton("myname", "test@ucl.ac.uk", 
                              "gitname", "myproj", "Python", 
                              "This is a test project", 
                              "MIT")

    assert pjn == 'myproj'
   # projskeleton.projskeleton("", "", "", "", "Python", "", "")
   # projskeleton.projskeleton("", "", "", "", "fortran", "", "")


