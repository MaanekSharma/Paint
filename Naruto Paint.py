
#INDIVIDUAL FEATURES
'''
   -Spray paint
   -Fixed unfilled rectangle
   -Fixed the unfilled ellipse
   -Added a stamp/background tab sysytem
   -Added scrolling to the  unfilled Ellipse and Rectangle
   -Highlight wich tool is selected
   -Added the description box
   -Music with play/stop
   -Undo/Redo
   -Added the "Random Tool"
'''
#ATTENTION TO DETAIL
'''
   -Show the pixel location of the mouse while on the canvas. When the mouse is off the canvas, it stops displaying the position
   -Display the current size
   -When the user changes the tab, the tool resets to avoid confusion
   -The icon is Naruto themed
   -The caption is changed to "Naruto Paint!"
   -Mouse cursor in the middle of the picture when using stamps
   -Created an outline around the canvas while the mouse is being clicked inside the canvas
   -Created a rect that shows the user where the colour was selected last on the palette
'''
from pygame import*
from pygame import font as fnt #This is to stop the collision of Tk's font and pygame's font. If not, the program won't run
from random import*
from math import*
from getName import * #getName is used for save

#tkinter for load
try:from tkinter import filedialog #Tkinter will sometimes crash on certain computers
except:                             #This will try to see if it will run without crashing.
        pass

screen = display.set_mode((1100,800))
display.set_caption("NARUTO PAINT!")#Changes the program's caption

icon=image.load("images/Naruto_Icon.png")#Program's icon in the top left corner
display.set_icon(icon)

init() #This is to get the music to work
mixer.music.load("music/07 - the raising fighting spirit.mp3") #Load the song

background = image.load("images/hidden leaf village.jpg") #image.load loads the image
background=transform.scale(background,(1100,800)) #Scaling down the background to fit the screen
screen.blit(background,(0,0))#Blitting the background so that it covers the entire screen

color=image.load("images/colourspectrum.jpg")
color=transform.scale(color,(200,200))
screen.blit(color,(10,582))#Blitting the palette to its position

#Font
font.init() #This is to get the font working
font=font.SysFont("Agency FB",35) # I chose "Agency FB" font.
                                  #The size I want it to be is 35
#Canvas
canvasRect=Rect(380,100,700,550)
draw.rect(screen,(255,255,255),canvasRect) #Canvas

#Tool icons
pencil=image.load("images/pencilicon.png")
screen.blit(pencil,(1030,730)) #Blitting the tool icons

eraser=image.load("images/erasericon.png")
screen.blit(eraser,(1028,668))

spray=image.load("images/spray can.png")
screen.blit(spray,(963,662))

eyedropper=image.load("images/eyedropper.png")
screen.blit(eyedropper,(908,670))

random=image.load("images/randomicon.png")
screen.blit(random,(841,658))

line=image.load("images/line.png")
screen.blit(line,(905,725))

rect=image.load("images/rectangle.png")
rect=transform.scale(rect,(45,45))
screen.blit(rect,(730,730))

rectfill=image.load("images/fillrect.png")
rectfill=transform.scale(rectfill,(55,55))
screen.blit(rectfill,(725,665))

ellipse=image.load("images/ellipse.png")
ellipse=transform.scale(ellipse,(45,45))
screen.blit(ellipse,(788,730))

ellipsefill=image.load("images/fillellipse.png")
ellipsefill=transform.scale(ellipsefill,(45,45))
screen.blit(ellipsefill,(788,670))

bucket=image.load("images/bucket.png")
screen.blit(bucket,(844,729))

paintbrush=image.load("images/paintbrush.png")
screen.blit(paintbrush,(965,725))

music=image.load("images/musicicon.png")
screen.blit(music,(215,730))

load=image.load("images/loadicon.png")
screen.blit(load,(215,665))

save=image.load("images/save.png")
screen.blit(save,(275,665))

undo=image.load("images/undo.png")
screen.blit(undo,(216,610))

redo=image.load("images/redo.png")
screen.blit(redo,(278,610))

restart=image.load("images/restarticon.png")
screen.blit(restart,(280,730))

stampicon=image.load("images/stamp icon.png")
screen.blit(stampicon,(402,12))

backgroundicon=image.load("images/background icon.png")
screen.blit(backgroundicon,(402,63))

