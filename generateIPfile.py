import os 
import time 
"""Generator By @OfficialAhmed0"""
try:
    file = open("Generate Data.dat", "r")
    print("\n")
    try :
        temp = open("PS4 IP.txt", "r")
        temp.close()
        print("Overwriting the file...")
        time.sleep(5)
        generate = open("PS4 IP.txt", "w+")
        for copy in file:
            generate.write(copy)
        print("\n")
        print("Done... Don't forget to change the IP")
        print("auto turns off after 10 seconds")
        time.sleep(10)    
        generate.close()
    except:    
        print("Creating the file...")
        time.sleep(5)
        generate = open("PS4 IP.txt", "w+")
        for copy in file:
            generate.write(copy)
        print("\n")
        print("Done... Don't forget to change the IP")
        print("auto turns off after 10 seconds")
        time.sleep(10)    
        generate.close()      
except:
    print("[Generate Data.dat] is Missing")
    print("auto turns off after 10 seconds")
    time.sleep(10)

