import threading
import time


def first_func(age):
    print('I am a first child.', age)
    # time.delay()
    return

def second_func(age):
    print('I am a second child.')

    return

if __name__ == '__main__' :
    # threading.Tread()


    first = threading.Thread(target=first_func, args=(5,)) 
    #쓰레드에서 메소드를 받을 때는 타겟으로 파라미터는 아규로 받으면 된다.
    second = threading.Thread(target=second_func, args=(3,))

    first.start()
    second.start()

    first.join()
    second.join()

    while True:
        print('I am a parent.')
        
  