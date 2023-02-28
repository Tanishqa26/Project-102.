import os
import shutil
from_dir = "C:/Users/Anushka/Documents/class c102/images"
to_dir = "C:/Users/Anushka/Documents/python/Document_files"
list_of_files= os.listdir(from_dir)
print(list_of_files)

for file_name  in list_of_files:

    name,extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension=='':
        continue

    if extension in ['.txt', '.doc', '.docx', '.pdf', '.jpg']:
         path1= from_dir +'/'+ file_name
         path2 = to_dir + '/' + "Document_Files"
         path3 = to_dir + '/' + "Document_Files" + file_name
         print("path1",path1)
         print("path3",path3)

         #Check if Folder/Directory exists
         #else make a new folder/directory before moving
         if os.path.exists(path2):
             print("Moving" + file_name + "......")

             #move from path1--->path3
             shutil.move(path1,path3)
         
    else:
        os.makedirs(path2)
        print("Moving"+file_name+ ".....")
        shutil.move(path1,path3)





         
         





    
 


