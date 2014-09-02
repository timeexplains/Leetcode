__author__ = 'butterfly'


# Definition for a point
class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution:
    def isLine(self,x1,y1,x2,y2,x3,y3):
        return (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1)
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, listP):
        #print("orgin list length is:%d"%len(listP))
        p= set()
        for item in listP:
            find = None
            for it in p:
                if it.x == item.x and it.y == item.y:
                    find = it
                    break
               # p.add(item)
                #item.cnt = 1
            if find == None:
                item.cnt = 1
                p.add(item)
            else:
                find.cnt = find.cnt + 1
            #else:
                #item.cnt = item.cnt + 1
        #print("remove duplicated point,length is:%d"%len(p))
        #points = list(p)
        length = len(p)
        max = 2
        while length >=2:
            point1 = p.pop()
            point2 = p.pop()
            length =  length - 1
            length = length - 1

            set1 = set()
            set1.add(point1)
            set1.add(point2)
            result = point1.cnt + point2.cnt

            for item in p:
               if self.isLine(point1.x,point1.y,point2.x,point2.y,item.x,item.y):
                   set1.add(item)
                   result = item.cnt + result
            if result > max:
                max = result









        #pointDict = {}
        #length = len(points)
        #for i in range(length):
         #   for j in range(i+1,length):
          #      pointDict[i*length+j] = False
           #     pointDict[j*length+i] = False
        #max = 2
        #for i in range(length):
         #   for j in range(i+1,length):
#                if pointDict[i*length +j] == True:
 #                   continue
          #      result = points[i].cnt + points[j].cnt
                #s = set()
                #s.add((i,points[i].x,points[i].y))
                #s.add((j,points[j].x,points[j].y))
           #     for k in range(j+1,length):
            #        if self.isLine(points[i].x,points[i].y,points[j].x,points[j].y,points[k].x,points[k].y):
             #           result = result + points[k].cnt
  #                      pointDict[i*length+k] = True
   #                     pointDict[j*length+k] = True
    #                    pointDict[i+k*length] = True
     #                   pointDict[j+k*length] = True


                 #       s.add((k,points[k].x,points[k].y))

               # print("i is:%d,j is:%d:,result is:%d,set is:%s"%(i,j,result,s))
              #  if result > max:
               #           max = result
            #    pointDict[i*length+j] = True
             #   pointDict[j*length+i] = True
        return max
    def build(self,list):
        #for set in sets:
        #print(len(list))
        #print(list,"*","\n\n")
        points = []
        for tupleItem in list:
            #item = tuple(tupleItem)
            x = tupleItem[0]
            y = tupleItem[1]
            point = Point(x,y)
            points.append(point)
        return points

#print(list(range(1,10)))
#for i in range(11,10):
 #   print(i)


#print(Solution().maxPoints([(0,0),(0,0)]))

#print(Solution().maxPoints(Solution().build([(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)])))