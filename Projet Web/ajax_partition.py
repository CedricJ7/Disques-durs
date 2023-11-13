from browser import document, ajax, alert

def open_disk_manager_via_ajax(event):
    alert("Vous pouvez utilisez cette outil pour créer une partition sur votre disque dur. Pour plus d'information, veuillez consulter la documentation.")
    document["response"].text = "Ouverture du Gestionnaire de disques..."
    req=ajax.get('http://localhost:5000/api/open-disk-manager', oncomplete=handle_open_disk_manager_response)
    return req
def handle_open_disk_manager_response(req):
    if req.status == 200:
        # Vous pouvez gérer la réponse ici si nécessaire
        print("Gestionnaire de disques ouvert avec succès.")
        document["response"].text = "Gestionnaire des disques ouvert avec succès."
    else:
        print("Erreur lors de l'ouverture du Gestionnaire de disques.")
        document["response"].text = "Erreur lors de l'ouverture du Gestionnaire de disques."

# Assurez-vous d'ajouter un bouton ou un élément HTML pour déclencher cette action
document["create-partition-btn"].bind("click", open_disk_manager_via_ajax)
document["delete-partition-btn"].bind("click", open_disk_manager_via_ajax)
