# contine at casltling error if_under_check>queen_part>bishop_part> check_moves() returning - value for y
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
        self.chess_data = ["d2", "d4", "d7", "d6","g1", "f3", "g7", "g6","g2", "g3", "f8", "g7","f1", "g2", "b8", "c6","c2", "c3", "e7", "e5","d4", "e5", "d6", "e5","d1", "b3", "g8", "e7","c1", "g5", "h7", "h6","g5", "e3", "e8", "f8","e1", "g1", "a8", "b8","b1", "d2", "e7", "f5","e3", "c5", "f8", "e8","d8", "e4", "b7", "b6","c5", "b4", "c6", "b4","b3", "b4", "c7", "c5","b4", "b5", "c8", "b7","a1", "d1", "d8", "e7","e4", "d2", "e5", "e4","f3", "h4", "f5", "h4","g3", "h4", "e7", "h4","f2", "f3", "f8", "e5","h2", "h3", "e4", "e3","b5", "c4", "g7", "g3","e1", "f2", "g3", "f2","g1", "h1", "e3", "d2","c4", "d3", "f2", "e1","d1", "e1", "d2", "e1","g2", "f1", "e1", "f1"]


        self.pieces =[
            King(0,4,'white','k'),#0
            King(7,4,'black','k'),#1
            Queen(0,3,'white','q'),#2
            Queen(7,3,'black','q'),#3
            Knight(0,1,'white','n'),#4
            Knight(0,6,'white','n'),#5
            Knight(7,1,'black','n'),#6
            Knight(7,6,'black','n'),#7
            Bishop(0,5,'white','b'),#8
            Bishop(0,2,'white','b'),#9
            Bishop(7,5,'black','b'),#10
            Bishop(7,2,'black','b'),#11
            Rookh(0,0,'white','r'),#12
            Rookh(0,7,'white','r'),#13
            Rookh(7,0,'black','r'),#14
            Rookh(7,7,'black','r'),#15
            Pawn(1,0,'white','p'),#16
            Pawn(1,1,'white','p'),#17
            Pawn(1,2,'white','p'),#18
            Pawn(1,3,'white','p'),#19
            Pawn(1,4,'white','p'),#20
            Pawn(1,5,'white','p'),#21
            Pawn(1,6,'white','p'),#22
            Pawn(1,7,'white','p'),#23
            Pawn(6,0,'black','p'),#24
            Pawn(6,1,'black','p'),#25
            Pawn(6,2,'black','p'),#26
            Pawn(6,3,'black','p'),#27
            Pawn(6,4,'black','p'),#28
            Pawn(6,5,'black','p'),#29
            Pawn(6,6,'black','p'),#30
            Pawn(6,7,'black','p')]#31

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
        if False:
            try:
                x,y = self.txt_to_pos(input(txt))
                if (x and y) not in list(range(8)):
                    print("invalid input")
                    self.input_data()
            except:
                print("invalid input")
                self.input_data()
            else:
                return x,y
        if True:
            
            x,y = self.txt_to_pos(self.chess_data[0])
            print(x,y,self.chess_data[0])
            self.chess_data.pop(0)
            return x,y


    def under_check(self):
        danger_tiles=[]
        self.safe_tiles=[]
        self.blocking_moves = []
        print("CHECK!!")
        print("!")
        print()

        if self.turn == "white":
            for piece in self.pieces:
                
                try:
                    for (a,b) in piece.capture():
                        if self.chess_board[a][b] == "k" and piece.color == "black":
                            self.checks_by.append(["pawn",[piece.x,piece.y]])
                        
                except:
                    index = -1
                    for (a,b) in piece.check_moves():
                        index += 1
                        if self.chess_board[a][b] == "k" and piece.color == "black":
                            self.checks_by.append([piece.type,[piece.x,piece.y],piece.directions[index]])
                piece.reset_valid_moves()

            for data in self.checks_by:
                if data[0] == "p":
                    for piece in self.pieces:
                        if [piece.x,piece.y] == data[1]:
                            danger_tiles.extend(piece.capture())
                            piece.reset_valid_moves()
                else:
                    for piece in self.pieces:
                        if [piece.x,piece.y] == data[1]:
                            for i in range(len(piece.check_moves())):
                                if piece.directions[i] == data[2] and piece.valid_moves[i] not in danger_tiles:
                                    danger_tiles.append(piece.valid_moves[i])
                            piece.reset_valid_moves()

            
            # moving king out of check
            for moves in self.pieces[0].check_moves():
                if moves not in danger_tiles and self.chess_board[moves[0]][moves[1]] not in ["r","n","b","q","p"]:
                    self.safe_tiles.append(moves)
            self.pieces[0].reset_valid_moves()
            # blocking the check by moving other pieces
            for piece in self.pieces:
                if piece.color == "white" and piece.type != "k":
                    for moves in piece.check_moves():
                        if moves in danger_tiles:
                            self.blocking_moves.append(moves)
                if piece.color == "white" and piece.type == "p":
                    for moves in piece.capture():
                        if moves in danger_tiles:
                            if self.chess_board[moves[0]][moves[1]] in ["r'","n'","b'","q'","p'"]:
                                self.blocking_moves.append(moves)
                piece.reset_valid_moves()
        
        if self.turn == "black":
            for piece in self.pieces:
                
                try:
                    for (a,b) in piece.capture():
                        if self.chess_board[a][b] == "k'" and piece.color == "white":
                            self.checks_by.append(["pawn",[piece.x,piece.y]])
                        
                except:
                    index = -1
                    for (a,b) in piece.check_moves():
                        index += 1
                        if self.chess_board[a][b] == "k'" and piece.color == "white":
                            try:
                                self.checks_by.append([piece.type,[piece.x,piece.y],piece.directions[index]])
                            except:
                                self.checks_by.append([piece.type,[piece.x,piece.y],None])
                piece.reset_valid_moves()

            for data in self.checks_by:
                if data[0] == "p":
                    for piece in self.pieces:
                        if [piece.x,piece.y] == data[1]:
                            danger_tiles.extend(piece.capture())
                            piece.reset_valid_moves()
                else:
                    for piece in self.pieces:
                        if [piece.x,piece.y] == data[1]:
                            for i in range(len(piece.check_moves())):
                                print(i)
                                try:
                                    if piece.directions[i] == data[2] and piece.valid_moves[i] not in danger_tiles:
                                        danger_tiles.append(piece.valid_moves[i])
                                except:
                                    if piece.valid_moves[i] not in danger_tiles:
                                        danger_tiles.append(piece.valid_moves[i])
                        piece.reset_valid_moves()
            # moving king out of check
            for moves in self.pieces[1].check_moves():
                if moves not in danger_tiles and self.chess_board[moves[0]][moves[1]] not in ["r'","n'","b'","q'","p'"]:
                    self.safe_tiles.append(moves)
            self.pieces[1].reset_valid_moves()
            # blocking the check by moving other pieces
            for piece in self.pieces:
                if piece.color == "black" and piece.type != "k":
                    for moves in piece.check_moves():
                        if moves in danger_tiles:
                            self.blocking_moves.append(moves)
                if piece.color == "black" and piece.type == "p" :
                    for moves in piece.capture():
                        if moves in danger_tiles:
                            if self.chess_board[moves[0]][moves[1]] in ["r","n","b","q","p"]:
                                self.blocking_moves.append(moves)
                piece.reset_valid_moves()

        print("danger",danger_tiles)
        print("block",self.blocking_moves)
        print("safe",self.safe_tiles)

        if len(self.safe_tiles+self.blocking_moves) == 0:
            print("CHECKMATE!!")
            if self.turn == "white":
                print("Black wins")
                self.black_win = True
            elif self.turn == "black":
                print("White wins")
                self.white_win = True
            self.loopbraker = True
            self.loopcontinuer = True
                


    
        
            
