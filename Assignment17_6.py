import schedule
import datetime
import time


def writex():
    print("lunch time")    

def writexx():
    print("wrap up")    

def main():
    schedule.every().day.at("13:00").do(writex)
    schedule.every().day.at("18:00").do(writexx)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()