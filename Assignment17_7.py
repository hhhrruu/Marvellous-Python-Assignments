import os
import schedule
import time

def backup():
    logfile = time.ctime()
    logfile = logfile.replace(" ","_")
    logfile = logfile.replace(":","_")
    fobj = open(logfile,"w")
    bobj = open("marvellous.txt","r")
    data = bobj.read()
    fobj.write(data+"\n")
    fobj.close()
    bobj.close()

    if not os.path.exists("Backup.txt"):
        fobj = open("Backup.txt","w")
        fobj.write(logfile+"\n")
        fobj.close()
    else:
        fobj = open("backup.txt","a")
        fobj.write(logfile+"\n")
 


def main():
    
    
    schedule.every(1).hour.do(backup)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()