#----------------------------------------MAIN----------------------------------------#
    def start_game(self):
        print()

        self.checks =[]
        self.checks_by = [] #[type,piece,direction]
        while (self.white_win and self.black_win) == False:
            print("no of self.checks",len(self.checks))

            # update chess_board for the pieces 
            for piece in self.pieces:
                piece.update_chess_board(self.chess_board)

            self.loopbraker = False
            self.loopcontinuer = False
            caputre_move = False

            #check moves
            if len(self.checks) > 0:
                self.under_check()
                if self.loopbraker:
                    break
            
            print(f"{self.turn}'s turn")
            self.print_board()

            self.x1,self.y1 = self.input_data("enter the position of the piece that you want to select: ")
            if (self.turn == "white" and self.chess_board[self.x1][self.y1] not in ["r","n","b","q","k","p"]) or (self.turn == "black" and self.chess_board[self.x1][self.y1] not in ["r'","n'","b'","q'","k'","p'"]):
                print("please select your own piece, Try again!")
                break
                continue
            # ERROR : selected blank space
            if self.chess_board[self.x1][self.y1] == '':
                print("No piece at the position, Try again!")
                break
                continue

            self.x2,self.y2 = self.input_data("enter the position where you want to move/caputre: ")
            
            # Error : cannot capture your piece
            if (self.turn == "white" and self.chess_board[self.x2][self.y2] in ["r","n","b","q","k","p"]) or (self.turn == "black" and self.chess_board[self.x2][self.y2] in ["r'","n'","b'","q'","k'","b'","n'","r'"]):
                print("Invalid move: Can not capture your own piece, Try again!")
                break
                continue 
            
            #capture
            if ((self.turn == "white" and self.chess_board[self.x2][self.y2] in ["q'","b'","n'","r'","p'"]) or (self.turn == "black" and self.chess_board[self.x2][self.y2] in ["q","b","n","r","p"])):
                caputre_move = True
                print("capture")

            #normal move
            else:
                print("normal move")

            if len(self.checks) == 0:
                index = -1
                
                # en passant
                #white
                if self.turn == "white":
                    for white_piece in list(self.pieces)[16:24]:
                        if self.x1 == 4 and [self.x1,self.y1] == [white_piece.x,white_piece.y]:
                            for i in range(-1,2):
                                if self.x2 == 5 and self.y1+i in list(range(8)) and self.y1+i == self.y2:
                                    for black_piece in self.pieces:
                                        if type(black_piece) == Pawn and black_piece.color == "black":
                                            if [black_piece.x,black_piece.y] == [4,self.y2] and black_piece.en_passant_var == 1:
                                                white_piece.move(self.x2,self.y2)
                                                self.chess_board[self.x1][self.y1],self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y2] = "","p",""
                #black
                elif self.turn == "black":
                    for black_piece in list(self.pieces)[24:32]:
                        if self.x1 == 3 and [self.x1,self.y1] == [black_piece.x,black_piece.y]:
                            for i in range(-1,2):
                                if self.x2 == 2 and self.y1+i in list(range(8)) and self.y1+i == self.y2:
                                    for white_piece in self.pieces:
                                        if type(white_piece) == Pawn and black_piece.color == "white":
                                            if [white_piece.x,white_piece.y] == [3,self.y2] and white_piece.en_passant_var == 1:
                                                black_piece.move(self.x2,self.y2)
                                                self.chess_board[self.x1][self.y1],self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y2] = "","p'",""
                                    
                # castling 
                if self.pieces[0].first_move and self.pieces[0].x == self.x1 and self.pieces[0].y == self.y1:
                    if  self.pieces[12].first_move and  (self.chess_board[0][1],self.chess_board[0][2],self.chess_board[0][3]) == ("","","")  and [self.x2,self.y2] == [0,2]:
                        temp_var1 = King(0,1,"white",'k')
                        temp_var2 = King(0,2,"white",'k')
                        temp_var3 = King(0,3,"white",'k')
                        temp_var1.update_chess_board(self.chess_board)
                        temp_var2.update_chess_board(self.chess_board)
                        temp_var3.update_chess_board(self.chess_board)
                        templist_ = []
                        templist_.extend(temp_var1.if_under_check())
                        templist_.extend(temp_var2.if_under_check())
                        templist_.extend(temp_var3.if_under_check())
                        if len(templist_) == 0:
                            self.chess_board[0][0],self.chess_board[0][1],self.chess_board[0][2],self.chess_board[0][3],self.chess_board[0][4] = "","","k","r",""
                            self.pieces[0].move(0,2)
                            self.pieces[12].move(0,3)
                            self.toogle_turn()
                            self.loopcontinuer = True

                    elif  self.pieces[13].first_move and (self.chess_board[0][5],self.chess_board[0][6]) == ("","")  and [self.x2,self.y2] == [0,6]:
                        temp_var1 = King(0,5,"white",'k')
                        temp_var2 = King(0,6,"white",'k')
                        temp_var1.update_chess_board(self.chess_board)
                        temp_var2.update_chess_board(self.chess_board)
                        templist_ = []
                        templist_.extend(temp_var1.if_under_check())
                        templist_.extend(temp_var2.if_under_check())
                        if len(templist_) == 0:
                            self.chess_board[0][4],self.chess_board[0][5],self.chess_board[0][6],self.chess_board[0][7] = "","r","k",""
                            self.pieces[0].move(0,6)
                            self.pieces[13].move(0,5)
                            self.toogle_turn()
                            self.loopcontinuer = True

                elif self.pieces[1].first_move and self.pieces[1].x == self.x1 and self.pieces[1].y == self.y1:
                    if  self.pieces[14].first_move and  (self.chess_board[7][1],self.chess_board[7][2],self.chess_board[7][3]) == ("","","")  and [self.x2,self.y2] == [7,2]:
                        temp_var1 = King(7,1,"black",'k')
                        temp_var2 = King(7,2,"black",'k')
                        temp_var3 = King(7,3,"black",'k')
                        temp_var1.update_chess_board(self.chess_board)
                        temp_var2.update_chess_board(self.chess_board)
                        temp_var3.update_chess_board(self.chess_board)
                        templist_ = []
                        templist_.extend(temp_var1.if_under_check())
                        print(templist_)
                        templist_.extend(temp_var2.if_under_check())
                        print(templist_)
                        templist_.extend(temp_var3.if_under_check())
                        print(templist_)
                        temp_var1.reset_valid_moves()
                        temp_var2.reset_valid_moves()
                        temp_var3.reset_valid_moves()
                        if len(templist_) == 0:
                            self.chess_board[7][0],self.chess_board[7][1],self.chess_board[7][2],self.chess_board[7][3],self.chess_board[7][4] = "","","k'","r'",""
                            self.pieces[1].move(7,2)
                            self.pieces[14].move(7,3)
                            self.toogle_turn()
                            self.loopcontinuer = True

                    elif  self.pieces[15].first_move and (self.chess_board[7][5],self.chess_board[7][6]) == ("","")  and [self.x2,self.y2] == [7,6]:
                        temp_var1 = King(7,5,"black",'k')
                        temp_var2 = King(7,6,"black",'k')
                        temp_var1.update_chess_board(self.chess_board)
                        temp_var2.update_chess_board(self.chess_board)
                        templist_ = []
                        templist_.extend(temp_var1.if_under_check())
                        templist_.extend(temp_var2.if_under_check())
                        if len(templist_) == 0:
                            self.chess_board[7][4],self.chess_board[7][5],self.chess_board[7][6],self.chess_board[7][7] = "","r'","k'",""
                            self.pieces[1].move(7,6)
                            self.pieces[15].move(7,5)
                            self.toogle_turn()
                            self.loopcontinuer = True



                        

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
                                    self.loopcontinuer = True
                                    break
                                self.toogle_turn()

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
                                break
                            self.toogle_turn()

                        else:
                            print("invalid Move!")
                            print(self.pieces[index].valid_moves)

                        if self.turn == "white":
                            self.checks.extend(self.pieces[0].if_under_check())
                        elif self.turn == "black":
                            self.checks.extend(self.pieces[1].if_under_check())
                        
                        break
                self.loopcontinuer = True

            if self.loopcontinuer:
                continue
            if self.loopbraker:
                break

            #check moves
            if len(self.checks) > 0:

                for piece in self.pieces:   
                    if [piece.x,piece.y] == [self.x1,self.y1] and [self.x2,self.y2] in self.blocking_moves:
                        print([self.x2,self.y2])
                        if caputre_move and self.chess_board[self.x2][self.y2] != "" and type(self.piece) == Pawn:
                            if [self.x2,self.y2] in piece.capture():
                                print(piece.valid_moves)
                                print("capture move")
                                templist = self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1]
                                self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = self.chess_board[self.x1][self.y1],''
                                piece.move(self.x2,self.y2)
                                if (self.turn == "white" and len(self.pieces[0].if_under_check())>0) or (self.turn == "black" and len(self.pieces[1].if_under_check())>0):
                                    print("invalid move! moving this piece will put your king under check")
                                    self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = templist
                                    piece.move(self.x1,self.y1)
                                    self.loopcontinuer = True
                                    break
                                self.toogle_turn()
                                #self.loopbraker = True
                        elif [self.x2,self.y2] in self.pieces[index].check_moves():
                            print(piece.valid_moves)
                            print("valid move")
                            templist = self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1]
                            self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = self.chess_board[self.x1][self.y1],''
                            piece.move(self.x2,self.y2)
                            if (self.turn == "white" and len(self.pieces[0].if_under_check())>0) or (self.turn == "black" and len(self.pieces[1].if_under_check())>0):
                                print("invalid move! moving this piece will put your king under check")
                                self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = templist
                                piece.move(self.x1,self.y1)
                                break
                            self.toogle_turn()

                    elif piece.type == "k" and [self.x2,self.y2] in self.safe_tiles:
                        templist = self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1]
                        self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = self.chess_board[self.x1][self.y1],''
                        piece.move(self.x2,self.y2)
                        if (self.turn == "white" and len(self.pieces[0].if_under_check())>0) or (self.turn == "black" and len(self.pieces[1].if_under_check())>0):
                            print("invalid move! moving this piece will put your king under check")
                            self.chess_board[self.x2][self.y2],self.chess_board[self.x1][self.y1] = templist
                            piece.move(self.x1,self.y1)
                            break
                        self.toogle_turn()

                    self.checks = []
                    self.checks_by = []

                    if self.turn == "white":
                        self.checks.extend(self.pieces[0].if_under_check())
                    elif self.turn == "black":
                        self.checks.extend(self.pieces[1].if_under_check())
                    
            
            if self.loopcontinuer:
                continue
            if self.loopbraker:
                break

                  

