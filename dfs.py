
class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1]          #return last element

    def is_empty(self):
        return len(self.list) == 0     #return true if the stack is empty

goal_state= [0, 1, 2, 3, 4, 5, 6, 7, 8]
#goalTest = [[0,1,2],[3,4,5],[6,7,8]]


def __init__(self, depth,parent, move,cost, State):

     self.depth = depth

     self.parent = parent

     self.move = move

     self.cost=cost

     self.State = State

     self.id = ''.join(map(str, self.State))

     self.GoalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

     self.goalid = ''.join(map(str, self.GoalState))

     if parent is None:

         self.depth = 0

     else:

         self.depth = parent.depth + 1


def compare(self):
    if self.id == self.goalid:
        return True
    return False
#def getChildren(self):
 #   children = []
  #  children.append(self.moveUp())
   # children.append(self.moveRight())
    #children.append(self.moveDown())
    #children.append(self.moveLeft())
    #return list(filter(None, children))


def depth_first_search(graph, initial_state):
    frontier = Stack()
    frontier.push(initial_state)
    path = []
    explored = set()
    currentDepth=0
    while not frontier.is_empty():
        state = frontier.pop()
        if state in explored:
            continue
        #if state.state == goal_state:
         #   goal_node = state
         #   return frontier
        explored.add(state)
        if state.compare():
            state.getMoves()
            return  state
        for neighbor in state.getChildren():
            if neighbor not in frontier:
               frontier.push(neighbor)
               if neighbor.depth > currentDepth:
                   currentDepth = neighbor.depth

    return explored

def main():

    initial_state=[1, 2, 5, 3, 4, 0, 6, 7, 8]
    cost=0
    dfs_path = depth_first_search(initial_state, initial_state[1])
    print(dfs_path)


if __name__ == '__main__':
    main()


