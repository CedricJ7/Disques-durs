from browser import document, ajax, bind

def get_disk_info_via_ajax(event):
    document["response"].text = "Récupération des informations sur les disques réalisée"
    req = ajax.get('http://localhost:5000/api/get-disk-info', oncomplete=handle_disk_info_response, mode="json")
    return req

def handle_disk_info_response(req):
    if req.status == 200:
        disk_info = req.json
        display_disk_info(disk_info)
    else:
        print("Erreur lors de la récupération des informations sur les disques.")
        document["response"].text = "Erreur lors de la récupération des informations sur les disques."

def display_disk_info(disk_info):
    # document <= disk_info
    table_body = document["disk-table"]
    #table_body.clear()
    end=7
    for i, disk in enumerate(disk_info, start=1):
        if i > end:
            break
        row = document.createElement("tr")
        name = document.createElement("td")
        name.text = disk["nom"]
        free_space = document.createElement("td")
        free_space.text = f"{disk['espace_libre']} Go"
        used_space = document.createElement("td")
        used_space.text = f"{disk['espace_occupe']} Go"
        total_space = document.createElement("td")
        total_space.text = f"{disk['espace_total']} Go"

        # Utilisez les identifiants dynamiques en fonction de la boucle
        document[f"nom{i}"].textContent = name.textContent
        document[f"espace_l{i}"].textContent = free_space.textContent
        document[f"espace_u{i}"].textContent = used_space.textContent
        document[f"espace_t{i}"].textContent = total_space.textContent

    # for disk in disk_info:
    #     row = document.createElement("tr")
    #     name = document.createElement("td")
    #     name.text = disk["nom"] 
    #     free_space = document.createElement("td")
    #     free_space.text = f"{disk['espace_libre']} Go"  
    #     used_space = document.createElement("td")
    #     used_space.text = f"{disk['espace_occupe']} Go"
    #     total_space = document.createElement("td")
    #     total_space.text = f"{disk['espace_total']} Go"
    #     # row <= name
    #     # row <= free_space   #crée un nouveau tableau sans format
    #     # row <= used_space
    #     # row <= total_space
    #     # table_body <= row
    #     document["nom1"].textContent = name.textContent
    #     document["espace_l1"].textContent = free_space.textContent
    #     document["espace_u1"].textContent = used_space.textContent
    #     document["espace_t1"].textContent = total_space.textContent

# document["get-disk-info-btn"].bind("click", get_disk_info_via_ajax)

# document.bind("DOMContentLoaded", get_disk_info_via_ajax)

document.bind("mouseenter", get_disk_info_via_ajax)