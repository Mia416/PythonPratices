'''
Created on Jun 1, 2017

@author: chenz

\d
Matches any decimal digit; this is equivalent to the class [0-9].
\D
Matches any non-digit character; this is equivalent to the class [^0-9].
\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
\s
Matches Unicode whitespace characters
\S
Matches any character which is not a Unicode whitespace character. 

.
In the default mode, this matches any character except a newline
^
match start
$
match end

*
* matches zero or more times,

+
 which matches one or more times.
 
 ?
 matches either once or zero times;
 
 \1
 
 match the first () ,using the original content
 
 \
 
 zhuanyi char like \\1   \\

'''

import re

#replace ab using &&
test = 'abcdf5gasfjklsjfl;sda6'
resp = re.sub(r'a\w*\d','&&',test)
print (resp)
