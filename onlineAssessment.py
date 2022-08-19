from tkinter import *
import ast

#creating window
win=Tk()

#defining methods
class Search:
    def Linear(self):
        arr=elist.get()
        ispresent=False
        dic=ast.literal_eval(edict.get())
        try:
            item=int(eitem.get())
        except(ValueError):
            linlabel=Label(win,text="INVALID SEARCH ITEM")
            linlabel.grid(row=4,column=2)
            return
        if arr=="":
            if item in dic.keys():
                ispresent=True
                mylabel=Label(win,text=str(item)+" in the given Dictionary(Linear Search)-> "+str(ispresent)+"with value: "+str(dic[item]))
        else:
            arr=map(int,list(elist.get().split(",")))
            if arr is not None:
                
                for i in arr:
                    if i==item:
                        ispresent=True
                mylabel=Label(win,text=str(item)+" in the given array(Linear Search)-> "+str(ispresent))
        mylabel.grid(row=4,column=2)
    
    def Binary(self):
        
        def search(arr,x):
            low=0
            high=len(arr)-1
            mid =0
            while low<=high:
                mid=(low+high)//2
                if arr[mid]<x:
                    low=mid+1
                elif arr[mid]>x:
                    high=mid-1
                else:
                    return mid
            return -1
        
        
        
        arr=elist.get()
        dic=ast.literal_eval(edict.get())
        try:
            item=int(eitem.get())
        except(ValueError):
            binlabel=Label(win,text="INVALID SEARCH ITEM")
            binlabel.grid(row=4,column=2)

        if arr=="":
            list1=[]
            for i in dic.keys():
                list1.append(i)
            list1.sort()
            ans=search(list1,item)
            if ans==-1:
                binlabel=Label(win,text=str(item)+" was not Found in Given Dictionary!")
                binlabel.grid(row=4,column=2)
            else:
                binlabel=Label(win,text=str(item)+" was Found in Given Dictionary! \nIt's value:"+str(dic[item]))
                binlabel.grid(row=4,column=2)
            
        else:
            arr=list(map(int,arr.split(","))) 
            arr.sort()
            ans=search(arr,item)
            if ans!=-1:
                binlabel=Label(win,text=str(item)+" was found in the given List at "+str(ans+1))
            else:
                binlabel=Label(win,text=str(item)+" was Not found in the given list")
            binlabel.grid(row=4,column=2)
            
                           