#Description Images
pencil_description=image.load("images/pencil description.png")
eraser_description=image.load("images/eraser description.png")
spraypaint_description=image.load("images/spraypaint description.png")
paintbrush_description=image.load("images/paintbrush description.png")
bucket_description=image.load("images/bucket description.png")
rect_description=image.load("images/rectangle description.png")
rectfill_description=image.load("images/filled rectangle description.png")
ellipse_description=image.load("images/ellipse description.png")
filled_ellipse_description=image.load("images/filled ellipse description.png")
line_description=image.load("images/line description.png")
random_description=image.load("images/random tool description.png")
eyedropper_description=image.load("images/eyedropper description.png")
stamps_descriptions=image.load("images/stamps description.png")
restart_description=image.load("images/restart description.png")
music_description=image.load("images/music description.png")
save_description=image.load("images/save description.png")
load_description=image.load("images/load description.png")
undo_description=image.load("images/undo description.png")
redo_description=image.load("images/redo description.png")
background_tab=image.load("images/background tab description.png")
stamp_tab=image.load("images/stamps tab description.png")
backgrounds_descriptions=image.load("images/backgrounds description.png")

#Variables for tool icons
pencilRect=Rect(1025,725,55,55)
paintbrushRect=Rect(965,725,55,55)
recttRect=Rect(725,725,55,55)
eraserRect=Rect(1025,665,55,55)
sprayRect=Rect(965,665,55,55)
bucketRect=Rect(845,725,55,55)
lineRect=Rect(905,725,55,55)
rectfillRect=Rect(725,665,55,55)
ellipseRect=Rect(785,725,55,55)
ellipsefillRect=Rect(785,665,55,55)
randomRect=Rect(845,665,55,55)
eyedropperRect=Rect(905,665,55,55)
musicRect=Rect(215,725,55,55)
loadRect=Rect(215,665,55,55)
restartRect=Rect(275,725,55,55)
saveRect=Rect(275,665,55,55)
undoRect=Rect(215,605,55,55)
redoRect=Rect(275,605,55,55)

#Tab Icons
tab1Rect=Rect(400,10,35,35)
tab2Rect=Rect(400,60,35,35)

#Tab Box
tabRect=Rect(450,5,630,90) #Empty tab box

#Description Box
descriptionRect=Rect(380,667,340,115) #Empty description box

#Stamps and Thumbnails
Narutostamp=image.load("images/narutostamp.png")
sakurastamp=image.load("images/sakura stamp.png")
orochimarustamp=image.load("images/orochimaru stamp.png")
obitostamp=image.load("images/obito stamp.png")
kakashistamp=image.load("images/kakashi stamp.png")
itachistamp=image.load("images/itachi stamp.png")
sasukestamp=image.load("images/sasuke stamp.png")

NarutoThumbnail=image.load("images/naruto_Thumbnail.png")
screen.blit(NarutoThumbnail,(995,13)) #Pics of stamp thumbnails

sakuraThumbnail=image.load("images/sakura_Thumbnail.png")
screen.blit(sakuraThumbnail,(905,10))

sasukeThumbnail=image.load("images/sasuke_Thumbnail.png")
screen.blit(sasukeThumbnail,(820,10))

kakashiThumbnail=image.load("images/kakashi_Thumbnail.png")
screen.blit(kakashiThumbnail,(725,11))

orochimaruThumbnail=image.load("images/orochimaru_Thumbnail.png")
screen.blit(orochimaruThumbnail,(630,10))

itachiThumbnail=image.load("images/itachi_Thumbnail.png")
screen.blit(itachiThumbnail,(545,20))

obitoThumbnail=image.load("images/obito_Thumbnail.png")
screen.blit(obitoThumbnail,(452,11))

#Stamp Rects
stamp1Rect= Rect(995,10,80,80)
stamp2Rect=Rect(905,10,80,80)
stamp3Rect= Rect(815,10,80,80)
stamp4Rect=Rect(725,10,80,80)
stamp5Rect=Rect(635,10,80,80)
stamp6Rect=Rect(545,10,80,80)
stamp7Rect=Rect(455,10,80,80)

#Background Thumbnails
background_1=image.load("images/5-small.jpg")
background_1=transform.scale(background_1,(143,82)) #Scaling the images down to thumbnail size

background_2=image.load("images/6-small.png")
background_2=transform.scale(background_2,(143,82))

background_3=image.load("images/7-small.jpg")

background_4=image.load("images/8-small.jpg")
background_4=transform.scale(background_4,(143,82))

full_background1=image.load("images/5-full.jpg")
full_background1=transform.scale(full_background1,(700,550))#Scaled down to the canvas size to fit

