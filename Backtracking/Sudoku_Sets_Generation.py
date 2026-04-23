class Sudoku:
    def __init__(self):
        self.board=[[1,2,3],[0,9,0],[4,0,0]]
        self.cnt=1
        print(self.board)

    def isvalid(self):
        t=set()
        zc=0
        for i in range(3):
            for j in range(3):
                if self.board[i][j]==0:
                    zc+=1
                else:
                    t.add(self.board[i][j])
        #print("Validity",self.board,zc,t)
        if len(t)+zc==9:
            return True
        else:
            return False

    def print_all_patterns(self,cell):
        #print(cell,self.board)
        if cell==0 or self.isvalid():
            #print("Hello")
            if cell==9:
                print("Valid Solution = ",self.cnt,self.board)
                self.cnt+=1
                return
            i=int(cell/3)
            j=cell-int(cell/3)*3
            if self.board[i][j]==0:
                for num in range(1,10):
                    self.board[i][j]=num
                    self.print_all_patterns(cell+1)
                    self.board[i][j]=0
            else:
                self.print_all_patterns(cell+1)
        else:
            return
        


s=Sudoku()
s.print_all_patterns(0)