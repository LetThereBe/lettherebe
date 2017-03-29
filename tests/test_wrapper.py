import pytest
from lettherebe import ccwrapper


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
    assert pjn.find('myproj') > 0
