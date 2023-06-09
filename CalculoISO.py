from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image, ImageChops, ImageEnhance, ImageOps


ventana=Tk()# llama a la libreria TK
##para formato de tamaño
ventana.geometry("740x500")

ventana.title("Ajustes de ISO")
ventana.resizable(False,False)


##logo
imagen=PhotoImage(file="header2.PNG")
#imagen = imagen.zoom(1) #with 250,
imagen = imagen.subsample(2, 2)
Limag=Label(ventana,image=imagen).place(x=0,y=0)


#-------------------------------------------------------------------------
#--------------Calculo Recomendaciones
#-----------------------------------------------------------




def pro():
    
    
    DR={'1':[(-14,-2),(-17,-4),(-21,-6),(-26,-7),(-31.-9),(-37,-10),(-45,-13),(-52,-15),(-61,-18),(-70,-21)],
        '2':[(-11,1),(-13,0),(-16,-1),(-20,-1),(-24,-1),(-28,-1),(-33,-1),(-38,-1),(-45,-2),(-51,-2)],
        '3':[(0,0),(0,0),(-7,8),(-9,10),(-11,11),(-13,14),(-15,17),(-18,19),(-21,22),(-24,25)],
        '4':[(-4,8),(-4,9),(-4,10),(-5,14),(-5,19),(-5,21),(-6,26),(-6,31),(-7,36),(-7,42)],
        '5':[(12,0),(13,0),(15,0),(19,0),(22,0),(27,0),(32,0),(37,0),(43,0),(49,0)],
        '6':[(15,3),(17,4),(20,5),(25,6),(29,7),(36,9),(42,10),(49,12),(57,14),(64,15)],
        '7':[(-6,-22),(-7,-27),(-8,32),(-10,-39),(-14,-48),(-18,-59),(-23,-78),(-36,-101),(-52,-133),(-76,-169)],
        '8':[(-3,-19),(-3,-23),(-4,-28),(-5,-34),(-7,-41),(-9,-50),(-11,-62),(-16,-76),(-23,-93),(-31,113)],
        '9':[(3,-13),(4,-16),(5,-19),(6,-23),(6,-18),(8,-33),(10,-39),(12,-46),(13,-52),(15,-60)],
        '10':[(0,0),(0,0),(14,-10),(17,-12),(19,-15),(23,-18),(28,-21),(32,-25),(37,-28),(42,-33)],
        '11':[(10,-6),(13,-7),(17,-7),(21,-8),(25,-9),(30,-11),(37,-12),(44,-13),(51,-14),(59,-16)],
        '12':[(16,0),(20,0),(24,0),(29,0),(34,0),(41,0),(49,0),(57,0),(65,0),(75,0)],
        '13':[(19,3),(24,4),(29,5),(35,6),(41,7),(50,9),(59,10),(69,12),(79,14),(90,15)],
        '14':[(25,7),(34,10),(43,13),(52,16),(62,20),(75,25),(90,30),(106,36),(123,43),(142,50)],
        '15':[(21,14),(36,18),(44,22),(54,27),(66,33),(80,41),(95,49),(112,58),(131,68),(151,79)],
        '16':[(37,14),(50,20),(62,25),(77,32),(94,40),(114,50),(136,60),(161,72),(188,85),(218,100)],
        '17':[(35,21),(46,28),(56,34),(70,43),(84,53),(102,66),(125,79),(148,94),(173,110),(201,129)],
        '18':[(26,-13),(33,-15),(40,-18),(48,-22),(59,-26),(70,-31),(83,-37),(97,-44),(113,-50),(129-58)],
        '19':[(30,0),(48,0),(58,0),(70,0),(85,0),(101,0),(120,0),(141,0),(163,0),(187,0)],
        '20':[(53,14),(68,20),(83,25),(102,32),(125,40),(151,50),(180,60),(213,72),(248,85),(287,100)],
        '21':[(59,20),(78,30),(98,40),(120,50),(181,80),(220,100),(261,120),(308,145),(357,170)],
        '22':[(120,0),(150,0),(180,0),(220,0),(260,0),(320,0),(380,0),(440,0),(500,0),(580,0)],
        '23':[(140,20),(180,30),(220,40),(270,50),(315,65),(400,80),(480,100),(560,120),(645,145),(750,170)],
        #'24':[(180,60),(220,70),(260,80),(315,95),(370,110),(440,130),(520,150),(610,180),(700,210),(820,280)],
        '25':[(390,270),(420,270),(460,280),(510,290),(560,300),(630,320),(720,360,),(820,410),(0,0),(0,0)]}
   



    valorN =int(E1.get())
    print('Rango',valorN)
    P=int(E2.get())
    N=int(E3.get())
    list_1=[]

    li=[]

    #print(valorN,P,N)


    def calcuP(li, N, P):
        index=0
        h=0
        if N<P:      
            aux = P   
            P = N    
            N = aux
                    
        for i in range(len(li)):
            if li[i][0] < 0 and li[i][1] < 0:
                if li[i][0] in range(P,N+1) and li[i][1] in range(P,N+1):
                    index = li.index(li[i])
                        
                            
                            
            elif li[i][0] >= 0 and li[i][1] >= 0:
                if li[i][0] in range(P,N+1) and li[i][1] in range(P,N+1):
                    index = li.index(li[i])
                            

            elif li[i][0] <= 0 and li[i][1] > 0 or li[i][0] >= 0 and li[i][1] < 0:
                if li[i][0] in range(P,N+1) and li[i][1] in range(P,N+1):
                            index = li.index(li[i])
            else:
                print('No esta en el rango')
        h=(list(DR)[index])
        #print(h)
        return(list(DR)[index])





    #--------------Rangos
    
    cal=0
    if valorN in range(1,4):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[0])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[0])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[0])
            cal=calcuP(list_1,N,P)
            #print(cal)
    #---------------------
    elif valorN in range(4,6):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[1])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[1])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[1])
            cal=calcuP(list_1,N,P)
            #print(cal)     

    #------------------
    elif valorN in range(6,11):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[2])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[2])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[2])
            cal=calcuP(list_1,N,P)
            #print(cal)
    #---------------------------
    elif valorN in range(11,19):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[3])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[3])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[3])
            cal=calcuP(list_1,N,P)
            #print(cal) 
    #--------------------------
    elif valorN in range(19,31):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[4])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[4])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[4])
            cal=calcuP(list_1,N,P)
            #print(cal)     
    #----------------------------
    elif valorN in range(31,51):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[5])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[5])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[5])
            cal=calcuP(list_1,N,P)
            #print(cal)

    #--------------------------        
    elif valorN in range(51,81):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[6])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[6])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[6])
            cal=calcuP(list_1,N,P)
            #print(cal)
    #-----------------------------------
    elif valorN in range(88,121):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[7])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[7])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[7])
            cal=calcuP(list_1,N,P)
            #print(cal)   
    #-----------------------------
    elif valorN in range(121,181):
        print('entro')
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[8])
            cal=calcuP(list_1,N,P)
            #print()
            #return cal
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[8])
            cal=calcuP(list_1,N,P)
            #print(cal)
            #return cal
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[8])
            cal=calcuP(list_1,N,P)
            #print(cal)
            #return cal
           
    #-----------------------------
    elif valorN in range(181,251):
        if P<0 and N<0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[9])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        elif P>0 and N>0:
            for key in  DR:
                val = DR[key]
                list_1.append(val[9])
            cal=calcuP(list_1,N,P)
            #print(cal)
            
        else:
            for key in  DR:
                val = DR[key]
                list_1.append(val[9])
            cal=calcuP(list_1,N,P)
            #print(cal)
    #--------------------------
    else:
        print('No esta en el Rango')

    #####
    recomendados=cal
    print('Esto es calculo de la tabla recomendados:',recomendados)
  
     
