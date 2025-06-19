import schedule
import time
import datetime

def Myschedule():
    print("JAY GANESH")

def main():
    print("inside automation script ")
    print("current time is ",datetime.datetime.now())
    schedule.every(2).seconds.do(Myschedule)
  
    print("Application is in waiting state")
    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()


 