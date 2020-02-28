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


# import os 
# os.chdir                      = change working directory
# os.getcwd()                   = gets your current working directory
# os.joinpath()                 = joins multiple folders, files together in one string to work across multiple platforms 
# absoulte file path            = beign with route folder c:\\
# relative file path            = uses os.chdir or does not start with the root folder
# .                             = this folder
# ..                            = the paren folder move one up file path
# os.path.abspath('filename')   = will pull up files absolute path
# os.path.isabs('filepath')     = will tell if filepath is absolute
# os.path.exist                 = tells you if a path is TRue or False
# os.path.isfile                = tells you if file
# os.path.isdir                 = will tell you if its the directory
# os.path.getsize('filename')   = return size of file in bytes as a int()
# os.listdir('filepath')        = pull up files in folder as a list
# os.makedir()                  = can be used to make folders 



