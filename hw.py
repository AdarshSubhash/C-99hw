import os
import shutil
import time
#main function
def main():
    deletedfoldercount=0
    deletedfilescount=0
    path="/pathtodelete"
    day=30
    #convertingdaysintoseconds
    seconds=time.time()-(day*24*60*60)
    #checkingiffileispresentinthegivenpath
    if os.path.exists(path):
        for rootfolder,folders,files in os.walk(path):
            if seconds>=getfile(rootfolder):
                removefolder(rootfolder)
                deletedfoldercount+=1
                break
            else:
                for folder in folders:
                    folderpath=os.path.join(rootfolder,folder)
                    if seconds>=getfile(folderpath):
                        removefolder(folderpath)
                        deletedfoldercount+=1
                for file in files:
                    filepath=os.path.join(rootfolder,file)
                    if seconds>=getfile(filepath):
                        removefile(filepath)
                        deletedfilescount+=1
    else:
        print(f"{path}isnotfound")
        deletedfilescount+=1
    print(f"totalfolderdeleted:{deletedfoldercount}")
    print(f"totalfilesdeleted:{deletedfilescount}")
def removefolder(path):
    if not shutil.rmtree(path):
        print(f"{path}is removed successfully")
    else:
        print("Unable to delete"+path)
def removefile(path):
    if not os.remove(path):
        print(f"{path}is removed successfully")
    else:
        print("Unable to delete"+path)
def getfile(path):
    ctime=os.stat(path).st_ctime
    return ctime
main()                                                        


