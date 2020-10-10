import xml.etree.ElementTree as ET

def cube_cost(tree, level):
    if tree.attrib['color'] in colors.keys():
        colors[tree.attrib['color']] += level
    else:
        colors[tree.attrib['color']] = level
    if tree.getchildren():
        for child in tree.getchildren():
            cube_cost(child, level + 1)
    else:
        return

tree = input()

root = ET.fromstring(tree)
# print(root.getchildren())
# print(root.attrib['color'])
colors = {}
cube_cost(root, 1)
print(colors['red'], colors['green'], colors['blue'])



