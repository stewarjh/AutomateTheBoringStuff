import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumberRegex.findall(message))

# .findall = pulls all of the patter out
# .search = pulls out the first pattern found 
# re.compile() = will create a regular expression obect EX. re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
