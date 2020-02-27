# \d = number
# | = is looking for or EX. (r'0|1|2|3|4) 
# ? = 0 or 1 times can be used for phone numbers re.compile(r('\d\d\d-\d\d\d-\d\d\d\d')) or re.compile((r'(d\d\d-)?\d\d\d-d\d\d\d)) to help distginush two different fornot (\d\d\d-)? states it can have or not
# * = match zero or more 
# + = match one or more
# {} = match number of times {3} (inserted) in a row# {x, y} = (x = min) (y = min)
# {}? = do a non greedy match
# greedy match = trys to get the longest possible string
# .search = finds first match
# .findall = finds all the matches
# ^ = negative EX (r'[^aeioou]')
# ^ = has to be at the begging of the string EX  (r'^Hello')
# $ = has to be at the end of the string EX (r'world'$')
# ^$ = contain all EX (r'^apple$'
# . = can have any character EX (r'.at')
# .* = any pattern EX nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') 

