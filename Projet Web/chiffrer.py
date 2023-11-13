from browser import document, ajax, alert

def open_terminal_via_ajax(event):
    alert("pour chiffrer ou verouiller/deverouiller un volume utilise le terminal et des commandes tel que manage-bde -status, manage-bde -on X: (sur cmd Windows)... pour plus d'infos va voir la doc")
    document["response"].text = "Ouverture du terminal en cours..."
    req = ajax.get('http://localhost:5000/api/open-terminal', oncomplete=handle_open_terminal_response)
    return req

def handle_open_terminal_response(req):
    if req.status == 200:
        print("Terminal ouvert avec succès.")
        document["response"].text = "Terminal ouvert avec succès."
    else:
        print("Erreur lors de l'ouverture du terminal.")
        document["response"].text = "Erreur lors de l'ouverture du terminal."



document["encrypt-volume-btn"].bind("click", open_terminal_via_ajax)
document["unlock-volume-btn"].bind("click", open_terminal_via_ajax)