#-------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#--------------------------------------------
#------------datos de entrada--------
    VN=int(cal)
    def check(val):
        if val == 1:
            valor1 = 'H6'
            valor2 = 'p5'
            return valor1, valor2
        elif val == 2:
            valor1 = 'H6'
            valor2 = 'n5'
            return valor1, valor2
        elif val == 3:
            valor1 = 'H6'
            valor2 = 'k5'
            return valor1, valor2
        elif val == 4:
            valor1 = 'H6'
            valor2 = 'j5'
            return valor1, valor2
        elif val == 5:
            valor1 = 'H6'
            valor2 = 'h5'
            return valor1, valor2
        elif val == 6:
            valor1 = 'H6'
            valor2 = 'g5'
            return valor1, valor2
        elif val == 7:
            valor1 = 'H7'
            valor2 = 's6'
            return valor1, valor2
        elif val == 8:
            valor1 = 'H7'
            valor2 = 'r6'
            return valor1, valor2
        elif val == 9:
            valor1 = 'H7'
            valor2 = 'n6'
            return valor1, valor2
        elif val == 10:
            valor1 = 'H7'
            valor2 = 'k6'
            return valor1, valor2
        elif val == 11:
            valor1 = 'H7'
            valor2 = 'j6'
            return valor1, valor2
        elif val == 12:
            valor1 = 'H7'
            valor2 = 'h6'
            return valor1, valor2
        elif val == 13:
            valor1 = 'H7'
            valor2 = 'g6'
            return valor1, valor2
        elif val == 14:
            valor1 = 'H7'
            valor2 = 'f7'
            return valor1, valor2
        elif val == 15:
            valor1 = 'F8'
            valor2 = 'h6'
            return valor1, valor2
        elif val == 16:
            valor1 = 'H7'
            valor2 = 'e8'
            return valor1, valor2
        elif val == 17:
            valor1 = 'E8'
            valor2 = 'h6'
            return valor1, valor2
        elif val == 18:
            valor1 = 'H8'
            valor2 = 'j9'
            return valor1, valor2
        elif val == 19:
            valor1 = 'H8'
            valor2 = 'h9'
            return valor1, valor2
        elif val == 20:
            valor1 = 'H8'
            valor2 = 'e9'
            return valor1, valor2
        elif val == 21:
            valor1 = 'H8'
            valor2 = 'd9'
            return valor1, valor2
        elif val == 22:
            valor1 = 'H11'
            valor2 = 'h11'
            return valor1, valor2
        elif val == 23:
            valor1 = 'H11'
            valor2 = 'd11'
            return valor1, valor2
        elif val == 24:
            valor1 = 'H11'
            valor2 = 'c11'
            return valor1, valor2
        elif val == 25:
            valor1 = 'H11'
            valor2 = 'a11'
            return valor1, valor2

        
    
    val1,val2= check(VN)
    RA=val1
    RE= val2
    print('Tipo de norma:',RA,RE)

