from cvplibrary import CVPGlobalVariables, GlobalVariableNames
import yaml
import cvp
from jinja2 import Template

# load CVP info and connect to server
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
cvp_user = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_USERNAME)
cvp_passwd = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_PASSWORD)
server = cvp.Cvp("localhost")
server.authenticate(cvp_user, cvp_passwd)

# Load yaml
vars_file = server.getConfiglet('lab_vars')
vars = yaml.load(vars_file.config)

# Load spine j2
spine_j2 = server.getConfiglet('spine_j2')
spine_template = Template(spine_j2.config)

# Load leaf j2
leaf_j2 = server.getConfiglet('leaf_j2')
leaf_template = Template(leaf_j2.config)

for site in vars:
    if site == hostname:
        if 'spine' in site:
            config = spine_template.render(vars[site])
            print(config)
        elif 'leaf' in site:
            config = leaf_template.render(vars[site])
            print(config)