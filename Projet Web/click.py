from browser import document, alert

def c(ev):
    alert("tu as click!")


document["button_alert"].bind("click", c)