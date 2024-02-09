from tkinter import *
import textwrap

class MyApp():
    def __init__(self, root, color1,color2,cs1,cs2):
        self.firstaiclick=True
        self.firstclick=True
        self.cs1=cs1
        self.cs2=cs2
        self.root = root
        root.title("ChessBoard")
        self.root.configure(background='grey20')
        self.root_center(1260,640)
        root.resizable(False, False)
        self.size = 60
        self.rows=8
        self.columns=8
        self.create_canvas()
        self.counter = 1
        self.aicounter = 1
        f=open('GAME_OPTIONS.txt','r', encoding = 'utf-8')
        datas=[]
        for x in f:
           datas.append(x)
        self.p1n=datas[0]
        self.p2n=datas[2]
        self.p1n='\n'.join(textwrap.wrap(self.p1n,10))
        self.p2n='\n'.join(textwrap.wrap(self.p2n,10))
        self.images()
        self.imagemove = 0
        self.aiimagemove = 0
        self.changingpawn=0
        self.imagedel = 0
        self.aiimagedel = 0
        self.greenrectli=[]
        self.positions = {}
        self.userscore = 0
        self.aiscore = 0
        self.chess_score(root)
        self.position()   
        self.color1=color1
        self.color2=color2
        self.what_happened = "ai played"
        self.symbols = "PRNBQK"
        self.pieces = {}
        for i in range(8, 0, -1):
            for z in range(8, 0, -1):
                self.pieces["({},{})".format(i, z)] = ' '
        for s in self.symbols:
            if s == "P":
                for i in range(1,9):
                    p1 = Piece(s, self.color1,"(2,{})".format(i), 100)
                    self.pieces[p1.position] = p1
                for i in range(1,9):
                    p2= Piece(s, self.color2,"(7,{})".format(i), 100)
                    self.pieces[p2.position] = p2
            if s == "R":
                for i in range(1,9,7):
                    p1 = Piece(s, self.color1,"(1,{})".format(i), 300)
                    self.pieces[p1.position] = p1
                for i in range(1,9,7):
                    p2 = Piece(s, self.color2,"(8,{})".format(i), 300)
                    self.pieces[p2.position] = p2
            if s == "N":
                for i in range(2,8,5):
                    p1 = Piece(s, self.color1,"(1,{})".format(i), 300)
                    self.pieces[p1.position] = p1
                for i in range(2,8,5):
                    p2 = Piece(s, self.color2,"(8,{})".format(i), 300)
                    self.pieces[p2.position] = p2
            if s == "B":
                for i in range(3,7,3):
                    p1 = Piece(s, self.color1,"(1,{})".format(i), 500)
                    self.pieces[p1.position] = p1
                for i in range(3,7,3):
                    p2 = Piece(s, self.color2,"(8,{})".format(i), 500)
                    self.pieces[p2.position] = p2
            if s == "Q":
                p1 = Piece(s, self.color1,"(1,5)", 900)
                p2 = Piece(s, self.color2,"(8,5)", 900)
                self.pieces[p1.position] = p1
                self.pieces[p2.position] = p2
            if s == "K":
                p1 = Piece(s, self.color1,"(1,4)", 5000)
                p2 = Piece(s, self.color2,"(8,4)", 5000)
                self.pieces[p1.position] = p1
                self.pieces[p2.position] = p2

    def root_center(self,r,e):
        width_of_window=r
        height_of_window=e
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width_of_window/2)
        y_coordinate=(screen_height/2)-(height_of_window/2)
        self.root.geometry('%dx%d+%d+%d' % (width_of_window,height_of_window,x_coordinate,y_coordinate))

####################################################  CHESS SCORE  #############################################################

    def chess_score(self,root):
        self.f1=Frame(root,bg='grey50')
        self.f1.grid(row=0,column=1)
       
        v3=StringVar()
        self.curscor2=Label(self.f1,textvariable=v3,font='Arial 20 bold',bg='red',fg='white')
        self.curscor2.grid(row=2,column=2,padx=4,pady=4)
        v3.set(self.cs2)
                           
        self.nam1=Label(self.f1,text=self.p2n,font='Arial 20 bold',bg='grey10',fg='white')
        self.nam1.grid(row=0,column=1,padx=4)
        self.guide2=Label(self.f1,text='right\nclick',font='Arial 15 bold',bg='grey10',fg='white')
        self.guide2.grid(row=0,column=0,padx=4)

        v4=StringVar()
        self.curscor1=Label(self.f1,textvariable=v4,font='Arial 20 bold',bg='red',fg='white')
        self.curscor1.grid(row=2,column=3,padx=4)
        v4.set(self.cs1)
       
        self.nam2=Label(self.f1,text=self.p1n,font='Arial 20 bold',bg='grey90',fg='black')
        self.nam2.grid(row=0,column=4,padx=4)
        self.guide1=Label(self.f1,text='left\nclick',font='Arial 15 bold',bg='grey90',fg='black')
        self.guide1.grid(row=0,column=5,padx=4)

        v1=StringVar()
        self.sc1=Label(self.f1,textvariable=v1,font='Arial 30 bold',bg='grey50',fg='black')
        self.sc1.grid(row=2,column=1,pady=4)
        v1.set(self.userscore)
       
        v2=StringVar()
        self.sc2=Label(self.f1,textvariable=v2,font='Arial 30 bold',bg='grey50',fg='black')
        self.sc2.grid(row=2,column=4,pady=4)
        v2.set(self.aiscore)

        self.clock2=Label(self.f1,text='120',font='arial 18 bold')
        self.clock2.grid(row=2,column=5,padx=10)
       
        self.remaining1 = 0
        self.remaining2 = 0
        self.remaining3 = 0
        self.remaining4 = 0

        self.countdown2(120)

######################################################  CHESS TIMER  ###########################################################

    def countdown1(self, remaining1 = None):
        if remaining1 is not None:
            self.remaining1 = remaining1
        if self.remaining1 <= 0:
            self.userscore+=5000
            self.game_ends()
        else:
            self.clock1.configure(text="%d" % self.remaining1)
            self.remaining1 = self.remaining1 - 1
            self.clock1.after(1000, self.countdown1)

    def countdown2(self, remaining2 = None):
        if remaining2 is not None:
            self.remaining2 = remaining2
        if self.remaining2 <= 0:
            self.aiscore+=5000
            self.game_ends()
        else:
            self.clock2.configure(text="%d" % self.remaining2)
            self.remaining2 = self.remaining2 - 1
            self.clock2.after(1000, self.countdown2)

    def countdown3(self, remaining3 = None):
        if remaining3 is not None:
            self.remaining3 = remaining3
        if self.remaining3 <= 0:
            self.userscore+=5000
            self.game_ends()
        else:
            self.clock3.configure(text="%d" % self.remaining3)
            self.remaining3 = self.remaining3 - 1
            self.clock3.after(1000, self.countdown3)

    def countdown4(self, remaining4 = None):
        if remaining4 is not None:
            self.remaining4 = remaining4
        if self.remaining4 <= 0:
            self.aiscore+=5000
            self.game_ends()
        else:
            self.clock4.configure(text="%d" % self.remaining4)
            self.remaining4 = self.remaining4 - 1
            self.clock4.after(1000, self.countdown4)


