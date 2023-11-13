from browser import document,ajax, bind


def pourcentage(event):
    req=ajax.get('http://localhost:5000/api/jauge', oncomplete=jauge, mode="json")
    return req
    
def jauge(req):
    p=round(req.json)
    fill_bar = document["bar-fill"]
    fill_bar.style.width = f'{p}%'
    document["response"].text = f"{p}%"
    return p
document["get-disk-info-btn"].bind("click", pourcentage)


