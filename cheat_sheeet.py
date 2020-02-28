# \d            = number
# |             = is looking for or EX. (r'0|1|2|3|4) 
# ?             = 0 or 1 times can be used for phone numbers re.compile(r('\d\d\d-\d\d\d-\d\d\d\d')) or re.compile((r'(d\d\d-)?\d\d\d-d\d\d\d)) to help distginush two different fornot (\d\d\d-)? states it can have or not
# *             = match zero or more 
# +             = match one or more
# {}            = match number of times {3} (inserted) in a row# {x, y} = (x = min) (y = min)
# {}?           = do a non greedy match
# greedy match  = trys to get the longest possible string
# .search       = finds first match
# .findall      = finds all the matches
# ^             = negative EX (r'[^aeioou]')
# ^             = has to be at the begging of the string EX  (r'^Hello')
# $             = has to be at the end of the string EX (r'world'$')
# ^$            = contain all EX (r'^apple$'
# .             = can have any character EX (r'.at')
# .*            = any pattern EX nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') 


#WORKING WITH FILES

#MUST IMPORT OS
# os.chdir      = change working directory
# os.getcwd()   = gets your current working directory
# os.joinpath() = joins multiple folders, files together in one string to work across multiple platforms
# os.unlink()   = will allow to delete a single file
# os.rmdir()    = allows you to delete a whole folder cant have any files or folders in it
# os.walk       = lets you pull list of folder, sub folders, nad files)


#MANIPULATING FILE AND FOLDERS
# open(filename)                        = allows you to open the file if commanded and read 
                                        # nameGiven = (Filename)    
# nameGiven.read()                      = allows you to read the file as a single string 
# nameGiven.close()                     = no longer able to run commands for file closed
# nameGiven.readlines()                 = returns all lines as strings in a list
# nameGiven.flush()                     = if files arent showing changes this will force the change to occur

#To be able to write in a file must 1st 
# nameGiven = open('filepath', 'w')         = overwrite content in file (if file does not exist will create the file)
# nameGiven.write('Insert Text')            = command that allows you to actually write in file
# nameGiven = open('filepath', 'a')         = adds content to end of file
# nameGiven = open('filepath', 'a+')        = adds content to end of file and allows to read but from the last postion  its at to move position use nameGiven.seek(len)

# Must import shutil
# shutil.copy('filename, path')                 = copies a file to a new location
# shutil.copy('filename', 'path\\name.format')  = copies a file to a new location and renames it
# shutil.copytree('folder', 'foldername')       = copies afolder and allows to rename
# shutil.move('filename', 'path')               = moves a file to a new location (to rename move it to same file and add name & format to path)
# shutil.rmtree('path')                         = deletes a folder no matter whats in it

# USEFUL MODULES
# import os         = neede to use os.<> commands
# import shelve     = store a dictonary on computer
# import shutil     = allows to move and rename folder and files

