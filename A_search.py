import heapq
import math

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
        return f'{self.confg}'

goal_state = Board([[0, 1, 2], [3, 4, 5], [6, 7, 8]], None, None, None)

def search(board):
    initial_state_manh = Board(board, MANHATTAN, None, 0)
    initial_state_eucl = Board(board, EUCLIDEAN, None, 0)
    
    manh_out = A_star_search(initial_state_manh)
    eucl_out = A_star_search(initial_state_eucl)
    
def A_star_search(initial_state: Board):
    pass
    