#########################################################  CANVAS  #############################################################
           
    def create_canvas(self):
        canvas_width = (self.columns+2) * self.size
        canvas_height = (self.rows+2) * self.size
        self.canvas =Canvas(self.root, width=canvas_width, height=canvas_height, background="brown")
        self.canvas.grid(row=0,column=0,padx=20, pady=20)
        color = 'royalblue'
        for r in range(0,self.rows):
            if color == 'royalblue':
                color = "white"
            else:
                color='royalblue'
            for c in range(1,self.columns+1):
                x1 = (c * self.size)
                y1 = ((8-r) * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="area")
                if color == 'royalblue':
                    color = "white"
                else:
                    color='royalblue'   
        self.canvas.bind("<Button-3>", self.black_play )
        self.canvas.bind("<Button-1>",self.white_play )
        self.root.bind("<Key-Escape>", self.menu)      

########################################################  MOVEMENT  ############################################################
   
    def white_play(self, event):
        if self.what_happened == "ai played":    
            if self.firstaiclick==True:
                self.clock2.destroy()
                self.clock4=Label(self.f1,text='120',font='arial 18 bold')
                self.clock4.grid(row=2,column=5,padx=10)
                self.countdown4(self.remaining2)
            if self.counter % 2 != 0:
                self.fx, self.fy = event.x, event.y
                self.positionx, self.positiony = self.fx//self.size, self.fy//self.size
                self.colorpossmoves(self.positiony,self.positionx,'"white"')
                self.firstaiclick=False
                if self.positions[(self.positiony, self.positionx)] != ' ':
                    if self.positions[(self.positiony, self.positionx)] == 'wP1': self.aiimagemove = self.pawnW1
                    if self.positions[(self.positiony, self.positionx)] == 'wP2': self.aiimagemove = self.pawnW2
                    if self.positions[(self.positiony, self.positionx)] == 'wP3': self.aiimagemove = self.pawnW3
                    if self.positions[(self.positiony, self.positionx)] == 'wP4': self.aiimagemove = self.pawnW4
                    if self.positions[(self.positiony, self.positionx)] == 'wP5': self.aiimagemove = self.pawnW5
                    if self.positions[(self.positiony, self.positionx)] == 'wP6': self.aiimagemove = self.pawnW6
                    if self.positions[(self.positiony, self.positionx)] == 'wP7': self.aiimagemove = self.pawnW7
                    if self.positions[(self.positiony, self.positionx)] == 'wP8': self.aiimagemove = self.pawnW8
                    if self.positions[(self.positiony, self.positionx)] == 'wR1': self.aiimagemove = self.rookW1
                    if self.positions[(self.positiony, self.positionx)] == 'wN1': self.aiimagemove = self.knightW1
                    if self.positions[(self.positiony, self.positionx)] == 'wB1': self.aiimagemove = self.bishopW1
                    if self.positions[(self.positiony, self.positionx)] == 'wQ': self.aiimagemove = self.queenW
                    if self.positions[(self.positiony, self.positionx)] == 'wK': self.aiimagemove = self.kingW
                    if self.positions[(self.positiony, self.positionx)] == 'wB2': self.aiimagemove = self.bishopW2
                    if self.positions[(self.positiony, self.positionx)] == 'wN2': self.aiimagemove = self.knightW2
                    if self.positions[(self.positiony, self.positionx)] == 'wR2': self.aiimagemove = self.rookW2
                    if self.positions[(self.positiony, self.positionx)] == 'wQ2': self.aiimagemove = self.queenW2
                    if self.positions[(self.positiony, self.positionx)] == 'wQ3': self.aiimagemove = self.queenW3
                    if self.positions[(self.positiony, self.positionx)] == 'wB3': self.aiimagemove = self.bishopW3
                    if self.positions[(self.positiony, self.positionx)] == 'wR3': self.aiimagemove = self.rookW3
                    if self.positions[(self.positiony, self.positionx)] == 'wN3': self.aiimagemove = self.knightW3
                    if self.positions[(self.positiony, self.positionx)] == 'wQ4': self.aiimagemove = self.queenW4
                    if self.positions[(self.positiony, self.positionx)] == 'wB4': self.aiimagemove = self.bishopW4
                    if self.positions[(self.positiony, self.positionx)] == 'wR4': self.aiimagemove = self.rookW4
                    if self.positions[(self.positiony, self.positionx)] == 'wN4': self.aiimagemove = self.knightW4
                    if self.positions[(self.positiony, self.positionx)] == 'wQ5': self.aiimagemove = self.queenW5
                    if self.positions[(self.positiony, self.positionx)] == 'wB5': self.aiimagemove = self.bishopW5
                    if self.positions[(self.positiony, self.positionx)] == 'wR5': self.aiimagemove = self.rookW5
                    if self.positions[(self.positiony, self.positionx)] == 'wN5': self.aiimagemove = self.knightW5
                    if self.positions[(self.positiony, self.positionx)] == 'wQ6': self.aiimagemove = self.queenW6
                    if self.positions[(self.positiony, self.positionx)] == 'wB6': self.aiimagemove = self.bishopW6
                    if self.positions[(self.positiony, self.positionx)] == 'wR6': self.aiimagemove = self.rookW6
                    if self.positions[(self.positiony, self.positionx)] == 'wN6': self.aiimagemove = self.knightW6
                    if self.positions[(self.positiony, self.positionx)] == 'wQ7': self.aiimagemove = self.queenW7
                    if self.positions[(self.positiony, self.positionx)] == 'wB7': self.aiimagemove = self.bishopW7
                    if self.positions[(self.positiony, self.positionx)] == 'wR7': self.aiimagemove = self.rookW7
                    if self.positions[(self.positiony, self.positionx)] == 'wN7': self.aiimagemove = self.knightW7
                else:
                    print("Try again")
                    self.counter-=1
            if self.counter % 2 == 0:
                self.canvas.delete('greenrect')
                self.destx, self.desty = event.x//self.size, event.y//self.size
                if (self.destx > 1 and self.desty > 1) or (self.destx < 9 and self.desty < 9):
                    if '{}{}'.format(self.destx, self.desty) in self.greenrectli:
                        if self.targetisvalid(self.desty, self.destx, self.positiony, self.positionx):
                            dx, dy = self.destx - self.positionx, self.desty - self.positiony 
                            self.canvas.move(self.aiimagemove, dx*self.size, dy*self.size)
                            self.pieces["({},{})".format(self.desty, self.destx)] = self.pieces["({},{})".format(self.positiony, self.positionx)]
                            self.pieces["({},{})".format(self.positiony, self.positionx)] = ' '
                            self.positions[(self.desty, self.destx)] = str(self.positions[(self.positiony, self.positionx)])
                            self.positions[(self.positiony, self.positionx)] = ' '
                            if self.desty==8 and self.positions[(self.desty, self.destx)][:2] =='wP':
                                self.changingpawn=self.aiimagemove
                                self.pawn_change_white()
                            self.firstaiclick=True
                            self.what_happened = "human played"
                            self.clock4.destroy()
                            self.clock1=Label(self.f1,text='120',font='arial 18 bold')
                            self.clock1.grid(row=2,column=0,padx=10)
                            self.countdown1(120)
                            self.aiimagemove = 0
                    else:
                        print("Invalid move")
                else:
                    print("Your move is invalid")
            dx = 0
            dy = 0
            self.counter += 1
            self.game_ends()

    def black_play(self, event):
        if self.what_happened == "human played":
            if self.firstclick==True:
                self.clock1.destroy()
                self.clock3=Label(self.f1,text='120',font='arial 18 bold')
                self.clock3.grid(row=2,column=0,padx=10)
                self.countdown3(self.remaining1)
            if self.aicounter % 2 != 0:
                self.firstclick=False
                self.firstx, self.firsty = event.x, event.y
                self.positionx, self.positiony = self.firstx//self.size, self.firsty//self.size
                self.colorpossmoves(self.positiony,self.positionx,'"black"')
                if self.positions[(self.positiony, self.positionx)] != ' ':
                    if self.positions[(self.positiony, self.positionx)] == 'bP1': self.imagemove = self.pawnB1
                    if self.positions[(self.positiony, self.positionx)] == 'bP2': self.imagemove = self.pawnB2
                    if self.positions[(self.positiony, self.positionx)] == 'bP3': self.imagemove = self.pawnB3
                    if self.positions[(self.positiony, self.positionx)] == 'bP4': self.imagemove = self.pawnB4
                    if self.positions[(self.positiony, self.positionx)] == 'bP5': self.imagemove = self.pawnB5
                    if self.positions[(self.positiony, self.positionx)] == 'bP6': self.imagemove = self.pawnB6
                    if self.positions[(self.positiony, self.positionx)] == 'bP7': self.imagemove = self.pawnB7
                    if self.positions[(self.positiony, self.positionx)] == 'bP8': self.imagemove = self.pawnB8
                    if self.positions[(self.positiony, self.positionx)] == 'bR1': self.imagemove = self.rookB1
                    if self.positions[(self.positiony, self.positionx)] == 'bN1': self.imagemove = self.knightB1
                    if self.positions[(self.positiony, self.positionx)] == 'bB1': self.imagemove = self.bishopB1
                    if self.positions[(self.positiony, self.positionx)] == 'bQ': self.imagemove = self.queenB
                    if self.positions[(self.positiony, self.positionx)] == 'bK': self.imagemove = self.kingB
                    if self.positions[(self.positiony, self.positionx)] == 'bB2': self.imagemove = self.bishopB2
                    if self.positions[(self.positiony, self.positionx)] == 'bN2': self.imagemove = self.knightB2
                    if self.positions[(self.positiony, self.positionx)] == 'bR2': self.imagemove = self.rookB2
                    if self.positions[(self.positiony, self.positionx)] == 'bQ2': self.imagemove = self.queenB2
                    if self.positions[(self.positiony, self.positionx)] == 'bQ3': self.imagemove = self.queenB3
                    if self.positions[(self.positiony, self.positionx)] == 'bB3': self.imagemove = self.bishopB3
                    if self.positions[(self.positiony, self.positionx)] == 'bR3': self.imagemove = self.rookB3
                    if self.positions[(self.positiony, self.positionx)] == 'bN3': self.imagemove = self.knightB3
                    if self.positions[(self.positiony, self.positionx)] == 'bQ4': self.imagemove = self.queenB4
                    if self.positions[(self.positiony, self.positionx)] == 'bB4': self.imagemove = self.bishopB4
                    if self.positions[(self.positiony, self.positionx)] == 'bR4': self.imagemove = self.rookB4
                    if self.positions[(self.positiony, self.positionx)] == 'bN4': self.imagemove = self.knightB4
                    if self.positions[(self.positiony, self.positionx)] == 'bQ5': self.imagemove = self.queenB5
                    if self.positions[(self.positiony, self.positionx)] == 'bB5': self.imagemove = self.bishopB5
                    if self.positions[(self.positiony, self.positionx)] == 'bR5': self.imagemove = self.rookB5
                    if self.positions[(self.positiony, self.positionx)] == 'bN5': self.imagemove = self.knightB5
                    if self.positions[(self.positiony, self.positionx)] == 'bQ6': self.imagemove = self.queenB6
                    if self.positions[(self.positiony, self.positionx)] == 'bB6': self.imagemove = self.bishopB6
                    if self.positions[(self.positiony, self.positionx)] == 'bR6': self.imagemove = self.rookB6
                    if self.positions[(self.positiony, self.positionx)] == 'bN6': self.imagemove = self.knightB6
                    if self.positions[(self.positiony, self.positionx)] == 'bQ7': self.imagemove = self.queenB7
                    if self.positions[(self.positiony, self.positionx)] == 'bB7': self.imagemove = self.bishopB7
                    if self.positions[(self.positiony, self.positionx)] == 'bR7': self.imagemove = self.rookB7
                    if self.positions[(self.positiony, self.positionx)] == 'bN7': self.imagemove = self.knightB7
                else:
                    print("Try again")
                    self.aicounter-=1
            if self.aicounter % 2 == 0:
                self.canvas.delete('greenrect')
                self.destx, self.desty = event.x//self.size, event.y//self.size
                if (self.destx > 1 and self.desty > 1) or (self.destx < 9 and self.desty < 9):
                    if '{}{}'.format(self.destx, self.desty) in self.greenrectli:
                        if self.targetisvalid(self.desty, self.destx, self.positiony, self.positionx):
                            dx, dy = self.destx - self.positionx, self.desty - self.positiony 
                            self.canvas.move(self.imagemove, dx*self.size, dy*self.size)
                            self.pieces["({},{})".format(self.desty, self.destx)] = self.pieces["({},{})".format(self.positiony, self.positionx)]
                            self.pieces["({},{})".format(self.positiony, self.positionx)] = ' '
                            self.positions[(self.desty, self.destx)] = str(self.positions[(self.positiony, self.positionx)])
                            self.positions[(self.positiony, self.positionx)] = ' '
                            if self.desty==1 and self.positions[(self.desty, self.destx)][:2] =='bP':
                                self.changingpawn=self.imagemove    
                                self.pawn_change_black()
                            self.firstclick=True
                            self.imagemove = 0
                            self.what_happened = "ai played"
                            self.clock3.destroy()
                            self.clock2=Label(self.f1,text='120',font='arial 18 bold')
                            self.clock2.grid(row=2,column=5,padx=10)
                            self.countdown2(120)
                             
                    else: print("Invalid move")
                else:
                    print("Your move is invalid")
            dx = 0
            dy = 0
            self.aicounter += 1
            self.game_ends()

    def queen(self):
        self.canvas.delete(self.changingpawn)
        if self.positions[(self.desty, self.destx)][0]=='w':
            if 'wQ6' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wQ7'
                self.queenW7=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenw,tag='piece')
            elif 'wQ5' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wQ6'
                self.queenW6=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenw,tag='piece')
            elif 'wQ4' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wQ5'
                self.queenW5=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenw,tag='piece')
            elif 'wQ3' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wQ4'
                self.queenW4=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenw,tag='piece')
            else:
                self.positions[(self.desty, self.destx)]='wQ3'
                self.queenW3=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenw,tag='piece')
        else:
            if 'bQ6' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bQ7'
                self.queenB7=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenb,tag='piece')
            elif 'bQ5' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bQ6'
                self.queenB6=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenb,tag='piece')
            elif 'bQ4' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bQ5'
                self.queenB5=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenb,tag='piece')
            elif 'bQ3' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bQ4'
                self.queenB4=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenb,tag='piece')
            else:
                self.positions[(self.desty, self.destx)]='bQ3'
                self.queenB3=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.queenb,tag='piece')
        self.window.destroy()
            
    def bishop(self):
        self.canvas.delete(self.changingpawn)
        if self.positions[(self.desty, self.destx)][0]=='w':
            if 'wB6' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wB7'
                self.bishopW7=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopw,tag='piece')
            elif 'wB5' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wB6'
                self.bishopW6=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopw,tag='piece')
            elif 'wB4' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wB5'
                self.bishopW5=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopw,tag='piece')
            elif 'wB3' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wB4'
                self.bishopW4=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopw,tag='piece')
            else:
                self.positions[(self.desty, self.destx)]='wB3'
                self.bishopW3=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopw,tag='piece')
        else:
            if 'bB6' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bB7'
                self.bishopB7=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopb,tag='piece')
            elif 'bB5' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bB6'
                self.bishopB6=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopb,tag='piece')
            elif 'bB4' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bB5'
                self.bishopB5=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopb,tag='piece')
            elif 'bB3' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bB4'
                self.bishopB4=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopb,tag='piece')
            else:
                self.positions[(self.desty, self.destx)]='bB3'
                self.bishopB3=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.bishopb,tag='piece')
        self.window.destroy()
        
    def rook(self):
        self.canvas.delete(self.changingpawn)
        if self.positions[(self.desty, self.destx)][0]=='w':
            if 'wR6' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wR7'
                self.rookW7=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookw,tag='piece')
            elif 'wR5' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wR6'
                self.rookW6=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookw,tag='piece')
            elif 'wR4' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wR5'
                self.rookW5=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookw,tag='piece')
            elif 'wR3' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wR4'
                self.rookW4=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookw,tag='piece')
            else:
                self.positions[(self.desty, self.destx)]='wR3'
                self.rookW3=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookw,tag='piece')
        else:
            if 'bR6' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bR7'
                self.rookB7=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookb,tag='piece')
            elif 'bR5' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bR6'
                self.rookB6=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookb,tag='piece')
            elif 'bR4' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bR5'
                self.rookB5=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookb,tag='piece')
            elif 'bR3' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bR4'
                self.rookB4=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookb,tag='piece')
            else:
                self.positions[(self.desty, self.destx)]='bR3'
                self.rookB3=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.rookb,tag='piece')
        self.window.destroy()
        
    def knight(self):
        self.canvas.delete(self.changingpawn)
        if self.positions[(self.desty, self.destx)][0]=='w':
            if 'wN6' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wN7'
                self.knightW7=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightw,tag='piece')
            elif 'wN5' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wN6'
                self.knightW6=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightw,tag='piece')
            elif 'wN4' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wN5'
                self.knightW5=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightw,tag='piece')
            elif 'wN3' in self.positions.values():
                self.positions[(self.desty, self.destx)]='wN4'
                self.knightW4=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightw,tag='piece')
            else:
                self.positions[(self.desty, self.destx)]='wN3'
                self.knightW3=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightw,tag='piece')
        else:
            if 'bN6' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bN7'
                self.knightB7=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightb,tag='piece')
            elif 'bN5' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bN6'
                self.knightB6=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightb,tag='piece')
            elif 'bN4' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bN5'
                self.knightB5=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightb,tag='piece')
            elif 'bN3' in self.positions.values():
                self.positions[(self.desty, self.destx)]='bN4'
                self.knightB4=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightb,tag='piece')
            else:
                self.positions[(self.desty, self.destx)]='bN3'
                self.knightB3=self.canvas.create_image(self.destx*self.size+self.size/2, self.desty*self.size+self.size/2, image = self.knightb,tag='piece')
        self.window.destroy()            
    def pawn(self):
             self.window.destroy()
    
    def pawn_change_black(self):
        self.window=Tk()
        self.window.title("Transformers")
        self.window_center(280,200)
        self.window.configure(background='grey20')
        self.bn=Button(self.window,text='Knight',font='Arial 15 bold',bg='orange',fg='black',command=self.knight,padx=20)
        self.bn.grid(row=0,column=0,ipadx=4,ipady=4,padx=10,pady=5)
        self.bb=Button(self.window,text='Bishop',font='Arial 15 bold',bg='red2',fg='black',command=self.bishop,padx=20)
        self.bb.grid(row=0,column=1,ipadx=4,ipady=4,padx=10,pady=5)
        self.br=Button(self.window,text='Rook',font='Arial 15 bold',bg='yellow',fg='black',command=self.rook,padx=20)
        self.br.grid(row=1,column=0,ipadx=4,ipady=4,padx=10,pady=5)
        self.bq=Button(self.window,text='Queen',font='Arial 15 bold',bg='lawn green',fg='black',command=self.queen,padx=20)
        self.bq.grid(row=2,column=0,ipadx=4,ipady=4,padx=10,pady=5)
        self.bp=Button(self.window,text='Pawn',font='Arial 15 bold',bg='purple1',fg='black',command=self.pawn,padx=20)
        self.bp.grid(row=1,column=1,ipadx=4,ipady=4,padx=10,pady=5)
        self.pick_black=Label(self.window,text='Choose\nwisely!',font='Arial 20 bold',bg='grey20',fg='white')
        self.pick_black.grid(row=2,column=1,ipady=4,padx=5)

    def pawn_change_white(self):
        self.window=Tk()
        self.window.title("Transformers")
        self.window_center(280,200)
        self.window.configure(background='grey80')
        self.bn=Button(self.window,text='Knight',font='Arial 15 bold',bg='orange',fg='white',command=self.knight,padx=20)
        self.bn.grid(row=0,column=0,ipadx=4,ipady=4,padx=10,pady=5)
        self.bb=Button(self.window,text='Bishop',font='Arial 15 bold',bg='red',fg='white',command=self.bishop,padx=20)
        self.bb.grid(row=0,column=1,ipadx=4,ipady=4,padx=10,pady=5)
        self.br=Button(self.window,text='Rook',font='Arial 15 bold',bg='blue',fg='white',command=self.rook,padx=20)
        self.br.grid(row=1,column=0,ipadx=4,ipady=4,padx=10,pady=5)
        self.bq=Button(self.window,text='Queen',font='Arial 15 bold',bg='green',fg='white',command=self.queen,padx=20)
        self.bq.grid(row=2,column=0,ipadx=4,ipady=4,padx=10,pady=5)
        self.bp=Button(self.window,text='Pawn',font='Arial 15 bold',bg='purple',fg='white',command=self.pawn,padx=20)
        self.bp.grid(row=1,column=1,ipadx=4,ipady=4,padx=10,pady=5)
        self.pick_white=Label(self.window,text='Choose\nwisely!',font='Arial 20 bold',bg='grey80',fg='black')
        self.pick_white.grid(row=2,column=1,ipady=4,padx=5)
        
    def window_center(self,r,e):
        width_of_window=r
        height_of_window=e
        screen_width=self.window.winfo_screenwidth()
        screen_height=self.window.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width_of_window/2)
        y_coordinate=(screen_height/2)-(height_of_window/2)
        self.window.geometry('%dx%d+%d+%d' % (width_of_window,height_of_window,x_coordinate,y_coordinate))

