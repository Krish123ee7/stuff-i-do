
class Chess():
    def __init__(self):
        self.chess_board = [["r","n","b","q","k","b","n","r"],
                            ["p","p","p","p","p","p","p","p"],
                            ["","","","","","","",""],
                            ["","","","","","","",""],
                            ["","","","","","","",""],
                            ["","","","","","","",""],
                            ["p'","p'","p'","p'","p'","p'","p'","p'"],
                            ["r'","n'","b'","q'","k'","b'","n'","r'"]]
        self.white_win = False
        self.black_win = False
        self.turn = "white"
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None


        self.pieces =[
            King(0,4,'white'),
            King(7,4,'black'),
            Queen(0,3,'white'),
            Queen(7,3,'black'),
            Knight(0,1,'white'),
            Knight(0,6,'white'),
            Knight(7,1,'black'),
            Knight(7,6,'black'),
            Bishop(0,5,'white'),
            Bishop(0,2,'white'),
            Bishop(7,5,'black'),
            Bishop(7,2,'black'),
            Rookh(0,0,'white'),
            Rookh(0,7,'white'),
            Rookh(7,0,'black'),
            Rookh(7,7,'black'),
            Pawn(1,0,'white'),
            Pawn(1,1,'white'),
            Pawn(1,2,'white'),
            Pawn(1,3,'white'),
            Pawn(1,4,'white'),
            Pawn(1,5,'white'),
            Pawn(1,6,'white'),
            Pawn(1,7,'white'),
            Pawn(6,0,'black'),
            Pawn(6,1,'black'),
            Pawn(6,2,'black'),
            Pawn(6,3,'black'),
            Pawn(6,4,'black'),
            Pawn(6,5,'black'),
            Pawn(6,6,'black'),
            Pawn(6,7,'black')]

        self.selected_piece = None
    #basic thing
    def print_board(self):
        alph=['a','b','c','d','e','f','g','h']
        for i in range(8):
            print(8-i,"-",end="")
            for j in range(8):
                if "'" in self.chess_board[-i-1][j]:
                    print(f"| {self.chess_board[-i-1][j]}",end="")
                elif self.chess_board[-i-1][j] == "":
                    print("|   ",end='')
                else:
                    print(f"| {self.chess_board[-i-1][j] }",end=" ")
            print("|")
        print("     |   |   |   |   |   |   |   |")
        print("     a   b   c   d   e   f   g   h")

    def toogle_turn(self):
        if self.turn == 'white':
            self.turn = "black"
        elif self.turn  == "black":
            self.turn = 'white'

    def txt_to_pos(self,txt):
        alph=['a','b','c','d','e','f','g','h']
        x=int(txt[1]) -1
        y= None
        for i in range(8):
            if txt[0]== alph[i]:
                y = i

        return x,y
            
    def input_data(self,txt):
        x,y = self.txt_to_pos(input(txt))
        try:
            if (x and y) not in list(range(8)):
                print("invalid input")
                self.input_data()
        except:
            print("invalid input")
            self.input_data()
        else:
            return x,y

    
        
            