##-----Table Agujero

    ###Rangos de  Agujero

    DA={'G6':[(3,10),(4,12),(5,14),(6,17),(7,20),(9,25),(10,29),(12,34),(14,39),(15,44)],
    'H6':[(0,7),(0,8),(0,9),(0,11),(0,13),(0,16),(0,19),(0,22),(0,25),(0,29)],
    'J6':[(-4,3),(-4,4),(-4,5),(-5,6),(-5,8),(-6,10),(-6,13),(-6,-16),(-7,18),(-7,22)],
    'K6':[(0,0),(0,0),(-7,2),(-9,2),(-11,2),(-13,3),(-15,4),(-18,4),(-21,4),(-24,5)],
    'M6':[(-7,0),(-9,-1),(-12,-3),(-15,-4),(-17,-4),(-20,-4),(-24,-5),(-28,-6),(-33,-8),(-37,-8)],
    'N6':[(-11,-4),(-13,-5),(-16,-7),(-20,-9),(-24,-11),(-33,-14),(-38,-16),(-45,-20),(-51,-22)],
    'E7':[(14,23),(20,32),(25,40),(32,50),(40,61),(50,75),(60,90),(72,107),(85,125),(100,146)],
    'F7':[(7,16),(10,22),(13,28),(16,34),(20,41),(25,50),(30,60),(36,71),(43,83),(50,96)],
    'G7':[(3,12),(4,16),(5,20),(6,24),(7,28),(9,34),(10,40),(12,47),(14,54),(15,61)],
    'H7':[(0,9),(0,12),(0,15),(0,18),(0,21),(0,25),(0,30),(0,35),(0,40),(0,46)],
    'J7':[(-6,3),(-7,5),(-7,8),(-8,10),(-9,12),(-11,14),(-12,18),(-13,22),(-14,25),(-16,30)],
    'K7':[(0,0),(0,0),(-10,5),(-12,6),(-15,6),(-18,7),(-21,9),(-25,10),(-28,12),(-33,13)],
    'M7':[(-9,0),(-12,0),(-15,0),(-18,0),(-21,0),(-25,0),(-30,.0),(-35,0),(-40,0),(-46,0)],
    'N7':[(-13,-4),(-16,-4),(-19,-4),(-23,-5),(-28,-7),(-33,-8),(-45,-10),(-52,-12),(-60,-14)],
    'P7':[(-16,-7),(-20,-8),(-24,-9),(-29,-11),(-35,-14),(-42,-17),(-51,-21),(-59,-24),(-68,-28),(-79,-33)],
    'D8':[(20,34),(30,48),(40,62),(50,77),(65,98),(80,119),(100,146),(120,174),(145,208),(170,242)],
    'E8':[(14,28),(20,38),(25,47),(32,59),(40,73),(50,89),(60,106),(72,126),(85,148),(100,172)],
    'F8':[(7,21),(10,28),(13,35),(16,43),(20,53),(25,64),(30,76),(36,90),(43,106),(50,122)],
    'H8':[(0,14),(0,18),(0,22),(0,27),(0,33),(0,39),(0,46),(0,54),(0,63),(0,72)],
    'J8':[(-7,7),(-9,9),(-10.12),(-12,15),(-13,20),(-15,24),(-18,28),(-20,34),(-22,41),(-25,47)],
    'K8':[(0,0),(0,0),(-16,6),(-19,8),(-23,10),(-27,12),(-32,14),(-38,16),(-43,20),(-50,22)],
    'M8':[(0,0),(0,0),(-21,1),(-25,2),(-29,4),(-34,5),(-41,5),(-48,6),(-55,8),(-63,9)],
    'N8':[(-15,-1),(-20,-2),(-25,-3),(-30,-3),(-36,-3),(-42,-3),(-50,-4),(-58,-4),(-67,-4),(-77,-5)],
    'D9':[(20,45),(30,60),(40,76),(50,93),(65,112),(80,142),(100,174),(120,207),(145,245),(170,285)],
    'E9':[(14,39),(20,50),(25,61),(32,75),(40,92),(50,112),(60,134),(72,159),(85,185),(100,215)],
    'H9':[(0,25),(0,30),(0,36),(0,43),(0,52),(0,62),(0,74),(0,87),(0,100),(0,115)],
    'J9':[(-13,12),(-15,15),(-18,18),(-21,22),(-26,26),(-31,31),(-37,37),(-44,43),(-50,50),(-58,57)],
    'D10':[(20,60),(30,78),(40,96),(50,120),(65,149),(80,180),(100,220),(120,260),(145,305),(170,355)],
    'H10':[(0,40),(0,48),(0,58),(0,70),(0,84),(0,100),(0,120),(0,140),(0,160),(0,185)],
    'J10':[(-20,20),(-24,24),(-29,29),(-35,35),(-42,42),(-50,50),(-60,60),(-70,70),(-80,80),(-93,92)],
    'D11':[(20,80),(30,100),(40,130),(50,160),(65,195),(80,240),(100,290),(120,340),(145,395),(170,460)],
    'H11':[(0,60),(0,75),(0,90),(0,110),(0,130),(0,160),(0,190),(0,220),(0,250),(0,290)],
    'J11':[(-30,30),(-38,37),(-45,45),(-55,55),(-65,65),(-80,80),(-95,95),(-110,110),(-125,125),(-145,145)],
    }

    Agu=RA
    
    for i in DA:
        if i == Agu:
            val=(DA[Agu])
            #print(DA)
            #print(val)
            if valorN in range(1,4):
                R2=val[0]
                v1=R2[0]
                v2=R2[1]
                #print(v1)
            elif valorN in range(4,7):
                R2=val[1]
                v1=R2[0]
                v2=R2[1]
                #print(v1,v2)            
            elif valorN in range(7,11):
                R2=val[2]
                v1=R2[0]
                v2=R2[1]
                #print(v1)
            elif valorN in range(11,19):
                R2=val[3]
                v1=R2[0]
                v2=R2[1]
                #print(v1)
            elif valorN in range(19,31):
                R2=val[4]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(31,51):
                R2=val[5]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(51,81):
                R2=val[6]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(81,121):
                R2=val[7]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(121,181):
                R2=val[8]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(181,251):
                R2=val[9]
                v1=R2[0]
                v2=R2[1]
                #print(v1)
            AR1=v1
            AR2=v2
            print('Entro al Agujero:',AR1,AR2)
                 
