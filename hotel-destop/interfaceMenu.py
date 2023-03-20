import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GdkPixbuf
import modifierNom
import formulaire

class FenetreApp(Gtk.Window):
    def __init__(self, login_form):
        self.login_form = login_form
        
        Gtk.Window.__init__(self, title="Logiciel de Gestion d'Hotel")
        self.set_size_request(840, 580)
        self.set_position(Gtk.WindowPosition.CENTER)
        grid = Gtk.Grid()
        self.add(grid)

        menubar = Gtk.MenuBar()
        menubar.set_hexpand(True)
        grid.attach(menubar, 0, 0, 1, 1)
        
        #Bar header
        headerbar = Gtk.HeaderBar()
        headerbar.set_title("Logiciel de Gestion d'Hotel")
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

        #Menu Gestion de l'hotel
        menuitem_edit = Gtk.MenuItem(label="EDITION")
        menubar.append(menuitem_edit)
        
        #Sous menu Gestion de l'hotel
        submenu_edit = Gtk.Menu()
        menuitem_edit.set_submenu(submenu_edit)
        menuitem_modif_nom = Gtk.MenuItem(label="Modifier le nom de l'hotel")
        submenu_edit.append(menuitem_modif_nom)
        menuitem_modif_nom.connect('activate', self.formulaire_modif_nom)
        
        menuitem_modif_tarif = Gtk.MenuItem(label="Modifier les tarifs")
        submenu_edit.append(menuitem_modif_tarif)
        menuitem_modif_tarif.connect('activate', self.on_menu_open)
        
        menuitem_ren_hotel = Gtk.MenuItem(label="Reinitialiser Hotel")
        submenu_edit.append(menuitem_ren_hotel)
        menuitem_ren_hotel.connect('activate', self.on_menu_open)  
        
        #Les Chambres
        menuitem_chambre = Gtk.MenuItem(label="LES CHAMBRES")
        menubar.append(menuitem_chambre)

        #Sous menu Chambres
        
        submenu_chambre = Gtk.Menu()
        menuitem_chambre.set_submenu(submenu_chambre)
        menuitem_list_cham = Gtk.MenuItem(label="LISTES DES CHAMBRES")
        submenu_chambre.append(menuitem_list_cham)
        menuitem_list_cham.connect('activate', self.on_menu_open)
        menuitem_cham_libre = Gtk.MenuItem(label="CHAMBRES LIBRES")
        submenu_chambre.append(menuitem_cham_libre)
        menuitem_cham_libre.connect('activate', self.on_menu_open)
        menuitem_cham_occup = Gtk.MenuItem(label="CHAMBRES OCCUPEES")
        submenu_chambre.append(menuitem_cham_occup)
        menuitem_cham_occup.connect('activate', self.on_menu_open)
        menuitem_cham_reserv = Gtk.MenuItem(label="CHAMBRES RESERVEES")
        submenu_chambre.append(menuitem_cham_reserv)
        menuitem_cham_reserv.connect('activate', self.on_menu_open)
        menuitem_class_cham = Gtk.MenuItem(label="CLASSE D'UNE CHAMBRE")
        submenu_chambre.append(menuitem_class_cham)
        menuitem_class_cham.connect('activate', self.on_menu_open)
        
        #les Clients
        menuitem_client = Gtk.MenuItem(label="LES CLIENTS")
        menubar.append(menuitem_client)
        
        #Sous menu les clients
        submenu_client = Gtk.Menu()
        menuitem_client.set_submenu(submenu_client)
        menuitem_list_cli = Gtk.MenuItem(label="LISTES DES CLIENTS")
        submenu_client.append(menuitem_list_cli)
        menuitem_list_cli.connect('activate', self.on_menu_open)
        menuitem_cli_sort = Gtk.MenuItem(label="CLIENTS QUI SORTENT AUJOURD'HUI")
        submenu_client.append(menuitem_cli_sort)
        menuitem_cli_sort.connect('activate', self.on_menu_open)
        menuitem_list_cliReserv = Gtk.MenuItem(label="LISTES DES CLIENTS RESERVES")
        submenu_client.append(menuitem_list_cliReserv)
        menuitem_list_cliReserv.connect('activate', self.on_menu_open)
        menuitem_cli_hot = Gtk.MenuItem(label="CLIENTS QUI SONT DANS L'HOTEL")
        submenu_client.append(menuitem_cli_hot)
        menuitem_cli_hot.connect('activate', self.on_menu_open)
        menuitem_sup_cli = Gtk.MenuItem(label="SUPPRESSION CLIENT")
        submenu_client.append(menuitem_sup_cli)
        menuitem_sup_cli.connect('activate', self.on_menu_open)
               
        #Menu Reservation
        menuitem_reserv = Gtk.MenuItem(label="RESERVATION")
        menubar.append(menuitem_reserv)
        
        #Sous menu Reservations
        submenu_reserv = Gtk.Menu()
        menuitem_reserv.set_submenu(submenu_reserv)
        menuitem_listReserv = Gtk.MenuItem(label="LISTE DES RESERVATIONS")
        submenu_reserv.append(menuitem_listReserv)
        menuitem_listReserv.connect('activate', self.on_menu_open)
        menuitem_annulReserv = Gtk.MenuItem(label="ANNULER UNE RESERVATION")
        submenu_reserv.append(menuitem_annulReserv)
        menuitem_annulReserv.connect('activate', self.on_menu_open)
        menuitem_ajoutReserv = Gtk.MenuItem(label="AJOUTER UNE RESERVATION")
        submenu_reserv.append(menuitem_ajoutReserv)
        menuitem_ajoutReserv.connect('activate', self.formulaire_reservation)
         
        #Menu Factures
        menuitem_fact = Gtk.MenuItem(label="FACTURES")
        menubar.append(menuitem_fact)
        
        #Menu Statististat
        menuitem_stat = Gtk.MenuItem(label="STATISTIQUES")
        menubar.append(menuitem_stat)
        
        button_logout = Gtk.MenuItem(label="LOGOUT")
        menubar.append(button_logout)
        button_logout.connect("activate", self.bouton_logout)

        self.show_all()
        self.connect("delete-event", Gtk.main_quit)

    def bouton_logout(self, widget):
        print("Logout clicked")
        self.hide()
        self.login_form.show_all()
        
        #Formulaire pour ajouter une reservation
    def formulaire_reservation(self, widget):
        formulaire.FenetreForm(self)
        # Empêche le menu d'être cliquable
        self.set_sensitive(False)

    #Ajout de sous menu
    def on_menu_open(self, widget):
        print("add file open dialog")

    def on_menu_quit(self, widget):
        Gtk.main_quit()
        
    def formulaire_modif_nom(self, widget):
        modifierNom.Renommer(self)


# win = FenetreApp()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()