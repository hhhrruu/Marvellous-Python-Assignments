import schedule
import datetime
import time


def writex():
    fobj = open("marvellous.txt","a+")
    fobj.write(time.ctime())
    fobj.close()


def main():
    schedule.every(10).minutes.do(writex)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()