#-----------------------------
#----------Table Eje
    
    
    #dic Eje
    DE={'g5':[(-3,-8),(-4,-9),(-5,-11),(-6,-14),(-7,-16),(-9,-20),(-10,-23),(-12,-27),(-14,-32),(-15,-35)],
        'h5':[(0,-5),(0,-5),(0,-6),(0,-8),(0,-9),(0,-11),(0,-13),(0,-15),(0,-18),(0,-20)],
        'j5':[(4,-1),(4,-1),(4,-2),(5,-3),(5,-4),(6,-5),(6,-7),(6,-9),(7,-11),(7,-13)],
        'k5':[(0,0),(0,0),(7,1),(9,1),(11,2),(13,2),(15,2),(18,3),(21,3),(24,4)],
        'm5':[(7,2),(9,4),(12,6),(15,7),(17,8),(20,9),(24,11),(28,13),(33.15),(37,17)],
        'n5':[(7,2),(9,4),(12,6),(15,7),(17,8),(20,9),(24,11),(28,13),(33,15),(37,17)],
        'g6':[(-3,-10),(-4,-12),(-5,-14),(-6,-17),(-7,-20),(-9,-25),(-10,-29),(-12,-34),(-14,-39),(-15,-44)],
        'h6':[(0,-7),(0,-8),(0,-9),(0,-11),(0,-13),(0,-18),(0,-19),(0,-22),(0,-22),(0,-25),(0,-29)],
        'j6':[(6,-1),(7,-1),(7,-2),(8,-3),(9,-4),(11,-5),(12,-7),(13,-9),(14,-11),(16,-13)],
        'k6':[(0,0),(0,0),(10,1),(12,1),(15,2),(18,2),(21,2),(25,3),(28,3),(33,4)],
        'm6':[(9,2),(12,4),(15,6),(18,7),(21,8),(25,9),(30,11),(35,13),(40,15),(46,17)],
        'n6':[(13,6),(16,8),(19,10),(23,12),(28,15),(33,17),(39,20),(45,23),(52,27),(60,31)],
        'p6':[(16,9),(20,12),(24,15),(29,18),(35,22),(42,26),(51,32),(59,37),(68,43),(79,50)],
        'e7':[(-14,-23),(-20,-32),(-25,-40),(-32,-50),(-40,-61),(-50,-75),(-60,-90),(-72,-107),(-85,-125),(-100,-146)],
        'f7':[(-7,-16),(-10,-22),(-13,-28),(-16,-34),(-20,-41),(-25,-50),(-30,-60),(-36,-71),(-43,-83),(-50,-96)],
        'h7':[(0,-9),(0,-12),(0,-15),(0,-18),(0,-21),(0,-25),(0,-35),(0,-40),(0,-46)],
        'j7':[(7,-2),(9,-3),(10,-5),(12,-6),(13,-8),(15,-10),(18,-12),(20,-15),(22,-18),(25,-21)],
        'k7':[(0,0),(0,0),(16,1),(19,1),(23,2),(27,2),(32,2),(38,3),(43,3),(50,4)],
        'm7':[(0,0),(0,0),(21,6),(25,7),(29,8),(34,9),(41,11),(48,13),(55,15),(63,17)],
        'n7':[(15,6),(20,8),(25,10),(30,12),(36,15),(42,17),(50,20),(58,23),(67,27),(77,31)],
        'd8':[(-20,-34),(-30,-48),(-40,-62),(-50-77),(-65,-98),(-80,-119),(-120,-174),(-145,-208),(-170,-242)],
        'e8':[(-14,-28),(-20,-38),(-25,-47),(-25,-47),(-32,-59),(-40,-73),(-50,-89),(60,-106),(-72,-126),(-85,-148),(-100,-172)],
        'f8':[(-7,-21),(-10,-18),(-13,-35),(-16,-43),(-20,-53),(-25,-54),(-30,-76),(-36,-90),(-43,-106),(-50,-122)],
        'h8':[(0,-14),(0,-18),(0,-22),(0,-27),(0,-33),(0,-39),(0,-48),(0,-54),(0,-63),(0,-72)],
        'j8':[(7,-7),(9,-9),(11,-11),(14,-13),(17,-16),(20,-19),(23,-23),(27,-27),(32,-31),(36,-36)],
        'k8':[(14,0),(18,0),(22,0),(27,0),(33,0),(39,0),(46,0),(54,0),(63,0),(72,0)],
        'd9':[(-20,-45),(-30,-60),(-40,-75),(-50,-93),(-65,-117),(-80,-142),(-100,-174),(-1200,-207),(-145,-243),(-170,-285)],
        'e9':[(-14,-39),(-20,-50),(-25,-61),(-32,-75),(-40,-92),(-50,-112),(-60,-134),(-72,-159),(-85,-185),(-100,-215)],
        'h9':[(0,-25),(0,-30),(0,-36),(0,-43),(0,-52),(0,-62),(0,-74),(0,-87),(0,-100),(0,-115)],
        'j9':[(13,-12),(15,-15),(18,-18),(22,-21),(26,-26),(31,-31),(37,-37),(44,-43),(50,-50),(58,-57)],
        'k9':[(25,0),(30,0),(36,0),(43,0),(52,0),(62,0),(74,0),(87,0),(100,0),(115,0)],
        'd10':[(-20,-60),(-30,-78),(-40,-98),(-50,-120),(-65,-149),(-80,-180),(100,-220),(-120,-260),(-145,-305),(-170,-355)],
        'h10':[(0,-40),(0,-48),(0,-58),(0,-70),(0,-84),(0,-100),(0,-120),(0,-140),(0,-160),(0,-185)],
        'j10':[(20,-20),(24,-24),(29,-29),(35,-35),(24,-24),(50,-50),(60,-60),(70,-70),(80,-80),(93,-92)],
        'k10':[(40,0),(48,0),(58,0),(70,0),(84,0),(100,0),(120,0),(140,0),(160,0),(185,0)],
        'd11':[(-20,-80),(-30,-105),(-40,-130),(-50,-160),(65,-185),(-80,-240),(100,-290),(-120,-340),(-145,-395),(-170,-460)],
        'h11':[(0,-60),(0,-75),(0,-90),(0,-110),(0,-130),(0,-160),(0,-190),(0,-220),(0,-250),(0,-290)],
        'j11':[(30,-30),(38,-37),(45,-45),(55,-55),(65,-65),(80,-80),(95,-95),(110,-110),(125,-125),(145,-145)],
        'k11':[(60,0),(75,0),(90,0),(110,0),(130,0),(160,0),(190,0),(220,0),(250,0),(290,0)],
        }

    Eje=RE

    #Rangos de los Ejes  
    for i in DE:
        if i == Eje:
            val=(DE[Eje])
            #print(DA)
            #print(val)
            if valorN in range(1,4):
                R2=val[0]
                v1=R2[0]
                v2=R2[1]
                #print(v1)
            elif valorN in range(4,7):
                R2=val[1]
                v1=R2[0]
                v2=R2[1]
                #print(v1,v2)            
            elif valorN in range(7,11):
                R2=val[2]
                v1=R2[0]
                v2=R2[1]
                print(v1)
            elif valorN in range(11,19):
                R2=val[3]
                v1=R2[0]
                v2=R2[1]
                #print(v1)
            elif valorN in range(19,31):
                R2=val[4]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(31,51):
                R2=val[5]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(51,81):
                R2=val[6]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(81,121):
                R2=val[7]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            elif valorN in range(121,181):
                R2=val[8]
                v1=R2[0]
                v2=R2[1]
                #print('Aqui si entro',v1,v2) 
            elif valorN in range(181,251):
                R2=val[9]
                v1=R2[0]
                v2=R2[1]
                #print(v1) 
            ER1=v1
            ER2=v2
            print('Entro en el Eje:',ER1,ER2)

