from browser import document, ajax, alert

def terminal(event):
    req=ajax.get('http://localhost:5000/api/create_partition', oncomplete=t)
    return req
def t(req):
    if req.status == 200:
        document["response"].text = "Processus en cours..."
    else:
        print("Ereur lors de la requête")

# Assurez-vous d'ajouter un bouton ou un élément HTML pour déclencher cette action
document["terminal"].bind("click", terminal)