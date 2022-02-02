
import xml.etree.ElementTree as ET
import os
import shutil
def delete(path):
    for file in os.listdir(path):
        if file.endswith(".xml"):
            index=0
            flag=0
            St1='Final Verdict:INCONC'
            st2='Final Verdict:FAIL'
            st3='Final Verdict:PASS'
            file_path = f"{path}\{file}"
           
            
            file1 = open(file_path, "r")
            for line in file1:
                index = index + 1
                if St1 in line or st2 in line:
                    flag = 1
                    break
                if st3 in line:
                    print("Found Verdict:PASS in line",index)
            file1.close()

            if flag==1:
                print('Found In Line', index)
                del_file=file_path.replace("/","\\")
                del_file=del_file.replace("\\"+file,"")
                if os.path.exists(del_file):
                    
                    temp=file
                    temp=temp.replace(".xml","")
                    tcfile=file_path
                    tcfile=tcfile.replace(temp+"\\"+file,"tc_log.xml")
                    tree=ET.parse(tcfile)
                    root=tree.getroot()
                    path_file=temp+"\\"+file
                    for i in root.findall("TCASE"):
                        if i.findtext("LOG")==path_file:
                            root.remove(i)
                    tree.write(tcfile)
                    
                    print(del_file+" deleting this directory")
                    shutil.rmtree(del_file)
                else:
                    print("File not found in the directory")
              
        else:
            current_path = "".join((path, "/", file))
            if os.path.isdir(current_path):
             delete(current_path)
delete(r"C:\Users\mukes\Downloads\SAMPLEWork")