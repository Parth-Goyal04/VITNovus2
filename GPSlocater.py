def enzolocation(x,y):
    if (x-12.972576272433912)**2+(y-79.15886082535462)**2<0.00000625:
        print("you can take a delivery from enzo")
    
def quickbiteslocation(x,y):
    if  (x-12.972907622362047)**2+(y-79.16392388302653)**2<0.00000625:
        print("you can take a delivery from quickbites")

def darlingcanteenlocation(x,y):
    if (x-12.970166973144979)**2+(y-79.15915036953444)**2<0.00000625:
        print("you can take a delivery from darling canteen")

def foodcourtlocation(x,y):
    if (x-12.97208852655021)**2+(y-79.1582451087028)**2<0.00000625:
        print("you can take a delivery from food court")

def dcbakerylocation(x,y):
    if (x-12.97208852655021)**2+(y-79.1582451087028)**2<0.00000625:
        print("you can take a delivery from dcbakery")


def arasanlocation(x,y):
    if (x-12.970977483068195)**2+(y-79.164430796518668)**2<0.00000625:
        print("you can take a delivery from arasan")

def onefoodworldlocation(x,y):
    if (x-12.97284306739387)**2+(y-79.15702259837042)**2<0.00000625:
        print("you can take a delivery from one food world")

def hangsandswigslocation(x,y):
    if (x-12.971850418564438)**2+(y-79.16468193884667)**2<0.00000625:
        print("you can take a delivery from hangs and swigs")


def main():
    x=float(input("enter latitude of your position"))
    y=float(input("enter longitude of your position"))
    enzolocation(x,y)
    quickbiteslocation(x,y)
    darlingcanteenlocation(x,y)
    foodcourtlocation(x,y)
    dcbakerylocation(x,y)
    arasanlocation(x,y)
    onefoodworldlocation(x,y)
    hangsandswigslocation(x,y)

main()
#12.969970314201683, 79.1557290406984 - anna auditorium
#12.970877892592355, 79.15951637025026 - technology tower