#----------------------------------------PIECES----------------------------------------#
class Piece():
    def __init__(self,x,y,color,type_):
        self.type = type_
        self.x = x
        self.y = y
        self.color = color
        self.first_move = True
        self.valid_moves = []
        self.directions = []
        self.chess_board = []
        self.under_check = False

    def reset_valid_moves(self):
        self.valid_moves = []


    def move(self,x,y):
        self.x,self.y = x,y
        self.reset_valid_moves()
        self.first_move = False
    def update_chess_board(self,chess_board):
        self.chess_board = chess_board

class King(Piece):

    def check_moves(self):
        for i in range(-1,2):
            for j in range(-1,2):
                if self.x + i in list(range(8)) and self.y + j in list(range(8)):
                    self.valid_moves.append([self.x+i,self.y+j])
        return self.valid_moves


    def if_under_check(self):
        
        rookh_part = Rookh(self.x,self.y,self.color,'r')
        bishop_part = Bishop(self.x,self.y,self.color,'b')
        knight_part = Knight(self.x,self.y,self.color,'n')
        pawn_part = Pawn(self.x,self.y,self.color,'p')

        rookh_part.update_chess_board(self.chess_board)
        bishop_part.update_chess_board(self.chess_board)
        knight_part.update_chess_board(self.chess_board)
        pawn_part.update_chess_board(self.chess_board)

        check_by_rookh = False
        check_by_bishop = False
        check_by_knight = False
        check_by_pawn = False
        check_by_queen = False

        self.rookh_moves = rookh_part.check_moves()
        self.bishop_moves = bishop_part.check_moves()
        self.knight_moves = knight_part.check_moves()
        self.pawn_moves = pawn_part.capture()
        rookh_part.reset_valid_moves()
        bishop_part.reset_valid_moves()
        knight_part.reset_valid_moves()
        pawn_part.reset_valid_moves()
        self.queen_moves = self.rookh_moves + self.bishop_moves
        self.all_moves = self.queen_moves + self.knight_moves + self.pawn_moves

        if self.color == "white":
            for a,b in self.knight_moves:
                try:
                    if self.chess_board[a][b] == "n'" and a in list(range(8)) and list(range(8)):
                        self.knight_pos =[a,b]
                        check_by_knight = True
                except:
                    pass 
            for a,b in self.pawn_moves:
                if self.chess_board[a][b] == "p'" and a in list(range(8)) and b in list(range(8)):
                    self.pawn_pos = [a,b]
                    check_by_pawn = True
            for a,b in self.queen_moves:
                if self.chess_board[a][b] == "q'" and a in list(range(8)) and b in list(range(8)):
                    self.queen_pos = [a,b]
                    check_by_queen = True
            for a,b in self.rookh_moves:
                if self.chess_board[a][b] == "r'" and a in list(range(8)) and b in list(range(8)):
                    self.rookh_pos=[a,b]
                    check_by_rookh = True
            for a,b in self.bishop_moves:
                if self.chess_board[a][b] == "b'" and a in list(range(8)) and b in list(range(8)):
                    self.bishop_pos = [a,b]
                    check_by_bishop = True
            
        if self.color == "black":
            for a,b in self.knight_moves:
                try:
                    if self.chess_board[a][b] == "n" and a in list(range(8)) and b in list(range(8)):
                        self.knight_pos = [a,b]
                        check_by_knight = True
                except:
                    pass
            for a,b in self.pawn_moves:
                if self.chess_board[a][b] == "p" and a in list(range(8)) and b in list(range(8)):
                    self.pawn_pos = [a,b]
                    check_by_pawn = True
            for a,b in self.queen_moves:
                if self.chess_board[a][b] == "q" and a in list(range(8)) and b in list(range(8)):
                    self.queen_pos = [a,b]
                    print([a,b])
                    check_by_queen = True
            for a,b in self.rookh_moves:
                if self.chess_board[a][b] == "r" and a in list(range(8)) and b in list(range(8)):
                    self.rookh_pos = [a,b]
                    check_by_rookh = True
            for a,b in self.bishop_moves:
                if self.chess_board[a][b] == "b" and a in list(range(8)) and b in list(range(8)):
                    self.bishop_pos = [a,b]
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