#######################################################  IMAGES(GIFS)  #########################################################

    def images(self):
        self.rookw = PhotoImage(file = "whitepieces/RookW.gif")
        self.knightw = PhotoImage(file = "whitepieces/KnightW.gif")
        self.bishopw = PhotoImage(file = "whitepieces/BishopW.gif")
        self.queenw = PhotoImage(file = "whitepieces/QueenW.gif")
        self.kingw = PhotoImage(file = "whitepieces/KingW.gif")
        self.pawnw = PhotoImage(file = "whitePieces/PawnW.gif")
        ###########################################################
        self.rookb = PhotoImage(file = "blackpieces/RookB.gif")
        self.knightb = PhotoImage(file = "blackpieces/KnightB.gif")
        self.bishopb = PhotoImage(file = "blackpieces/BishopB.gif")
        self.queenb = PhotoImage(file = "blackpieces/QueenB.gif")
        self.kingb = PhotoImage(file = "blackpieces/KingB.gif")
        self.pawnb = PhotoImage(file = "blackPieces/PawnB.gif")
        #################################################################
        self.rookW1 = self.canvas.create_image(90, 90, image = self.rookw,tag='piece')
        self.knightW1 = self.canvas.create_image(150, 90, image = self.knightw,tag='piece')
        self.bishopW1 = self.canvas.create_image(210, 90, image = self.bishopw,tag='piece')
        self.queenW = self.canvas.create_image(330, 90, image = self.queenw,tag='piece')
        self.kingW = self.canvas.create_image(270, 90, image = self.kingw,tag='piece')
        self.bishopW2 = self.canvas.create_image(390, 90, image = self.bishopw,tag='piece')
        self.knightW2 = self.canvas.create_image(450, 90, image = self.knightw,tag='piece')
        self.rookW2 = self.canvas.create_image(510, 90, image = self.rookw,tag='piece')
        self.pawnW1 = self.canvas.create_image(90, 150, image = self.pawnw,tag='piece')
        self.pawnW2 = self.canvas.create_image(90 + 60, 150, image = self.pawnw,tag='piece')
        self.pawnW3 = self.canvas.create_image(90 + 60*2, 150, image = self.pawnw,tag='piece')
        self.pawnW4 = self.canvas.create_image(90 + 60*3, 150, image = self.pawnw,tag='piece')
        self.pawnW5 = self.canvas.create_image(90 + 60*4, 150, image = self.pawnw,tag='piece')
        self.pawnW6 = self.canvas.create_image(90 + 60*5, 150, image = self.pawnw,tag='piece')
        self.pawnW7 = self.canvas.create_image(90 + 60*6, 150, image = self.pawnw,tag='piece')
        self.pawnW8 = self.canvas.create_image(90 + 60*7, 150, image = self.pawnw,tag='piece')
        #####################################################################
        self.rookB1 = self.canvas.create_image(90, 510, image = self.rookb,tag='piece')
        self.knightB1 = self.canvas.create_image(150, 510, image = self.knightb,tag='piece')
        self.bishopB1 = self.canvas.create_image(210, 510, image = self.bishopb,tag='piece')
        self.queenB = self.canvas.create_image(330, 510, image = self.queenb,tag='piece')
        self.kingB = self.canvas.create_image(270, 510, image = self.kingb,tag='piece')
        self.bishopB2 = self.canvas.create_image(390, 510, image = self.bishopb,tag='piece')
        self.knightB2 = self.canvas.create_image(450, 510, image = self.knightb,tag='piece')
        self.rookB2 = self.canvas.create_image(510, 510, image = self.rookb,tag='piece')
        self.pawnB1 = self.canvas.create_image(90 , 450, image = self.pawnb,tag='piece')
        self.pawnB2 = self.canvas.create_image(90 + 60, 450, image = self.pawnb,tag='piece')
        self.pawnB3 = self.canvas.create_image(90 + 60*2, 450, image = self.pawnb,tag='piece')
        self.pawnB4 = self.canvas.create_image(90 + 60*3, 450, image = self.pawnb,tag='piece')
        self.pawnB5 = self.canvas.create_image(90 + 60*4, 450, image = self.pawnb,tag='piece')
        self.pawnB6 = self.canvas.create_image(90 + 60*5, 450, image = self.pawnb,tag='piece')
        self.pawnB7 = self.canvas.create_image(90 + 60*6, 450, image = self.pawnb,tag='piece')
        self.pawnB8 = self.canvas.create_image(90 + 60*7, 450, image = self.pawnb,tag='piece')

    def position(self):
        for i in range(8, 0, -1):
            for z in range(8, 0, -1):
                self.positions[(i, z)] = ' '
                if i == 1:
                    if z == 1:self.positions[(i, z)] = 'wR1'
                    if z == 2:self.positions[(i, z)] = 'wN1'
                    if z == 3:self.positions[(i, z)] = 'wB1'
                    if z == 4:self.positions[(i, z)] = 'wK'
                    if z == 5:self.positions[(i, z)] = 'wQ'
                    if z == 6:self.positions[(i, z)] = 'wB2'
                    if z == 7:self.positions[(i, z)] = 'wN2'
                    if z == 8:self.positions[(i, z)] = 'wR2'
                if i == 2:self.positions[(i, z)] = 'wP{}'.format(z)
                if i == 8:
                    if z == 1:self.positions[(i, z)] = 'bR1'
                    if z == 2:self.positions[(i, z)] = 'bN1'
                    if z == 3:self.positions[(i, z)] = 'bB1'
                    if z == 4:self.positions[(i, z)] = 'bK'
                    if z == 5:self.positions[(i, z)] = 'bQ'
                    if z == 6:self.positions[(i, z)] = 'bB2'
                    if z == 7:self.positions[(i, z)] = 'bN2'
                    if z == 8:self.positions[(i, z)] = 'bR2'
                if i == 7:self.positions[(i, z)] = 'bP{}'.format(z)

    def targetisvalid(self, desty, destx, posy, posx):
        if self.what_happened == "ai played":
            self.mycolor='"white"'
            self.opcolor='"black"'
        else:
            self.opcolor='"white"'
            self.mycolor='"black"'
        validtarget = False
        if self.positions[(desty, destx)] == ' ': validtarget = True
        if self.positions[(desty, destx)] != ' ' and self.positions[(posy, posx)]:
            lastpiece = self.pieces["({},{})".format(desty, destx)]
            firstpiece = self.pieces["({},{})".format(posy, posx)]
        try:
            if lastpiece.team==self.opcolor:
                validtarget = True
                if firstpiece.team == self.color2: self.userattack(desty, destx, posy, posx)
                else: self.aiattack(desty, destx, posy, posx)
            else: validtarget = False
        except:pass
        return validtarget
   
