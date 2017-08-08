import os

base_path = os.path.dirname(os.path.abspath(__file__))

def place_xml(path, app_path):
    xml_path = base_path + "/templates.d/starttemp.xml"
    new_file = open(path, 'w')
    with open(xml_path) as f:
        for line in f:
            if "**script**" in line:
                # confirm how to get dynamic path for the application main file
                new_file.write("\t\t<string>" + app_path +"/zeromac.app</string>\n")
            else:
                new_file.write(line)
    new_file.close()
    print ("done")