#----------------------------------------MAIN----------------------------------------#
    def start_game(self):
        print()

        checks =[]
        while (self.white_win and self.black_win) == False:
            print("no of checks",len(checks))

            # update chess_board for the pieces 

            for piece in self.pieces:
                piece.update_chess_board(self.chess_board)


            loopbraker = False
            loopcontinuer = False
            caputre_move = False
            
            print(f"{self.turn}'s turn")
            self.print_board()
            self.x1,self.y1 = self.input_data("enter the position of the piece that you want to select: ")
            if (self.turn == "white" and self.chess_board[self.x1][self.y1] not in ["r","n","b","q","k","p"]) or (self.turn == "black" and self.chess_board[self.x1][self.y1] not in ["r'","n'","b'","q'","k'","p'"]):
                print("please select your own piece, Try again!")
                continue
            # ERROR : selected blank space
            if self.chess_board[self.x1][self.y1] == '':
                print("No piece at the position, Try again!")
                continue

            self.x2,self.y2 = self.input_data("enter the position where you want to move/caputre: ")
            
            # Error : cannot capture your piece
            if (self.turn == "white" and self.chess_board[self.x2][self.y2] in ["r","n","b","q","k","p"]) or (self.turn == "black" and self.chess_board[self.x2][self.y2] in ["r'","n'","b'","q'","k'","b'","n'","r'"]):
                print("Invalid move: Can not capture your own piece, Try again!")
                continue
            
            
            #capture
            if ((self.turn == "white" and self.chess_board[self.x2][self.y2] in ["q'","b'","n'","r'","p'"]) or (self.turn == "black" and self.chess_board[self.x2][self.y2] in ["q","b","n","r","p"])):
                caputre_move = True
                print("capture")

            #normal move
            else:
                print("normal move")

            if len(checks) == 0:
                index = -1
                
                for piece in self.pieces:
                    index +=1
                    if [piece.x,piece.y] == [self.x1,self.y1]:
                        print(index)
                        print([self.x2,self.y2])
                        if caputre_move and type(self.pieces[index]) == Pawn:
                            if [self.x2,self.y2] in self.pieces[index].capture():
                                print(self.pieces[index].valid_moves)
                                print("capture move")
                                templist = self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1]
                                self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = self.chess_board[self.x1][self.y1],''
                                self.pieces[index].move(self.x2,self.y2)
                                if (self.turn == "white" and len(self.pieces[0].if_under_check())>0) or (self.turn == "black" and len(self.pieces[1].if_under_check())>0):
                                    print("invalid move! moving this piece will put your king under check")
                                    self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = templist
                                    self.pieces[index].move(self.x1,self.y1)
                                    loopcontinuer = True
                                    break
                                self.toogle_turn()
                                #loopbraker = True
                        elif [self.x2,self.y2] in self.pieces[index].check_moves():
                            print(self.pieces[index].valid_moves)
                            print("valid move")
                            templist = self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1]
                            self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = self.chess_board[self.x1][self.y1],''
                            self.pieces[index].move(self.x2,self.y2)
                            if (self.turn == "white" and len(self.pieces[0].if_under_check())>0) or (self.turn == "black" and len(self.pieces[1].if_under_check())>0):
                                    print("invalid move! moving this piece will put your king under check")
                                    self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = templist
                                    self.pieces[index].move(self.x1,self.y1)
                                    checks =[]
                                    break
                            self.toogle_turn()
                            #loopbraker = True
                        break

            if loopcontinuer:
                continue
            if loopbraker:
                break

            if self.turn == "white":
                checks.extend(self.pieces[0].if_under_check())
            elif self.turn == "black":
                checks.extend(self.pieces[1].if_under_check())
            #check moves
            if len(checks) > 0:
                print("CHECK!!")

            
            if loopcontinuer:
                continue
            if loopbraker:
                break

                  

#----------------------------------------PIECES----------------------------------------#
class King():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.valid_moves = []
        self.chess_board = []
        self.under_check = False

    def check_moves(self):
        for i in range(-1,2):
            for j in range(-1,2):
                if self.x + i in list(range(8)) and self.y + j in list(range(8)):
                    self.valid_moves.append([self.x+i,self.y+j])
        return self.valid_moves

    def reset_valid_moves(self):
        self.valid_moves = []

    def move(self,x,y):
        self.x,self.y = x,y
        self.reset_valid_moves()

    def update_chess_board(self,chess_board):
        self.chess_board = chess_board  

    def if_under_check(self):
        
        rookh_part = Rookh(self.x,self.y,self.color)
        bishop_part = Bishop(self.x,self.y,self.color)
        knight_part = Knight(self.x,self.y,self.color)
        pawn_part = Pawn(self.x,self.y,self.color)

        rookh_part.update_chess_board(self.chess_board)
        bishop_part.update_chess_board(self.chess_board)
        knight_part.update_chess_board(self.chess_board)
        pawn_part.update_chess_board(self.chess_board)

        check_by_rookh = False
        check_by_bishop = False
        check_by_knight = False
        check_by_pawn = False
        check_by_queen = False

        print(self.color)
        rookh_moves = rookh_part.check_moves()
        print("rook",rookh_moves)
        bishop_moves = bishop_part.check_moves()
        print("bishop",bishop_moves)
        knight_moves = knight_part.check_moves()
        print("knight",knight_moves)
        pawn_moves = pawn_part.capture()
        print("pawn",pawn_moves)
        queen_moves = rookh_moves + bishop_moves
        print("queen",queen_moves)

        if self.color == "white":
            for a,b in knight_moves:
                try:
                    if self.chess_board[a][b] == "n'":
                        check_by_knight = True
                except:
                    pass 
            for a,b in pawn_moves:
                if self.chess_board[a][b] == "p'":
                    check_by_pawn = True
            for a,b in queen_moves:
                if self.chess_board[a][b] == "q'":
                    check_by_queen = True
            for a,b in rookh_moves:
                if self.chess_board[a][b] == "r'":
                    check_by_rookh = True
            for a,b in bishop_moves:
                if self.chess_board[a][b] == "b'":
                    check_by_bishop = True
            
        if self.color == "black":
            for a,b in knight_moves:
                try:
                    if self.chess_board[a][b] == "n":
                        check_by_knight = True
                except:
                    pass
            for a,b in pawn_moves:
                if self.chess_board[a][b] == "p":
                    check_by_pawn = True
            for a,b in queen_moves:
                if self.chess_board[a][b] == "q":
                    check_by_queen = True
            for a,b in rookh_moves:
                if self.chess_board[a][b] == "r":
                    check_by_rookh = True
            for a,b in bishop_moves:
                if self.chess_board[a][b] == "b":
                    check_by_bishop = True
        return_list = []
        if check_by_rookh:
            return_list.append("check by rookh")
        if check_by_bishop:
            return_list.append("check by bishop")
        if check_by_knight:
            return_list.append("check by knight")
        if check_by_pawn:
            return_list.append("check by pawn")
        if check_by_queen:
            return_list.append("check by queen")
        return return_list