################################################  ATTACK MECHANISM  ############################################################

    def userattack(self, desty, destx, posy, posx):
        if self.positions[(desty, destx)] == 'wP1': self.imagedel = self.pawnW1
        if self.positions[(desty, destx)] == 'wP2': self.imagedel = self.pawnW2
        if self.positions[(desty, destx)] == 'wP3': self.imagedel = self.pawnW3
        if self.positions[(desty, destx)] == 'wP4': self.imagedel = self.pawnW4
        if self.positions[(desty, destx)] == 'wP5': self.imagedel = self.pawnW5
        if self.positions[(desty, destx)] == 'wP6': self.imagedel = self.pawnW6
        if self.positions[(desty, destx)] == 'wP7': self.imagedel = self.pawnW7
        if self.positions[(desty, destx)] == 'wP8': self.imagedel = self.pawnW8
        if self.positions[(desty, destx)] == 'wR1': self.imagedel = self.rookW1
        if self.positions[(desty, destx)] == 'wN1': self.imagedel = self.knightW1
        if self.positions[(desty, destx)] == 'wB1': self.imagedel = self.bishopW1
        if self.positions[(desty, destx)] == 'wQ': self.imagedel = self.queenW
        if self.positions[(desty, destx)] == 'wK': self.imagedel = self.kingW
        if self.positions[(desty, destx)] == 'wB2': self.imagedel = self.bishopW2
        if self.positions[(desty, destx)] == 'wN2': self.imagedel = self.knightW2
        if self.positions[(desty, destx)] == 'wR2': self.imagedel = self.rookW2
        if self.positions[(desty, destx)] == 'wQ3': self.imagedel = self.queenW3
        if self.positions[(desty, destx)] == 'wB3': self.imagedel = self.bishopW3
        if self.positions[(desty, destx)] == 'wR3': self.imagedel = self.rookW3
        if self.positions[(desty, destx)] == 'wN3': self.imagedel = self.knightW3
        if self.positions[(desty, destx)] == 'wQ4': self.imagedel = self.queenW4
        if self.positions[(desty, destx)] == 'wB4': self.imagedel = self.bishopW4
        if self.positions[(desty, destx)] == 'wR4': self.imagedel = self.rookW4
        if self.positions[(desty, destx)] == 'wN4': self.imagedel = self.knightW4
        if self.positions[(desty, destx)] == 'wQ5': self.imagedel = self.queenW5
        if self.positions[(desty, destx)] == 'wB5': self.imagedel = self.bishopW5
        if self.positions[(desty, destx)] == 'wR5': self.imagedel = self.rookW5
        if self.positions[(desty, destx)] == 'wN5': self.imagedel = self.knightW5
        if self.positions[(desty, destx)] == 'wQ6': self.imagedel = self.queenW6
        if self.positions[(desty, destx)] == 'wB6': self.imagedel = self.bishopW6
        if self.positions[(desty, destx)] == 'wR6': self.imagedel = self.rookW6
        if self.positions[(desty, destx)] == 'wN6': self.imagedel = self.knightW6
        if self.positions[(desty, destx)] == 'wQ7': self.imagedel = self.queenW7
        if self.positions[(desty, destx)] == 'wB7': self.imagedel = self.bishopW7
        if self.positions[(desty, destx)] == 'wR7': self.imagedel = self.rookW7
        if self.positions[(desty, destx)] == 'wN7': self.imagedel = self.knightW7
        self.canvas.delete(self.imagedel)
        lostpiece = self.pieces["({},{})".format(desty, destx)]
        self.userscore += lostpiece.value
        us=self.userscore
        v1=StringVar()
        self.sc1=Label(self.f1,textvariable=v1,font='Arial 20 bold',bg='grey50',fg='black')
        self.sc1.grid(row=2,column=1)
        v1.set(us)


    def aiattack(self, desty, destx, posy, posx):
        if self.positions[(desty, destx)] == 'bP1': self.aiimagedel = self.pawnB1       
        if self.positions[(desty, destx)] == 'bP2':self.aiimagedel = self.pawnB2
        if self.positions[(desty, destx)] == 'bP3':self.aiimagedel = self.pawnB3
        if self.positions[(desty, destx)] == 'bP4': self.aiimagedel = self.pawnB4
        if self.positions[(desty, destx)] == 'bP5': self.aiimagedel = self.pawnB5
        if self.positions[(desty, destx)] == 'bP6': self.aiimagedel = self.pawnB6
        if self.positions[(desty, destx)] == 'bP7': self.aiimagedel = self.pawnB7
        if self.positions[(desty, destx)] == 'bP8': self.aiimagedel = self.pawnB8
        if self.positions[(desty, destx)] == 'bR1': self.aiimagedel = self.rookB1
        if self.positions[(desty, destx)] == 'bN1': self.aiimagedel = self.knightB1
        if self.positions[(desty, destx)] == 'bB1': self.aiimagedel = self.bishopB1
        if self.positions[(desty, destx)] == 'bQ': self.aiimagedel = self.queenB
        if self.positions[(desty, destx)] == 'bK': self.aiimagedel = self.kingB
        if self.positions[(desty, destx)] == 'bB2': self.aiimagedel = self.bishopB2
        if self.positions[(desty, destx)] == 'bN2': self.aiimagedel = self.knightB2
        if self.positions[(desty, destx)] == 'bR2': self.aiimagedel = self.rookB2
        if self.positions[(desty, destx)] == 'bQ3': self.aiimagedel = self.queenB3
        if self.positions[(desty, destx)] == 'bB3': self.aiimagedel = self.bishopB3
        if self.positions[(desty, destx)] == 'bR3': self.aiimagedel = self.rookB3
        if self.positions[(desty, destx)] == 'bN3': self.aiimagedel = self.knightB3
        if self.positions[(desty, destx)] == 'bQ4': self.aiimagedel = self.queenB4
        if self.positions[(desty, destx)] == 'bB4': self.aiimagedel = self.bishopB4
        if self.positions[(desty, destx)] == 'bR4': self.aiimagedel = self.rookB4
        if self.positions[(desty, destx)] == 'bN4': self.aiimagedel = self.knightB4
        if self.positions[(desty, destx)] == 'bQ5': self.aiimagedel = self.queenB5
        if self.positions[(desty, destx)] == 'bB5': self.aiimagedel = self.bishopB5
        if self.positions[(desty, destx)] == 'bR5': self.aiimagedel = self.rookB5
        if self.positions[(desty, destx)] == 'bN5': self.aiimagedel = self.knightB5
        if self.positions[(desty, destx)] == 'bQ6': self.aiimagedel = self.queenB6
        if self.positions[(desty, destx)] == 'bB6': self.aiimagedel = self.bishopB6
        if self.positions[(desty, destx)] == 'bR6': self.aiimagedel = self.rookB6
        if self.positions[(desty, destx)] == 'bN6': self.aiimagedel = self.knightB6
        if self.positions[(desty, destx)] == 'bQ7': self.aiimagedel = self.queenB7
        if self.positions[(desty, destx)] == 'bB7': self.aiimagedel = self.bishopB7
        if self.positions[(desty, destx)] == 'bR7': self.aiimagedel = self.rookB7
        if self.positions[(desty, destx)] == 'bN7': self.aiimagedel = self.knightB7
        self.canvas.delete(self.aiimagedel)
        lostpiece = self.pieces["({},{})".format(desty, destx)]
        self.aiscore += lostpiece.value
        ai=self.aiscore
        v2=StringVar()
        self.sc2=Label(self.f1,textvariable=v2,font='Arial 20 bold',bg='grey50',fg='black')
        self.sc2.grid(row=2,column=4)
        v2.set(ai)
