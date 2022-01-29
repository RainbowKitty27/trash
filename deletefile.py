from logging import root
import os
import shutil
import time

def main():
    deletedFiles=0
    deletedFolder=0
    
    path="delete"
    days=30
    second=time.time()-(days*24*60*60)
    print(second)
    if os.path.exists(path):
        for rootfolder, folders, files in os.walk(path):
            if second>=getfileorfolderage(rootfolder):
                removefolder(rootfolder)
                deletedFolder+=1
                break
            else:
                folderPath=os.path.join(rootfolder,folders)
                if second>=getfileorfolderage(rootfolder):
                    removefolder(rootfolder)
                    deletedFolder+=1
        for file in files:
            filepath=os.path.join(rootfolder, file)     
            if second>=getfileorfolderage(filepath):
                removefolder(filepath)
                deletedFiles+=1
        else:
            if second>=getfileorfolderage(path):
                removefolder(path)
                deletedFolder+=1
    else:
        print(f'"{path}"in not found')
        deletedFiles+=1
    print(f"total files deleted: {deletedFiles}")
    print(f"total folders deleted: {deletedFolder}")
def removefolder(path):
    if not shutil.rmtree(path):
        print("File has been Removed")
    else:
        print("Unable to delete this file")
def getfileorfolderage(path):
    ctime=os.stat(path).st_ctime
    return ctime

main()