class Sorting:

    def BubbleSort(self):
        
        def bub(arr): 
            n = len(arr)  
            for i in range(n): 
                for j in range(0, n-i-1):  
                    if arr[j] > arr[j+1]: 
                        arr[j], arr[j+1] = arr[j+1], arr[j]
        
        
        arr=elist.get()
        dic=ast.literal_eval( edict.get())
        if arr=="":
            list1=list(dic.keys())
            bub(list1)
            ansdict={}
            for i in list1:
                ansdict[i]=dic[i]
            bubLabel=Label(win,text="(Bubble sort)Sorted Dictionary (on keys) ->"+str(ansdict))
            bubLabel.grid(row=6,column=2)
        else:
            ans=list(map(int,arr.split(",")))
            bub(ans)
            bubLabel=Label(win,text="(Bubble sort)Sorted array->"+str(ans))
            bubLabel.grid(row=6,column=2)

    def InsertionSort(self):
        
        def insSort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i-1
                while j >= 0 and key < arr[j] :
                        arr[j + 1] = arr[j]
                        j -= 1
                arr[j + 1] = key
        
        
        arr=elist.get()
        dic=ast.literal_eval( edict.get())
        if arr=="":
            list1=list(dic.keys())
            insSort(list1)
            ansdict={}
            for i in list1:
                ansdict[i]=dic[i]
            bubLabel=Label(win,text="(Insertion sort)Sorted Dictionary (on keys) ->"+str(ansdict))
            bubLabel.grid(row=6,column=2)
        else:
            ans=list(map(int,arr.split(",")))
            insSort(ans)
            bubLabel=Label(win,text="(Inserion sort)Sorted array->"+str(ans))
            bubLabel.grid(row=6,column=2)

    def SelectionSort(self):
        
        def selSort(A):
            for i in range(len(A)):
                min_idx = i
                for j in range(i+1, len(A)):
                    if A[min_idx] > A[j]:
                        min_idx = j      
                A[i], A[min_idx] = A[min_idx], A[i]
        
        
        arr=elist.get()
        dic=ast.literal_eval( edict.get())
        if arr=="":
            list1=list(dic.keys())
            selSort(list1)
            ansdict={}
            for i in list1:
                ansdict[i]=dic[i]
            bubLabel=Label(win,text="(Selection Sort)Sorted Dictionary (on keys) ->"+str(ansdict))
            bubLabel.grid(row=6,column=2)
        else:
            ans=list(map(int,arr.split(",")))
            selSort(ans)
            bubLabel=Label(win,text="(Selection Sort)Sorted array->"+str(ans))
            bubLabel.grid(row=6,column=2)
        
    def MergeSort(self):
        
        def merSort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]
                merSort(L)
                merSort(R)
        
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
        
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
        
        
        
        arr=elist.get()
        dic=ast.literal_eval( edict.get())
        if arr=="":
            list1=list(dic.keys())
            merSort(list1)
            ansdict={}
            for i in list1:
                ansdict[i]=dic[i]
            bubLabel=Label(win,text="Merge Dictionary (on keys) ->"+str(ansdict))
            bubLabel.grid(row=6,column=2)
        else:
            ans=list(map(int,arr.split(",")))
            merSort(ans)
            bubLabel=Label(win,text="(merge sort)Sorted array->"+str(ans))
            bubLabel.grid(row=6,column=2)
    
    def QuickSort(self):
        
        def partition(array, low, high):
            pivot = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
            
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            return i + 1

        def qsort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                qsort(array, low, pi - 1)
                qsort(array, pi + 1, high)
        
        arr=elist.get()
        dic=ast.literal_eval( edict.get())
        if arr=="":
            list1=list(dic.keys())
            qsort(list1,0,len(list1)-1)
            ansdict={}
            for i in list1:
                ansdict[i]=dic[i]
            bubLabel=Label(win,text="(Quick sort)Sorted Dictionary (on keys) ->"+str(ansdict))
            bubLabel.grid(row=6,column=2)
        else:
            ans=list(map(int,arr.split(",")))
            qsort(ans,0,len(ans)-1)
            bubLabel=Label(win,text="(Quick sort)Sorted array->"+str(ans))
            bubLabel.grid(row=6,column=2)

#windows Start

objsearch=Search()
objsort=Sorting()


#creating
win.title("Searching And Sorting")
elist=Entry(win,borderwidth=5,width=100)
edict=Entry(win,borderwidth="5",width=100)
eitem=Entry(win,borderwidth="5",width=100)

elist.insert(0,"")
edict.insert(1,'{}')

llist=Label(win,text="List:")
ldict=Label(win,text="Dictionary:")
litem=Label(win,text="Item to be searched:")
linst=Label(win,text="(Please Enter you list in comma separated manner such as 1,2,3,4)")
empty=Label(win,text="  ")
empty1=Label(win,text="  ")
empty2=Label(win,text="  ")

lsearch=Button(win,text="Linear Search",padx=10,pady=10,command=objsearch.Linear,fg='white',bg='black')
bsearch=Button(win,text="Binary Search",padx=10,pady=10,command=objsearch.Binary,fg='white',bg='black')

bubsort=Button(win,text="Bubble Sort",padx=10,pady=10,command=objsort.BubbleSort,fg='yellow',bg='black')
inssort=Button(win,text="Insertion Sort",padx=10,pady=10,command=objsort.InsertionSort,fg='yellow',bg='black')
selsort=Button(win,text="Selection Sort",padx=10,pady=10,command=objsort.SelectionSort,fg='yellow',bg='black')
qsort=Button(win,text="Quick Sort",padx=10,pady=10,command=objsort.QuickSort,fg='yellow',bg='black')
msort=Button(win,text="Merge Sort",padx=10,pady=10,command=objsort.MergeSort,fg='yellow',bg='black')
#functions for buttons

#showing
linst.grid(row=0,column=2)
llist.grid(row=1,column=0)
elist.grid(row=1,column=2)

ldict.grid(row=2,column=0)
edict.grid(row=2,column=2)

litem.grid(row=3,column=0)
eitem.grid(row=3,column=2)

empty.grid(row=4,column=0)

lsearch.grid(row=5,column=1)
bsearch.grid(row=5,column=2,sticky="W")

empty1.grid(row=6,column=2)

bubsort.grid(row=8,column=0)
inssort.grid(row=8,column=1)
selsort.grid(row=8,column=2,sticky="W")
empty2.grid(row=9,column=0)
qsort.grid(row=10,column=0)
msort.grid(row=10,column=1)
win.mainloop()