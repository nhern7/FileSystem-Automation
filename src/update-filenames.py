import os
import datetime

root = os.path.join("..","food") 

for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        source_name = os.path.join(directory, name) #meaning the "source" path for the current iteration is whatever file it finds in the current directory its in
        #so all the files in all the directories. like navigate to fruits - every file then vegetables - every file

        timestamp = os.path.getmtime(source_name) #returns an unreadable timestamp, so have to convert to a standard datetime string
        modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':', '.')

        target_name = os.path.join(directory, f'{modified_date}_{name}') #last part is the new file name
        #f is formating stuff

        print(f'Renaming: {source_name} to: {target_name}')

        os.rename(source_name, target_name)
#after using this script, do python list-directory-contents.py > food-directory-last-modified.txt 
#which writes the directory tree with these newly updated names to a new text file
# > is how you write a script to a different file, notice list-directory only uses prints. we're writing those prints to the txt file
