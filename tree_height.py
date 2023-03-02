# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    place = [[] for _ in range(n)]
    root = None
    for i in range(n):
        if parents[i] == -1: 
            root = i
        else: 
            place[parents[i]].append(i)

    def max_height(p):
        height = 1
        if not place[p]: 
            return height
        else:
            for child in place[p]:
                height = max(height,max_height(child))
            return height + 1
    return max_height(root)


def main():
    text=input("F or I: ")
    if "I" in text:
        n=int(input())
        parents=list(map(int, input().split()))
    elif "F" in text:
        name=input()
        path='./test/'
        file = path+name
        if "a" not in name:
            try:
                with open(file) as f:
                    n=int(f.readline())
                    parents=list(map(int,f.readline().split()))
            except Exception as e:
                print("Kļūda", str(e))
                return
        else:
            print("Kļūda")
            return
    else:
        print("F or Ip: ")
        return
    print(compute_height(n,parents))


# sys.setrecursionlimit(10**7) 
# threading.stack_size(2**27)  
# threading.Thread(target=main).start()
main()
