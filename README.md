# Programme Python : Readme

Ce programme Python envoie des messages en boucle à des webhooks Discord. Il utilise le module `requests` pour envoyer des requêtes HTTP POST à l'API Discord Webhooks.

## Installation du module `requests`

Le module `requests` peut être installé à l'aide de `pip`. Pour cela, ouvrez un terminal et exécutez la commande suivante :

```bash
pip install requests
```

## Utilisation du programme

### Configuration

Avant de lancer le programme, vous devez configurer les paramètres dans le fichier `config.json`. Les paramètres disponibles sont :

- `"webhooks"` : une liste de liens de webhooks Discord à utiliser pour envoyer les messages. Vous pouvez ajouter autant de liens que vous le souhaitez.
- `"lien"` : un lien vers le site Web que vous souhaitez inclure dans le message.
- `"auteur"` : le nom de l'utilisateur Discord qui envoie les messages.

Vous devez remplir les champs correspondants dans le fichier `config.json` avant d'exécuter le programme.

### Lancement du programme

Une fois que vous avez configuré les paramètres dans le fichier `config.json`, vous pouvez lancer le programme en exécutant le fichier `main.py`.

Le programme envoie des messages en boucle à tous les webhooks Discord configurés dans config.json. Les messages contiennent un lien vers le site Web spécifié et une image animée. Les messages sont envoyés toutes les 3 secondes.

### Remarque

- Ce script est conçu à des fins éducatives uniquement et ne doit pas être utilisé pour nuire à autrui ou violer les conditions d'utilisation de Discord.
- L'utilisation de ce script pour effectuer un raid sur un serveur sans l'autorisation du propriétaire du serveur est illégale.
- L'auteur de ce script n'est pas responsable des dommages ou des problèmes juridiques pouvant résulter de l'utilisation de ce script.
  
### Licence

Ce programme est sous licence MIT. Veuillez consulter le fichier `LICENSE` pour plus d'informations.
