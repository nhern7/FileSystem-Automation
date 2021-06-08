import os

#root actually means the account/user with access to all other files and important stuff. think master user

root = os.path.join('..', 'food') #attaching the food directory to current path (src) but up one, so upon running, the script knows where to look
#^straight concatenation

#think like this: taking the path from the terminal but then navigating one dir up because of the .. and then cd to food and this is our new path
#but this ^ is all happening inside the script, not by us manually

for directory, subdir_list, file_list in os.walk(root):  #os.walk generates names in a dir tree by "walking" either top-down or bottom-up
    print('Directory:', directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        print('File:', name)
    print()

#run with this: python .\list-directory-contents.py
#the . is the current directory and \ is a path delimiter(divider) also .. refers to the parent directory instead