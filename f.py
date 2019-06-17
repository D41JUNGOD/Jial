from parse import *
import threading

def main():
    t2 = threading.Thread(target=parse_down_2)
    t3 = threading.Thread(target=parse_down_3)
    t4 = threading.Thread(target=parse_down_4)
    t5 = threading.Thread(target=parse_down_5)
    
    t2.start()
    t3.start()
    t4.start()
    t5.start()

if __name__ == '__main__':
    main()

