import subprocess
import random
import logging

# Configuration de la journalisation
logging.basicConfig(filename='/var/log/...', level=logging.INFO)

# Fonction pour générer une nouvelle adresse IP
def generate_new_ip():
    return f"192.168.100.{random.randint(10, 254)}"

def change_ip(server, current_ip):
    new_ip = generate_new_ip()
    subprocess.run(["ssh", pc, f"sudo ip addr add {new_ip}/24 dev eth0"])
    subprocess.run(["ssh", pc, f"sudo ip addr del {current_ip}/24 dev eth0"])
    logging.info(f"Changed IP of {pc} from {current_ip} to {new_ip}")
    return new_ip

pcs = ["pc1", "pc2", "pc3"]
current_ips = ["192.168.100.10", "192.168.100.11", "192.168.100.12"]

# Changer les adresses IP des serveurs cibles
for i, server in enumerate(pcs):
    current_ip = current_ips[i]
    new_ip = change_ip(pc, current_ip)
    current_ips[i] = new_ip