class Queen():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.valid_moves = []
        self.chess_board = []

    def check_moves(self):
        rookhpart = Rookh(self.x,self.y,self.color)
        bishoppart = Bishop(self.x,self.y,self.color)
        self.valid_moves.extend(rookhpart.check_moves())
        self.valid_moves.extend(bishoppart.check_moves())
        return self.valid_moves

    def reset_valid_moves(self):
        self.valid_moves = []

    def move(self,x,y):
        self.x,self.y = x,y
        self.reset_valid_moves()
    
    def update_chess_board(self,chess_board):
        self.chess_board = chess_board

class Rookh():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.valid_moves = []
        self.chess_board = []
        self.first_move = True

    def check_moves(self):
        #up moves
        for i in range(1,8):
            try:
                if self.x + i in list(range(8)) and self.chess_board[self.x+i][self.y] == '':
                    self.valid_moves.append([self.x+i,self.y])
                elif self.x + i in list(range(8)) and self.color == "white" and self.chess_board[self.x+i][self.y] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x+i][self.y] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x+i,self.y])
                    break
                else:
                    break
            except:
                break

        #down moves
        for i in range(1,8):
            try:
                if self.x - i in list(range(8)) and self.chess_board[self.x-i][self.y] == '':
                    self.valid_moves.append([self.x-i,self.y])
                elif self.x - i in list(range(8)) and self.color == "white" and self.chess_board[self.x-i][self.y] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x-i][self.y] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x-i,self.y])
                    break
                else:
                    break
            except:
                break

        #right moves
        for i in range(1,8):
            try:
                if self.y + i in list(range(8)) and self.chess_board[self.x][self.y+i] == '':
                    self.valid_moves.append([self.x,self.y+i])
                elif self.y + i in list(range(8)) and self.color == "white" and self.chess_board[self.x][self.y+i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x][self.y+i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x,self.y+i])
                    break
                else:
                    break
            except:
                break

        #left moves
        for i in range(1,8):
            try:
                if self.y - i in list(range(8)) and self.chess_board[self.x][self.y-i] == '':
                    self.valid_moves.append([self.x,self.y-i])
                elif self.y - i in list(range(8)) and self.color == "white" and self.chess_board[self.x][self.y-i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x][self.y-i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x,self.y-i])
                    break
                else:
                    break
            except:
                break

        return self.valid_moves

    def reset_valid_moves(self):
        self.valid_moves = []

    def move(self,x,y):
        self.x,self.y = x,y
        self.reset_valid_moves()

    def update_chess_board(self,chess_board):
        self.chess_board = chess_board

class Knight():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.valid_moves = []
        self.chess_board = []

    def check_moves(self):
        if self.x+2 in list(range(8)) and self.y+1 in list(range(8)):
            self.valid_moves.append([self.x+2,self.y+1])
        if self.x+2 in list(range(8)) and self.y-1 in list(range(8)):
            self.valid_moves.append([self.x+2,self.y-1])
        if self.x-2 in list(range(8)) and self.y+1 in list(range(8)):
            self.valid_moves.append([self.x-2,self.y+1])
        if self.x-2 in list(range(8)) and self.y-1 in list(range(8)):
            self.valid_moves.append([self.x-2,self.y-1])
        if self.x+1 in list(range(8)) and self.y+2 in list(range(8)):
            self.valid_moves.append([self.x+1,self.y+2])
        if self.x+1 in list(range(8)) and self.y-2 in list(range(8)):
            self.valid_moves.append([self.x+1,self.y-2])
        if self.x-1 in list(range(8)) and self.y+2 in list(range(8)):
            self.valid_moves.append([self.x-1,self.y+2])
        if self.x-1 in list(range(8)) and self.y-2 in list(range(8)):
            self.valid_moves.append([self.x-1,self.y-2])

        return self.valid_moves

    def reset_valid_moves(self):
        self.valid_moves = []

    def move(self,x,y):
        self.x,self.y = x,y
        self.reset_valid_moves()

    def update_chess_board(self,chess_board):
        self.chess_board = chess_board

