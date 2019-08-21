#!/usr/bin/env python
#-*-coding:utf-8-*-

cost = [[0,6,2,1000,1000,1000,1000],
		[6,0,1000,1000,1,1000,1000],
		[2,1000,0,2,1000,11,1000],
		[1000,1000,2,0,4,6,1000],
		[1000,1,1000,4,0,1000,7],
		[1000,1000,11,6,1000,0,3],
		[1000,1000,1000,1000,7,3,0]]
def min_dist(s,dist):
	min_ = 1000
	index = None
	for i, d in enumerate(dist):
		if i not in s and d <min_ and d != 0:
			index = i
			min_ = d
	if min_ == 1000:
		return None
	return index

def search_ver(s,dist,u):
	ww = []
	for i, d in enumerate(cost[u]):
		if i not in s and d!=1000 and d!=0:
			ww.append(i)
	return ww
n = len(cost)
# 标记是否找到shortest path
s =[0]
# 原点到i的shortest path, 初始化
dist = cost[0]
path = [[0] for i in range(n)]
pos = [0 for i in range(n)]

for i in range(n-1):
	u = min_dist(s,dist)
	s.append(u)
	print(u,dist,path)
	path[u].append(u)
	ww = search_ver(s,dist,u)
	for w in ww:
			if dist[u]+cost[u][w]<dist[w]:
				dist[w] = dist[u]+cost[u][w]
				if w == 4:
					print(path,dist[u]+cost[u][w])
				path[w] = [x for x in path[u]]

print(dist)
print(path)
