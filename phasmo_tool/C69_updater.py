try:
    import requests
except Exception:
    print(chr(69))
    import os
    import sys
    os.system(f"{sys.executable} -m pip install requests")
    import requests
import subprocess
import shutil
import json
import sys
import os

def download(url:str) -> None:
    get_responce = requests.get(url, stream=True)
    filename = url.split('/')[-1]
    
    with open(filename, "wb") as f:
        for chunk in get_responce.iter_content(chunk_size=1024):
            f.write(chunk)
            
    return filename

def check_update(project_name:str, version:str) -> tuple:
    r = requests.get("https://c69projectrepo.crossroadsactua.repl.co/stuff.json")
    projects = json.loads(r.content.decode('utf-8'))
    
    if projects[project_name]["version"] != version:
        return (True, projects[project_name])
    
    return (False, "All up to date")
    

def update_program(project_name:str) -> None:
    filename = download(f"https://c69projectrepo.crossroadsactua.repl.co/{project_name}.zip")
    
    shutil.unpack_archive(filename, f"./")
    os.remove(filename)
    subprocess.Popen(f"{sys.executable} ./Gui.py")
    sys.exit(0)


