#Ping Pong with Turtle - Python for Beginners by Jorge Ibanez
#Inspired in youtube video: https://www.youtube.com/watch?v=C6jJg9Zan7w&t=865s
<<<<<<< HEAD
#------------------------------------------------------------------------
#Ping Pong con Turtle - Python para principiantes, hecho por Jorge Ibanez
#Inspirado en el video de youtube: https://www.youtube.com/watch?v=C6jJg9Zan7w&t=865s

import turtle
=======
#-------------------------------------------------------------------------------
#Ping Pong con Turtle - Python para principiantes, hecho por Jorge Ibanez
#Inspirado (más no copiado xd) en el video de youtube: https://www.youtube.com/watch?v=C6jJg9Zan7w&t=865s

import turtle
import playsound
import threading 
#Los módulos "playsound" y "threading" son únicamente para reproducir el sonido, no son indispensable para el juego
#The modules "playsound" and "threading" are only to reproduce sound, they aren't essential for the game
>>>>>>> Ver2.0

#Initialization
ventana = turtle.Screen() #Creating and configuration of the window
ventana.title("Ping Pong by Jorge Ibanez")
ventana.bgcolor("black") 
ventana.setup(width = 760, height = 640)
ventana.delay(0)
ScoreP1, ScoreP2 = 0, 0

<<<<<<< HEAD
=======
#Sonido - Sound
def Sound():
	playsound._playsoundWin("impact.mp3", False)
	#playsound._playsoundOSX("impact.mp3", False)
	#playsound._playsoundNix("impact.mp3", False)
def PlaySound(): 
	threading.Thread(target=Sound).start()

>>>>>>> Ver2.0
#Raqueta 1 - Paddle 1
raqueta1 = turtle.Turtle()
raqueta1.shape("square")
raqueta1.penup()
raqueta1.shapesize(stretch_wid = 4, stretch_len = 1) #Width = 80p and Length = 20p
raqueta1.color("white")
raqueta1.speed(0)
raqueta1.goto(-360,0)

#Raqueta 2 - Paddle 2
raqueta2 = turtle.Turtle()
raqueta2.shape("square")
raqueta2.penup()
raqueta2.shapesize(stretch_wid = 4, stretch_len = 1)
raqueta2.color("white")
raqueta2.speed(0)
raqueta2.goto(360,0)

#Pelota - Ball
pelota = turtle.Turtle()
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.speed(0)
pelota.goto(0,0)
pelota.dirX = 1
pelota.dirY = 1

<<<<<<< HEAD
#Letras y Puntuacion - Letters and Score
=======
#Letras y Puntuación - Letters and Score
>>>>>>> Ver2.0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.ht()
def Draw():
	global ScoreP1, ScoreP2, pen
	pen.clear()
	pen.goto(0,320) #To draw the midline
	pen.pendown()
	pen.goto(0,-320)
	pen.penup()
	pen.goto(0, 190)
	pen.write("Player 1: {}    Player 2: {}".format(ScoreP1, ScoreP2), align="center", font=("Courier", 24, "normal") )
Draw()

<<<<<<< HEAD
#Configuracion del Teclado - Keyboard configuration
=======
#Configuración del Teclado - Keyboard configuration
>>>>>>> Ver2.0
def Raqueta1Up():
	y = raqueta1.ycor()
	VentanaHeight = ventana.window_height()
	if y + 40 < VentanaHeight//2:
		y+=40
		x = raqueta1.xcor()		
		raqueta1.goto(x,y)
def Raqueta1Down():
	y = raqueta1.ycor()
	VentanaHeight = ventana.window_height()
	if y - 40 > -VentanaHeight//2:
		y-=40
		x = raqueta1.xcor()		
		raqueta1.goto(x,y)
def Raqueta2Up():
	y = raqueta2.ycor()
	VentanaHeight = ventana.window_height()
	if y + 40< VentanaHeight//2:
		y+=40
		x = raqueta2.xcor()		
		raqueta2.goto(x,y)
