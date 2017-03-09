
#RUN IN PYTHON2

# INPUT FORMAT FOR THE GRAPH
#ENTER THE NUMBER OF NODES :N
#ENTER THE NUMBER OF EDGES IN THE GRAPH :L
#THE L LINES CONTAIN SPACE SEPARATED PAIRS OF NODES THAT SIGNIFY AN EDGE IN THE GRAPH



def dfs(start,visited,graph):
	if(graph.has_key(start) == False):
		visited[start -1] =1
		print start 
	else:
		visited[start-1]=1
		print start
		l=graph[start]
		for i in l:
			if(visited[i-1] == 0):
				dfs(i,visited,graph)
				


def makeGraph():
	print "Enter the number of nodes in the graph, indexing of the node starts from 1"
	N=int(input())
	print "Enter the number of edges in the graph"
	L=int(input())
	graph={}
	visited=[]
	for i in range(N):
		visited.append(0)

	for i in range(L):
		print 'enter an edge of the graph'
		a,b=raw_input().strip().split(' ')
		a=int(a,10)
		b=int(b,10)

		if(graph.has_key(a)):
			graph[a].append(b)
		else:
			graph[a]=[b]

		if(graph.has_key(b)):
			graph[b].append(a)
		else:
			graph[b]=[a]
	return visited,graph


	

v,g=makeGraph()
print "Printing the traversal"
dfs(1,v,g)