#####----------Calculos


    V1= valorN
    
    V2=ER1/1000  #Eje
    print('primer valor del Eje:',ER1,'dividcion', V2)
    V3=ER2/1000  #Eje
    #---tipo de Norma
    TN= RA+'-'+RE

    E91.delete(0,END)
    E91.insert(0,TN)
    #----
    
    V4=AR2/1000  #######agu
    V5=AR1/1000  ### agu


    
        
         #Calculo de T. Eje 
    dmax=V2+V1
    #dimax=round(dmax,3)
    E5.delete(0,END)
    E5.insert(0,dmax)
        
    dmin=V3+V1
    E6.delete(0,END)
    E6.insert(0,dmin)

    TE=dmax-dmin
    TOE=round(TE,4)
    E7.delete(0,END)
    E7.insert(0,TOE)
    ###---Agujero
        
    Dmax=V4+V1
    E8.delete(0,END)
    E8.insert(0,Dmax)
        

    Dmin=V5+V1
    E9.delete(0,END)
    E9.insert(0,Dmin)

    TA=Dmax-Dmin
    TOA=round(TA,4)
    E10.delete(0,END)
    E10.insert(0,TOA)
        
        ###Calculo de T.Ajuste

        


##
##    ima=Image.open('jueg.PNG')
##    render=ImageTK.PhotoImage(ima)
##    img1=Label(ventana,image=render)
##    img1.image=render
##    img1.Lim.place(x=510,y=415)
    
    A=Dmin-dmax
    A1=round(A,4)
    E33.delete(0,END)
    E33.insert(0,A1)

    B=Dmax-dmin
    B1=round(B,4)
    E34.delete(0,END)
    E34.insert(0,B1)

    TOTAL=B-A
    TOT=round(TOTAL,4)
    E35.delete(0,END)
    E35.insert(0,TOT)

    global img_label

    img_label=Label(ventana)
    img_label.place(x=510,y=115)
    
    if(TE<TA):
        CA="Juego"
        E31.delete(0,END)
        E31.insert(0,CA)
        img=Image.open("jueg.png")
        new_ima= ImageTk.PhotoImage(img)
        img_label=Label(ventana,image=new_ima)
        img_label.image=new_ima
        img_label.place(x=510,y=130)
        
        
    elif(TA<TE):
        CA="Apriete"
        E31.delete(0,END)
        E31.insert(0,CA)
        img=Image.open("aprie.png")
        new_ima= ImageTk.PhotoImage(img)
        img_label=Label(ventana,image=new_ima)
        img_label.image=new_ima
        img_label.place(x=510,y=130)

    else:
        CA="Indeterminado"
        E31.delete(0,END)
        E31.insert(0,CA)
        img=Image.open("inde.png")
        new_ima= ImageTk.PhotoImage(img)
        img_label=Label(ventana,image=new_ima)
        img_label.image=new_ima
        img_label.place(x=510,y=130)
        
            
        

        
        
