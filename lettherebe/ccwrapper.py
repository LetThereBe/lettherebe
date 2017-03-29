from cookiecutter.main import cookiecutter
import json
import urllib.request

def downloadtemplate(url):
    response = urllib.request.urlopen(url)
    data = response.read()      
    text = data.decode('utf-8')
    return(text)

def projskeleton(full_name, email, github_username, 
                 project_name, language_name,
                 project_short_description, 
                 license, 
                 version = '0.1.0'):
    """
    parameter:
    ---------------
    full_name: str

    """
    gitlocation = {
        "C++": "https://github.com/13coders/cookiecutter-kata-gtest", 
        "Python": "https://github.com/audreyr/cookiecutter-pypackage"
    }

    jsonlocation = {
        "Python": "https://raw.githubusercontent.com/audreyr/cookiecutter-pypackage/master/cookiecutter.json",
        "C++": "https://raw.githubusercontent.com/13coders/cookiecutter-kata-cpputest/master/cookiecutter.json"
    }

    jsoncontent = downloadtemplate(jsonlocation[language_name])
    jsondict = json.loads(jsoncontent)


    jsondict['full_name'] = full_name 
    jsondict['email'] = email
    jsondict['github_username'] = github_username
    jsondict['project_name'] = project_name # Python
    jsondict['kata'] = project_name # C++
    jsondict['project_short_description'] = project_short_description
    jsondict['license'] = license # C++
    jsondict['open_source_license'] = license # Python
    jsondict['version'] = version
    jsondict['use_pytest'] = "y"

    txt = json.dumps(jsondict)
    with open("cookiecutter.json", "w") as f:
        f.write(json.dumps(txt, ensure_ascii=False))

    cookiecutter(gitlocation[language_name], 
                 extra_context=jsondict,
                 config_file="cookiecutter.json",
                 overwrite_if_exists=True, 
                 default_config=False,
                 no_input=True, 
                 output_dir="/tmp")

    return(jsondict['project_name'])

    
    





