from glob import glob
import time
import threading
total=0
num_of_threads=30
stop=False
def PrintFirst(length):
    #Initial variable for the base case. 
    global total,num_of_threads,stop
    first =length
    n=1
    num=2
    b=True
    while True:
        num=2
        b=True
        while(num*num<=first and b):
            if(first % num==0):
                b=False
            num+=1
            if(stop):
                return 0
        
        if(b):
            n+=1
            total+=1
            #print(first)


        first+=num_of_threads


def main():
    
    global total,num_of_threads,stop
    thread_num=num_of_threads
    """
    for i in range(thread_num):
        x = threading.Thread(target=PrintFirst, args=(i,))  
        x.start()
    

    while(total<1000000):
        time.sleep(2)
        print(total)

    """
    for j in range(thread_num):
        num_of_threads=j+1
        stop=False
        total=0
        a=time.time()
        for i in range(num_of_threads):
            x = threading.Thread(target=PrintFirst, args=(i+1,))  
            x.start()
        
        while(total<100000):
            #print(total)
            time.sleep(0.1)
        b=time.time()
        stop=True
        time.sleep(5)
        print(str(j+1)+" threads took:" +str(b-a)+" secends")

    """
    #print("seconds =" +str(time.time()))
    a=time.time()
    PrintFibonacci(10000)
    b=time.time()
    #print("seconds =" +str(time.time()))
    print("time mesure (10000)="+str(b-a))

    a=time.time()
    PrintFibonacci(100000)
    b=time.time()
    print("time mesure (100000)="+str(b-a))


    a=time.time()
    PrintFibonacci(1000000)
    b=time.time()
    print("time mesure (1000000)="+str(b-a))
    """
    pass

if __name__ == "__main__":
    main()