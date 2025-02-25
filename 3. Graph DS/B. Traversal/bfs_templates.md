'''
Traverse Graph by Level by level
Queue used - FIFO

'''

# psudo code
'''
function_bfs(mission, visisted)
  queue <- Queue()
  queue.push(mission)
  visited.add(mission)
  # we have a mission in a quue which is not complete yet
  while not queue.empty():
    # mission to compltete next
    mission = queue.pop()
    complete_mission(mission)
    for each unlocked mission:
      if unlocked not in visited:
        queue.push(unlocked)
        visited.add(unlocked)
'''

'''
function_bfs(graph, vertex, visited)
   queue = Queue()
   queue.push(vertex)
   visited.add(vertex)
   while not queue.empty()
        vertex = queue.pop()
        print(vertex)
        for each neighbor in graph[vertex]:
            if neighbor not in visited:
               queue.push(neighbor)
               visted.add(neighbor)

'''