def Raqueta2Down():
	y = raqueta2.ycor()
	VentanaHeight = ventana.window_height()
	if y - 40 > -VentanaHeight//2:
		y-=40
		x = raqueta2.xcor()		
		raqueta2.goto(x,y)
ventana.listen()
ventana.onkeypress(Raqueta1Up, "w")
ventana.onkeypress(Raqueta1Down, "s")
ventana.onkeypress(Raqueta2Up, "Up")
ventana.onkeypress(Raqueta2Down, "Down")

#Colisiones - Collisions
def ChoqueArriba(coordY):
	global pelota
	VentanaHeight = ventana.window_height()
	if coordY>= VentanaHeight//2 - 10:
		pelota.dirY = -pelota.dirY
<<<<<<< HEAD
=======
		PlaySound()

>>>>>>> Ver2.0
def ChoqueAbajo(coordY):
	global pelota
	VentanaHeight = ventana.window_height()
	if coordY<= -VentanaHeight//2 + 10:
		pelota.dirY = -pelota.dirY
<<<<<<< HEAD
=======
		PlaySound()

>>>>>>> Ver2.0
def ChoqueDerecha(coordX):
	global pelota
	VentanaWidth = ventana.window_width()
	if coordX >= VentanaWidth//2 - 10:
		pelota.dirX = -pelota.dirX
		return True
	return False

def ChoqueIzquierda(coordX):
	global pelota
	VentanaWidth = ventana.window_width()
	if coordX<= -VentanaWidth//2 + 10:
		pelota.dirX = -pelota.dirX
		return True
	return False

def ChoqueRaqueta1(coordX, coordY):
	global pelota, raqueta1
	if  (raqueta1.ycor() + 40) >= coordY-10 and  coordY + 10 >= (raqueta1.ycor() -40) and coordX - 10 <= raqueta1.xcor() + 10:
		pelota.dirX = -pelota.dirX
<<<<<<< HEAD
=======
		PlaySound()
>>>>>>> Ver2.0
		if coordX - 10 < raqueta1.xcor() + 10:
			pelota.setx( raqueta1.xcor() + 20 )
			
def ChoqueRaqueta2(coordX, coordY):
	global pelota, raqueta2
	if  (raqueta2.ycor() + 40) >= coordY-10 and  coordY + 10 >= (raqueta2.ycor() -40) and coordX + 10 >= raqueta2.xcor() - 10:
		pelota.dirX = -pelota.dirX
<<<<<<< HEAD
=======
		PlaySound()
>>>>>>> Ver2.0
		if coordX + 10 >= raqueta2.xcor() - 10:
			pelota.setx( raqueta2.xcor() - 20 )

#Refreshing
<<<<<<< HEAD

=======
>>>>>>> Ver2.0
while True:
	ventana.update()
	#Movimiento Pelota - Ball movement
	pelota.setx( pelota.xcor() + pelota.dirX)
	pelota.sety( pelota.ycor() + pelota.dirY)
	ChoqueArriba( pelota.ycor() )
	ChoqueAbajo( pelota.ycor() )
<<<<<<< HEAD
	if ChoqueDerecha( pelota.xcor() ): #Score Player 1
		ScoreP1+=1
		pelota.goto(0,0)
		Draw()
	if ChoqueIzquierda( pelota.xcor() ): #Score Player 2
=======
	if ChoqueDerecha( pelota.xcor() ): #Score Player 1++
		ScoreP1+=1
		pelota.goto(0,0)
		Draw()
	if ChoqueIzquierda( pelota.xcor() ): #Score Player 2++
>>>>>>> Ver2.0
		ScoreP2+=1
		pelota.goto(0,0)
		Draw()
	ChoqueRaqueta1( pelota.xcor(), pelota.ycor())
	ChoqueRaqueta2( pelota.xcor(), pelota.ycor())
<<<<<<< HEAD

=======
>>>>>>> Ver2.0
