import cv2 
import numpy as np
class node:
    def __init__(self):
        self.prob=None
        self.pixel_val=None
        self.left=None
        self.right=None

def parent(i):
    i=(i-2)//2
    return i

def heapify(heap,size):
    i=size-1
    while(i>0):
        if(heap[parent(i)].prob>heap[i].prob):
            heap[parent(i)],heap[i]=heap[i],heap[parent(i)]
        i=parent(i)
def create(x,y):
    temp=node()
    temp.prob=x.prob+y.prob
    temp.left=x
    temp.right=y
    return temp

def build_tree(prob):
    heap=[]
    for i in range(256):
        temp=node()
        temp.pixel_val=i
        temp.prob=prob[i]
        heap.append(temp)
        heapify(heap,len(heap))
    while(len(heap)>1):
    #for i in range(1):
        x=heap.pop(0)
        heapify(heap,len(heap))
        y=heap.pop(0)
        heapify(heap,len(heap))
        temp=create(x,y)
        heap.append(temp)
        heapify(heap,len(heap))
    return heap[0]

def traverse(root,val,f_map,r_map):
    if(root.left==None and root.right==None):
        if(root.pixel_val not in f_map):
            f_map[root.pixel_val]=val
        if(val not in r_map):
            r_map[val]=root.pixel_val
        return
    traverse(root.left,val+"0",f_map,r_map)
    traverse(root.right,val+"1",f_map,r_map)



def abc():
    im=cv2.imread("phonebbok\puppy.jpg",0)
    hist=np.bincount(im.ravel(),minlength=256)           #calculates number of occurence of each pixel.
                                                         #Since each pixel will lie between (0-255) therfore
                                                         # we set the bin value to 256. 
    prob=hist/256
    root=build_tree(prob)
    f_map={}
    r_map={}
    traverse(root,"",f_map,r_map)
    c_size=0
    for i in range(256):
        x=len(f_map[i])
        c_size+=x
    #print(f_map)
    sh=np.shape(im)
    h,w=sh[0],sh[1]
    input_bits=h*w*8
    #print(c_size)
    #print(input_bits)
    compression=(1-c_size/input_bits)*100
    print(compression)
    #print(input_bits)
    #print(c_size/8)
    #print(compression)
abc()