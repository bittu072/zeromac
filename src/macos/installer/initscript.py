import os

base_path = os.path.dirname(os.path.abspath(__file__))

def place_xml(path):
    xml_path = base_path + "/templates.d/starttemp.xml"
    new_file = open(path, 'w')
    with open(xml_path) as f:
        for line in f:
            if "**title**" in line:
                # instead of trial make it more efficient and dynamic name
                new_file.write("\t<string>trial</string>\n")
            elif "**script**" in line:
                # confirm how to get static path
                new_file.write("\t\t<string>" + path +"/zeromac.app</string>\n")
            else:
                new_file.write(line)
    new_file.close()
    print ("done")
