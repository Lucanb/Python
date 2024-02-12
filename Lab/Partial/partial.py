import os
import sys


def main(directory_path):

    senders=[]
    recivers=[]
    try:
        file_created = os.fdopen('summary.data') # sau cu makefile creez un nou fisier
    except IOError as err:
        print(f"file can't be created, {err}")  

    try:
        if not os.path.isdir(directory_path):
            raise ValueError("Wrong path to directory!")
        else:
            k=0
            for dir_path,tst,fileNames in os.walk(directory_path):
                try:
                   for file in fileNames:
                    extension = os.path.splitext(file)
                    if extension[1] == ".mail":  
                        with open(file,"r") as f: 
                              data = f.read() #citesc restul
                              sw = 0
                              message =""    #aici parsez
                              for i in data :
                                  if sw == 0:
                                   senders[k].append(i)
                                  if sw == 1:
                                   recivers[k].append(i)      
                                  if i == '\n':
                                      sw +=1  
                                  if sw == 2:
                                      message+= i
                                  if sw == 1 and i == '\n':
                                      k+=1
                              with open(file_created,"w") as f:
                                    #f.write() #scriu mesajul parasat  
                            dict1={}
                           #redescid fisierul si dupa in dict 1 vad senderiii si in dict 2 masor cate cuv de acel fel sunt
                            dict2 ={}

                            
                except IOError as error:
                    print(f"Reading error {error}")  
    except ValueError as valueError:
        print(f"Value Error , {valueError}")   
    return
    


if __name__ == '__main__':

     
    if len(sys.argv) !=2 :
        print("Wrong number of arguments")
    else:
        p0 = sys.argv[1] #p0 is the directoy
        main(p0)





