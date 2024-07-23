class Chess():
    def __init__(self):
        self.chess_board = [["r","n","b","q","k","b","n","r"],
                       ["p","p","p","p","p","p","p","p"],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["","","","","","","",""],
                       ["p'","p'","p'","p'","p'","p'","p'","p'"],
                       ["r'","n'","b'","q'","k'","b'","n'","r'"],]
        self.white_win = False
        self.black_win = False
        self.turn = "White"
        self.x = None
        self.y = None

        self.white_king = King(0,4,'white')
        self.black_king = King(7,4,'black')
        self.white_queen = Queen(0,3,'white')
        self.black_queen = Queen(7,3,'black')
        self.white_knight1 = Knight(0,1,'white')
        self.white_knight2 = Knight(0,6,'white')
        self.black_knight1 = Knight(7,1,'black')
        self.black_knight2 = Knight(7,6,'black')
        self.white_ws_bishop = Bishop(0,5,'white')
        self.white_bs_bishop = Bishop(0,2,'white')
        self.black_ws_bishop = Bishop(7,5,'black')
        self.black_bs_bishop = Bishop(7,2,'black')
        self.white_rookh1 = Rookh(0,0,'white')
        self.white_rookh2 = Rookh(0,7,'white')
        self.black_rookh1 = Rookh(7,0,'black')
        self.black_rookh2 = Rookh(7,7,'black')
        self.a2 = White_pawn(1,0,'white')
        self.b2 = White_pawn(1,1,'white')
        self.c2 = White_pawn(1,2,'white')
        self.d2 = White_pawn(1,3,'white')
        self.e2 = White_pawn(1,4,'white')
        self.f2 = White_pawn(1,5,'white')
        self.g2 = White_pawn(1,6,'white')
        self.h2 = White_pawn(1,7,'white')
        self.a7 = Black_pawn(6,0,'black')
        self.b7 = Black_pawn(6,1,'black')
        self.c7 = Black_pawn(6,2,'black')
        self.d7 = Black_pawn(6,3,'black')
        self.e7 = Black_pawn(6,4,'black')
        self.f7 = Black_pawn(6,5,'black')
        self.g7 = Black_pawn(6,6,'black')
        self.h7 = Black_pawn(6,7,'black')

        self.pieces = [self.white_king,self.black_king,self.white_queen,self.black_queen,self.white_knight1,self.white_knight2,self.black_knight1,self.black_knight2,self.white_ws_bishop,self.white_bs_bishop,self.black_ws_bishop,self.black_bs_bishop,self.white_rookh1,self.white_rookh2,self.black_rookh1,self.black_rookh2,self.a2,self.b2,self.c2,self.d2,self.e2,self.f2,self.g2,self.h2,self.a7,self.b7,self.c7,self.d7,self.e7,self.f7,self.g7,self.h7]
        
        #self.position = {self.white_king : self.white_king.possition(),
        #              self.black_king : [7,4],
        #              self.white_queen : [0,3],
        #              self.black_queen : [7,3],
        #              self.white_knight1 : [0,1],
        #              self.white_knight2 : [0,6],
        #              self.black_knight1 : [7,1],
        #              self.black_knight2 : [7,6],
        #              self.white_ws_bishop : [0,5],
        #              self.white_bs_bishop : [0,2],
        #              self.black_ws_bishop : [7,5],
        #              self.black_bs_bishop : [7,2],
        #              self.white_rookh1 : [0,0],
        #              self.white_rookh2 : [0,7],
        #              self.black_rookh1 : [7,0],
        #              self.black_rookh2 : [7,7],
        #              self.a2 : [1,0],
        #              self.b2 : [1,1],
        #              self.c2 : [1,2],
        #              self.d2 : [1,3],
        #              self.e2 : [1,4],
        #              self.f2 : [1,5],
        #              self.g2 : [1,6],
        #              self.h2 : [1,7],
        #              self.a7 : [6,0],
        #              self.b7 : [6,1],
        #              self.c7 : [6,2],
        #              self.d7 : [6,3],
        #              self.e7 : [6,4],
        #              self.f7 : [6,5],
        #              self.g7 : [6,6],
        #              self.h7 : [6,7],}

        self.selected_piece = None

    def print_board(self):
        alph = ['a','b','c','d','e','f','g','h']
        for i in range(1,9):
            print(9-i,end="-")
            for piece in self.chess_board[-i] :
                if piece in ["r'","n'","b'","q'","k'","p'"]:
                    print("|",piece,"|",end='')
                elif piece in ["r","n","b","q","k","p"]:
                    print("|",piece," |",end='')
                else:
                    print("|    |",end="")
                
            print()
        print("    ",end="")
        for i in range(0,8):
            print(alph[i],end="     ")
        print()

    def toogle_turn(self):
        if self.turn == "White":
            self.turn = "Black"
        else:
            self.turn = "White"

    def input_gui(self,x=None,y=None):
        return x,y
        

    def _input_(self,text = "enter sellection possition: "):
        #try:
        
        #if self.input_gui() is None:
        _input_ = input(text)
        alph = ['a','b','c','d','e','f','g','h']
        for i in range(0,8):
            if _input_[0] == alph[i]:
                self.y=i
            if int(_input_[1]) == i+1:
                self.x=i
                print(self.x,self.y)
        #elif self.input_gui() is not None:
        #    self.x,self.y = self.input_gui()
        #except:
        return [self.x,self.y]

    def check_pos(self):
        for i in self.pieces:
            if i.position()== [self.x,self.y]:
                return i
                
            
    def start(self):
        while (self.white_win == False) and (self.black_win == False):
            print(f"{self.turn}'s turn")
            self.print_board()
            self.first_input = self._input_()
            if self.chess_board[self.x][self.y] == "":
                print("no piece is selected")
                self.x,self.y == None,None
                continue
            if (self.turn == "White" and self.chess_board[self.x][self.y] in ["r'","n'","b'","q'","k'","p'"]) or (self.turn == "Black" and self.chess_board[self.x][self.y] in ["r","n","b","q","k","p"]):
                print("please select your own piece")
                self.x,self.y == None,None
                continue
            self.selected_piece = self.check_pos()
            self.second_input = self._input_("enter secondary sellection possition: ")
            if (self.turn == "White" and self.chess_board[self.x][self.y] in ["r","n","b","q","k","p"]) or (self.turn == "Black" and self.chess_board[self.x][self.y] in ["r'","n'","b'","q'","k'","p'"]):
                print("you can not capture your own piece")
                self.x,self.y == None,None
                continue
            if self.first_input == self.second_input:
                print("invalid move")
                print(self.first_input,self.second_input)
                self.x,self.y == None,None
                continue
            # for normal move
            if self.chess_board[self.first_input[0]][self.first_input[1]] in ["k","k'","n","n'"] and ((self.chess_board[self.second_input[0]][self.second_input[1]] == "") or (self.turn == "White" and self.chess_board[self.x][self.y] in ["r'","n'","b'","q'","k'","p'"]) or (self.turn == "Black" and self.chess_board[self.x][self.y] in ["r","n","b","q","k","p"])) and (self.selected_piece.check_move(self.second_input) and self.first_input != self.second_input):
                print(self.chess_board[self.second_input[0]][self.second_input[1]],self.chess_board[self.first_input[0]][self.first_input[1]])
                self.chess_board[self.x][self.y],self.chess_board[self.first_input[0]][self.first_input[1]] = self.chess_board[self.first_input[0]][self.first_input[1]],""
                self.toogle_turn()
                self.x,self.y == None,None
                # for check 
                continue
            elif self.chess_board[self.first_input[0]][self.first_input[1]] in ["r","r'","b","b'"] and ((self.chess_board[self.second_input[0]][self.second_input[1]] == "") or (self.turn == "White" and self.chess_board[self.x][self.y] in ["r'","n'","b'","q'","k'","p'"]) or (self.turn == "Black" and self.chess_board[self.x][self.y] in ["r","n","b","q","k","p"])) and (self.selected_piece.check_move(self.second_input,self.chess_board,self.turn) and self.first_input != self.second_input):
                print(self.chess_board[self.second_input[0]][self.second_input[1]],self.chess_board[self.first_input[0]][self.first_input[1]])
                self.chess_board[self.x][self.y],self.chess_board[self.first_input[0]][self.first_input[1]] = self.chess_board[self.first_input[0]][self.first_input[1]],""
                self.toogle_turn()
                self.x,self.y == None,None
                # for check 
                continue
            elif self.chess_board[self.first_input[0]][self.first_input[1]] in ["p","p'"] and ((self.chess_board[self.second_input[0]][self.second_input[1]] == "") and self.selected_piece.check_move(self.second_input)):
                print(self.chess_board[self.second_input[0]][self.second_input[1]],self.chess_board[self.first_input[0]][self.first_input[1]])
                self.chess_board[self.x][self.y],self.chess_board[self.first_input[0]][self.first_input[1]] = self.chess_board[self.first_input[0]][self.first_input[1]],""
                self.toogle_turn()
                self.x,self.y == None,None
                # for check 
                continue
            elif ((self.turn == "White" and self.chess_board[self.x][self.y] in ["r'","n'","b'","q'","k'","p'"]) or (self.turn == "Black" and self.chess_board[self.x][self.y] in ["r","n","b","q","k","p"])) and (self.chess_board[self.first_input[0]][self.first_input[1]] in ["p","p'"] and self.selected_piece.check_capture(self.second_input)):
                print(self.chess_board[self.second_input[0]][self.second_input[1]],self.chess_board[self.first_input[0]][self.first_input[1]])
                self.chess_board[self.x][self.y],self.chess_board[self.first_input[0]][self.first_input[1]] = self.chess_board[self.first_input[0]][self.first_input[1]],""
                self.toogle_turn()
                self.x,self.y == None,None
                # for check 
                continue
            else:
                print("invalid move")
                print("here")
                self.x,self.y == None,None
            
                


