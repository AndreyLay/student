
import sys, os

name = "Dir"

def Mk_dir():

    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), '{}-{}'.format(name, i))
        #print(os.getcwd())
        os.mkdir(new_path)

def Del_dir():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), '{}-{}'.format(name, i))
        os.rmdir(new_path)

#Mk_dir()
#Del_dir()