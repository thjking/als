# 图的表示
    ## 邻接列表及其类似结构
        ### 邻接列表
'''
a, b, c, d, e, f, g, h = range(8)
N = [
    [b, c, d, e, f], #a
    [c, e], #b
    [d], #c
    [e], #d
    [f], #e
    [c, g, h], #f
    [f, h], #g
    [f, g] #h
]
print (N)
'''

        ### 加权邻接字典
'''
a, b, c, d, e, f, g, h = range(8)
N = [
    {b:2, c:1, d:3, e:9, f:4}, #a
    {c:4, e:3}, #b
    {d:8}, #c
    {e:7}, #d
    {f:5}, #e
    {c:2, g:2, h:2}, #f
    {f:1, h:6}, #g
    {f:9, g:8} #h
]
print (N)
'''
    ##邻接矩阵
        ##嵌套list实现的邻接矩阵

'''
a, b, c, d, e, f, g, h = range(8)
N = [[0,1,1,1,1,1,0,0], #a
    [0,0,1,0,1,0,0,0], #b
    [0,0,0,1,0,0,0,0], #c
    [0,0,0,0,1,0,0,0], #d
    [0,0,0,0,0,1,0,0], #e
    [0,0,1,0,0,0,1,1], #f
    [0,0,0,0,0,1,0,1], #g
    [0,0,0,0,0,1,1,0]  #h
]
print (N)
'''

        ##带权值的邻接矩阵
'''
a, b, c, d, e, f, g, h = range(8)
inf = float('inf')
W = [[0, 2, 1, 3, 9, 4, inf, inf], #a
    [inf, 0, 4, inf, 3, inf, inf, inf], #b
    [inf, inf, 0, 8, inf, inf, inf, inf], #c
    [inf, inf, inf, 0, 7, inf, inf, inf], #d
    [inf, inf, inf, inf, 0, 5, inf, inf], #e
    [inf, inf, 2, inf, inf, 0, 2, 2], #f
    [inf, inf, inf, inf, inf, 1, 0, 6], #g
    [inf, inf, inf, inf, inf, 9, 8, 0]  #h
]
print (W)
'''
#树的表示
    #二维列表表示法（一般树）
'''
T = [['a','b'],['c'],['d',['e','f']]]
print (T[0][1])
'''
    #二叉树表示法
'''
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right
t = Tree(Tree('a','b'),Tree('c','d'))
print (t.left.left)
'''
    #多路搜索路，每个节点指向它的子节点和它的兄弟节点
'''
class Tree:
    def __init__(self,kids,next=None):
        self.kids = self.val = kids
        self.next = next
t = Tree(Tree('a',Tree('b',Tree('c',Tree('d')))))
print (t.kids.next.next.next.val)
'''