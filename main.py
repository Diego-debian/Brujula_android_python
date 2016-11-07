#*-* coding:utf-8 *-*
#qpy:kivy
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget 
from kivy.uix.effectwidget import EffectWidget
from kivy.uix.camera import Camera
import random
kivy.require('1.9.0')

from plyer import compass

class CompasTest(App):
    def Hardware(self, *args):
        try:
            self.Encender()
            self.tetha = 0
            print "Encendiendo compas"
            if True:
                print "Empezando lectura"
                Hilo1 = Clock.schedule_interval(self.Lectura, 1 / 20.)
                Hilo2 = Clock.schedule_interval(self.Empareja_todo, 1 / 20.)
                self.Disparar()
                return True

        except NotImplementedError:
            import traceback
            traceback.print_exc()
            status = "No reconoce el sensor magnetico en su dispositivo"
            print "No reconoce el compas"
            return False


    def Encender(self, *args):
        print "Se esta encendiendo"
        compass.enable()
        
    def Apagar(self, *args):
        print "Se esta apagando"
        compass.disable()

    def Lectura(self, *args):
        x,y,z = compass.orientation
        try:
            xf = round(x,  3)
            yf = round(y,  3)
            zf = round(z,  3)
            self.Bx = xf
            self.By = yf
            self.Bz = zf
            lbl1.text = "Sensor de Campo Magnetico \nBx = "+str(xf)+"\n"+"By = "+str(yf)+"\n"+"Bz = "+str(zf)          

        except: 
            print "No hay ningun dato todavia espere"


    def Empareja_todo(self, *args):
        try:
            self.Clasifica_tetha()
            self.Dispercion1()
            self.Disparar()
        except:
            print "Fallo al emparejar todo"

    def Dispersion1(self):
        self.dis1 = Scatter()
        self.dis1.pos =  100, 300
        #self.dis1.pos =  random.randrange(100,680), 100
        self.dis1.size_hint = None, None
        #self.dis1.size = 100, 100
        self.dis1.do_rotation= False
        self.dis1.do_scale= False
        self.dis1.do_translation= False
        self.dis1.scale = 1.8
        lbl2.text= "HACK-VISION DEMO \n Angulo tetha: " + str(self.tetha)
        self.dis1.rotation = self.tetha + 90

    def Clasifica_tetha(self):
        #Sentido MAnecillas del reloj
        #Primer cuadrante
        try:
            self.tetha != None
            if ((self.Bz > -25)&(self.Bz <=0)&(self.Bx <= 0)&(self.By<=0)):
                tetha = (self.Bz*90)/25 + 90
                self.tetha = round(tetha,3)
                return self.tetha
            

                #segundo cuadrante
            if ((self.Bz>0)&(self.Bz<=25)&(self.Bx <= 0)&(self.By<=0)):
                tetha= self.Bz*90/25 + 90
                self.tetha = round(tetha,3)
                return self.tetha
                
       
                #tercer cuadrante
            if ((self.Bz>0)&(self.Bz<=25)&(self.Bx >= 0)&(self.By<=0)):
                tetha= (-1)*(self.Bz*90/25 -270) 
                self.tetha = round(tetha,3)
                return self.tetha
            
                #Quinto cuadrante
            if ((self.Bz > -25)&(self.Bz <=0)&(self.Bx >= 0)&(self.By<=0)):         
                tetha= (-1)*(self.Bz*90/25 - 270)
                self.tetha = round(tetha,3)
                return self.tetha

        except:
            print "Nada"
            
       

    def Dispersion2(self):
        self.dis2 = Scatter()
        self.dis2.pos =  -90, -50
        #self.dis2.pos =  random.randrange(100,680), 100
        self.dis2.size_hint = None,None
        #      self.dis2.size = 86, 86
        self.dis2.do_rotation= False
        self.dis2.do_scale= False
        self.dis2.do_translation= False
        self.dis2.rotation = 0
        self.dis2.scale= 1.7


    def Animacion1(self, *args):
        global Anim
        lol = Widget()
        Anim = Image()
        Anim.source = "img/fondo_brujula.png"
        # Anim.size = 700,700
        #Anim.source = "img/caballo.zip"
        #Anim.anim_delay=(0.15)
        # Anim.pos_hint= {"x": -0.1, "center_y": -1}
        # Anim.pos = 10, 10
        #Anim.pos = random.randrange(100,680), random.randrange(100,460)
        self.dis1.add_widget(Anim)
        lol.add_widget(self.dis1)
        self.widget1.add_widget(lol)


    def Camara(self, *args):
#        self.Dispersion2()

        camwidget = Widget()  #Create a camera Widget
        cam = Camera()        #Get the camera
        cam.resolution=(640,480)
        cam.size= 1000,800
        cam.pos=(-100,-100)

        cam.play=True         #Start the camera

        camwidget.add_widget(cam) 
        # self.widget1.add_widget(camwidget) 
        self.dis2.add_widget(camwidget)
        self.widget1.add_widget(self.dis2)




    def Label1(self):
        global lbl1
        lbl1 = Label()
     #   lbl1.text =  "Esperando instrucciones:"
        lbl1.pos = 200,100
        self.widget1.add_widget(lbl1)
        

    def Label2(self):
        global lbl2
        lbl2 = Label()
     #   lbl2.text =  "Esperando instrucciones:"
        lbl2.pos = 200,10
        self.widget1.add_widget(lbl2)

  
    def Disparar(self):
        self.x = 0
        Hilo2 = Clock.schedule_interval(self.disparo1, 0.9)
     #   self.disparo1()
       

    def disparo1(self, *args):
        if self.opcion== 1:
            self.dis1.remove_widget(Anim)
            self.widget1.remove_widget(self.dis1)          
            self.opcion=0
   
        if self.opcion == 0:
            self.Dispersion1()
            self.Animacion1()
            self.x = self.x + 10
            self.opcion=1

        
 
    
    def build(self):
        self.opcion = 0        
        self.widget1 = Widget()
        self.Dispersion2()
        self.Camara()
        self.Label1()
        self.Label2()
        self.Hardware()
    
        
        return self.widget1

if __name__=='__main__':
    CompasTest().run()
