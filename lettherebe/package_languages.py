from .registry import package_language

from cookiecutter.main import cookiecutter
import json
import urllib.request
from lettherebe import ccwrapper

def downloadtemplate(url):
    response = urllib.request.urlopen(url)
    data = response.read()      
    text = data.decode('utf-8')
    return(text)


@package_language('python')
def set_up_python_package(full_name, email, github_username, 
                          project_name, project_short_description, 
                          license, version = '0.1.0'):
    """
    Set up a basic Python package

    Parameters
    ----------
    full_name : str
        Author's full name
    email : str
        Author's email address
    github_username : str
        Author's GitHub username
    project_name : str
        The project name
    project_short_description : str
        Give a short description of your project
    license : {'MIT', 'BSD', 'ISC', 'Apache', 'GNU', 'Not open'}
        Choose a licence for your project
    version : str, optional
        First version of your package. Default is 0.1.0
    """

    jsonlocation = "https://raw.githubusercontent.com/audreyr/cookiecutter-pypackage/master/cookiecutter.json"
    jsoncontent = downloadtemplate(jsonlocation)
    jsondict = json.loads(jsoncontent)

    licensedict = {"MIT": "MIT license",
                   "BSD": "BSD license",
                   "ISC": "ISC license",
                   "Apache": "Apache Software License 2.0",
                   "GNU": "GNU General Public License v3",
                   "Not open": "Not open source"}
    
    jsondict['full_name'] = full_name 
    jsondict['email'] = email
    jsondict['github_username'] = github_username
    jsondict['project_name'] = project_name
    jsondict['project_short_description'] = project_short_description
    jsondict['open_source_license'] = licensedict[license]
    jsondict['version'] = version
    jsondict['use_pytest'] = "y"
    jsondict['language_name'] = "Python"

    return(ccwrapper.projskeleton(jsondict))
    pass


@package_language('cpp')
def set_up_cpp_package(project_name, license):
    """
    Set up a basic C++ package with gTest infrastructure

    Parameters
    ----------
    project_name : str
        The project name
    license : {'MIT', 'Apache', 'GNU'}
        Choose a licence for your project
    """

    jsonlocation = "https://raw.githubusercontent.com/13coders/cookiecutter-kata-cpputest/master/cookiecutter.json"
    jsoncontent = downloadtemplate(jsonlocation)
    jsondict = json.loads(jsoncontent)

    licensedict = {"MIT": "MIT license",
                   "Apache": "Apache Software License 2.0",
                   "GNU": "GNU General Public License v3"}
    
    jsondict['kata'] = project_name
    jsondict['project_name'] = project_name
    jsondict['license'] = licensedict[license]
    jsondict['language_name'] = "C++"
 
    return(ccwrapper.projskeleton(jsondict))
    pass