class Queen(Piece):

    def check_moves(self):
        rookhpart = Rookh(self.x,self.y,self.color,'r')
        bishoppart = Bishop(self.x,self.y,self.color,'b')
        rookhpart.update_chess_board(self.chess_board),bishoppart.update_chess_board(self.chess_board)
        self.valid_moves.extend(rookhpart.check_moves())
        self.directions.extend(rookhpart.directions)
        self.valid_moves.extend(bishoppart.check_moves())
        self.directions.extend(bishoppart.directions)
        return self.valid_moves

class Rookh(Piece):

    def check_moves(self):
        #up moves
        for i in range(1,8):
            try:
                if self.x + i in list(range(8)) and self.chess_board[self.x+i][self.y] == '':
                    self.valid_moves.append([self.x+i,self.y])
                    self.directions.append("up")
                elif self.x + i in list(range(8)) and self.color == "white" and self.chess_board[self.x+i][self.y] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x+i][self.y] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x+i,self.y])
                    self.directions.append("up")
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
                    self.directions.append("down")
                elif self.x - i in list(range(8)) and self.color == "white" and self.chess_board[self.x-i][self.y] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x-i][self.y] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x-i,self.y])
                    self.directions.append("down")
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
                    self.directions.append("right")
                elif self.y + i in list(range(8)) and self.color == "white" and self.chess_board[self.x][self.y+i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x][self.y+i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x,self.y+i])
                    self.directions.append("right")
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
                    self.directions.append("left")
                elif self.y - i in list(range(8)) and self.color == "white" and self.chess_board[self.x][self.y-i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x][self.y-i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x,self.y-i])
                    self.directions.append("left")
                    break
                else:
                    break
            except:
                break

        return self.valid_moves

