from random import choice

moves = ["R", "P", "S"]
win_logic = [("R", "S"), ("P", "R"), ("S", "P")] #This list encapsulates the 3 rules for winning: 1. "R" beats "S" 2: "P" beats "R" 3. "S" beats "P" 
run = True

while run:
   player_move = input("Make your move (R, P, or S): ")
   while player_move not in moves:
        print("'" + player_move + "'" + " is not a valid move!")
        print()
        player_move = input("Make your move: ")

   CPU_move = choice(moves)
   print("Player " + "(" + player_move + ")" + " : " + "CPU " + "(" + CPU_move + ")")

   #victory check
   if player_move == CPU_move:
       print("Tie!")
   else:
        for w in win_logic:
            if player_move in w and CPU_move in w:
                if player_move == w[0]:
                    print("Player wins!")
                else:
                    print("CPU wins!")
                run = False
                break