def clearTextInput():
    
    img_label.destroy()
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E91.delete(0,END)
    E31.delete(0,END)
    E34.delete(0,END)
    E5.delete(0,END)
    E6.delete(0,END)
    E7.delete(0,END)
    E8.delete(0,END)
    E9.delete(0,END)
    E10.delete(0,END)
    E33.delete(0,END)
    E34.delete(0,END)
    E35.delete(0,END)
    
def help():
    messagebox.showinfo('Mensaje de Ayuda','Este trabajo es tomado de las tablas del prontuario de maquinas. \n Dado caso de que no se de la resolucion verificar que los datos ingresados este acorde a las tablas trabajadas en clase.' )
    

    
    
#------------------------------------------------------------------------------
####------------Calculo Interfaz
#---------------------------------------------------------------------------

    




###ingreso de Datosy creacion de las

L1=Label(ventana,text="Diametro Nominal")  #Label -> la parte escrita 
L1.place(x=10,y=127)
E1=Entry(ventana)                       #Entry -> la parte de los cuadros
E1.place(x=15,y=145)


L2=Label(ventana,text="Valor Max del Ajuste")
L2.place(x=10,y=170)
E2=Entry(ventana)
E2.place(x=15,y=190)

L3=Label(ventana,text="Valor Min del Ajuste")  
L3.place(x=10,y=210)
E3=Entry(ventana)
E3.place(x=15,y=230)


