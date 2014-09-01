from sys import stdin

import json
from lxml import etree

results = json.loads(stdin.read())

root = etree.Element('pmd')

for item in results["results"]['warning']['items']:
    child = etree.Element('file')
    location = item['location'].rsplit(':')
    child.set('name', location[0])

    violation = etree.Element('violation')
    violation.set('beginline', location[1])
    violation.set('endline', location[1])
    violation.set('priority', '3')
    violation.set('rule', item['title'])
    violation.text = "{0}: {1} ({2})".format(item['title'], item['name'], item['description'])

    child.append(violation)
    root.append(child)

print etree.tostring(root, pretty_print=True, encoding="UTF-8", xml_declaration=True)