import webbrowser
from tkinter import * 
import customtkinter
from PIL import ImageTk, Image
# MED PIL kan vi sætte billeder ind til senere.

# Laver et dictionary med nødsituationsnavne og deres links
health_emergencies = {'Hjertestop': 'https://hjertestarter.dk/saadanredderduliv/hjertestart-trin-for-trin',
                      'Blodprop i hjernen': 'https://hjerteforeningen.dk/min-hjerte-kar-sygdom/apopleksi-blodprop-i-hjernen-og-hjernebloedning/',
                      'Kvælning': 'https://www.falck.dk/foerstehjaelp/saadan-goer-du/vejrtraekning/heimlich/',
                      'Blødning': 'https://www.falck.dk/foerstehjaelp/saadan-goer-du/bloedning/ydre-bloedninger/',
                      'Forgiftelse': 'https://www.bispebjerghospital.dk/giftlinjen/alt-om-gift/foerstehjaelp/Sider/default.aspx'}

# print listen af nødtilfælde og deres numre 
#for i, emergency in enumerate(health_emergencies.keys()):
    #print(f"{i+1}. {emergency}")


def clicked(choice):
    # Giver brugeren mulighed for at nedskrive numret på den forekomne nødsituation
    while True:
        try:
            if choice in range(1, len(health_emergencies)+1):
                break
            else:
                print("Fejl. Indtast et nummer mellem 1 og", len(health_emergencies))
        except ValueError:
            print("Fejl. Indtast et nummer.")

    # open the selected website in a new tab in the default browser
    emergency = list(health_emergencies.keys())[choice-1]
    website = health_emergencies[emergency]
    print("Åbner websiden for", emergency)
    webbrowser.open_new_tab(website)

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.geometry("400x400")
#canvas= Canvas(root, width= 600, height= 400)
#canvas.pack()

#img1 = Image.open("C:/Users/g-elr/Desktop/Pictures/Hjertestop_Preeksamen.png")
#img2 = Image.open("C:/Users/g-elr/Desktop/Pictures/Slagtilfælde.jpg")
#img3 = Image.open("C:/Users/g-elr/Desktop/Pictures/choking.png")
#img4 = Image.open("C:/Users/g-elr/Desktop/Pictures/blødning.jpg")
#img5 = Image.open("C:/Users/g-elr/Desktop/Pictures/forgiftelse.jpg")
img = Image.open("C:/Users/g-elr/Desktop/Pictures/Ambulance.jpg")
#imgHjertestop = ImageTk.PhotoImage(img1)
#imgSlagtilfælde = ImageTk.PhotoImage(img2)
#imgKvælning = ImageTk.PhotoImage(img3)
#imgBlødning = ImageTk.PhotoImage(img4)
#imgForgiftelse = ImageTk.PhotoImage(img5)

#resized_image1= imgHjertestop.resize((300,205), Image.ANTIALIAS)
#new_image1= ImageTk.PhotoImage(resized_image1)
#panelHjertstop = Label(root, image = new_image1).grid(row=0, column=0)

#resized_image2= imgSlagtilfælde.resize((300,205), Image.ANTIALIAS)
#new_image2= ImageTk.PhotoImage(resized_image2)
#panelSlagtilfælde = Label(root, image = new_image2).grid(row=0, column=1)

#resized_image3= imgKvælning.resize((300,205), Image.ANTIALIAS)
#new_image3= ImageTk.PhotoImage(resized_image3)
#panelKvælning = Label(root, image = new_image3).grid(row=0, column=2)

#resized_image4= imgBlødning.resize((300,205), Image.ANTIALIAS)
#new_image4= ImageTk.PhotoImage(resized_image4)
#panelBlødning = Label(root, image = new_image4).grid(row=0, column=3)

#resized_image5= imgForgiftelse.resize((300,205), Image.ANTIALIAS)
#new_image5= ImageTk.PhotoImage(resized_image5)
#panelForgiftelse = Label(root, image = new_image5).grid(row=0, column=4)

new_image6= ImageTk.PhotoImage(img)
panelHjertstop = Label(root, image = new_image6).grid(row=0, column=0)



buttomHjertestop = customtkinter.CTkButton(master=root, text="Hjertestop",command=lambda:clicked(1))
buttomBlodpropihjernen = customtkinter.CTkButton(master=root, text="Blodpropihjernen",command=lambda:clicked(2))
buttomKvælning = customtkinter.CTkButton(master=root, text="Kvælning",command=lambda:clicked(3))
buttomBlødning = customtkinter.CTkButton(master=root, text="Blødning",command=lambda:clicked(4))
buttomForgiftelse = customtkinter.CTkButton(master=root, text="Forgiftelse",command=lambda:clicked(5))

exit_button = customtkinter.CTkButton(root,text='Exit',command=lambda: root.quit())

# can be, n, ne, e, se, s, sw, w, nw or centor
buttomHjertestop.place(relx = 0.1, rely = 0.5, anchor = CENTER)
buttomBlodpropihjernen.place(relx = 0.3, rely = 0.5, anchor = CENTER)
buttomKvælning.place(relx = 0.5, rely = 0.5, anchor = CENTER)
buttomBlødning.place(relx = 0.7, rely = 0.5, anchor = CENTER)
buttomForgiftelse.place(relx = 0.9, rely = 0.5, anchor = CENTER)

exit_button.place(relx = 0.5, rely = 0.9, anchor = CENTER)

w = 800 # width for the Tk root
h = 650 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop()