import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from datetime import datetime
#import requests

class FenetreForm(Gtk.Window):
    def __init__(self, fen_win):
        self.fen_win = fen_win
        Gtk.Window.__init__(self, title="Formulaire de réservation")
        
        self.set_transient_for(fen_win)
        self.connect("destroy", self.no_click_menu)

        self.set_border_width(10)
        self.set_default_size(500, 900)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        #Header Bar
        headerbar = Gtk.HeaderBar()
        headerbar.set_title("Logiciel de Gestion d'Hotel")
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

        # Grilles
        grid = Gtk.Grid()
        self.add(grid)
        grid.set_column_spacing(5)  
        grid.set_row_spacing(5)  

        # Labels
        label_nom = Gtk.Label("Nom")
        label_prenom = Gtk.Label("Prénom")
        label_telephone = Gtk.Label("Téléphone")
        label_dateReservation = Gtk.Label("Date de reservation")
        label_dateEntree = Gtk.Label("Date d'entrée")
        label_dateSortie = Gtk.Label("Date de sortie")
        label_nuite = Gtk.Label("Nuite")
        label_Classe = Gtk.Label("Classe :")
        label_numChambre = Gtk.Label("Nuite")
        label_tarif_spe = Gtk.Label("Groupe spécial")
        label_pti_dej = Gtk.Label("Petit déjeuner")
        label_phone = Gtk.Label("Utilisation du tel :")
        label_bar = Gtk.Label("Visite au bar")
        label_tarif_chambre = Gtk.Label("tarif chambre")
        label_tarif_pti_dej = Gtk.Label("tarif pti dej")
        label_tarif_phone = Gtk.Label("tarif phone")
        label_tarif_bar = Gtk.Label("tarif bar")
        label_total = Gtk.Label("total")

        # Les Champs de saisies
        self.nom = Gtk.Entry()
        self.prenom = Gtk.Entry()
        self.telephone = Gtk.Entry()
        self.dateReservation =Gtk.Entry()
        self.dateEntree = Gtk.Entry()
        self.dateSortie = Gtk.Entry()
        self.nuite = Gtk.Entry()
        self.numChambre = Gtk.Entry()
        self.tarif_chambre =Gtk.Entry()
        self.tarif_pti_dej =Gtk.Entry()
        self.tarif_phone =Gtk.Entry()
        self.tarif_bar =Gtk.Entry()
        self.total =Gtk.Entry()
        

        #Les boutons Checkboxes
        self.tarif_spe = Gtk.CheckButton()
        self.pti_dej = Gtk.CheckButton()
        self.phone = Gtk.CheckButton()
        self.bar = Gtk.CheckButton()
        
        #Liste Choix
        self.liste_Classe = Gtk.ComboBoxText()
        self.liste_Classe.insert(0, "0", "A")
        self.liste_Classe.insert(1, "1", "B")
        self.liste_Classe.insert(2, "2", "C")
        self.liste_Classe.set_active(0)
        
        #Les Bouttons
        button = Gtk.Button(label="Envoyer")
        button.connect("clicked", self.on_button_clicked)

        # Ajout des elements aux grilles
        grid.attach(label_nom, 0, 0, 1, 1)
        grid.attach(self.nom, 1, 0, 1, 1)
        grid.attach(label_prenom, 0, 1, 1, 1)
        grid.attach(self.prenom, 1, 1, 1, 1)
        grid.attach(label_telephone, 0, 2, 1, 1)
        grid.attach(self.telephone, 1, 2, 1, 1)
        grid.attach(label_dateReservation, 0, 3, 1, 1)
        grid.attach(self.dateReservation, 1, 3, 1, 1)
        grid.attach(label_dateEntree, 0, 4, 1, 1)
        grid.attach(self.dateEntree, 1, 4, 1, 1)
        grid.attach(label_dateSortie, 0, 5, 1, 1)
        grid.attach(self.dateSortie, 1, 5, 1, 1)
        grid.attach(label_nuite, 0, 6, 1, 1)
        grid.attach(self.nuite, 1, 6, 1, 1)
        
        grid.attach(label_Classe, 0, 7, 1, 1)
        grid.attach(self.liste_Classe, 1, 7, 1, 1)
        grid.attach(label_numChambre, 0, 8, 1, 1)
        grid.attach(self.numChambre, 1, 8, 1, 1)
        grid.attach(label_tarif_spe, 0, 9, 1, 1)
        grid.attach(self.tarif_spe, 1, 9, 1, 1)
        
        grid.attach(label_pti_dej, 0, 10, 1, 1)
        grid.attach(self.pti_dej, 1, 10, 1, 1)
        grid.attach(label_phone, 0, 11, 1, 1)
        grid.attach(self.phone, 1, 11, 1, 1)
        grid.attach(label_bar, 0, 12, 1, 1)
        grid.attach(self.bar, 1, 12, 1, 1)
        
        grid.attach(label_tarif_chambre, 0, 13, 1, 1)
        grid.attach(self.tarif_chambre, 1, 13, 1, 1)
        grid.attach(label_tarif_pti_dej, 0, 14, 1, 1)
        grid.attach(self.tarif_pti_dej, 1, 14, 1, 1)
        grid.attach(label_tarif_phone, 0, 15, 1, 1)
        grid.attach(self.tarif_phone, 1, 15, 1, 1)
        grid.attach(label_tarif_bar, 0, 16, 1, 1)
        grid.attach(self.tarif_bar, 1, 16, 1, 1)
        grid.attach(label_total, 0, 17, 1, 1)
        grid.attach(self.total, 1, 17, 1, 1)
        grid.attach(button, 1, 18, 1, 1)
        
        # Initialize error message label
        self.error_label = Gtk.Label()
        grid.attach(self.error_label, 0, 19, 1, 1)
        
        # Centrer la Gtk.Grid dans la fenêtre
        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.CENTER)
        
        self.show_all()
        
    def no_click_menu(self, widget):
        # Permet au menu d'être cliquable à nouveau
        self.get_transient_for().set_sensitive(True)

    def on_button_clicked(self, widget):
        nom = self.nom.get_text()
        prenom = self.prenom.get_text()
        tel = self.telephone.get_text()
        dateReservation = self.dateReservation.get_text()
        dateEntree = self.dateEntree.get_text()
        dateSortie = self.dateSortie.get_text()
        nuite = self.nuite.get_text()
        tarif_spe = self.tarif_spe.get_active()
        pti_dej = self.pti_dej.get_active()
        phone = self.phone.get_active()
        bar = self.bar.get_active()
        tarif_chambre = self.tarif_chambre.get_text()
        tarif_pti_dej = self.tarif_pti_dej.get_text()
        tarif_phone = self.tarif_phone.get_text()
        tarif_bar = self.tarif_bar.get_text()
        total = self.total.get_text()
        classe = self.liste_Classe.get_active_text()

        # Conversion des dates
        reserv_date = datetime.strptime(dateReservation, '%d/%m/%Y')
        entree_date = datetime.strptime(dateEntree, '%d/%m/%Y')
        sortie_date = datetime.strptime(dateSortie, '%d/%m/%Y')

        # Vérification de la validité de la date
        if entree_date > sortie_date:
            self.error_label.set_text("La date de début ne peut pas être après la date de fin")
        else:
            self.error_label.set_text("Formulaire envoyé avec succès")
        
        #Url de l'API GO
        url = 'http://localhost:8000/enregistrer_utilisateur'
        
        #Fichier Json
        data = {'nom': nom, 'prenom' : prenom, 'tel': tel, 'dateReservation' : dateReservation, 'dateEntree': dateEntree, 'dateSortie': dateSortie, 'nuite': nuite, 'classe': classe, 'tarif_spe': tarif_spe, 'pti_dej': pti_dej, 'phone': phone, 'bar': bar, 'tarif_chambre': tarif_chambre, 'tarif_pti_dej': tarif_pti_dej, 'tarif_phone': tarif_phone, 'tarif_bar': tarif_bar, 'total': total}
        
        # Faire appel a l'API GO
        response = requests.post(url, data=data)

        if response.status_code == 200:
            self.error_label.set_text("Formulaire envoyé avec succès")
            self.hide()
        else:
            self.error_label.set_text("Error")

# win = FenetreForm()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()