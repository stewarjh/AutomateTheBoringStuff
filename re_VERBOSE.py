re.compiler(r'''
\d\d\d      #area code
-
\d\d\d      #first 3 digits
-
\d\d\d\d    # last 4 digits
/sx\d{2,4}  # extension''', re.VERBOSE)
