import os
import schedule
import time

def checking():
    print("checking email")
 


def main():
    schedule.every(10).seconds.do(checking)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()