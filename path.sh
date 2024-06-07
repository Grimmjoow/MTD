import subprocess
import random

# Liste des chemins des scripts ou exécutables
declare -A paths
paths=(
    ["/usr/local/bin/critical_script.sh"]="/usr/local/bin"
)

# Fonction pour randomiser les chemins
randomize_paths() {
    for script in "${!paths[@]}"; do
        base_dir=${paths[$script]}
        new_name=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13)
        new_path="$base_dir/$new_name.sh"
        
        # Renommer le script
        mv "$script" "$new_path"
        
        # Mettre à jour les configurations dépendantes
        # Exemple : mise à jour d'un cron job
        sed -i "s|$script|$new_path|g" /etc/crontab
        
        echo "$script déplacé à $new_path"
    done
}

# Exécution de la randomisation des chemins
randomize_paths