
import numpy as np
import time


class Node():
    def __init__(self, state, parent, action, depth,  path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.path_cost = path_cost
        # children node
        self.move_up = None
        self.move_left = None
        self.move_down = None
        self.move_right = None

    def try_move_down(self):
        zero_index = [i[0] for i in np.where(self.state == 0)]
        if zero_index[0] == 0:
            return False
        else:
            up_value = self.state[zero_index[0] - 1, zero_index[1]]  # value of the upper tile
            new_state = self.state.copy()
            new_state[zero_index[0], zero_index[1]] = up_value
            new_state[zero_index[0] - 1, zero_index[1]] = 0
            return new_state, up_value

    def try_move_right(self):
        zero_index = [i[0] for i in np.where(self.state == 0)]
        if zero_index[1] == 0:
            return False
        else:
            left_value = self.state[zero_index[0], zero_index[1] - 1]  # value of the left tile
            new_state = self.state.copy()
            new_state[zero_index[0], zero_index[1]] = left_value
            new_state[zero_index[0], zero_index[1] - 1] = 0
            return new_state, left_value

    def try_move_up(self):
        zero_index = [i[0] for i in np.where(self.state == 0)]
        if zero_index[0] == 2:
            return False
        else:
            lower_value = self.state[zero_index[0] + 1, zero_index[1]]  # value of the lower tile
            new_state = self.state.copy()
            new_state[zero_index[0], zero_index[1]] = lower_value
            new_state[zero_index[0] + 1, zero_index[1]] = 0
            return new_state, lower_value

    def try_move_left(self):
        zero_index = [i[0] for i in np.where(self.state == 0)]
        if zero_index[1] == 2:
            return False
        else:
            right_value = self.state[zero_index[0], zero_index[1] + 1]
            new_state = self.state.copy()
            new_state[zero_index[0], zero_index[1]] = right_value
            new_state[zero_index[0], zero_index[1] + 1] = 0
            return new_state, right_value

    def print_path(self):
        state_trace = [self.state]
        action_trace = [self.action]
        depth_trace = [self.depth]
        path_cost_trace = [self.path_cost]

        while self.parent:
            self = self.parent

            state_trace.append(self.state)
            action_trace.append(self.action)
            depth_trace.append(self.depth)
            path_cost_trace.append(self.path_cost)

        step_counter = 0
        while state_trace:
            print('step', step_counter)
            print (state_trace.pop())
            print('action=', action_trace.pop(), ', depth=', str(depth_trace.pop()),
                ', total_cost=',  str(path_cost_trace.pop()) + '\n')

            step_counter += 1

    def depth_first_search(self, goal_state):
        start = time.time()

        stack = [self]
        num_nodes_popped = 0
        max_length = 1
        depth = [0]
        path_cost = [0]
        visited = set([])
        while stack:
            if len(stack) > max_length:
                max_length = len(stack)

            current_node = stack.pop(0)
            num_nodes_popped += 1

            current_depth = depth.pop(0)
            current_path_cost = path_cost.pop(0)
            visited.add(tuple(current_node.state.reshape(1, 9)[0]))

            if np.array_equal(current_node.state, goal_state):
                current_node.print_path()

                print('Time performance:', str(num_nodes_popped), 'nodes popped off the stack.')
                print('Space performance:', str(max_length), 'nodes in the stack at its max.')
                print('Time spent: %0.2fs' % (time.time() - start))
                return True

            else:
                if current_node.try_move_down():
                    new_state, up_value = current_node.try_move_down()
                    # check if the resulting node is already visited
                    if tuple(new_state.reshape(1, 9)[0]) not in visited:
                        current_node.move_down = Node(state=new_state, parent=current_node, action='down',
                                                      depth=current_depth + 1,
                                                       path_cost=current_path_cost + up_value)
                        stack.insert(0, current_node.move_down)
                        depth.insert(0, current_depth + 1)
                        path_cost.insert(0, current_path_cost + up_value)

                if current_node.try_move_right():
                    new_state, left_value = current_node.try_move_right()
                    if tuple(new_state.reshape(1, 9)[0]) not in visited:
                        # create a new child node
                        current_node.move_right = Node(state=new_state, parent=current_node, action='right',
                                                       depth=current_depth + 1
                                                       , path_cost=current_path_cost + left_value,
                                                       )
                        stack.insert(0, current_node.move_right)
                        depth.insert(0, current_depth + 1)
                        path_cost.insert(0, current_path_cost + left_value)

                if current_node.try_move_up():
                    new_state, lower_value = current_node.try_move_up()
                    # check if the resulting node is already visited
                    if tuple(new_state.reshape(1, 9)[0]) not in visited:
                        # create a new child node
                        current_node.move_up = Node(state=new_state, parent=current_node, action='up',
                                                    depth=current_depth + 1, path_cost=current_path_cost + lower_value)
                        stack.insert(0, current_node.move_up)
                        depth.insert(0, current_depth + 1)
                        path_cost.insert(0, current_path_cost + lower_value)

                if current_node.try_move_left():
                    new_state, right_value = current_node.try_move_left()
                    if tuple(new_state.reshape(1, 9)[0]) not in visited:
                        current_node.move_left = Node(state=new_state, parent=current_node, action='left',
                                                      depth=current_depth + 1, path_cost=current_path_cost + right_value)

                        stack.insert(0, current_node.move_left)
                        depth.insert(0, current_depth + 1)
                        path_cost.insert(0, current_path_cost + right_value)


initial_state = np.array([1, 2, 3, 8, 6, 4, 7, 5, 0]).reshape(3, 3)
goal_state = np.array([1, 2, 3, 8, 0, 4, 7, 6, 5]).reshape(3, 3)
print(initial_state, '\n')
print(goal_state)

root_node = Node(state=initial_state, parent=None, action=None, depth=0,  path_cost=0)
root_node.depth_first_search(goal_state)

