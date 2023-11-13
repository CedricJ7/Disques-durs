from flask import Flask
import subprocess

app = Flask(disk_partition)

@app.route('/run_command')
def run_command():
    try:
        if "win" in request.headers.get('User-Agent'):
            result = subprocess.check_output(["diskmgmt.msc"], shell=True)  # Ouvre le Gestionnaire de disques sur Windows
        elif "linux" in request.headers.get('User-Agent'):
            result = subprocess.check_output(["gnome-disks"], shell=True)  # Ouvre le Gestionnaire de disques sur Linux (GNOME)
        else:
            return "Système d'exploitation non pris en charge"
        
        return result
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
