from cookiecutter.main import cookiecutter
import json
import urllib.request

def projskeleton(infodict):
    gitlocation = {
        "C++": "https://github.com/13coders/cookiecutter-kata-gtest", 
        "Python": "https://github.com/audreyr/cookiecutter-pypackage"
    }


    txt = json.dumps(infodict)
    with open("cookiecutter.json", "w") as f:
        f.write(json.dumps(txt, ensure_ascii=False))

    cookiecutter(gitlocation[infodict['language_name']], 
                 extra_context=infodict,
                 config_file="cookiecutter.json",
                 overwrite_if_exists=True, 
                 default_config=False,
                 no_input=True, 
                 output_dir="/tmp")

    return('/tmp/' + infodict['project_name'])

    
    





