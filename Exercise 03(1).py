l = 70                                   #调节距离  
t = 100                                  #调节时间  
for a in range(t):  
    v= int(a*l/t)                       #即a时刻的位移：x=a*v=a*l/t   
    s= v*" "
    print (s,"#         #########    ######## ")
    print (s,"#         #           #        #")
    print (s,"#         #           #        #")
    print (s,"#         #########   #        #")
    print (s,"#         #           #        #")
    print (s,"#         #           #        #")
    print (s,"########  #########    ######## ")
    import os  
    i = os.system('cls')  
    
