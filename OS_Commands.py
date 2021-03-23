import os, sys

print ("something")

os.chdir("C:\\")

print(os.getcwd())

os.chdir("C:\\AWSDeployment")

print(os.getcwd())

path=os.getcwd()


newpath = path + "\\deployment"

print(newpath)

os.chdir(newpath)

print(os.getcwd())