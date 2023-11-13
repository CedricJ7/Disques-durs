import os
from browser import document

def open_disk_manager(event):
    try:
        os.system("diskmgmt.msc")  # Ouvre le Gestionnaire de disques sur Windows
    except Exception:
        try:
            os.system("gnome-disks")  # Ouvre le Gestionnaire de disques sur Linux (GNOME)
        except Exception as e:
            document["actions-section"].innerHTML = "Erreur lors de l'ouverture du Gestionnaire de disques : " + str(e)

document["create-partition-btn"].bind("click", open_disk_manager)