class Knight(Piece):

    def check_moves(self):
        if self.x+2 in list(range(8)) and self.y+1 in list(range(8)):
            self.valid_moves.append([self.x+2,self.y+1])
            self.directions.append("up-right")
        if self.x+2 in list(range(8)) and self.y-1 in list(range(8)):
            self.valid_moves.append([self.x+2,self.y-1])
            self.directions.append("up-left")
        if self.x-2 in list(range(8)) and self.y+1 in list(range(8)):
            self.valid_moves.append([self.x-2,self.y+1])
            self.directions.append("down-right")
        if self.x-2 in list(range(8)) and self.y-1 in list(range(8)):
            self.valid_moves.append([self.x-2,self.y-1])
            self.directions.append("down-left")
        if self.x+1 in list(range(8)) and self.y+2 in list(range(8)):
            self.valid_moves.append([self.x+1,self.y+2])
            self.directions.append("right-up")
        if self.x+1 in list(range(8)) and self.y-2 in list(range(8)):
            self.valid_moves.append([self.x+1,self.y-2])
            self.directions.append("left-up")
        if self.x-1 in list(range(8)) and self.y+2 in list(range(8)):
            self.valid_moves.append([self.x-1,self.y+2])
            self.directions.append("right-down")
        if self.x-1 in list(range(8)) and self.y-2 in list(range(8)):
            self.valid_moves.append([self.x-1,self.y-2])
            self.directions.append("left-down")

        return self.valid_moves


