import sqlite3
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, GdkPixbuf
import subprocess
import interfaceMenu


class PopoverWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Page d'identification")
        
        self.conn = sqlite3.connect('utilisateurs.db')
        self.c = self.conn.cursor()
        
        self.set_border_width(10)
        self.set_default_size(580, 450)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        #Header Bar
        headerbar = Gtk.HeaderBar()
        headerbar.set_title("Logiciel de Gestion d'Hotel")
        #headerbar.set_subtitle("HeaderBar Subtitle")
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

        # box0 is the main box container which will hold the mb0
        box0 = Gtk.Box(spacing=8, orientation=Gtk.Orientation.VERTICAL)
        self.add(box0)

        # mb0 is Gtk.MenuButton which will include the coming popover
        mb0 = Gtk.MenuButton()
        mb0.set_label("Cliquer ici pour s'identifier")
        box0.pack_start(mb0, False, True, 5)
 
        # Create popover
        popover = Gtk.Popover()
            
        # vbox container for adding items in Popover menu
        vbox = Gtk.Box(spacing=1, orientation=Gtk.Orientation.VERTICAL)
        vbox.set_border_width(5)
        
        # Username
        username_label = Gtk.Label(label="Nom d'utilisateur :")
        self.username = Gtk.Entry()
        vbox.pack_start(username_label, True, True, 5)
        vbox.pack_start(self.username, True, True, 5)
        
        #Password
        password_label = Gtk.Label(label="Mot de passe :")
        self.password = Gtk.Entry()
        vbox.pack_start(password_label, True, True, 5)
        vbox.pack_start(self.password, True, True, 5)
        self.password.set_visibility(False)
        
        # Button Login
        sign_in= Gtk.ToggleButton()
        sign_in.set_label("SIGN IN")
        sign_in.connect("clicked", self.on_button_login_clicked)
        vbox.pack_start(sign_in, True, True, 5)

        # hbox is horzitontal box container for adding items sidewise 
        # in vbox of Popover menu.
        # we are packing container with widgets inside container (hbox in vbox)
        hbox = Gtk.Box(spacing=1, orientation=Gtk.Orientation.HORIZONTAL)
        hbox.set_border_width(0)
        
        #Ajout du bouton quitter       
        quitter=Gtk.CheckButton()
        quitter.set_label("Quitter")
        quitter.connect("clicked", Gtk.main_quit)
        hbox.pack_start(quitter, True, True, 5)
        
        #ajout hbox dans la boite
        vbox.pack_start(hbox, True, True, 0)
        
        #ajout du conteneur vbox et les autres widgets
        # in popover menu
        popover.add(vbox)
        popover.set_position(Gtk.PositionType.BOTTOM)
        
        # ajouter le popover a l'interieur de Gtk.MenuButton()
        mb0.set_popover(popover)

        # Montrer le widget
        popover.show_all()
        
        #Formulaire d'inscription
        mb1 = Gtk.MenuButton()
        mb1.set_label("Cliquer ici pour creer un compte")
        box0.pack_start(mb1, False, True, 5)
        
        popover1= Gtk.Popover()
        
        #Box1
        vbox1 = Gtk.Box(spacing=1, orientation=Gtk.Orientation.VERTICAL)
        vbox1.set_border_width(5)
        
        # NOM d'Utilisateur
        label_nom = Gtk.Label(label="Nom d'utilisateur :")
        self.nom = Gtk.Entry()
        vbox1.pack_start(label_nom, True, True, 5)
        vbox1.pack_start(self.nom, True, True, 5)
        
        #Prenom
        label_prenom = Gtk.Label(label="Prenom d'utilisateur :")
        self.prenom = Gtk.Entry()
        vbox1.pack_start(label_prenom, True, True, 5)
        vbox1.pack_start(self.prenom, True, True, 5)
        
        #Email
        label_email = Gtk.Label("Email")
        self.email = Gtk.Entry()
        vbox1.pack_start(label_email, True, True, 5)
        vbox1.pack_start(self.email, True, True, 5)
        
        #Password
        label_mdp = Gtk.Label(label="Mot de passe :")
        self.mdp = Gtk.Entry()
        vbox1.pack_start(label_mdp, True, True, 5)
        vbox1.pack_start(self.mdp, True, True, 5)
        self.mdp.set_visibility(False)
        
        #S'inscrire
        bouton_enregistrer = Gtk.Button(label="S'inscrire")
        bouton_enregistrer.connect("clicked", self.enregistrer_utilisateur)
        vbox1.pack_start(bouton_enregistrer, False, False, 0)
        
        
        # 4th Add quit menu item
        quitter=Gtk.CheckButton()
        quitter.set_label("Quitter")
        quitter.connect("clicked", Gtk.main_quit)
        
        hbox1 = Gtk.Box(spacing=1, orientation=Gtk.Orientation.HORIZONTAL)
        hbox1.set_border_width(0)
                
        hbox1.pack_start(quitter, True, True, 5)
         
        vbox1.pack_start(hbox1, True, True, 0)
        
        popover1.add(vbox1)
        popover1.set_position(Gtk.PositionType.BOTTOM)
        
        mb1.set_popover(popover1)
        popover1.show_all()
        

    def on_button_login_clicked(self, widget):
        username = self.username.get_text()
        password = self.password.get_text()

        if username == "user" and password == "pass":
            print("Authenticated")
            self.hide()
            #menuForm.MenuForm(self)
            interfaceMenu.FenetreApp(self)
        else:
            print("Invalid username or password")
            
    def enregistrer_utilisateur(self, button):
        nom = self.nom.get_text()
        prenom = self.prenom.get_text()
        email = self.email.get_text()
        mdp = self.mdp.get_text()

        self.c.execute('''INSERT INTO utilisateurs(nom, prenom, email, mdp) VALUES(?,?,?,?)''', (nom, prenom, email, mdp))
        self.conn.commit()

        message = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Utilisateur enregistré")
        message.run()
        message.destroy()

        self.nom.set_text("")
        self.prenom.set_text("")
        self.email.set_text("")
        self.motdepasse.set_text("")
            

win = PopoverWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()