from flask import Flask, jsonify, render_template
from flask_cors import CORS
import psutil
import os
import platform
import subprocess
import time
import webbrowser

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route('/')
def index():
    disks = [
        {"name": "Disque 1", "free_space": "100 Go", "used_space": "50 Go", "total_space": "150 Go"},
        {"name": "Disque 2", "free_space": "200 Go", "used_space": "30 Go", "total_space": "230 Go"},
        # Ajoutez d'autres données de disque au besoin
    ]
    return render_template('index.html', disks=disks)

# @app.route("/", methods=['GET'])
# def execute_flask_function():
#     m= "<p>La fonction Flask a été exécutée avec succès !</p>"
#     return jsonify(m)



@app.route("/api/open-disk-manager", methods=['GET'])
def open_disk_manager():
    try:
        # Détermine le système d'exploitation
        system = platform.system()
        if system == "Windows":
            os.system("diskmgmt.msc")  # Ouvre le Gestionnaire de disques sur Windows
        if system == "Linux":
            subprocess.run(["gnome-disks"]) # Ouvre le Gestionnaire de disques sur Linux (GNOME)
        else:
            return jsonify("Système d'exploitation non pris en charge")
        
    except Exception as e:
        print(f'Erreur : {e}')
        return jsonify("erreur")
    
    return jsonify("ok")


@app.route("/api/open-terminal", methods=['GET'])
def api_open_terminal():
    try:
        # Détermine le système d'exploitation
        system = platform.system()

        if system == "Windows":
            os.system("start cmd")
        elif system == "Linux":
            # os.system("gnome-terminal")
            # subprocess.run(["gnome-terminal"])
            os.system("terminator")
            
            
        else:
            return jsonify("Système d'exploitation non pris en charge")

        return jsonify("")
    except Exception as e:
        print(f'Erreur : {e}')
        print(f'Système : {system}')
        return jsonify("erreur")
    
@app.route("/api/get-disk-info", methods=['GET'])
def api_get_disk_info():
    try:
        system = platform.system()
        if system == "Windows":
            disks = psutil.disk_partitions()
            disk_info = []
            for disk in disks:
                usage = psutil.disk_usage(disk.device)
                if bytes_to_gb(usage.total) > 1:
                    disk_data = {
                        "nom": disk.device,
                        "espace_libre": bytes_to_gb(usage.free),
                        "espace_occupe": bytes_to_gb(usage.used),
                        "espace_total": bytes_to_gb(usage.total)
                    }
                    disk_info.append(disk_data)
            return jsonify(disk_info)
        if system == "Linux":
            
            
            disks = psutil.disk_partitions()
            disk_info = []
            hdd1 = psutil.disk_usage("/")
            hdd2 = psutil.disk_usage("/dev/sda1")

        # Ajouter les informations des deux disques spécifiques à la liste
            disk_info.append({
            "nom": "/",
            "espace_libre": bytes_to_gb(hdd1.free),
            "espace_occupe": bytes_to_gb(hdd1.used),
            "espace_total": bytes_to_gb(hdd1.total)
        })
            disk_info.append({
            "nom": "/dev/sda1",
            "espace_libre": bytes_to_gb(hdd2.free),
            "espace_occupe": bytes_to_gb(hdd2.used),
            "espace_total": bytes_to_gb(hdd2.total)
        })


            for disk in disks:
            
                usage = psutil.disk_usage(disk.device)
                if bytes_to_gb(usage.total) > 1:
                    disk_data = {
                "nom": disk.device,
                "espace_libre": bytes_to_gb(usage.free),
                "espace_occupe": bytes_to_gb(usage.used),
                "espace_total": bytes_to_gb(usage.total)
            }
                disk_info.append(disk_data)

        return jsonify(disk_info)

    except Exception as e:
        return "erreur"

def bytes_to_gb(bytes):
    return round(bytes / (1024 * 1024 * 1024))

@app.route("/api/create_partition", methods=['GET'])
def create_partition():
    if platform.system == "Windows":
        os.system("start cmd")
    elif platform.system() == "Linux":
        url = "https://phoenixnap.com/kb/linux-create-partition"
        webbrowser.open(url)
        command = 'terminator -x sudo bash -c "echo Appuyez sur Entrée pour afficher les informations sur les disques...; read; fdisk -l; echo Appuyez sur Entrée pour scanner les disques...; read; lsblk; echo Appuyez sur Entrée pour lancer fdisk...; read; fdisk /dev/sda; sleep 100; exit"'
        os.system(command)
    else:
        return jsonify("Système d'exploitation non pris en charge")
    return jsonify("ok")
    
@app.route("/api/jauge", methods=['GET'])
def jauge():
    try:
        hdd1 = psutil.disk_usage("/")
        occupation = (hdd1.free / hdd1.total) * 100
        return jsonify(occupation)
    except Exception as e:
        return "erreur"

    
    

if __name__ == '__main__':
    app.run()