class White_pawn():
    def __init__(self,x,y,color):
        self.x1 = x
        self.y1 = y
        self.color = color
        self.first_move = True

    def position(self):
        return [self.x1,self.y1]

    def check_move(self,value):
        if (self.first_move == True and value == [3,self.y1]) or (value == [self.x1 + 1,self.y1]):
            self.first_move = False
            self.x1,self.y1 = value
            return True

    def check_capture(self,value):
        if (value == [self.x1 + 1,self.y1 +1]) or (value == [self.x1 + 1,self.y1 -1]):
            self.first_move = False
            self.x1,self.y1 = value
            return True


class Black_pawn():
    def __init__(self,x,y,color):
        self.x1 = x
        self.y1 = y
        self.color = color
        self.first_move = True

    def position(self):
        return [self.x1,self.y1]

    def check_move(self,value):
        if (self.first_move == True and value == [4,self.y1]) or (value == [self.x1 - 1,self.y1]):
            self.first_move = False
            self.x1,self.y1 = value
            return True

    def check_capture(self,value):
        if (value == [self.x1 - 1,self.y1 +1]) or (value == [self.x1 - 1,self.y1 -1]):
            self.first_move = False
            self.x1,self.y1 = value
            return True

class King():
    def __init__(self,x,y,color):
        self.x1 = x
        self.y1 = y
        self.color = color
        self.first_move = True

    def position(self):
        return [self.x1,self.y1]

    def posible_moves(self):
        moves = []
        for i in range(-1,2):
            for j in range(-1,2):
                if [i,j] not in [0,0]:
                    moves.append([self.x1 +i,self.y1 +j])
        return moves
    def check_move(self,value):
        if value in self.posible_moves():
            self.first_move = False
            self.x1,self.y1 = value
            return True
        

