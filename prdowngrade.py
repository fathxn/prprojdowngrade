import os
import gzip
import shutil
import xml.etree.ElementTree as ET

print("""
 ┌─┐┬─┐┌─┐┬─┐┌─┐ ┬            
 ├─┘├┬┘├─┘├┬┘│ │ │            
o┴  ┴└─┴  ┴└─└─┘└┘            
╔╦╗┌─┐┬ ┬┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
 ║║│ ││││││││ ┬├┬┘├─┤ ││├┤ ├┬┘
═╩╝└─┘└┴┘┘└┘└─┘┴└─┴ ┴─┴┘└─┘┴└─
───────────────── by fathan0x1
""")

path_in = input("Enter file full path: ")

# extract prproj
def extractProj():
    with gzip.GzipFile(path_in, 'rb') as prproj:
        proj_r = prproj.read()
        with open(path_in.replace('.prproj',''), 'wb') as extproj:
            extproj.write(proj_r)
    return path_in.replace('.prproj','')

# edit prproj
def editProj():
    tree = ET.parse(str(extractProj()))
    root = tree.getroot()
    for project in root.findall('Project'):
        project.set('Version', '1')
    tree.write(extractProj())
    return path_in.replace('.prproj','')

# main
def main():
    with open(editProj(),'rb') as f_input:
        with gzip.open(editProj()+"_Downgrade.prproj",'wb') as f_output:
            shutil.copyfileobj(f_input,f_output)
    os.remove(editProj())

if __name__ == "__main__":
    main()
    print("Done!")
