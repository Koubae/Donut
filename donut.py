import os
from math import sin, cos
import time 
import sys

def donut():
    a=0
    b=0

    height=24
    width=80
    #height=int(input("Enter Screen Height : "))
    #width=int(input("Enter Screen Width : "))
    
	# for clearing console (windows and unix systems)
    clear = "cls"
    if os.name == "posix":
        clear = "clear"
    CLEAR_TOKEN = "\033[H\033[J"

    os.system(clear)
    t = time.time()
    l_time = None
    cache = list()
    count = 1
    print("Creating Donut")
    while True:
        t2 = time.time()
        if not l_time:
            l_time = t2
        elif (t2-l_time) <= 1/60: 
            # os.system.clear()
            
            continue;
        else:
            l_time = t2

        z = [0 for _ in range(4*height*width)]
        screen = [' ' for _ in range(height*width)]

        j=0
        for _ in range(90):
            j+=0.07
            if j>=6.28: break;
            i=0

            for _ in range(315):
                i+=0.02
                if i >= 6.28: break;

                sinA=sin(a)
                cosA=cos(a)
                cosB=cos(b)
                sinB=sin(b)

                sini=sin(i)
                cosi=cos(i)
                cosj=cos(j)
                sinj=sin(j)

                cosj2=cosj+2
                mess=1/(sini*cosj2*sinA+sinj*cosA+5)
                t=sini*cosj2*cosA-sinj* sinA

                # 40 is the left screen shift
                x = int(40+30*mess*(cosi*cosj2*cosB-t*sinB))
                # 12 is the down screen shift
                y = int(11+15*mess*(cosi*cosj2*sinB +t*cosB))
                # all are casted to int, ie floored
                o = int(x+width*y)
				# multiplying by 8 to bring in range 0-11 as 8*(sqrt(2))=11
				# because we have 11 luminance characters
                N = int(8*((sinj*sinA-sini*cosj*cosA)*cosB-sini*cosj*sinA-sinj*cosA-cosi *cosj*sinB))
				# if x,y inside screen and previous z-buffer is < mess 
				# i.e. when z[o] is 0 or the prev point is behind the new point
				# so we change it to the point nearer to the eye/ above prev point 
                if 0<y<height and 0<x<width and z[o] < mess:
                    z[o]=mess
                    screen[o]=".,-~:;=!*#$@"[N if N>0 else 0]
                
                if len(screen) == width:
                    screen.append('\n')
        # s = ''.join(screen)
        # print(s)
        # return
        # os.system(clear)
        # print('\n'*50)
        # for index, char in enumerate(screen):
        #     if index % width == 0:
        #         print()
        #     else:
        #         print(char, end='')


        donut = ''
        for index, char in enumerate(screen):
            if index % width == 0:
                donut += '\n'
            else:
                donut += char

        s = ''.join(screen)
        # print(donut)
        # donut = ['\n' if index%width==0 else char for index, char in enumerate(screen)]
        # donut = ''.join(donut)
        # os.system(clear)
        # print("\033[H\033[J", end="")
        # sys.stdout.write(CLEAR_TOKEN)
        # print(donut)
        if not donut in cache:
            # cache |= set([donut])
            cache.append(donut)
            count += 1 
        else: 
            print("donut in cace", count)
            with open(f'donut.txt', 'w') as f:
                for d in cache:
                    f.write(d)
                    f.write('\n\n\n\n')
            return 
        # print(len(cache))
        # donut_sign = CLEAR_TOKEN+donut
        if count == 500:
            import json 
            print("Writing donut")
            d = json.dumps(cache, indent=4)
            with open(f'donut.txt', 'w') as f:
                f.write(d)
            break 
        # sys.stdout.write(donut_sign)



        # return
        # incrementsch
        # a+=0.04
        # b+=0.02
        a+=0.05
        b+=0.025
    while True:
        for d in cache:
            donut_sign = CLEAR_TOKEN+d
            sys.stdout.write(donut_sign)
            time.sleep(1/60)

def donut2():
    with open('donut.txt', 'r') as f:
        donut_data = f.read()
    CLEAR_TOKEN = "\033[H\033[J"
    # clear_token credit https://stackoverflow.com/a/50560686/13903942
    donut = eval(donut_data)
    # print(donut)
    # donut_json = json.loads(donut_data)
    # print(donut_data)
    while True:
        for d in donut:
            donut_sign = CLEAR_TOKEN+d
            sys.stdout.write(donut_sign)
            time.sleep(1/60)

def donut_colorama():

    from colorama import init
    from colorama import Fore, Back, Style

    init()
    RED_TOKEN = '\033[31m'

    with open('donut.txt', 'r') as f:
        donut_data = f.read()
    CLEAR_TOKEN = "\033[H\033[J"
    # clear_token credit https://stackoverflow.com/a/50560686/13903942
    donut = eval(donut_data)
    # print(donut)
    # donut_json = json.loads(donut_data)
    # print(donut_data)
    # while True: RED 
    #     for d in donut:
    #         donut_sign = CLEAR_TOKEN+d
    #         sys.stdout.write(RED_TOKEN + donut_sign)
    #         time.sleep(1/60)
    
    print(Fore.WHITE + 'some red text')
    print(Back.BLACK + 'and with a green background')
    while True: 
        for d in donut:
            donut_sign = CLEAR_TOKEN+d
            sys.stdout.write(donut_sign)
            time.sleep(1/60)
    # print(Style.RESET_ALL)

if __name__ == "__main__":
    # donut()
    # donut2()
    donut_colorama()