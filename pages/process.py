# -*- coding: utf-8 -*-

from pynliner import Pynliner
import sys
import json
from pprint import pprint

folder = sys.argv[1]
if folder != '':
    template = open(folder + '/template.html', 'r').read()
    css = open(folder + '/style.css', 'r').read()

    p = Pynliner()
    p.from_string(template).with_cssString(css)
    prerender = p.run()

    with open(folder + '/data.json') as data_file:
        data = json.load(data_file)

    result = ""

    for item in data:
        prerender = prerender.replace("{photo}", item["photo"])
        prerender = prerender.replace("{name}", item["name"])
        prerender = prerender.replace("{position}", item["position"])
        prerender = prerender.replace("{information}", item["information"])

        links_block = ""

        for link in item["links"]:
            links_block += "<li><a href='%(link)s'>%(title)s</a></li>" % {'link':link['link'], 'title':link['title']}

        prerender = prerender.replace("{links}", links_block)
        result += prerender

    f = open(folder + '/index.html', 'w')
    f.write(result.encode("utf-8"))

    print "Generating complete"