class Knight():
    def __init__(self,x,y,color):
        self.x1 = x
        self.y1 = y
        self.color = color

    def position(self):
        return [self.x1,self.y1]

    def posible_moves(self):
        moves = [[self.x1+2,self.y1+1],[self.x1+2,self.y1-1],[self.x1-2,self.y1+1],[self.x1-2,self.y1-1],[self.x1+1,self.y1+2],[self.x1+1,self.y1-2],[self.x1-1,self.y1+2],[self.x1-1,self.y1-2]]
        return moves
    def check_move(self,value):
        if value in self.posible_moves():
            self.x1,self.y1=value
            return True

class Rookh():
    def __init__(self,x,y,color):
        self.x1 = x
        self.y1 = y
        self.color = color
        self.first_move = True

    def position(self):
        return [self.x1,self.y1]

    def posible_moves(self,chess_board,turn):
        moves = []
        #for white turn
        for i in range(1,8):
            if self.x1+i<8 and  (turn == "White") and (chess_board[self.x1 + i][self.y1] in [""]):
                moves.append([self.x1+i,self.y1])
            elif self.x1+i<8 and  (turn == "White") and (chess_board[self.x1 + i][self.y1] in ["r'","n'","b'","q'","k'","p'"]):
                moves.append([self.x1+i,self.y1+i])
                break
        for i in range(1,8):
            if self.y1 + i <8 and (turn == "White") and (chess_board[self.x1][self.y1 + i] in [""]):
                moves.append([self.x1,self.y1 + i])
            elif self.y1 + i <8 and (turn == "White") and (chess_board[self.x1][self.y1 + i] in ["r'","n'","b'","q'","k'","p'"]):
                moves.append([self.x1,self.y1 + i])
                break
        for i in range(1,8):
            if self.x1 - i >=0 and (turn == "White") and (chess_board[self.x1 - i][self.y1] in [""]):
                moves.append([self.x1-i,self.y1])
            if self.x1 - i >=0 and (turn == "White") and (chess_board[self.x1 - i][self.y1] in ["r'","n'","b'","q'","k'","p'"]):
                moves.append([self.x1-i,self.y1])
                break
        for i in range(1,8):
            if self.y1 - i >=0 and (turn == "White") and (chess_board[self.x1][self.y1 - i] in [""]):
                moves.append([self.x1,self.y1 - i])
            if self.y1 - i >=0 and (turn == "White") and (chess_board[self.x1][self.y1 - i] in ["r'","n'","b'","q'","k'","p'"]):
                moves.append([self.x1,self.y1 - i])
                break
        #for black turn
        for i in range(1,8):
            if self.x1+i<8 and  (turn == "Black") and (chess_board[self.x1 + i][self.y1] in [""]):
                moves.append([self.x1+i,self.y1])
            elif self.x1+i<8 and  (turn == "Black") and (chess_board[self.x1 + i][self.y1] in ["r","n","b","q","k","p"]):
                moves.append([self.x1+i,self.y1+i])
                break
        for i in range(1,8):
            if self.y1 + i <8 and (turn == "Black") and (chess_board[self.x1][self.y1 + i] in [""]):
                moves.append([self.x1,self.y1 + i])
            elif self.y1 + i <8 and (turn == "Black") and (chess_board[self.x1][self.y1 + i] in ["r","n","b","q","k","p"]):
                moves.append([self.x1,self.y1 + i])
                break
        for i in range(1,8):
            if self.x1 - i >=0 and (turn == "Black") and (chess_board[self.x1 - i][self.y1] in [""]):
                moves.append([self.x1-i,self.y1])
            if self.x1 - i >=0 and (turn == "Black") and (chess_board[self.x1 - i][self.y1] in ["r","n","b","q","k","p"]):
                moves.append([self.x1-i,self.y1])
                break
        for i in range(1,8):
            if self.y1 - i >=0 and (turn == "Black") and (chess_board[self.x1][self.y1 - i] in [""]):
                moves.append([self.x1,self.y1 - i])
            if self.y1 - i >=0 and (turn == "Black") and (chess_board[self.x1][self.y1 - i] in ["r","n","b","q","k","p"]):
                moves.append([self.x1,self.y1 - i])
                break
        return moves

    def check_move(self,value,chess_board,turn):
        if value in self.posible_moves(chess_board,turn):
            self.first_move = False
            self.x1,self.y1 = value
            return True

