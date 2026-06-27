#Import OS Library
import os

print ("Process abort after printing this line")

#Abort the current running process
os.abort()

print ("Process abort before printing this line")