import os

base_path = os.path.dirname(os.path.abspath(__file__))

def place_xml(path):
    xml_path = base_path + "/templates.d/starttemp.xml"
    new_file = open(path, 'w')
    with open(xml_path) as f:
        for line in f:
            if "**title**" in line:
                new_file.write("\t\tThis is test\n")
            elif "**script**" in line:
                new_file.write("\t\t\t" + path +"/zeromac\n")
            else:
                new_file.write(line)
    new_file.close()
    print ("done")