class Bishop(Piece):

    def check_moves(self):
        # up-right moves
        for i in range(1,8):
            try:
                if (self.x + i in list(range(8)) and self.y + i in list(range(8))) and (self.chess_board[self.x+i][self.y+i] == ''):
                    self.valid_moves.append([self.x+i,self.y+i])
                    self.directions.append("up-right")
                elif (self.x + i in list(range(8)) and self.y + i in list(range(8))) and self.color == "white" and self.chess_board[self.x+i][self.y+i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x+i][self.y+i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x+i,self.y+i])
                    self.directions.append("up-right")
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
                    self.directions.append("up-left")
                elif (self.x + i in list(range(8)) and self.y - i in list(range(8))) and  self.color == "white" and self.chess_board[self.x+i][self.y-i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x+i][self.y-i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x+i,self.y-i])
                    self.directions.append("up-left")
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
                    self.directions.append("down-right")
                elif (self.x - i in list(range(8)) and self.y + i in list(range(8))) and self.color == "white" and self.chess_board[self.x-i][self.y+i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x-i][self.y+i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x-i,self.y+i])
                    self.directions.append("down-right")
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
                    self.directions.append("down-left")
                elif (self.x - i in list(range(8)) and self.y - i in list(range(8))) and self.color == "white" and self.chess_board[self.x-i][self.y-i] in ["r'","n'","b'","q'","k'","p'"] or self.color == "black" and self.chess_board[self.x-i][self.y-i] in ["r","n","b","q","k","p"]:
                    self.valid_moves.append([self.x-i,self.y-i])
                    self.directions.append("down-left")
                    break
                else:
                    break
            except:
                break

        return self.valid_moves


class Pawn(Piece):

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


chess = Chess()
chess.start_game()
