import json
import site
import subprocess
import sys
import yaml
data = {'1. version of python': sys.version,
        '2. virtualenv': sys.exec_prefix,
        '3. python executable location': sys.executable,
        '4. pip location': str(subprocess.getoutput("which pip")),
        '5. PYTHONPATH': sys.path,
        '6. installed packages (name, version)':
            next(i for i in sys.path if "site-packages" in i),
        '7. site-packages location': site.getsitepackages()}
with open('data.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys=True, indent=4)