class Bishop():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.valid_moves = []
        self.chess_board = []

    def check_moves(self):
        # up-right moves
        for i in range(1,8):
            try:
                if (self.x + i in list(range(8)) and self.y + i in list(range(8))) and (self.chess_board[self.x+i][self.y+i] == ''):
                    self.valid_moves.append([self.x+i,self.y+i])
                elif (self.x + i in list(range(8)) and self.y + i in list(range(8))) and self.color == "white" and self.chess_board[self.x+i][self.y+i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x+i][self.y+i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x+i,self.y+i])
                    break
                else:
                    break
            except:
                break
        # up-left moves
        for i in range(1,8):
            try:
                if (self.x + i in list(range(8)) and self.y - i in list(range(8))) and self.chess_board[self.x+i][self.y-i] == '':
                    self.valid_moves.append([self.x+i,self.y-i])
                elif (self.x + i in list(range(8)) and self.y - i in list(range(8))) and  self.color == "white" and self.chess_board[self.x+i][self.y-i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x+i][self.y-i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x+i,self.y-i])
                    break
                else:
                    break
            except:
                break
        # down-right moves
        for i in range(1,8):
            try:
                if (self.x - i in list(range(8)) and self.y + i in list(range(8))) and self.chess_board[self.x-i][self.y+i] == '':
                    self.valid_moves.append([self.x-i,self.y+i])
                elif (self.x - i in list(range(8)) and self.y + i in list(range(8))) and self.color == "white" and self.chess_board[self.x-i][self.y+i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x-i][self.y+i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x-i,self.y+i])
                    break
                else:
                    break
            except:
                break
        # down-left moves
        for i in range(1,8):
            try:
                if (self.x - i in list(range(8)) and self.y - i in list(range(8))) and self.chess_board[self.x-i][self.y-i] == '':
                    self.valid_moves.append([self.x-i,self.y-i])
                elif (self.x - i in list(range(8)) and self.y - i in list(range(8))) and self.color == "white" and self.chess_board[self.x-i][self.y-i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x-i][self.y-i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x-i,self.y-i])
                    break
                else:
                    break
            except:
                break

        return self.valid_moves

    def reset_valid_moves(self):
        self.valid_moves = []

    def move(self,x,y):
        self.x,self.y = x,y
        self.reset_valid_moves()

    def update_chess_board(self,chess_board):
        self.chess_board = chess_board

class Pawn():
    def __init__(self,x,y,color,first_move = True):
        self.x = x
        self.y = y
        self.color = color
        self.first_move = first_move
        self.valid_moves = []
        self.chess_board = []

    def check_moves(self):
        if self.color == "white" and self.chess_board[self.x+1][self.y] == '':
            if self.first_move:
                self.valid_moves.append([self.x+2,self.y])
            self.valid_moves.append([self.x+1,self.y])

        elif self.color == "black" and self.chess_board[self.x-1][self.y] == '':
            if self.first_move:
                self.valid_moves.append([self.x-2,self.y])
            self.valid_moves.append([self.x-1,self.y])
        
        
        return self.valid_moves
    
    def capture(self):
        temp_list=[]
        if self.color == "white":
            temp_list.extend(([self.x+1,self.y+1],[self.x+1,self.y-1]))

        elif self.color == "black":
            temp_list.extend(([self.x-1,self.y+1],[self.x-1,self.y-1]))

        for a,b in temp_list:
            if a in list(range(8)) and b in list(range(8)):
                self.valid_moves.append([a,b])
        return self.valid_moves

    def reset_valid_moves(self):
        self.valid_moves = []

    def move(self,x,y):
        self.x,self.y = x,y
        self.first_move = False
        self.reset_valid_moves()

    def update_chess_board(self,chess_board):
        self.chess_board = chess_board



chess = Chess()
chess.start_game()
