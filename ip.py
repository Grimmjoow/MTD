import subprocess
import random

# Fonction pour générer une nouvelle adresse IP
def generate_new_ip():
    return f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"

# Fonction pour changer l'adresse IP d'un serveur cible
def change_ip(server):
    new_ip = generate_new_ip()
    subprocess.run(["ssh", server, f"sudo ip addr add {new_ip}/24 dev eth0"])
    subprocess.run(["ssh", server, f"sudo ip addr del {current_ip}/24 dev eth0"])
    print(f"Changed IP of {server} to {new_ip}")
    return new_ip

# Liste des serveurs cibles
servers = ["server1", "server2", "server3"]
current_ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]  # Adresse IP actuelle des serveurs

# Changer les adresses IP des serveurs cibles
for i, server in enumerate(servers):
    current_ip = current_ips[i]
    new_ip = change_ip(server)
    current_ips[i] = new_ip