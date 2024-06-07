import random
import subprocess

# Liste des services avec leurs ports par défaut
services = {
    'ssh': 22,
    'http': 80,
    'https': 443
}

# Fonction pour randomiser les ports
def randomize_ports(services):
    new_ports = {}
    for service, default_port in services.items():
        new_port = random.randint(1024, 65535)
        new_ports[service] = new_port
        
        # Mise à jour de la configuration des services
        if service == 'ssh':
            subprocess.run(['sudo', 'sed', '-i', f's/^#Port .*/Port {new_port}/', '/etc/ssh/sshd_config'])
            subprocess.run(['sudo', 'systemctl', 'restart', 'ssh'])
        elif service in ['http', 'https']:
            # Mettre à jour la configuration des services web (exemple avec Nginx)
            subprocess.run(['sudo', 'sed', '-i', f's/listen .*/listen {new_port};/', f'/etc/nginx/sites-available/default'])
            subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'])
        
        print(f'{service} port changé de {default_port} à {new_port}')
    
    return new_ports

# Exécution de la randomisation des ports
new_ports = randomize_ports(services)
print("Nouveaux ports :", new_ports)