import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sqlite3

# Création d'une connexion à la base de données
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Création de la table pour stocker les noms des interfaces
c.execute('''CREATE TABLE IF NOT EXISTS interface_names
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT)''')

class Renommer(Gtk.Window):

    def __init__(self, parent_window):
        Gtk.Window.__init__(self, title="")
        self.parent_window = parent_window
        self.set_size_request(200, 150)
        self.set_position(Gtk.WindowPosition.CENTER)
        # Création des éléments graphiques
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(10)
        self.grid.set_row_spacing(10)
        self.add(self.grid)

        self.entry = Gtk.Entry()
        self.grid.attach(self.entry, 0, 0, 3, 1)

        self.bouton_renommer = Gtk.Button(label="Renommer")
        self.bouton_renommer.connect("clicked", self.RenommerHotel)
        self.grid.attach(self.bouton_renommer, 0, 1, 3, 1)

        self.bouton_retour = Gtk.Button(label="Retour")
        self.bouton_retour.connect("clicked", self.RetourAuMenu)
        self.grid.attach(self.bouton_retour, 0, 2, 3, 1)

        self.show_all()
        
    def RenommerHotel(self, button):
        # Récupération du nouveau nom de l'interface
        new_name = self.entry.get_text()

        # Modification du titre de la fenêtre
        self.set_title(new_name)

        # Enregistrement du nouveau nom dans la base de données
        c.execute("INSERT INTO interface_names (name) VALUES (?)", (new_name,))
        conn.commit()

        # Vidage du champ de saisie
        self.entry.set_text('')

    def RetourAuMenu(self, button):
        self.parent_window.show_all()
        self.destroy()

