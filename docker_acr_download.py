import os
import threading
import time
import sys
import threading
import logging
import random
import string

#Enter docker credentials to test

screds = "username:password"
image_url = "testacrdev.azurecr.io/data-platform-python-loadtest:latest"

exitFlag = 0
exitcode = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      pull_docker_image(self.name)
      print ("Exiting " + self.name)


def pull_docker_image(threadName):
    
    
    # string of length 8
    random_string = get_random_string(8)


    cmd = str ('/usr/bin/skopeo --insecure-policy copy ' + \
          '--screds=%s' % screds + \
          ' docker://%s' % image_url + \
          ' dir:/home/azureuser/skopeo/test_image_%s_%s' % (threadName,random_string))

     
    #cmd = "/usr/local/bin/skopeo --insecure-policy copy --screds=username:password  docker://testacrdev.azurecr.io/data-platform-python-loadtest:latest dir:~/Downloads/skopeo/test1"
 

    run_cmd(cmd)
    if exitcode == 0:
        logging.info('Pulled docker image, stdout')
    else:
        msg = "Failed to pull docker image from registry."
        logging.warn(msg)
        raise ImageAccessException(msg)

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return(result_str)



def run_cmd(cmd):
    print("attempting to run ", cmd)
    before = time.time()
    try:
        os.system(cmd)
    except Exception as e:
        print("Command failed to execute")




# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 4)
thread5 = myThread(5, "Thread-5", 5)
thread6 = myThread(6, "Thread-6", 6)
thread7 = myThread(7, "Thread-7", 7)
thread8 = myThread(8, "Thread-8", 8)
thread9 = myThread(9, "Thread-8", 9)
thread10 = myThread(10, "Thread-10", 10)
thread11 = myThread(11, "Thread-11", 11)
thread12 = myThread(12, "Thread-12", 12)
thread11 = myThread(11, "Thread-11", 11)
thread12 = myThread(12, "Thread-12", 12)
thread13 = myThread(13, "Thread-13", 13)
thread14 = myThread(14, "Thread-14", 14)
thread15 = myThread(15, "Thread-15", 15)
thread16 = myThread(16, "Thread-16", 16)
thread17 = myThread(17, "Thread-17", 17)
thread18 = myThread(18, "Thread-18", 18)
thread19 = myThread(19, "Thread-19", 19)
thread20 = myThread(18, "Thread-20", 18)
thread21 = myThread(11, "Thread-21", 11)
thread22 = myThread(12, "Thread-12", 12)
thread23 = myThread(13, "Thread-23", 13)
thread24 = myThread(14, "Thread-24", 14)
thread25 = myThread(15, "Thread-25", 15)
thread26 = myThread(16, "Thread-26", 16)
thread27 = myThread(17, "Thread-27", 17)
thread28 = myThread(18, "Thread-28", 18)
thread29 = myThread(19, "Thread-29", 19)
thread30 = myThread(18, "Thread-30", 18)


# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()
thread17.start()
thread18.start()
thread19.start()
thread20.start()
thread21.start()
thread22.start()
thread23.start()
thread24.start()
thread25.start()
thread26.start()
thread27.start()
thread28.start()
thread29.start()
thread30.start()

print ("Exiting Main Thread")

