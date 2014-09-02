__author__ = 'butterfly'

class Solution:
    def initMarked(self,m,n):
        marked = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(False)
            marked.append(row)
        return marked
    def search(self, x, y,row,col,obstacleGrid):
        self.marked[x][y] = True
        val = obstacleGrid[x][y]
        if x+1 < col and val == obstacleGrid[x+1][y]:
            self.search(x+1,y,row,col,obstacleGrid)
        if y+1 < row and val == obstacleGrid[x][y+1]:
            self.search(x,y+1,row,col,obstacleGrid)
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        self.marked = self.initMarked(100,100)
        row = len(obstacleGrid)
        element = obstacleGrid[0]
        col = len(element)
        cnt = 0
        for i in range(row):
            for j in range(col):
                if self.marked[i][j] == False:
                    self.search(i,j,row,col,obstacleGrid)
                    cnt = cnt + 1
        return cnt

