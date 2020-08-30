# Author: Tai Karir
# Date: 08/29/2020
# Email: tai.karir@gmail.com
# Purpose: the purpose of this program is to have the computer solve a 2x2
#          rubik's cube. You can use two methods to solve the cube: brute
#          force, where the computer makes random moves to solve the cube,
#          and the Ortega method, where the computer first solves any face,
#          and then goes on to use the Ortega conditions to solve the cube.
import random
import time
class Piece:
    def __init__(self,a,b,c,d,e,f):
        #a,b,c,d,e,f represent the colors of each face of the piece. a is the front face, b is left, c is top, d is right, e is bottom, and f is the back face
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
class Cube:
    def __init__(self,prev,fcolor,fnumber,opposite,sequence,moves):
        #f=front,b=back,u=upper,d=lower,l=left,r=right. ful=front-upper-right piece, etc
        self.ful=Piece("W","O","B","","","")
        self.fur=Piece("W","","B","R","","")
        self.fdl=Piece("W","O","","","G","")
        self.fdr=Piece("W","","","R","G","")
        self.bul=Piece("Y","R","B","","","")
        self.bur=Piece("Y","","B","O","","")
        self.bdl=Piece("Y","R","","","G","")
        self.bdr=Piece("Y","","","O","G","")
        self.prev=prev
        self.oppositeMoves={0:0,1:2,2:1,3:4,4:3,5:6,6:5,7:8,8:7,9:10,10:9,11:12,12:11}
        self.oppositeColors={"W":"Y","Y":"W","O":"R","R":"O","B":"G","G":"B"}
        self.numberMove={1:"Ri",2:"R",3:"Li",4:"L",5:"Ui",6:"U",7:"Fi",8:"F",9:"Di",10:"D",11:"Bi",12:"B"}
        self.fcolor=fcolor
        self.fnumber=fnumber
        self.opposite=opposite
        self.scramblesequence=sequence
        self.moves=moves
    #this function prints the cube from its current position
    def print_cube(self):
        print(r"   ",self.bur.c,self.bul.c)
        print(r"   ",self.ful.c,self.fur.c)
        print(self.bur.d, self.ful.b, self.ful.a, self.fur.a, self.fur.d, self.bul.b,self.bul.a, self.bur.a)
        print(self.bdr.d, self.fdl.b, self.fdl.a, self.fdr.a, self.fdr.d, self.bdl.b,self.bdl.a, self.bdr.a)
        print(r"   ",self.fdl.e,self.fdr.e)
        print(r"   ",self.bdr.e,self.bdl.e)
    #this function performs an Ri turn on the cube (moves the right face counterclockwise)
    def Ri(self):
        self.moves+=1
        tempfura=self.fur.a;tempfurc=self.fur.c;tempfurd=self.fur.d;self.fur.a=self.bul.c;self.fur.c=self.bul.a;self.fur.d=self.bul.b;self.bul.a=self.bdl.e;self.bul.b=self.bdl.b;self.bul.c=self.bdl.a;self.bdl.a=self.fdr.e;self.bdl.b=self.fdr.d;self.bdl.e=self.fdr.a;self.fdr.a=tempfurc;self.fdr.d=tempfurd;self.fdr.e=tempfura
    #this function performs an R turn on the cube (moves the right face clockwise)
    def R(self):
        self.moves+=1
        tempfura=self.fur.a;tempfurc=self.fur.c;tempfurd=self.fur.d;self.fur.a=self.fdr.e;self.fur.c=self.fdr.a;self.fur.d=self.fdr.d;self.fdr.a=self.bdl.e;self.fdr.d=self.bdl.b;self.fdr.e=self.bdl.a;self.bdl.a=self.bul.c;self.bdl.b=self.bul.b;self.bdl.e=self.bul.a;self.bul.a=tempfurc;self.bul.b=tempfurd;self.bul.c=tempfura
    #this function performs an Li turn on the cube (moves the left face counterclockwise)
    def Li(self):
        self.moves+=1
        tempfula=self.ful.a;tempfulb=self.ful.b;tempfulc=self.ful.c;self.ful.a=self.fdl.e;self.ful.b=self.fdl.b;self.ful.c=self.fdl.a;self.fdl.a=self.bdr.e;self.fdl.b=self.bdr.d;self.fdl.e=self.bdr.a;self.bdr.a=self.bur.c;self.bdr.d=self.bur.d;self.bdr.e=self.bur.a;self.bur.a=tempfulc;self.bur.c=tempfula;self.bur.d=tempfulb
    #this function performs an L turn on the cube (moves the left face clockwise)
    def L(self):
        self.moves+=1
        tempfula=self.ful.a;tempfulb=self.ful.b;tempfulc=self.ful.c;self.ful.a=self.bur.c;self.ful.b=self.bur.d;self.ful.c=self.bur.a;self.bur.a=self.bdr.e;self.bur.c=self.bdr.a;self.bur.d=self.bdr.d;self.bdr.a=self.fdl.e;self.bdr.d=self.fdl.b;self.bdr.e=self.fdl.a;self.fdl.a=tempfulc;self.fdl.b=tempfulb;self.fdl.e=tempfula
    #this function performs a Ui turn on the cube (moves the upper face counterclockwise)
    def Ui(self):
        self.moves+=1
        tempfula=self.ful.a;tempfulb=self.ful.b;tempfulc=self.ful.c;self.ful.a=self.bur.d;self.ful.b=self.bur.a;self.ful.c=self.bur.c;self.bur.a=self.bul.b;self.bur.c=self.bul.c;self.bur.d=self.bul.a;self.bul.a=self.fur.d;self.bul.b=self.fur.a;self.bul.c=self.fur.c;self.fur.a=tempfulb;self.fur.c=tempfulc;self.fur.d=tempfula
    #this function performs a U turn on the cube (moves the upper face clockwise)
    def U(self):
        self.moves+=1
        tempfula=self.ful.a;tempfulb=self.ful.b;tempfulc=self.ful.c;self.ful.a=self.fur.d;self.ful.b=self.fur.a;self.ful.c=self.fur.c;self.fur.a=self.bul.b;self.fur.c=self.bul.c;self.fur.d=self.bul.a;self.bul.a=self.bur.d;self.bul.b=self.bur.a;self.bul.c=self.bur.c;self.bur.a=tempfulb;self.bur.c=tempfulc;self.bur.d=tempfula
    #this function performs a Di turn on the cube (moves the bottom face counterclockwise)
    def Di(self):
        self.moves+=1
        tempfdla=self.fdl.a;tempfdlb=self.fdl.b;tempfdle=self.fdl.e;self.fdl.a=self.fdr.d;self.fdl.b=self.fdr.a;self.fdl.e=self.fdr.e;self.fdr.a=self.bdl.b;self.fdr.d=self.bdl.a;self.fdr.e=self.bdl.e;self.bdl.a=self.bdr.d;self.bdl.b=self.bdr.a;self.bdl.e=self.bdr.e;self.bdr.a=tempfdlb;self.bdr.d=tempfdla;self.bdr.e=tempfdle
    #this function performs a D turn on the cube (moves the bottom face clockwise)
    def D(self):
        self.moves+=1
        tempfdla=self.fdl.a;tempfdlb=self.fdl.b;tempfdle=self.fdl.e;self.fdl.a=self.bdr.d;self.fdl.b=self.bdr.a;self.fdl.e=self.bdr.e;self.bdr.a=self.bdl.b;self.bdr.d=self.bdl.a;self.bdr.e=self.bdl.e;self.bdl.a=self.fdr.d;self.bdl.b=self.fdr.a;self.bdl.e=self.fdr.e;self.fdr.a=tempfdlb;self.fdr.d=tempfdla;self.fdr.e=tempfdle
    #this function performs an Fi turn on the cube (moves the front face counterclockwise)
    def Fi(self):
        self.moves+=1
        tempfula=self.ful.a;tempfulb=self.ful.b;tempfulc=self.ful.c;self.ful.a=self.fur.a;self.ful.b=self.fur.c;self.ful.c=self.fur.d;self.fur.a=self.fdr.a;self.fur.c=self.fdr.d;self.fur.d=self.fdr.e;self.fdr.a=self.fdl.a;self.fdr.d=self.fdl.e;self.fdr.e=self.fdl.b;self.fdl.a=tempfula;self.fdl.b=tempfulc;self.fdl.e=tempfulb
    #this function performs an F turn on the cube (moves the front face clockwise)
    def F(self):
        self.moves+=1
        tempfula=self.ful.a;tempfulb=self.ful.b;tempfulc=self.ful.c;self.ful.a=self.fdl.a;self.ful.b=self.fdl.e;self.ful.c=self.fdl.b;self.fdl.a=self.fdr.a;self.fdl.b=self.fdr.e;self.fdl.e=self.fdr.d;self.fdr.a=self.fur.a;self.fdr.d=self.fur.c;self.fdr.e=self.fur.d;self.fur.a=tempfula;self.fur.c=tempfulb;self.fur.d=tempfulc
    #this function performs a Bi turn on the cube (moves the back face counterclockwise
    def Bi(self):
        self.moves+=1
        tempbula=self.bul.a;tempbulb=self.bul.b;tempbulc=self.bul.c;self.bul.a=self.bur.a;self.bul.b=self.bur.c;self.bul.c=self.bur.d;self.bur.a=self.bdr.a;self.bur.c=self.bdr.d;self.bur.d=self.bdr.e;self.bdr.a=self.bdl.a;self.bdr.d=self.bdl.e;self.bdr.e=self.bdl.b;self.bdl.a=tempbula;self.bdl.b=tempbulc;self.bdl.e=tempbulb
    #this function performs a B turn on the cube (moves the back face clockwise)
    def B(self):
        self.moves+=1
        tempbula=self.bul.a;tempbulb=self.bul.b;tempbulc=self.bul.c;self.bul.a=self.bdl.a;self.bul.b=self.bdl.e;self.bul.c=self.bdl.b;self.bdl.a=self.bdr.a;self.bdl.b=self.bdr.e;self.bdl.e=self.bdr.d;self.bdr.a=self.bur.a;self.bdr.d=self.bur.c;self.bdr.e=self.bur.d;self.bur.a=tempbula;self.bur.c=tempbulb;self.bur.d=tempbulc
    #this function figures out if any face on the cube is solved and/or ifany face is solved
    def isFaceSolved(self,faceNumber):
        #checks if all faces are solved (the cube is complete)
        if faceNumber==0:
            cubeSolved=True
            for x in range(1,7):
                cubeSolved=cubeSolved and self.isFaceSolved(x)
            return cubeSolved
        #individual face completion checks
        if faceNumber==1:
            if self.ful.a==self.fur.a and self.fur.a==self.fdr.a and self.fdr.a==self.fdl.a:
                return True
            else:
                return False
        elif faceNumber==2:
            if self.ful.b==self.bur.d and self.bur.d==self.bdr.d and self.bdr.d==self.fdl.b:
                return True
            else:
                return False
        elif faceNumber==3:
            if self.ful.c==self.fur.c and self.fur.c==self.bul.c and self.bul.c==self.bur.c:
                return True
            else:
                return False
        elif faceNumber==4:
            if self.fur.d==self.fdr.d and self.fdr.d==self.bdl.b and self.bdl.b==self.bul.b:
                return True
        elif faceNumber==5:
            if self.fdl.e==self.fdr.e and self.fdr.e==self.bdl.e and self.bdl.e==self.bdr.e:
                return True
            else:
                return False
        elif faceNumber==6:
            if self.bul.a==self.bur.a and self.bur.a==self.bdr.a and self.bdr.a==self.bdl.a:
                return True
            else:
                return False
        #checks if any face is complete
        elif faceNumber==7:
            for i in range(1,7):
                if self.isFaceSolved(i):
                    if i==1:
                        self.fcolor=self.ful.a
                    elif i==2:
                        self.fcolor=self.ful.b
                    elif i==3:
                        self.fcolor=self.ful.c
                    elif i==4:
                        self.fcolor=self.fur.d
                    elif i==5:
                         self.fcolor=self.fdr.e
                    elif i==6:
                         self.fcolor=self.bul.a
                    self.fnumber=i
                    return True
            return False
    #this function makes a random move
    def move_random(self,y):
        if y==1:
            self.Ri()
        elif y==2:
            self.R()
        elif y==3:
            self.Li()
        elif y==4:
            self.L()
        elif y==5:
            self.Ui()
        elif y==6:
            self.U()
        elif y==7:
            self.Fi()
        elif y==8:
            self.F()
        elif y==9:
            self.Di()
        elif y==10:
            self.D()
        elif y==11:
            self.Bi()
        elif y==12:
            self.B()
    #this function scrambles the cube
    def scramble_cube(self,turns):
        for x in range(0,turns):
            y=random.randrange(1,13)
            self.move_random(y)
            self.scramblesequence.append(self.numberMove.get(y))
    #this function attempts to solve the rubik's cube by brute force (randomly picking moves)
    def brute_force_solver(self):
        y=random.randint(1,13)
        if y==self.oppositeMoves.get(self.prev):
            return False
        else:
            self.move_random(y)
            self.prev=y
            return True
    #this function moves the completed face to the bottom and then solves the top face (opposite of the solved one)
    def OLL(self):
        self.opposite=self.oppositeColors[self.fcolor]
        if self.fnumber==1:
            self.Ri();self.L()
        elif self.fnumber==2:
            self.Fi();self.B()
        elif self.fnumber==3:
            self.Ri();self.L();self.Ri();self.L()
        elif self.fnumber==4:
            self.F();self.Bi()
        elif self.fnumber==5:
            pass
        elif self.fnumber==6:
            self.R()
            self.Li()
        for x in range(0,4):
            if self.ful.a==self.opposite and self.fur.a==self.opposite and self.bul.a==self.opposite and self.bur.a==self.opposite:
                self.R();self.R();self.U();self.U();self.Ri();self.U();self.U();self.R();self.R()
            elif self.ful.b==self.opposite and self.fur.a==self.opposite and self.bul.a==self.opposite and self.bur.d==self.opposite:
                self.R();self.U();self.U();self.R();self.R();self.Ui();self.R();self.R();self.Ui();self.R();self.R();self.U();self.U();self.R()
            elif self.ful.b==self.opposite and self.fur.c==self.opposite and self.bul.c==self.opposite and self.bur.d==self.opposite:
                self.F();self.R();self.U();self.Ri();self.Ui();self.Fi()
            elif self.ful.a==self.opposite and self.fur.c==self.opposite and self.bul.c==self.opposite and self.bur.a==self.opposite:
                self.R();self.U();self.Ri();self.Ui();self.Ri();self.F();self.R();self.Fi()
            elif self.ful.a==self.opposite and self.fur.c==self.opposite and self.bul.b==self.opposite and self.bur.c==self.opposite:
                self.F();self.Ri();self.Fi();self.R();self.U();self.R();self.Ui();self.Ri()
            elif self.ful.c==self.opposite and self.fur.a==self.opposite and self.bul.b==self.opposite and self.bur.a==self.opposite:
                self.R();self.U();self.Ri();self.U();self.R();self.U();self.U();self.Ri()
            elif self.ful.a==self.opposite and self.fur.d==self.opposite and self.bul.c==self.opposite and self.bur.d==self.opposite:
                self.R();self.U();self.U();self.Ri();self.Ui();self.R();self.Ui();self.Ri()
            if self.isFaceSolved(3) and self.isFaceSolved(5):
               return
            else:
               self.U()
    #solves the cube after the top and bottom faces are complete
    def XLL(self):
        for m in range(0,4):
            if self.isFaceSolved(0):
                return True
            else:
                self.U()
        for i in range(0,4):
            for j in range(0,4):
                if self.ful.a==self.fur.a and self.fdl.a==self.fdr.a and self.fdr.d!=self.bdl.b and self.fur.d!=self.bul.b:
                    self.R();self.R();self.Ui();self.B();self.B();self.U();self.U();self.R();self.R();self.Ui();self.R();self.R()
                    for x in range(0,4):
                        if self.isFaceSolved(0):
                            return True
                        self.U()
                elif self.ful.a==self.oppositeColors[self.fur.a] and self.fdl.a==self.oppositeColors[self.fdr.a] and self.fdr.d==self.oppositeColors[self.bdl.b] and self.fur.d==self.oppositeColors[self.bul.b]:
                    self.R();self.R();self.F();self.F();self.R();self.R()
                    for x in range(0,4):
                        if self.isFaceSolved(0):
                            return True
                        self.U()
                elif self.ful.a==self.fur.a and self.fdl.a==self.oppositeColors[self.fdr.a] and self.fdr.d==self.oppositeColors[self.bdl.b]:
                    self.R();self.Ui();self.R();self.F();self.F();self.Ri();self.U();self.Ri()
                    for x in range(0,4):
                        if self.isFaceSolved(0):
                            return True
                        self.U()
                elif self.isFaceSolved(2) and self.fdl.a==self.fdr.a:
                    self.R();self.U();self.Ri();self.Ui();self.Ri();self.F();self.R();self.R();self.Ui();self.Ri();self.Ui();self.R();self.U();self.Ri();self.Fi()
                elif self.fdl.a==self.fdr.a and self.fdl.a==self.ful.a and self.ful.a==self.oppositeColors[self.fur.a] and not self.isFaceSolved(7):
                    self.F();self.R();self.Ui();self.Ri();self.Ui();self.R();self.U();self.Ri();self.Fi();self.R();self.U();self.Ri();self.Ui();self.Ri();self.F();self.R();self.Fi() 
                elif self.isFaceSolved(4) and self.ful.a==self.fur.a:
                    self.F();self.F();self.B();self.B();self.R();self.U();self.Ri();self.Ui();self.Ri();self.F();self.R();self.R();self.Ui();self.Ri();self.Ui();self.R();self.U();self.Ri();self.Fi() 
                elif self.fdl.a==self.fdr.a and self.ful.a==self.oppositeColors[self.fur.a] and self.fur.d==self.oppositeColors[self.bul.b]:
                    self.F();self.F();self.B();self.B();self.R();self.Ui();self.R();self.F();self.F();self.Ri();self.U();self.Ri()
                    for x in range(0,4):
                        if self.isFaceSolved(0):
                            return True
                        self.U()
                if self.isFaceSolved(0):
                    return True
                else:
                    self.U() 
            if self.isFaceSolved(0):
                return True
            else:
                self.D()
if __name__=="__main__":
    #execute only if run as a script
    myCube=Cube(0,0,0,0,[],0)
    print("Initial cube state")
    myCube.print_cube()
    print("Scramble sequence:")
    myCube.scramble_cube(32)
    print("\nScrambled cube state")
    myCube.print_cube()
    t=time.time()
    print("\nSequence:{}".format(myCube.scramblesequence))
    while True:
        if myCube.isFaceSolved(0):
            break
        if myCube.isFaceSolved(7):
            print("\nFirst face complete")
            myCube.print_cube()
            myCube.OLL()
            print("")
            myCube.XLL()
            break
        else:
            myCube.brute_force_solver()
    t2=time.time()
    print("")
    print("Solved state:")
    myCube.print_cube()
    print("")
    print("Time to solve cube: %s seconds!"%(t2-t))
    print("Number of moves to solve cube: %s"%myCube.moves)
    print("Moves per second: %s"%(myCube.moves/(t2-t)))
    #end of file
