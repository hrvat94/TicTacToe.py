import board
import KI

position = board.clear_board()

while True:
    board.draw_board(position)
    print()

    valid_move = False
    while not valid_move:
        #ZugvonSpieler1
        print("Bitte gebe eine Zahl von 0-8 an!")
        player_1_zug = int(input("Player_1: "))

        #Zugspielbar?
        valid_move = board.check_if_valid(position,player_1_zug)

    if valid_move == True:
        position[player_1_zug] = "X"  #SpieleZug
        board.draw_board(position)
        print()

    #HatSpieler1gewonnen?
    if board.check_win_condition(position):
        print("---> Sieger!")
        print("Player_1 hat gewonnen!!!")
        board.draw_board(position)
        break
    
    #ZugvonKI
    print("KI ist am Zug!")
    ki_zug = KI.make_random_move(position)
    #ki_zug = KI.make_good_move(position)

    position[ki_zug] = "O"  #SpieleZug
    
    #HatSpieler2gewonnen?
    if board.check_win_condition(position):
        print("---> Sieger!")
        print("KI hat gewonnen!!!")
        board.draw_board(position)
        break
