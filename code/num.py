# import random
# import math


# # Num nums
# class Num:

#     n = 0
    
#     def __init__(self, the, _has):
#         self.t = the
#         self._has = _has
#         self.lo = -math.inf
#         self.hi = math.inf
#         self.isSorted = True

#     def nums(self):
#         if not self.isSorted:
#             self.t.sort(self._has)
#             self.isSorted = True

#         return self._has

#     # per
#     def per(self, t, p):
#         p = math.floor(((p or 0.5) * self.t) + 0.5)
#         return t[max(1, min(self.t, p))]

#     # Num Add
#     def add(self, v, pos):
#         if type(v) == int or type(v) == float:
#             self.n += 1
#             self.lo = min(v, self.lo)
#             self.hi = max(v, self.hi)

#             if self._has < self.t.nums:
#                 pos = 1 + self._has
#             elif random.random() < self.t.nums/self.n:
#                 pos = self._has - 1

#             if pos:
#                 self.isSorted = False
#                 self._has[pos] = int(v)
#         else:
#             print("Symbol encountered!!")

#     # Num Div
#     def div(self, a):
#         a = self.nums()
#         return (self.per(a, 0.9) - self.per(a, 0.1)) / 2.58

#     # Num Mid
#     def mid(self):
#         return self.per(self.nums(), 0.5)





import math
import random
import sys
sys.path.append("./code")
from functions import per,the


class Num:
    
    #'Num' summarizes the stream of numbers
    def __init__(self,c=0,s=str()):
        self.n=0
        self.at=c
        self.name=s
        self._has=(0) * [the['nums']]
        self.low=math.inf
        self.high=-math.inf
        self.isSorted=True
        if(len(s)>0 and s[-1]=='-'):
            self.w=-1
        else:
            self.w=1
    
    def __str__(self):
        return "{"+ f" n:{self.n}, at:{self.at+1}, name:{self.name}, low:{self.low}, high:{self.high}, isSorted:{self.isSorted}, w:{self.w}"+"}"

    #Return kept numbers, sorted.
    def nums(self):
        # if (not self.isSorted):
        # list(sorted(self._has))
        self._has.sort()
        return self._has
            
        

    #Reservoir sampler. Keep atmost 'the[nums]' numbers 
    # (if we run out of space delete something old at random and add new)
    def add(self,ele,pos=None):
        the['nums'] = 32
        if ele!='?':
            self.n=self.n+1
            self.low=min(self.low,int(ele))
            self.high=max(self.high,int(ele))
            if ( (len(self._has))<(the['nums']) ):
                pos=1+len(self._has)
            elif ( random.randint(0,len(self._has)) < (the['nums'])/self.n ):
                pos=random.randint(1,the['nums'])
            if pos!=None:
                self.isSorted=False
                self._has.insert(pos,int(ele))
        the['nums'] = 512



    #Diversity (standard deviation from Nums, entropy for Syms)
    def div(self):
        a=self.nums()
        return (per(a,0.9)-per(a,0.1))/2.58 
    
    #Central tendency (median for Nums, mode for Syms)
    def mid(self):
        return per(self.nums(),0.5) 

