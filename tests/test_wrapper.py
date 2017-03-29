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

    info = {'full_name': "myname",
            'email': "test@gmail.com", 
            'github_username': "gitname", 
            'project_name': "myproj", 
            'language_name': "Python", 
            'project_short_description': "This is a test project",  
            'license': "BSD",
            'version': '0.1.0'}
    
    pjn = ccwrapper.projskeleton(info)

    assert pjn == 'tmp/myproj'
   # projskeleton.projskeleton("", "", "", "", "Python", "", "")
   # projskeleton.projskeleton("", "", "", "", "fortran", "", "")


