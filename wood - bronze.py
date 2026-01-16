import sys

def main():
    while True:
        try:
            opponent_move = input().strip()
            
            try:
                valid_action_count = int(input())
                valid_actions = []
                
                for _ in range(valid_action_count):
                    row, col = map(int, input().split())
                    valid_actions.append((row, col))
                
                if valid_actions:
                    print(f"{valid_actions[0][0]} {valid_actions[0][1]}")
                else:
                    print("0 0")
                    
            except ValueError:
                valid_boards_line = opponent_move
                valid_boards = list(map(int, valid_boards_line.split()))
                
                board_state = []
                for _ in range(9):
                    board_state.append(input().strip())
                
                move_found = False
                for board_idx in valid_boards if valid_boards[0] != -1 else range(9):
                    for cell_idx in range(9):
                        if board_state[board_idx][cell_idx] == '.':
                            print(f"{board_idx} {cell_idx}")
                            move_found = True
                            break
                    if move_found:
                        break
                
                if not move_found:
                    print("0 0")
            
            sys.stdout.flush()
            
        except EOFError:
            break
        except Exception:
            print("0 0")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
