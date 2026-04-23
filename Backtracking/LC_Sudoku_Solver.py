import sys

class Solution:
    def isValid(self):
        rowcnt=[0 for _ in range(9)]
        colcnt=[0 for _ in range(9)]
        grdcnt=[0 for _ in range(9)]
        rowset=[set() for _ in range(9)]
        colset=[set() for _ in range(9)]
        grdset=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                g=int(i/3)*3+int(j/3)
                if self.board[i][j]!='.':
                    rowcnt[i]+=1
                    colcnt[j]+=1
                    grdcnt[g]+=1
                    rowset[i].add(self.board[i][j])
                    colset[j].add(self.board[i][j])
                    grdset[g].add(self.board[i][j])
        for i in range(9):
            if len(rowset[i])!=rowcnt[i] or len(colset[i])!=colcnt[i] or len(grdset[i])!=grdcnt[i]:
                return False
        return True

    def sudokusolver(self,board,cell):
        if cell>self.mcell:
            self.mcell=cell
        if self.isValid() and self.flag:
            if cell==81:
                self.cnt+=1
                #print("Valid Solution = ",self.board)
                self.flag=False
                self.solution=copy.deepcopy(self.board)
                #print("Valid Solution 2 = ",self.solution)
                #print("IDS = ",id(self.solution),id(board),id(self.board))
                return self.board
                
            i=int(cell/9)
            j=cell-int(cell/9)*9
            g=int(i/3)*3+int(j/3)
            if self.board[i][j]=='.':
                self.eleset[cell]=(self.bseset-self.rowset[i])&(self.bseset-self.colset[j])&(self.bseset-self.grdset[g])
                for num in self.eleset[cell]:
                    self.rowset[i].add(num)
                    self.colset[j].add(num)
                    self.grdset[g].add(num)
                    self.board[i][j]=str(num)
                    self.sudokusolver(board,cell+1)
                    self.board[i][j]='.'
                    self.rowset[i].remove(num)
                    self.colset[j].remove(num)
                    self.grdset[g].remove(num)
            else:
                self.sudokusolver(board,cell+1)
        else:
            return

    def solveSudoku(self, board: List[List[str]]) -> None:
        #print("Initial ID=",id(board))
        self.bseset = set(['1','2','3','4','5','6','7','8','9'])
        self.rowset = [set() for i in range(9)]
        self.colset = [set() for i in range(9)]
        self.grdset = [set() for i in range(9)]
        self.eleset = [set() for i in range(81)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    g=int(i/3)*3+int(j/3)
                    #print(i,j,g)
                    e=9*i+j
                    self.rowset[i].add(board[i][j])
                    self.colset[j].add(board[i][j])
                    self.grdset[g].add(board[i][j])
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    g=int(i/3)*3+int(j/3)
                    e=9*i+j
                    self.eleset[e]=(self.bseset-self.rowset[i])&(self.bseset-self.colset[j])&(self.bseset-self.grdset[g])
        self.flag=True
        self.solution=[]
        self.board=board
        self.cnt=0
        self.mcell=-1
        self.sudokusolver(board,0)
        #print("Solution = ",self.cnt,self.solution)
        for i in range(9):
            for j in range(9):
                board[i][j]=self.solution[i][j]
        #print("IDS = ",id(self.solution),id(board),id(self.board))