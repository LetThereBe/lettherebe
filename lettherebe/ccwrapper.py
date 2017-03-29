from cookiecutter.main import cookiecutter
import json
import urllib.request

def downloadtemplate(url):
    response = urllib.request.urlopen(url)
    data = response.read()      
    text = data.decode('utf-8')
    return(text)

def projskeleton(infodict):
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

    #jsoncontent = downloadtemplate(jsonlocation[language_name])
    #infodict = json.loads(jsoncontent)

    infodict['kata'] = infodict['project_name']
    infodict['open_source_license'] = infodict['license'] 

    txt = json.dumps(infodict)
    with open("cookiecutter.json", "w") as f:
        f.write(json.dumps(txt, ensure_ascii=False))

    cookiecutter(gitlocation[infodict['language_name']], 
                 extra_context=infodict,
#                 config_file="cookiecutter.json",
                 overwrite_if_exists=True, 
                 default_config=False,
                 no_input=True, 
                 output_dir="/tmp")

    return(infodict['project_name'])

    
    





