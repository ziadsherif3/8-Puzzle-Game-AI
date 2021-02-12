import heapq
import math
import time

MANHATTAN = 1
EUCLIDEAN = 2

class Board():
    def __init__(self, confg, cost_type, parent, cost):
        self.confg = confg
        self.cost_type = cost_type
        self.parent = parent
        self.cost = cost
        self.total_cost = self.cal_total_cost(cost)
    
    def cal_total_cost(self, cost):
        
        if cost == None:
            return None
        
        else:
            heuristic_cost = 0
            
            if self.cost_type == MANHATTAN:
                for row_i in range(len(self.confg)):
                    for col_i in range(len(self.confg[row_i])):
                        for g_row_i in range(len(goal_state.confg)):
                            if self.confg[row_i][col_i] in goal_state.confg[g_row_i]:
                                heuristic_cost += (abs(row_i - g_row_i) + 
                                                   abs(col_i - goal_state.confg[g_row_i].index(self.confg[row_i][col_i])))
                                break
            
            else:
                for row_i in range(len(self.confg)):
                    for col_i in range(len(self.confg[row_i])):
                        for g_row_i in range(len(goal_state.confg)):
                            if self.confg[row_i][col_i] in goal_state.confg[g_row_i]:
                                heuristic_cost += math.sqrt(pow(row_i - g_row_i, 2) + 
                                                            pow(col_i - goal_state.confg[g_row_i].index(self.confg[row_i][col_i]), 2))
                                break
            
            return cost + heuristic_cost
    
    def get_neighbors(self):
        if self.cost_type == None:
            return None
        else:
            neighbors = []
            
            for row_i in range(len(self.confg)):
                if 0 in self.confg[row_i]:
                    r = row_i
                    c = self.confg[row_i].index(0)
                    break
            
            if (r - 1) >= 0: # Move upwards.
                new_neighbor = [[x, y, z] for x, y, z in self.confg]
                new_neighbor[r - 1][c], new_neighbor[r][c] = new_neighbor[r][c], new_neighbor[r - 1][c]
                neighbors.insert(len(neighbors), Board(new_neighbor, self.cost_type, self, self.cost + 1))
                
            if (r + 1) <= 2: # Move downwards.
                new_neighbor = [[x, y, z] for x, y, z in self.confg]
                new_neighbor[r + 1][c], new_neighbor[r][c] = new_neighbor[r][c], new_neighbor[r + 1][c]
                neighbors.insert(len(neighbors), Board(new_neighbor, self.cost_type, self, self.cost + 1))
                
            if (c - 1) >= 0: # Move to the left.
                new_neighbor = [[x, y, z] for x, y, z in self.confg]
                new_neighbor[r][c - 1], new_neighbor[r][c] = new_neighbor[r][c], new_neighbor[r][c - 1]
                neighbors.insert(len(neighbors), Board(new_neighbor, self.cost_type, self, self.cost + 1))
            
            if (c + 1) <= 2: # Move to the right.
                new_neighbor = [[x, y, z] for x, y, z in self.confg]
                new_neighbor[r][c + 1], new_neighbor[r][c] = new_neighbor[r][c], new_neighbor[r][c + 1]
                neighbors.insert(len(neighbors), Board(new_neighbor, self.cost_type, self, self.cost + 1))
                
            return neighbors
    
    def __lt__(self, other):
        return self.total_cost < other.total_cost
    
    def __eq__(self, other):
        return self.confg == other.confg
    
    def __str__(self):
        return f'{self.confg}\n'

goal_state = Board([[0, 1, 2], [3, 4, 5], [6, 7, 8]], None, None, None)

def decrease_key(heap, board):
    indx = heap.index(board)
    old_board = heap[indx]
    
    if board.total_cost < old_board.total_cost:
        heap[indx] = board
        heapq.heapify(heap)

def A_star_search(initial_state: Board):
    frontier = [initial_state]
    explored = []
    
    while len(frontier) != 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        
        if state == goal_state:
            return [True, state, explored]
        
        for neighbor in state.get_neighbors():
            if (neighbor not in frontier) and (neighbor not in explored):
                heapq.heappush(frontier, neighbor)
            elif neighbor in frontier:
                decrease_key(frontier, neighbor)
        
    return [False]

def search(board):
    print("Choose the heuristic function:\n1) Manhattan Distance\n2) Euclidean Distance\n")
    choice = input().split(" ")
    
    while (len(choice) != 1) or (not choice[0].isdigit()) or (int(choice[0]) < 1) or (int(choice[0]) > 2):
        print("Invalid input! Please retry.")
        choice = input().split(" ")
    
    if choice[0] == '1':
        initial_state_manh = Board(board, MANHATTAN, None, 0)
        
        manh_begin = time.time()
        manh_out = A_star_search(initial_state_manh)
        time.sleep(1)
        manh_end = time.time()
        
        manh_time = manh_end - manh_begin
        
        if not manh_out[0]:
            print("Failure, can't solve the puzzle.\n")
            return
        
        search_depth = 0
        
        for board in manh_out[2]:
            if board.cost > search_depth:
                search_depth = board.cost
        
        goal_path = [manh_out[1]]
        current_board = manh_out[1]
        
        while current_board.parent is not None:
            goal_path.insert(0, current_board.parent)
            current_board = current_board.parent
        
        print(f'Running time = {manh_time}\n')
        print(f'Search depth = {search_depth}\n')
        print(f'Cost of path = {manh_out[1].cost}\n')
        print("Nodes expanded:\n", *manh_out[2], "\n")
        print("Path to goal:\n", *goal_path, "\n")
        
    elif choice[0] == '2':
        initial_state_eucl = Board(board, EUCLIDEAN, None, 0)
        
        eucl_begin = time.time()
        eucl_out = A_star_search(initial_state_eucl)
        time.sleep(1)
        eucl_end = time.time()
        
        eucl_time = eucl_end - eucl_begin
        
        if not eucl_out[0]:
            print("Failure, can't solve the puzzle.\n")
            return
        
        search_depth = 0
        
        for board in eucl_out[2]:
            if board.cost > search_depth:
                search_depth = board.cost
        
        goal_path = [eucl_out[1]]
        current_board = eucl_out[1]
        
        while current_board.parent is not None:
            goal_path.insert(0, current_board.parent)
            current_board = current_board.parent
            
        print(f'Running time = {eucl_time}\n')
        print(f'Search depth = {search_depth}\n')
        print(f'Cost of path = {eucl_out[1].cost}\n')
        print("Nodes expanded:\n", *eucl_out[2], "\n")
        print("Path to goal:\n", *goal_path, "\n")
        
    
    
    
    