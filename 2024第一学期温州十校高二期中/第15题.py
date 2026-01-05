dic = {}


def dic_sum(lst):  # 统计球员总分
    score = [6, 4, 3, 2, 1]
    for i in range(1, len(lst)):
        for j in range(1, len(lst[i])):
            t = lst[i][j]
            if t not in dic:
                dic[t] = 0
            dic[t] += score[j - 1]
    return dic


def first_cnt(lst):  # 统计第一选票
    b = []
    lista=list(lst)
    for i in dic:
        s = 0
        for j in range(1, len(lst)):
            if i == lista [j][1]:
                s+= 1
        b.append([i, dic[i], s])
    return b  # b数组内一个元素结构


f = open('2024第一学期温州十校高二期中.txt', 'r',encoding='UTF-8')  # 以只读的方式打开文件
vote = []
line = f.readline()  # 从文件中读取一行
while line:  # 当line非空（从文件中读取到数据）
    line = line.strip().split()  # 将line转换为包含六个元素的列表
    vote.append(line)  # 此处append方法用于在列表vote末尾添加新对象line
    line = f.readline()
f.close()
dic = dic_sum(vote)
a = first_cnt(dic)
for i in range(3):  #根据评选规则生成前三名
    for j in range(i+1,len(a)):
        if a[j][1]>a[i][1] or a[i][1]==a[i][1] and a[j][2]>a[j][2]:
            a[j],a[i] = a[i],a[j]


#输出
for row in a[:4]:
    print(row)