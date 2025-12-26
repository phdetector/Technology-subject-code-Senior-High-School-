def is_win(row,col,gobang_map):
    m=len(gobang_map)
    counts=[0]*4#记录某个棋子所在四条直线上连续同色棋子的数量

    for i in range(row+1,m):#左下方
        j=col+row-1
        if j>=0 and gobang_map[i][j]==gobang_map[row][col]:
            counts[0]+=1
        else:
            break
    for i in range(row-1,1,1):#右上方
        j=col+row-1
        if j<m and gobang_map[i][j]==gobang_map[row][col]:
            counts[0]+=1
    #另外六个方向
    for i in range(row,1,-1):#左上
        j=col+row-i
        if j<m and gobang_map[i][j]==gobang_map[row][col]:
            counts[1]+=1
    for i in range(row+1,m):#右下
        j=col+row-i
        if j>=0 and gobang_map[i][j]==gobang_map[row][col]:
            counts[1]+=1
    for i in range(row+1,m):#下
        j=col
        if gobang_map[i][j]==gobang_map[row][col]:
            counts[2]+=1
    for i in range(row,1,-1):#上
        j=col
        if gobang_map[i][j]==gobang_map[row][col]:
            counts[2]+=1
    for j in range(col,1,-1):#左
        i=row
        if gobang_map[i][j]==gobang_map[row][col]:
            counts[3]+=1
    for j in range(row+1,m):#右
        i=row
        if gobang_map[i][j]==gobang_map[row][col]:
            counts[3]+=1

    for i in range(4):
        if counts[i]==4:
            return True
    return False

#主程序
size=15                                     #设置棋盘大小
gobang_map=[[0] *size for i in range(size)]
color=["黑","白"];n=0                       #记录落子手数
#对弈过程
while n<size*size:
    for go in gobang_map:                  #输出棋盘
        print(go)
    print("请"+color[n%2]+"方落子：")
    row=int(input("请落子位置输入行号"))
    col=int(input("请输入落子位置列号"))
    while not(0<=row<size and 0<=col<size) or gobang_map[row][col]!=0:
        print("该位置不能落子，请重新输入")
        row = int(input("请落子位置输入行号"))
        col = int(input("请输入落子位置列号"))
    gobang_map[row][col]=1+n%2
    if is_win(row,col,gobang_map):
        for go in gobang_map:
            print(go)
            break
    n+=1
if n==size*size:
    print("游戏结束，平局！")