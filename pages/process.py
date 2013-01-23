# -*- coding: utf-8 -*-

import sys
import json
from jinja2 import Template
sys.path.append('./libs')
from pynliner_encoded import Pynliner

folder = sys.argv[1]
if folder != '':
    template = open(folder + '/template.html', 'r').read()
    css = open(folder + '/style.css', 'r').read()

    with open(folder + '/data.json') as data_file:
        data = json.load(data_file)

    template = Template(template)
    template = template.render(data)

    p = Pynliner()
    p.from_string(template).with_cssString(css)
    template = p.run()

    open(folder + '/index.html', 'w').write(template.encode('utf-8'))

    print "Generating of %s template is complete" % folder
    print "Please look through %s/index.html file" % folder
else:
    print "You need to specify a template name as a parameter"