L91=Label(ventana,text="Tipo de Norma")  
L91.place(x=10,y=270)
E91=Entry(ventana)
E91.place(x=15,y=290)





###Resultados

L5=Label(ventana,text="RESULTADOS")  
L5.place(x=305,y=110)

L90=Label(ventana,text="GRAFICO")
L90.place(x=590,y=110)

L6=Label(ventana,text="EJE")
L6.place(x=328,y=140)

L7=Label(ventana,text="dmax")
L7.place(x=200,y=160)

E5=Entry(ventana)
E5.place(x=200,y=180)

L8=Label(ventana,text="dmin")
L8.place(x=200,y=200)

E6=Entry(ventana)
E6.place(x=200,y=220)

L9=Label(ventana,text="Tolerancia.E")
L9.place(x=350,y=180)

E7=Entry(ventana)
E7.place(x=350,y=200)

#----
L10=Label(ventana,text="AGUJERO")
L10.place(x=310,y=250)

L11=Label(ventana,text="Dmax")
L11.place(x=200,y=270)

E8=Entry(ventana)
E8.place(x=200,y=295)

L12=Label(ventana,text="Dmin")
L12.place(x=200,y=320)

E9=Entry(ventana)
E9.place(x=200,y=340)

L13=Label(ventana,text="Tolerancia.A")
L13.place(x=350,y=295)

