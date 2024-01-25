
def draw_board(positions):
    print(f"{positions[0]:<3}{positions[1]:^3}{positions[2]:>3}")
    print(f"{positions[3]:<3}{positions[4]:^3}{positions[5]:>3}")
    print(f"{positions[6]:<3}{positions[7]:^3}{positions[8]:>3}")

def check_if_valid(positions, zug):
    if positions[zug] == "":
        return True
    else:
        return False

def check_win_condition(positions):
    #print(positions)
    if (
        (positions[0] == "X" and positions[1] == "X" and positions[2] == "X")
        or (positions[3] == "X" and positions[4] == "X" and positions[5] == "X")
        or (positions[6] == "X" and positions[7] == "X" and positions[8] == "X")
        
        or (positions[0] == "X" and positions[3] == "X" and positions[6] == "X")
        or (positions[1] == "X" and positions[4] == "X" and positions[7] == "X")
        or (positions[2] == "X" and positions[5] == "X" and positions[8] == "X")

        or (positions[0] == "X" and positions[4] == "X" and positions[8] == "X")
        or (positions[2] == "X" and positions[4] == "X" and positions[6] == "X")

        or (positions[0] == "O" and positions[1] == "O" and positions[2] == "O")
        or (positions[3] == "O" and positions[4] == "O" and positions[5] == "O")
        or (positions[6] == "O" and positions[7] == "O" and positions[8] == "O")
        
        or (positions[0] == "O" and positions[3] == "O" and positions[6] == "O")
        or (positions[1] == "O" and positions[4] == "O" and positions[7] == "O")
        or (positions[2] == "O" and positions[5] == "O" and positions[8] == "O")
        
        or (positions[0] == "O" and positions[4] == "O" and positions[8] == "O")
        or (positions[2] == "O" and positions[4] == "O" and positions[6] == "O")
        ):
        return True
    
def clear_board():
    position = [""]*9 #ErzeugteinleeresSpielfeldFalse
    return position