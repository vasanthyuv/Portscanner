#!/bin/python3



#portscanner

import sys
import socket
from datetime import datetime

#define our target


if len(sys.argv)==2: #argv is a argument (python3 sanner.py is first argument and second argument is our ip) ==> python3 scanner.py 127.0.0.1
    target=socket.gethostbyname(sys.argv[1]) #it will get ipv4  or if it got hostname then it will convert to ipv4
    
    #Add a banner

    print("-" * 50)
    print("Scanning target:"+target)
    print("Time started:"+str(datetime.now()))
    print("-" * 50)

    
    try:
            for port in range(435,450):#change the port number according to your need
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                if result == 0:#if the connection is successful it results true
                    print(f"Port {port} is open")
                    s.close()    
    
    except KeyboardInterrupt: #if some one type ctrl+C  so we nee do display by providing information that the program exiting
        print("\n Exiting Program.")
        sys.exit()
    
    except socket.gaierror:
        print("Hostname could not be solved")
        sys.exit()
    
    except socket.error:
        print("Could not connect to the server")
        sys.exit()            
        
              

else:
    print("Invalid amount of arguments")
    print("Syntax:python3 scanner.py <ip>")
    