################################################################################################################################################################
    def colorpossmoves(self,posx,posy,color):
        self.greenrectli=[]
        self.greenrectli=self.get_possmoves(posx,posy,color)
        for i in self.get_possmoves(posx,posy,color):
            self.canvas.create_rectangle(int(i[0])*self.size,int(i[1])*self.size,(int(i[0])+1)*self.size,(int(i[1])+1)*self.size,fill='lightgreen',tag='greenrect')
        self.canvas.tag_raise('piece')    
    def get_possmoves(self,posx,posy,color):
        self.mycolor=color
        
        if self.mycolor==self.color1:
            self.opcolor=self.color2
        else:
            self.opcolor=self.color1
        row=posx
        column=posy
        self.possmoves=[]
        if self.mycolor[1]==self.positions[(posx,posy)][0]:
            if self.positions[(posx,posy)][1] == "P":
                if self.positions[(posx,posy)][0] =="w":
                    if row == 2:
                        if self.pieces['({},{})'.format(row+1,column)]==' ': self.possmoves.append('{}3'.format(column))
                        if self.pieces['({},{})'.format(row+2,column)]==' ': self.possmoves.append('{}4'.format(column))
                    if row<8 and self.pieces['({},{})'.format(row+1,column)]==' ':self.possmoves.append('{}{}'.format(column,row+1))
                    if row<8 and column>1 and self.pieces['({},{})'.format(row+1,column-1)]!=' ':
                        if self.pieces['({},{})'.format(row+1,column-1)].team==self.color2:
                            self.possmoves.append('{}{}'.format(column-1,row+1))
                    if column<8 and row<8 and  self.pieces['({},{})'.format(row+1,column+1)]!=' ':
                        if self.pieces['({},{})'.format(row+1,column+1)].team==self.color2:
                            self.possmoves.append('{}{}'.format(column+1,row+1))
                if self.positions[(posx,posy)][0] =="b":
                    if row == 7:
                        if self.pieces['({},{})'.format(row-1,column)]==' ': self.possmoves.append('{}6'.format(column))
                        if self.pieces['({},{})'.format(row-2,column)]==' ': self.possmoves.append('{}5'.format(column))
                    if row>1 and self.pieces['({},{})'.format(row-1,column)]==' ':self.possmoves.append('{}{}'.format(column,row-1))
                    if row>1 and column>1 and self.pieces['({},{})'.format(row-1,column-1)]!=' ':
                        if self.pieces['({},{})'.format(row-1,column-1)].team==self.color1:
                            self.possmoves.append('{}{}'.format(column-1,row-1))
                    if column<8 and row>1 and  self.pieces['({},{})'.format(row-1,column+1)]!=' ':
                        if self.pieces['({},{})'.format(row-1,column+1)].team==self.color1:
                            self.possmoves.append('{}{}'.format(column+1,row-1))
    ##############################
            if self.positions[(posx,posy)][1] == "Q":
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row+i,column)]==' ' or self.pieces['({},{})'.format(row+i,column)].team == self.opcolor:self.possmoves.append('{}{}'.format(column,row+i))
                        if self.pieces['({},{})'.format(row+i,column)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row,column-i)]==' ' or self.pieces['({},{})'.format(row,column-i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-i,row))
                        if self.pieces['({},{})'.format(row,column-i)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row-i,column)]==' ' or self.pieces['({},{})'.format(row-i,column)].team == self.opcolor: self.possmoves.append('{}{}'.format(column,row-i))
                        if self.pieces['({},{})'.format(row-i,column)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row,column+i)]==' ' or self.pieces['({},{})'.format(row,column+i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+i,row))
                        if self.pieces['({},{})'.format(row,column+i)]!=' ':
                            break
                    except:pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row+i,column+i)]==' ' or self.pieces['({},{})'.format(row+i,column+i)].team == self.opcolor:self.possmoves.append('{}{}'.format(column+i,row+i))
                        if self.pieces['({},{})'.format(row+i,column+i)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row+i,column-i)]==' ' or self.pieces['({},{})'.format(row+i,column-i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-i,row+i))
                        if self.pieces['({},{})'.format(row+i,column-i)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row-i,column+i)]==' ' or self.pieces['({},{})'.format(row-i,column+i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+i,row-i))
                        if self.pieces['({},{})'.format(row-i,column+i)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row-i,column-i)]==' ' or self.pieces['({},{})'.format(row-i,column-i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-i,row-i))
                        if self.pieces['({},{})'.format(row-i,column-i)]!=' ':
                            break
                    except: pass
    ##################################################            
            if self.positions[(posx,posy)][1] == "R":
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row+i,column)]==' ' or self.pieces['({},{})'.format(row+i,column)].team == self.opcolor:self.possmoves.append('{}{}'.format(column,row+i))
                        if self.pieces['({},{})'.format(row+i,column)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row,column-i)]==' ' or self.pieces['({},{})'.format(row,column-i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-i,row))
                        if self.pieces['({},{})'.format(row,column-i)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row-i,column)]==' ' or self.pieces['({},{})'.format(row-i,column)].team == self.opcolor: self.possmoves.append('{}{}'.format(column,row-i))
                        if self.pieces['({},{})'.format(row-i,column)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row,column+i)]==' ' or self.pieces['({},{})'.format(row,column+i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+i,row))
                        if self.pieces['({},{})'.format(row,column+i)]!=' ':
                            break
                    except: pass
    ################################
                        
            if self.positions[(posx,posy)][1] == "K":
                try:
                    if self.pieces['({},{})'.format(row+1,column-1)]==' ' or self.pieces['({},{})'.format(row+1,column-1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-1,row+1))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row-1,column+1)]==' ' or self.pieces['({},{})'.format(row-1,column+1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+1,row-1))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row,column+1)]==' ' or self.pieces['({},{})'.format(row,column+1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+1,row))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row,column-1)]==' ' or self.pieces['({},{})'.format(row,column-1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-1,row))
                except: pass
                try:
                     if self.pieces['({},{})'.format(row+1,column)]==' ' or self.pieces['({},{})'.format(row+1,column)].team == self.opcolor: self.possmoves.append('{}{}'.format(column,row+1))
                except: pass
                try:
                     if self.pieces['({},{})'.format(row-1,column)]==' ' or self.pieces['({},{})'.format(row-1,column)].team == self.opcolor: self.possmoves.append('{}{}'.format(column,row-1))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row+1,column+1)]==' ' or self.pieces['({},{})'.format(row+1,column+1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+1,row+1))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row-1,column-1)]==' ' or self.pieces['({},{})'.format(row-1,column-1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-1,row-1))
                except: pass

    #########################################
            if self.positions[(posx,posy)][1] == "B":
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row+i,column+i)]==' ' or self.pieces['({},{})'.format(row+i,column+i)].team == self.opcolor:self.possmoves.append('{}{}'.format(column+i,row+i))
                        if self.pieces['({},{})'.format(row+i,column+i)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row+i,column-i)]==' ' or self.pieces['({},{})'.format(row+i,column-i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-i,row+i))
                        if self.pieces['({},{})'.format(row+i,column-i)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row-i,column+i)]==' ' or self.pieces['({},{})'.format(row-i,column+i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+i,row-i))
                        if self.pieces['({},{})'.format(row-i,column+i)]!=' ':
                            break
                    except: pass
                for i in range(1,8):
                    try:
                        if self.pieces['({},{})'.format(row-i,column-i)]==' ' or self.pieces['({},{})'.format(row-i,column-i)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-i,row-i))
                        if self.pieces['({},{})'.format(row-i,column-i)]!=' ':
                            break
                    except: pass
            if self.positions[(posx,posy)][1] == "N":
                try:
                    if self.pieces['({},{})'.format(row+2,column+1)]==' ' or self.pieces['({},{})'.format(row+2,column+1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+1,row+2))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row+2,column-1)]==' ' or self.pieces['({},{})'.format(row+2,column-1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-1,row+2))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row-2,column+1)]==' ' or self.pieces['({},{})'.format(row-2,column+1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+1,row-2))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row-2,column-1)]==' ' or self.pieces['({},{})'.format(row-2,column-1)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-1,row-2))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row+1,column+2)]==' ' or self.pieces['({},{})'.format(row+1,column+2)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+2,row+1))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row-1,column+2)]==' ' or self.pieces['({},{})'.format(row-1,column+2)].team == self.opcolor: self.possmoves.append('{}{}'.format(column+2,row-1))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row-1,column-2)]==' ' or self.pieces['({},{})'.format(row-1,column-2)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-2,row-1))
                except: pass
                try:
                    if self.pieces['({},{})'.format(row+1,column-2)]==' ' or self.pieces['({},{})'.format(row+1,column-2)].team == self.opcolor: self.possmoves.append('{}{}'.format(column-2,row+1))
                except: pass
        return self.possmoves