E10=Entry(ventana)
E10.place(x=350,y=315)

#-----



######tipo de Norma
##
##L16=Label(ventana,text="Tipo de Norma")
##L16.place(x=330,y=260)
##
##E13=Entry(ventana)
##E13.place(x=310,y=280)



######Tipo Ajuste

L31=Label(ventana,text="TIPO DE AJUSTE")
L31.place(x=25,y=420)

E31=Entry(ventana)
E31.place(x=15,y=440)


L32=Label(ventana,text="AJUSTES")
L32.place(x=310,y=375)

L33=Label(ventana,text="Min")
L33.place(x=200,y=400)

E33=Entry(ventana)
E33.place(x=200,y=420)

L34=Label(ventana,text="Max")
L34.place(x=200,y=440)

E34=Entry(ventana)
E34.place(x=200,y=460)


L35=Label(ventana,text="Tolerancia Del Ajuste")
L35.place(x=350,y=420)

E35=Entry(ventana)
E35.place(x=350,y=440)





###Botones 
B1=Button(ventana, text="Calcular", command= pro)
B1.place(x=490,y=460)
#print(type(B1))



B2=Button(ventana, text="Limpiar",  command=clearTextInput)
B2.place(x=560,y=460)


B3=Button(ventana, text="Ayuda", command=help)
B3.place(x=630,y=460)


ventana.mainloop()
