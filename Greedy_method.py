# Define the 2D graph
graph = [
    [1, 2, 2, 3],
    [3, 1, 4, 2],
    [1, 5, 3, 3]]
i = j = 0
sum = graph[i][j]
n = len(graph)
m = len(graph[0])
while i < n -1 or j < m - 1:
    if i==n-1:
        j+=1
    elif j==m-1:
        i+=1
    elif graph[i][j+1] < graph[i+1][j]:
        j+=1
    else:
        i+=1
    sum+=graph[i][j]
print(sum)