######################################################  THE END  ###############################################################

    def game_ends(self):
        if self.aiscore >= 5000:
            x='{} is the winner!!!'.format(self.p1n)
            self.cs1+=1
            self.announcement(x)
           
        if self.userscore >= 5000:
            x='{} is the winner!!!'.format(self.p2n)
            self.cs2+=1
            self.announcement(x)

    def announcement(self,mes):
        self.count_click=0
        self.f1.destroy()
        self.message=Label(self.root)
        self.message.grid(row=0,column=1,ipadx=10,ipady=10,padx=40)
        self.winner=Message(self.message,text=mes,bg='lightgreen',font='arial 30 bold')
        self.winner.pack()
        self.but=Button(self.message,text='Skip',bg='black',font='arial 20 bold',fg='white',command=self.clicked)
        self.but.pack()

    def clicked(self):
        self.count_click +=1
        if self.count_click==1:
            self.message.destroy()
            self.f1.destroy()
            self.canvas.destroy()
            self.end_round()
        else:
           self.root.wait_window(self.message)
           self.root.wait_window(self.winner)
           self.root.wait_window(self.but)

    def menu(self,event):
        self.f1.destroy()
        self.canvas.destroy()
        self.the_end()

    def the_end(self):
        self.root.title("This is the end...but it doesn't even matter")
        self.root_center(300,200)
        re=Button(self.root,text='Restart ⟲',font='Arial 20 bold',bg='orange',fg='black',command=self.restart_game,padx=20)
        re.pack(ipady=4,ipadx=12,pady=20,padx=10)
        ex=Button(self.root,text='Exit ⓧ',font='Arial 20 bold',bg='blue',fg='white',command=self.exit_game,padx=20)
        ex.pack(ipadx=14,ipady=4,pady=20,padx=10)

    def end_round(self):
        self.root.title("This is the end...but it doesn't even matter")
        self.root_center(300,320)
        re=Button(self.root,text='Next Round',font='Arial 20 bold',bg='orange',fg='black',command=self.next_round,padx=20)
        re.pack(ipady=4,ipadx=12,pady=20,padx=10)
        ex=Button(self.root,text='Exit ⓧ',font='Arial 20 bold',bg='blue',fg='white',command=self.exit_game,padx=20)
        ex.pack(ipadx=14,ipady=4,pady=20,padx=10)
        con=Button(self.root,text='Restart ⟲',font='Arial 20 bold',bg='red',fg='black',command=self.restart_game,padx=20)
        con.pack(ipady=4,pady=20,padx=10)

    def next_round(self):
        self.root.destroy()
        root=Tk()
        app=MyApp(root,self.color1,self.color2,self.cs1,self.cs2)

    def restart_game(self):
        self.root.destroy()
        ChessGameMainMenu()

    def exit_game(self):
        self.root.destroy()
       
