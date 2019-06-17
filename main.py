from parse import *
import threading

def main():
    t1 = threading.Thread(target=parse_up)
    
    t1.start()

if __name__ == '__main__':
    main()

