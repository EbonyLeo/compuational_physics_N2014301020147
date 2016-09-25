Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x='1'
d={'1':'  '*1 ,'2':'    '*2,'3':'      '*3,'4':'        '*4,'5':'          '*4,'6':'            '*4,'7':'              '*4,'8':'                '*4}
import sys
import time
times=input('Please input the times you want the name to move horiziontally')
for y in range(times):
  for x in ['1','2','3','4','5','6','7','8']:
    print d[x],'#         ######    ###### '
    print d[x],'#         #        #      #'
    print d[x],'#         ######   #      #' 
    print d[x],'#         #        #      #'
    print d[x],'########  ######    ###### '       '    
    print('\n')  
    time.sleep(0.3)    
  sys.stderr.write("\x1b[2J\x1b[H")
  
SyntaxError: multiple statements found while compiling a single statement
>>> 