################################################################################################################################        

class Piece():
    def __init__(self,symbol, team, position, value):
        self.symbol = symbol
        self.team = team
        self.position = position
        self.value = value
       
####################################################  CHESS MAIN MENNU  ########################################################

class ChessGameMainMenu():
    def __init__(self):
        a='arial 15 bold'
        self.root=Tk()
        self.root.configure(background='grey20')
        self.root.title("Welcome to Python Chess!")
        self.frame=Frame(self.root,bg='grey20')
        self.frame.pack()
       
        self.instructionMessage=StringVar()
        Label(self.frame,textvariable=self.instructionMessage,font='arial 15 bold underline',bg='grey20',fg='red').grid(row=0)
        self.instructionMessage.set("GAME OPTIONS")

        Label(self.frame,text="Name",font='arial 15 bold underline',bg='grey20',fg='orange').grid(row=1,column=1)
       
        Label(self.frame,text="Player 1 (White)",font=a,bg='grey90',fg='black').grid(row=2,column=0)
        self.pl1nam=Entry(self.frame)
        self.pl1nam.grid(row=2,column=1,padx=10)
        self.pl1nam.insert(ANCHOR,"Kasparov")
       
        Label(self.frame,text="Player 2 (Black)",font=a,bg='black',fg='white').grid(row=3,column=0)
        self.pl2nam=Entry(self.frame)
        self.pl2nam.grid(row=3,column=1,padx=10)
        self.pl2nam.insert(ANCHOR,"Black")

        self.root.bind("<Return>", self.ok2)  
       
        b=Button(self.frame, text="Start the Game!",font='arial 18 bold',bg='red3',fg='yellow',command=self.ok1)
        b.grid(row=4,column=1,pady=20)

        self.root_center(600,220)
        self.count=0
        self.root.mainloop()

    def root_center(self,r,e):
        width_of_window=r
        height_of_window=e
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width_of_window/2)
        y_coordinate=(screen_height/2)-(height_of_window/2)
        self.root.geometry('%dx%d+%d+%d' % (width_of_window,height_of_window,x_coordinate,y_coordinate))    
           
    def ok1(self):
        self.count += 1
        if self.count==1:
            self.p1n=self.pl1nam.get()
            self.p1c="white"
            self.p2n=self.pl2nam.get()
            self.p2c="black"
            if self.p1n!="" and self.p2n!="":
                self.frame.destroy()
            else:
                if self.p1n=="":
                        self.p1n.insert(ANCHOR,"Kasparov")
                if self.p2n=="":
                        self.p2n.insert(ANCHOR,"Black")
            datas=[]
            datas.append(self.p1n)
            datas.append(self.p1c)
            datas.append(self.p2n)
            datas.append(self.p2c)
            f= open("GAME_OPTIONS.txt","w+", encoding = 'utf-8')
            with open('GAME_OPTIONS.txt', 'w', encoding = 'utf-8') as filehandle:
                for listitem in datas:
                    filehandle.write('%s\n' % listitem)
            self.GetGameSetupParams()
        else:
            self.root.wait_window(self.frame)

    def ok2(self,event):
        self.count += 1
        if self.count==1:
            self.p1n=self.pl1nam.get()
            self.p1c="white"
            self.p2n=self.pl2nam.get()
            self.p2c="black"
            if self.p1n!="" and self.p2n!="":
                self.frame.destroy()
            else:
                if self.p1n=="":
                        self.p1n.insert(ANCHOR,"Kasparov")
                if self.p2n=="":
                        self.p2n.insert(ANCHOR,"Black")
            datas=[]
            datas.append(self.p1n)
            datas.append(self.p1c)
            datas.append(self.p2n)
            datas.append(self.p2c)
            f= open("GAME_OPTIONS.txt","w+", encoding = 'utf-8')
            with open('GAME_OPTIONS.txt', 'w', encoding = 'utf-8') as filehandle:
                for listitem in datas:
                    filehandle.write('%s\n' % listitem)
            self.GetGameSetupParams()
        else:
            self.root.wait_window(self.frame)
       
    def GetGameSetupParams(self):
        self.root.destroy()
        main()

######################################################  THE START  #############################################################

def main():
    root = Tk()
    f=open('GAME_OPTIONS.txt','r', encoding = 'utf-8')
    datas=[]
    for x in f:
        datas.append(x)
    p1c=datas[1]
    p2c=datas[3]
    p1color='"{:.5s}"'.format(p1c)
    p2color='"{:.5s}"'.format(p2c)
    app = MyApp(root,p1color,p2color,0,0)
    root.mainloop()

ChessGameMainMenu()