class Bishop():
    def __init__(self,x,y,color):
        self.x1 = x
        self.y1 = y
        self.color = color

    def position(self):
        return [self.x1,self.y1]

    def posible_moves(self,chess_board,turn):
        moves = []
    #for white
        #up-right
        for  i in range(1,8):
            if self.x1 + i <8 and self.y1 + i <8 and turn == "White" and chess_board[self.x1+i][self.y1+i] in [""]:
                moves.append([self.x1+i,self.y1+i])
            elif self.x1 + i <8 and self.y1 <8 and turn == "White" and chess_board[self.x1+i][self.y1+i] in ["r'","n'","b'","q'","k'","p'"]:
                moves.append([self.x1+i,self.y1+i])
                break
        #up-left
        for  i in range(1,8):
            if self.x1 + i <8 and self.y1 - i >= 0 and turn == "White" and chess_board[self.x1+i][self.y1-i] in [""]:
                moves.append([self.x1+i,self.y1-i])
            elif self.x1 + i <8 and self.y1 - i >= 0 and turn == "White" and chess_board[self.x1+i][self.y1-i] in ["r'","n'","b'","q'","k'","p'"]:
                moves.append([self.x1+i,self.y1-i])
                break
        #down-right
        for  i in range(1,8):
            if self.x1 - i >= 0 and self.y1 + i <8 and turn == "White" and chess_board[self.x1-i][self.y1+i] in [""]:
                moves.append([self.x1-i,self.y1+i])
            elif self.x1 - i >= 0 and self.y1 <8 and turn == "White" and chess_board[self.x1-i][self.y1+i] in ["r'","n'","b'","q'","k'","p'"]:
                moves.append([self.x1-i,self.y1+i])
                break
        #down-left
        for  i in range(1,8):
            if self.x1 - i >= 0 and self.y1 - i >= 0 and turn == "White" and chess_board[self.x1-i][self.y1-i] in [""]:
                moves.append([self.x1-i,self.y1-i])
            elif self.x1 - i >= 0 and self.y1 - i >= 0 and turn == "White" and chess_board[self.x1-i][self.y1-i] in ["r'","n'","b'","q'","k'","p'"]:
                moves.append([self.x1-i,self.y1-i])
                break
    #for black
        #up-right
        for  i in range(1,8):
            if self.x1 + i <8 and self.y1 + i <8 and turn == "Black" and chess_board[self.x1+i][self.y1+i] in [""]:
                moves.append([self.x1+i,self.y1+i])
            elif self.x1 + i <8 and self.y1 <8 and turn == "Black" and chess_board[self.x1+i][self.y1+i] in ["r","n","b","q","k","p"]:
                moves.append([self.x1+i,self.y1+i])
                break
        #up-left
        for  i in range(1,8):
            if self.x1 + i <8 and self.y1 - i >= 0 and turn == "Black" and chess_board[self.x1+i][self.y1-i] in [""]:
                moves.append([self.x1+i,self.y1-i])
            elif self.x1 + i <8 and self.y1 - i >= 0 and turn == "Black" and chess_board[self.x1+i][self.y1-i] in ["r","n","b","q","k","p"]:
                moves.append([self.x1+i,self.y1-i])
                break
        #down-right
        for  i in range(1,8):
            if self.x1 - i >= 0 and self.y1 + i <8 and turn == "Black" and chess_board[self.x1-i][self.y1+i] in [""]:
                moves.append([self.x1-i,self.y1+i])
            elif self.x1 - i >= 0 and self.y1 <8 and turn == "Black" and chess_board[self.x1-i][self.y1+i] in ["r","n","b","q","k","p"]:
                moves.append([self.x1-i,self.y1+i])
                break
        #down-left
        for  i in range(1,8):
            if self.x1 - i >= 0 and self.y1 - i >= 0 and turn == "Black" and chess_board[self.x1-i][self.y1-i] in [""]:
                moves.append([self.x1-i,self.y1-i])
            elif self.x1 - i >= 0 and self.y1 - i >= 0 and turn == "Black" and chess_board[self.x1-i][self.y1-i] in ["r","n","b","q","k","p"]:
                moves.append([self.x1-i,self.y1-i])
                break
        return moves

    def check_move(self,value,chess_board,turn):
        if value in self.posible_moves(chess_board,turn):
            self.x1,self.y1 = value
            return True

class Queen():
    def __init__(self,x,y,color):
        self.x1 = x
        self.y1 = y
        self.color = color

    def position(self):
        return [self.x1,self.y1]

    def posible_moves(self,chess_board,turn):
        moves = []
        rookh_part = Rookh(self.x1,self.y1)
        moves.extend(rookh_part.posible_moves(chess_board,turn))
        bishop_part = Bishop(self.x1,self.y1)
        moves.extend(bishop_part(chess_board,turn))
        print(moves)
        return moves

    def check_move(self,value,chess_board,turn):
        if value in self.posible_moves(chess_board,turn):
            self.x1,self.y1 = value
            print("here")
            return True
    def check_ckeck(self,chess_board,turn):
        for pos in self.possible_moves(chess_board,turn):
            if (turn == "White" and chess_board[pos[0]][pos[1]] == "k'") or (turn == "Black" and chess_board[pos[0]][pos[1]] == "k"):
                print("check")

chess = Chess()
chess.start()
