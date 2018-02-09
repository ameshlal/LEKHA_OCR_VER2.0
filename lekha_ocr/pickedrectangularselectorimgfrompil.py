#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import matplotlib.patches
import matplotlib.widgets as widgets
from matplotlib.widgets import RectangleSelector
import sys
from matplotlib.patches import Rectangle
import matplotlib
myendcordinates=[]
overalapchecker=[]






def checkoverlap(l1x,l1y,r1x,r1y,l2x,l2y,r2x,r2y):
  #checking overlap
        
    # If one rectangle is on left side of other
    if l1x > r2x or l2x > r1x :
        print("i am printing in first if condition")
        return False
 
    #If one rectangle is above other
    if l1y > r2y or l2y > r1y :
        print("i am printing in second if condition")
        return False    
    return True

img = np.array(Image.open('/home/space-kerala/Downloads/test1.png'), dtype=np.uint8)
#img = mpimg.imread('/home/sajaras/Downloads/saj.png')
#lum_img = img[:, :, 0]
#imgv = plt.imshow(lum_img)

#xdata = np.linspace(0,9*np.pi, num=301)
#ydata = np.sin(xdata)

fig, ax = plt.subplots()
point, = ax.plot([],[], marker="o", color="crimson")
ax.imshow(img, aspect = 'equal',extent = None)







#fig, ax = plt.subplots()
#point, = ax.plot([],[], marker="o", color="crimson")
#line, = ax.imshow(lum_img)



def line_select_callback(eclick, erelease):
    #print(eclick)
    #print(erelease)
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    rid = fig.canvas.mpl_connect('button_press_event', lambda event: outsideclick(event,cid))
    cid = fig.canvas.mpl_connect('key_press_event', lambda event: press(event,x1,y1,x2,y2,cid))
    #if it is inside already drawn rectangles
    l2x = x1 
    l2y = y1
    r2x = x2
    r2y = y2
    count =len(overalapchecker)
    
    i = 0
    while i < count:
        l1x = overalapchecker[i][0]
        l1y = overalapchecker[i][1]
        r1x = overalapchecker[i][2]
        r1y = overalapchecker[i][3]
        print(l1x,l1y,r1x,r1y)
        ovrlap = checkoverlap(l1x,l1y,r1x,r1y,l2x,l2y,r2x,r2y)
        print(ovrlap)  
        if(ovrlap) :
            print(ovrlap)
            print(cid)     
            rs.to_draw.set_visible(False)
            fig.canvas.mpl_disconnect(cid)
           
              
      
       #print("overlap[i]=",overalapchecker[i][1])
        i = i +1 
        
   
   
    #print(cid)
  #  print(cid)
   # rect = plt.Rectangle( (min(x1,x2),min(y1,y2)), np.abs(x1-x2), np.abs(y1-y2),fill =False )
   # ax.add_patch(rect)



rs = RectangleSelector(ax,line_select_callback,
                       drawtype='box', useblit=False, button=[1], 
                       minspanx=2, minspany=2, spancoords='pixels', 
                       interactive=True)




def press(event,x1,y1,x2,y2,cid):
    print('press', event.key)
   # print (x1,y1,x2,y2,cid)
    sys.stdout.flush()
    if event.key == 'enter':
        print("Enter Key pressed")
        print("current selection box id=",cid)
        width = x2-x1
        height = y2-y1
        print(width,height)
        myendcordinates.append((x1,y1,width,height))
        overalapchecker.append((x1,y1,x2,y2))
        print(myendcordinates)
        

        #print(myendcordinates) 
        rect = plt.Rectangle( (min(x1,x2),min(y1,y2)), np.abs(x1-x2), np.abs(y1-y2),fill =False,picker=True)
        ax.add_patch(rect)
        fig.canvas.mpl_connect('key_press_event', lambda event: deletepress(event,rect,cid))

      #  rect.set_visible(False)  

   # elif event.key != 'enter':    
   #        print("disconnecting id=",cid) 
   #        plt.disconnect(cid)               

def outsideclick(event,cid):
  #  print(event.xdata,event.ydata)
    print("disconnecting",cid)
   # plt.disconnect(cid)
    fig.canvas.mpl_disconnect(cid)     
    
def deletepress(event,rect,cid):
    if event.key == 'delete':    
        rect.set_visible(False)  
        myendcordinates.clear()
        print(myendcordinates)



#def callback(event):
  #  print (event.xdata, event.ydata)


#plt.disconnect(cid)
#fig.canvas.callbacks.connect('button_press_event', callback)
def onpickrect(event):
   
    if isinstance(event.artist, Rectangle):
        print("hey you are inside a rectangle")
        

def onpick1(event):
   
    if isinstance(event.artist, Rectangle):
        patch = event.artist
        height=patch.get_height()
        #rectevent = event
        dx1 = patch.get_x()
        dy1 = patch.get_y()
        dh1 = patch.get_height()
        dw1 = patch.get_width() 
        patch.get_path()
        
        print('onpick1 patch:', patch.get_path())
        # patch.set_visible(False)
        print(dx1,dy1,dw1,dh1)
        patch.remove()
        # matplotlib.axes.Axes.relim(self)
        print('rectangle removed')
        myendcordinates.remove((dx1,dy1,dw1,dh1))
        print(myendcordinates)
        dx2 = dx1 + dw1
        dy2 = dy1 + dh1 
        overalapchecker.remove((dx1,dy1,dx2,dy2))  
       
def onclick(event,patch,connection_id):
    if event.dblclick:
        patch =event.artist
      #  print('double clicked')
     #   print(patch)
        patch.get_path()
        dx1 = patch.get_x()
        dy1 = patch.get_y()
        dh1 = patch.get_height()
        dw1 = patch.get_width() 
        patch.get_path()
        # patch.set_visible(False)
        print(dx1,dy1,dw1,dh1)
        patch.remove()
        # matplotlib.axes.Axes.relim(self)
        print('rectangle removed')
        myendcordinates.remove((dx1,dy1,dw1,dh1))
        print(myendcordinates)
        dx2 = dx1 + dw1
        dy2 = dy1 + dh1 
        overalapchecker.remove((dx1,dy1,dx2,dy2))
        fig.canvas.mpl_disconnect(connection_id)
        
        #patch.relim()
        # print(overalapchecker)  



fig.canvas.mpl_connect('pick_event', onpick1)

plt.show()










