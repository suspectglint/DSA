class CountSquares:
    #Approach - 1 : Build Square step-by-step by forming each side.
    #Data Structures :
    #Here we are using 3 data structures : xset, yset and pointcount.
    #1.xset - a dictionary where for a given x key, we store all the y values.
    #Every (x,yi) in xset is a point passed in add() function.
    #2.yset - a dictionary where for a given y key, we store all the x values.
    #Every (xi,y) in yset is a point passed in add() function.
    #3.pointcount - a dictionary where for a given (x,y) it stores the
    #count of this point occurences as repetitions are treated differently in this problem.
    #Algorithm :
    #For every point in add, we update xset, yset and pointcount.
    #For every point in count, we first search a potential (x,y1) where y1!=y and 
    #calculate d1=mod(y1-y).
    #Then for (x,y1) we find a potential (x2,y1) and calculate d2 = mod(x2-x)
    #and we proceed only if d1==d2. 
    #Once we have (x2,y1) we need to check if 4th corner (x2,y) is present by checking
    #pointcount[(x2,y)]>0 and then add to result.
    #result+=pointcount[(x,y1)]*pointcount[(x2,y1)]*pointcount[(x2,y)] 
    """
    def __init__(self):
        self.pointcount = defaultdict(int)
        self.xset = defaultdict(set)
        self.yset = defaultdict(set)
        
    def add(self, point: List[int]) -> None:
        x,y = point
        self.pointcount[(x,y)]+=1
        self.xset[x].add(y)
        self.yset[y].add(x)
        #print(self.pointcount,self.xset,self.yset)

    def count(self, point: List[int]) -> int:
        result=0
        x,y = point
        for y1 in self.xset[x]:
            if y1!=y:
                d1 = y1-y
                d1 = -d1 if d1<0 else d1
                #print("d1 = ",d1)
                for x2 in self.yset[y1]:
                    d2 = x2-x
                    d2 = -d2 if d2<0 else d2
                    #print("d2 = ",d2)
                    #print(x,x2,y,y1)
                    if d1==d2:
                        if self.pointcount[(x2,y)]>0:
                            result+=(self.pointcount[(x,y1)]*self.pointcount[(x2,y1)]*self.pointcount[(x2,y)])
        return result
    """
    #Approach - 2 - Build square by picking potential diagonals in pointlist
    #and check if every other corner is present in points or not.
    #In this approach, we use only one datastructure pointcount same as approach 1
    #and exclude xset,yset.
    #And then for every point we check if it is a potential diagonal, by checking
    #say (px,py) is potential diagonal, then abs(px-x)==abs(py-y) and px!=x.
    #And add the contents to the result.
    #IImportant point : when we access a key that is not present in defaultdict, it is
    #automatically added, so if you want to avoid that, always fetch keys using
    #dict.get(key,defaultvalue)
    def __init__(self):
        self.pointcount = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x,y = point
        self.pointcount[(x,y)]+=1
        
    def count(self, point: List[int]) -> int:
        result=0
        x,y = point
        for px,py in self.pointcount:
            if abs(px-x)==abs(py-y) and px!=x:
                result+=(self.pointcount.get((px,py),0)*self.pointcount.get((px,y),0)*self.pointcount.get((x,py),0))
        return result


