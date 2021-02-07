import A_search

def valid_board(board):
    try:
        # Check if input is 9 numbers.
        assert len(board) == 9
        
        # Check if all inputs are numbers.
        for el in board:
            if not el.isdigit():
                return False
        
        # Check if the input is 9 numbers between 0 and 8.
        iboard = list(map(int, board))
        assert len(list(filter(lambda x: x >= 0 and x < 9 and iboard.count(x) == 1, iboard))) == 9
        
        return True
    except AssertionError:
        return False
            

def input_configuration():
    print("Enter the initial board configuration")
    
    board_conf = input().split(" ")
    
    while not valid_board(board_conf):
        print("The board configuration is invalid! Please enter a valid configuration.")
        board_conf = input().split(" ")
    
    return list(map(int, board_conf))

def main():
    # Use whichever list is most convenient for you.
    board1d = input_configuration()
    board2d = [[x, y, z] for x, y, z in [board1d[:3], board1d[3:6], board1d[6:]]]
    
    print("Choose the search algorithm:\n1) BFS\n2) DFS\n3) A*")
    choice = input().split(" ")
    
    while (len(choice) != 1) or (not choice[0].isdigit()) or (int(choice[0]) < 1) or (int(choice[0]) > 3):
        print("Invalid input! Please retry.")
        choice = input().split(" ")
    
    if choice[0] == '1': # Call the BFS function.
        pass
    elif choice[0] == '2': # Call the DFS function.
        pass
    else: # Call the A* function.
        A_search.search(board2d)

if __name__ == "__main__":
    main()