full_background2=image.load("images/6-full.png")
full_background2=transform.scale(full_background2,(700,550))

full_background3=image.load("images/7-full.jpg")
full_background3=transform.scale(full_background3,(700,550))

full_background4=image.load("images/8-full.jpg")
full_background4=transform.scale(full_background4,(700,550))

#Background Rects
background1Rect=Rect(930,10,144,80) #Rects of the background tools
background2Rect=Rect(780,10,144,80)
background3Rect=Rect(630,10,143,80)
background4Rect=Rect(480,10,143,80)

#Rectangles for colour
colorRect=Rect(10,582,200,200) #Rects for colour palette
previewRect=Rect(10,529,50,50) #Actual preview rect for current colour
borderprevRect=Rect(10,527,51,51) #Outline for preview rect

c=(0,0,0) #Current colour when the program starts
draw.rect(screen,c,previewRect)
tool = "pencil" #Tool when the program starts
tab="tab1" #Tab when the program starts
mx,my = 0,0
size=10 #Size when the program starts
white=(255,255,255)
black=(0,0,0)
undolist=[screen.subsurface(canvasRect).copy()]#Makes sure that a picture of the canvas will be in the list
undopos=0
up_cropped = background.subsurface((379,99,701,1))#saving the outside of the canvas rect
down_cropped = background.subsurface((379,650,701,1))# 1 pixel around the canvas
left_cropped = background.subsurface((378,99,1,552))
right_cropped = background.subsurface((1080,99,1,552))
running =True
while running:
    click=False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==MOUSEBUTTONUP:
            if canvasRect.collidepoint(mx,my):
                if undopos<len(undolist)-1: #Checks if list is empty
                    del undolist[undopos+1:]
                undolist+=[screen.subsurface(canvasRect).copy()]
                undopos+=1 #Adds to the undopos to keep track
        if e.type==MOUSEBUTTONDOWN:
            click=True
            sx,sy=e.pos #This will be used for tools later on (start x and start y coords)
            back=screen.subsurface(canvasRect).copy() #A copy of the canvas is being made everytime the mouse is clicked
            if e.button==4: #Scrolling for bigger size
                size+=1
            if e.button==5: #Scrolling for smaller size
                size-=1
    if size<=0:
        size=1 #This is set so that the program won't crash (size can't be below 0)
    if size>=1000:
        size=999#This is so that the size won't be too big. In this case the size can't be more than 999
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    #Canvas Use
    canvasUSe=Rect(379,99,702,552)#Rect that outlines the canvas
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        draw.rect(screen,(0,0,0),(canvasUSe),1) #Rect that's drawn on the screen when using left click

    elif mb[1]==1 and canvasRect.collidepoint(mx,my): #Scroll click
        draw.rect(screen,(0,0,0),(canvasUSe),1)

    elif mb[2]==1 and canvasRect.collidepoint(mx,my): #Right click
        draw.rect(screen,(0,0,0),(canvasUSe),1)

    else:
        screen.blit(up_cropped,(379,99))
        screen.blit(down_cropped,(379,650)) #This is so that when the user stops clicking, the black outline goes away with the original images. If this wan't here, the drawn rects would stay on the canvas.
        screen.blit(left_cropped,(379,99))
        screen.blit(right_cropped,(1080,99))

    #Creates a box around the tool
    draw.rect(screen,(0),pencilRect,2) #Black rects
    draw.rect(screen,(0),paintbrushRect,2)
    draw.rect(screen,(0),recttRect,2)
    draw.rect(screen,(0),bucketRect,2)
    draw.rect(screen,(0),lineRect,2)
    draw.rect(screen,(0),rectfillRect,2)
    draw.rect(screen,(0),ellipseRect,2)
    draw.rect(screen,(0),ellipsefillRect,2)
    draw.rect(screen,(0),randomRect,2)
    draw.rect(screen,(0),eraserRect,2)
    draw.rect(screen,(0),sprayRect,2)
    draw.rect(screen,(0),eyedropperRect,2)
    draw.rect(screen,(0),restartRect,2)
    draw.rect(screen,(0),saveRect,2)
    draw.rect(screen,(0),loadRect,2)
    draw.rect(screen,(0),musicRect,2)
    draw.rect(screen,(0),undoRect,2)
    draw.rect(screen,(0),redoRect,2)
    draw.rect(screen,(white),tab2Rect)#White rect in the background of the tab rects
    draw.rect(screen,(white),tab1Rect)
    draw.rect(screen,(0),tab1Rect,2)
    draw.rect(screen,(0),tab2Rect,2)

    #Tab icons
    screen.blit(stampicon,(402,12))
    screen.blit(backgroundicon,(402,63))

    #Tab Box
    draw.rect(screen,(255,255,255),tabRect)#White rect
    draw.rect(screen,(0),tabRect,2)#Black outline

    #Description Box
    draw.rect(screen,(255,255,255),descriptionRect)#Description box white rect
    draw.rect(screen,(0),descriptionRect,2)#Description box black outline

    #Colour
    draw.rect(screen,(255,255,255),(10,582,200,200),1)#White borders
    draw.rect(screen,(255,255,255),previewRect,3)

    #Hovering
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(eraserRect),2) #Draws a red box when hovering on top of each tool

    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(pencilRect),2)

    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(sprayRect),2)

    if eyedropperRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(eyedropperRect),2)

    if lineRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(lineRect),2)

    if bucketRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(bucketRect),2)

    if paintbrushRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(paintbrushRect),2)

    if randomRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(randomRect),2)

    if ellipsefillRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(ellipsefillRect),2)

    if ellipseRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(ellipseRect),2)

    if recttRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(recttRect),2)

    if rectfillRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(rectfillRect),2)

    if stamp1Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(stamp1Rect),2)

    if stamp2Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(stamp2Rect),2)

    if stamp3Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(stamp3Rect),2)

    if stamp4Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(stamp4Rect),2)

    if stamp5Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(stamp5Rect),2)

    if stamp6Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(stamp6Rect),2)

    if stamp7Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(stamp7Rect),2)

    if undoRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(undoRect),2)

    if redoRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(redoRect),2)

    if musicRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(musicRect),2)

    if loadRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(loadRect),2)

    if saveRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(saveRect),2)

    if restartRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(restartRect),2)

    if tab1Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(tab1Rect),2)

    if tab2Rect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),(tab2Rect),2)

    #Selecting Colour
    if mb[0]==1 and colorRect.collidepoint(mx,my):
        c=screen.get_at((mx,my)) #Gets colour of where the mouses' position is
        draw.rect(screen,c,(10,529,50,50),0)#Colour preview box
        screen.set_clip(colorRect) #Boundry for the little rect that's drawn where the colour is currently at
        screen.blit(color,(10,582)) #Blitting the palette over and over because the black rect that's drawn needs to be reset
        draw.rect(screen,(0,0,0),(mx-5,my-5,10,10),1)#Black box that is set wherever the user selected colour from last
        screen.set_clip(None)

    #Selecting tools
    if mb[0]==1 and pencilRect.collidepoint(mx,my): #If mouse is clicked and it is colliding with the rect of the tools
        tool = "pencil"
    if mb[0]==1 and eraserRect.collidepoint(mx,my):
        tool = "eraser"
    if mb[0]==1 and sprayRect.collidepoint(mx,my):
        tool = "spraypaint"
    if mb[0]==1 and eyedropperRect.collidepoint(mx,my):
        tool = "eyedropper"
    if mb[0]==1 and paintbrushRect.collidepoint(mx,my):
        tool = "paintbrush"
    if mb[0]==1 and bucketRect.collidepoint(mx,my):
        tool = "bucket"
    if mb[0]==1 and lineRect.collidepoint(mx,my):
        tool = "line"
    if mb[0]==1 and recttRect.collidepoint(mx,my):
        tool = "rect"
    if mb[0]==1 and rectfillRect.collidepoint(mx,my):
        tool = "rectfill"
    if mb[0]==1 and ellipseRect.collidepoint(mx,my):
        tool = "ellipse"
    if mb[0]==1 and ellipsefillRect.collidepoint(mx,my):
        tool = "ellipsefill"
    if mb[0]==1 and randomRect.collidepoint(mx,my):
        tool = "random"

    #Selecting Tabs
    if mb[0]==1 and tab1Rect.collidepoint(mx,my):
        tab="tab1"

    if mb[0]==1 and tab2Rect.collidepoint(mx,my):
        tab="tab2"
        tool="" #This is so that the tool resets each time. If this was not set in place, the user might be using a stamp and not know about it when using the background tab

    #Rect created around the current tool
    if tool=="pencil":
        draw.rect(screen,(0,255,0),pencilRect,2) #Green box is created

    if tool=="spraypaint":
        draw.rect(screen,(0,255,0),(sprayRect),2)

    if tool=="eraser":
        draw.rect(screen,(0,255,0),(eraserRect),2)

    if tool=="eyedropper":
        draw.rect(screen,(0,255,0),(eyedropperRect),2)

    if tool=="paintbrush":
        draw.rect(screen,(0,255,0),(paintbrushRect),2)

    if tool=="line":
        draw.rect(screen,(0,255,0),(lineRect),2)

    if tool=="bucket":
        draw.rect(screen,(0,255,0),(bucketRect),2)

    if tool=="random":
        draw.rect(screen,(0,255,0),(randomRect),2)

    if tool=="ellipsefill":
        draw.rect(screen,(0,255,0),(ellipsefillRect),2)

    if tool=="ellipse":
        draw.rect(screen,(0,255,0),(ellipseRect),2)

    if tool=="rect":
        draw.rect(screen,(0,255,0),(recttRect),2)

    if tool=="rectfill":
        draw.rect(screen,(0,255,0),(rectfillRect),2)

    if tab=="tab1":
      draw.rect(screen,(0,255,0),(tab1Rect),2)

    if tab=="tab2":
      draw.rect(screen,(0,255,0),(tab2Rect),2)

    #Descriptions
    if tool=="pencil":
        screen.blit(pencil_description,(378,665)) #Blitting an already edited image
                                                  #There are seperate descriptions for each tool
    if tool=="eraser":
        screen.blit(eraser_description,(378,665))

    if tool=="spraypaint":
        screen.blit(spraypaint_description,(378,665))

    if tool=="paintbrush":
        screen.blit(paintbrush_description,(378,665))

    if tool=="bucket":
        screen.blit(bucket_description,(378,665))

    if tool=="rect":
        screen.blit(rect_description,(378,665))

    if tool=="rectfill":
        screen.blit(rectfill_description,(378,665))

    if tool=="ellipse":
        screen.blit(ellipse_description,(378,665))

    if tool=="ellipsefill":
        screen.blit(filled_ellipse_description,(378,665))

    if tool=="line":
        screen.blit(line_description,(378,665))

    if tool=="eyedropper":
        screen.blit(eyedropper_description,(378,665))

    if tool=="random":
        screen.blit(random_description,(378,665))

    if tool=="stamp1":
        screen.blit(stamps_descriptions,(378,665))

    if tool=="stamp2":
        screen.blit(stamps_descriptions,(378,665))

    if tool=="stamp3":
        screen.blit(stamps_descriptions,(378,665))

    if tool=="stamp4":
        screen.blit(stamps_descriptions,(378,665))

    if tool=="stamp5":
        screen.blit(stamps_descriptions,(378,665))

    if tool=="stamp6":
        screen.blit(stamps_descriptions,(378,665))

    if tool=="stamp7":
        screen.blit(stamps_descriptions,(378,665))

    if tab1Rect.collidepoint(mx,my): #This is if the user hovers over each tab
        screen.blit(stamp_tab,(378,665))

    if tab2Rect.collidepoint(mx,my):
        screen.blit(background_tab,(378,665))

    if restartRect.collidepoint(mx,my): #This is for hovering because the user must know what it does. As it can restart his canvas
        screen.blit(restart_description,(378,665))

    if musicRect.collidepoint(mx,my): #Hovering description
        screen.blit(music_description,(378,665))

    if saveRect.collidepoint(mx,my): #Hovering description
        screen.blit(save_description,(378,665))

    if loadRect.collidepoint(mx,my): #Hovering description
        screen.blit(load_description,(378,665))

    if undoRect.collidepoint(mx,my): #Hovering description
        screen.blit(undo_description,(378,665))

    if redoRect.collidepoint(mx,my): #Hovering description
        screen.blit(redo_description,(378,665))


    #Tools that are only one click
    if  mb[0]==1 and undoRect.collidepoint(mx,my):
            draw.rect(screen,(0,255,0),undoRect,2) #Displays a green box for a split second
                                                   #This is setup like this because they require you to press them more than just once.
    if  mb[0]==1 and redoRect.collidepoint(mx,my):
            draw.rect(screen,(0,255,0),redoRect,2)

    if  mb[0]==1 and saveRect.collidepoint(mx,my):
            draw.rect(screen,(0,255,0),saveRect,2)

    if  mb[0]==1 and restartRect.collidepoint(mx,my):
            draw.rect(screen,(0,255,0),restartRect,2)

    if  mb[0]==1 and loadRect.collidepoint(mx,my):
            draw.rect(screen,(0,255,0),loadRect,2)

    if  mb[0]==1 and musicRect.collidepoint(mx,my):
            draw.rect(screen,(0,255,0),musicRect,2)

    if  mb[2]==1 and musicRect.collidepoint(mx,my): #This one is here because the music function requires you to use the right click
            draw.rect(screen,(0,255,0),musicRect,2)


    #Use tools
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect) #Boundry for tools so that they dont draw outside of the canvas
        if tool =="pencil":
            draw.line(screen,c,(omx,omy),(mx,my),1)#Pencil doesn't have a changeable size because it's a pencil
        if tool =="eraser":
            x=mx-omx
            y=my-omy
            d=hypot(x,y)
            if d==0: #So that the program won't crash
                d=1

            for i in range(int(d)):
                dx=int(omx+i/d*x) #This ratio will get every pixel on the line with endpoints being omx,omy and mx,my
                dy=int(omy+i/d*y)
                draw.circle(screen,(255,255,255),(dx,dy),size)
        if tool=="spraypaint":
            for x in range(0,15): #Putting it in a for loop makes it spray faster
                spray_x=randint(-1*size,size) #range of the spray from the current size
                spray_y=randint(-1*size,size)
                if spray_x**2+spray_y**2<=size**2: #Equation of a circle to find the points to draw on the circle. Also since it is "<=size", it can lie on the circle border itslef too
                        draw.circle(screen,c,(mx+spray_x,my+spray_y),0)#Thickness of 0 will make it draw a filled circle
        if tool=="line":
            screen.blit(back,canvasRect)#This is to allow the user to make one line at a time. Without this, it'll be making a bunch of lines.
            draw.line(screen,c,(sx,sy),(mx,my),size)#sx,sy is the start position. mx,my is where the user lets go to draw the line
        if tool=="bucket":
            draw.rect(screen,c,canvasRect) #filling the canvas with the selected colour
        if tool=="paintbrush":
            x=mx-omx #This finds delta x and delta y
            y=my-omy
            d=hypot(x,y)
            if d==0: #So that the program won't crash
                d=1
            for i in range(int(d)):
                dx=int(omx+i/d*x) #This ratio will get every pixel on the line with endpoints being omx,omy and mx,my
                dy=int(omy+i/d*y)
                draw.circle(screen,c,(dx,dy),size)
        if tool=="random":
            for x in range(0,80): #Putting it in a for loop makes it run faster

                xrange=randint(mx-1*size,mx+size) #Range of the rect that the tool draws lines from
                yrange=randint(my-1*size,my+size)

                randcol=randint(0,16777215) #This will be a random colour each time.

                draw.line(screen,randcol,(mx,my),(xrange,yrange),1) #Draws random coloured lines from the mouse's position to how big the range will be.
        if tool=="rect":
            screen.blit(back,canvasRect)
            draw.rect(screen,c,(sx,sy,mx-sx,my-sy),size) #Using sx and sy to make the rect
            draw.rect(screen,c,(sx-size//2,sy-size//2,size,size))#The following four rects are drawn because the corners don't get filled when above a certain size with the unfilled rect
            draw.rect(screen,c,(mx-size//2,my-size//2,size,size))
            draw.rect(screen,c,(mx-size//2,sy-size//2,size,size))
            draw.rect(screen,c,(sx-size//2,my-size//2,size,size))

        if tool=="rectfill":
            screen.blit(back,canvasRect)
            draw.rect(screen,c,(sx,sy,mx-sx,my-sy))

        rad=Rect(sx,sy,mx-sx,my-sy)#rad=radian of the ellipse
        rad.normalize() #Normalize will make it positive if the values are negative
        if tool=="ellipse":
            screen.blit(back,canvasRect)
            if rad.width>=size*2 and rad.height>=size*2: #Checking if the width and radius are in proper proportions
                draw.ellipse(screen,c,rad,size)
                draw.ellipse(screen,c,(rad.x+1,rad.y,rad.width,rad.height),size)#This is to fix the ellipse that's drawn.
                draw.ellipse(screen,c,(rad.x-1,rad.y,rad.width,rad.height),size)#The four ellipses are drawn to cover "messed up" it gives on screen
                draw.ellipse(screen,c,(rad.x,rad.y+1,rad.width,rad.height),size)
                draw.ellipse(screen,c,(rad.x,rad.y-1,rad.width,rad.height),size)
            else:
                draw.ellipse(screen,c,rad) #Draws a normal filled ellipse when the width is greater than the radius

        if tool=="ellipsefill":
            screen.blit(back,canvasRect)
            if rad.width>=4 and rad.height>=4: #Checking to see if the rad is in the required range to draw the ellipse
                draw.ellipse(screen,c,rad)

        screen.set_clip(None)
        if tool=="eyedropper": #Eyedropper tool is not in the clip because if it was,the colour preview rect would be cut out
            c = screen.get_at((mx, my))
            draw.rect(screen,c,(10,529,50,50)) #Colour preview

    #Tools that are not used on the canvas
    if  click and undoRect.collidepoint(mx,my):
          if len(undolist)-1>0: #Checks if the list is empty or not
            undopos-=1 #Subtracts from the counter to get the right position
            screen.blit(undolist[undopos],(380,100)) #Blits the capture
          if undopos<=1:
            screen.blit(undolist[undopos],(380,100))
            undopos=1 #Sets a restriction so that the index doesn't go out of range

    if  click and redoRect.collidepoint(mx,my):
        if len(undolist)-1>0:#Checks if the list is empty or not
            if undopos>=len(undolist)-1: #Makes sure the index isn't out of range
                    screen.blit(undolist[undopos],(380,100))
            else:
                    undopos+=1
                    screen.blit(undolist[undopos],(380,100))

    if mb[0]==1 and saveRect.collidepoint(mx,my): #saving the canvas
        savingName=getName(screen,False)#getName function is a file inside the folder.The file holds the function that allows the save function in this program to work.
        image.save(screen.subsurface(canvasRect),savingName)#The image of the canvas being saved

    if mb[0]==1 and loadRect.collidepoint(mx,my): #Loading an image
        draw.rect(screen,(0,255,0),loadRect,2)
        try: #Try will see if the program can do the command because tkinter likes to crash on certain computers.
            fname=filedialog.askopenfilename(filetypes=[("images","*.png;*.jpg;*.jpeg")])#This will create a window so the user can choose what type of file they can pick and what file to load.
            loadpic=image.load(fname)                 #This will load the image and
            loadpic=transform.scale(loadpic,(700,550))#scale it down to fit the canvas
            screen.blit(loadpic,(380,100))#Blits the load image
        except: #If it doesn't work it will simply let it go and not crash the program
            pass

    if mb[0]==1 and restartRect.collidepoint(mx,my):
        draw.rect(screen, (255, 255, 255), canvasRect) #draws a blank canvas

    if mb[0]==1 and musicRect.collidepoint(mx,my):
        mixer.music.play()#Right click will start the music

    if mb[2]==1 and musicRect.collidepoint(mx,my):
        mixer.music.stop()#Left click will stop the music

    #Tabs
    if tab=="tab1":
        screen.blit(NarutoThumbnail,(995,13)) #Blitting the thumbnails of the stamps to their spots
        screen.blit(sakuraThumbnail,(905,10))
        screen.blit(sasukeThumbnail,(820,10))
        screen.blit(kakashiThumbnail,(725,11))
        screen.blit(orochimaruThumbnail,(632,10))
        screen.blit(itachiThumbnail,(545,20))
        screen.blit(obitoThumbnail,(454,11))
        #Selecting Stamps
        if mb[0]==1 and stamp1Rect.collidepoint(mx,my):
            tool="stamp1"
        if mb[0]==1 and stamp2Rect.collidepoint(mx,my):
            tool="stamp2"
        if mb[0]==1 and stamp3Rect.collidepoint(mx,my):
            tool="stamp3"
        if mb[0]==1 and stamp4Rect.collidepoint(mx,my):
            tool="stamp4"
        if mb[0]==1 and stamp5Rect.collidepoint(mx,my):
            tool="stamp5"
        if mb[0]==1 and stamp6Rect.collidepoint(mx,my):
            tool="stamp6"
        if mb[0]==1 and stamp7Rect.collidepoint(mx,my):
            tool="stamp7"

    if tab=="tab2":
        draw.rect(screen,(255,255,255),tabRect,)
        draw.rect(screen,(0),tabRect,2)
        screen.blit(background_1,(930,10)) #Blitting the thumbnails of the backgrounds to their spots
        screen.blit(background_2,(780,10))
        screen.blit(background_3,(630,10))
        screen.blit(background_4,(480,10))
        #Hovering Backgrounds
        if background1Rect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(background1Rect),2) #Red hovering rect
        if background2Rect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(background2Rect),2)
        if background3Rect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(background3Rect),2)
        if background4Rect.collidepoint(mx,my):
            draw.rect(screen,(255,0,0),(background4Rect),2)
        #Selecting Backgrounds
        if mb[0]==1 and background1Rect.collidepoint(mx,my):
            tool="background1"
        if mb[0]==1 and background2Rect.collidepoint(mx,my):
            tool="background2"
        if mb[0]==1 and background3Rect.collidepoint(mx,my):
            tool="background3"
        if mb[0]==1 and background4Rect.collidepoint(mx,my):
            tool="background4"

    #Box created around the current stamp
    if tab=="tab1":
        if tool=="stamp1":
            draw.rect(screen,(0,255,0),stamp1Rect,2)#Green rect
        if tool=="stamp2":
            draw.rect(screen,(0,255,0),stamp2Rect,2)
        if tool=="stamp3":
            draw.rect(screen,(0,255,0),stamp3Rect,2)
        if tool=="stamp4":
            draw.rect(screen,(0,255,0),stamp4Rect,2)
        if tool=="stamp5":
            draw.rect(screen,(0,255,0),stamp5Rect,2)
        if tool=="stamp6":
            draw.rect(screen,(0,255,0),stamp6Rect,2)
        if tool=="stamp7":
            draw.rect(screen,(0,255,0),stamp7Rect,2)


    #Box created around the current stamp, using background, and descriptions of the backgrounds
    if tab=="tab2":
        if tool=="background1":
            draw.rect(screen,(0,255,0),background1Rect,2)
            screen.blit(full_background1,(380,100))
            screen.blit(backgrounds_descriptions,(378,665))
        if tool=="background2":
            draw.rect(screen,(0,255,0),background2Rect,2)
            screen.blit(full_background2,(380,100))
            screen.blit(backgrounds_descriptions,(378,665))
        if tool=="background3":
            draw.rect(screen,(0,255,0),background3Rect,2)
            screen.blit(full_background3,(380,100))
            screen.blit(backgrounds_descriptions,(378,665))
        if tool=="background4":
            draw.rect(screen,(0,255,0),background4Rect,2)
            screen.blit(full_background4,(380,100))
            screen.blit(backgrounds_descriptions,(378,665))

    #Using Stamps
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect) #This is to not make any stamps outside the canvas.
        if tool=="stamp1":
            screen.blit(back,canvasRect) #This is to make it an actual "stamp". #Without blitting it, it will make a trail of the picture selected
            screen.blit(Narutostamp,(mx-Narutostamp.get_width()/2,my-Narutostamp.get_height()/2)) #This is to get the mouse cursor in the middle of the picture when using the stamp
        if tool=="stamp2":
            screen.blit(back,canvasRect)
            screen.blit(sakurastamp,(mx-sakurastamp.get_width()/2,my-sakurastamp.get_height()/2))
        if tool=="stamp3":
            screen.blit(back,canvasRect)
            screen.blit(sasukestamp,(mx-sasukestamp.get_width()/2,my-sasukestamp.get_height()/2))
        if tool=="stamp4":
            screen.blit(back,canvasRect)
            screen.blit(kakashistamp,(mx-kakashistamp.get_width()/2,my-kakashistamp.get_height()/2))
        if tool=="stamp5":
            screen.blit(back,canvasRect)
            screen.blit(orochimarustamp,(mx-orochimarustamp.get_width()/2,my-orochimarustamp.get_height()/2))
        if tool=="stamp6":
            screen.blit(back,canvasRect)
            screen.blit(itachistamp,(mx-itachistamp.get_width()/2,my-itachistamp.get_height()/2))
        if tool=="stamp7":
            screen.blit(back,canvasRect)
            screen.blit(obitostamp,(mx-obitostamp.get_width()/2,my-obitostamp.get_height()/2))
        screen.set_clip(None)

    #Displaying Text
    if canvasRect.collidepoint(mx,my):  #The canvas rect is at(380,100), so the coords have to subtracted to get the coords of the mouse inside the canvas
        cordt=font.render("X:%d  Y:%d"%(mx-380,my-100),True,(0,0,0))#While mouse is in the canvas
    else:
        cordt=font.render("X:---  Y:---",True,(0,0,0))#While mouse is not in the canvas
    size_text=font.render("Size:%d"%(size),True,(0,0,0)) #Displays the size on the screen
    screen.blit(background.subsurface((260,10,140,80)),(260,10))#This is so that the coords dont get overlapped by eachother when they change
    screen.blit(cordt,(260,10)) # Current Coords on the canavs
    screen.blit(size_text,(260,50))#Current Size

    omx,omy = mx,my
    display.flip()
quit()

