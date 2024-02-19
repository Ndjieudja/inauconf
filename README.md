# Inauconf


Inauconf is the script to hidden real Text 
Ce projet est une application Python qui effectue diverses opérations. Il est écrit en utilisant le langage de programmation Python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install inauconf
```

## Fonctionnalités

- **Cryptage et décryptage** : L'application permet de crypter et de décrypter des chaînes de caractères ou des fichiers en utilisant un algorithme personnalisé.
- **Manipulation de fichiers** : Vous pouvez également utiliser l'application pour chiffrer ou déchiffrer des fichiers.
- **Hashage de fichiers** : L'application calcule également la valeur de hachage SHA-256 d'un fichier.

## Comment utiliser l'application

Voici comment utiliser l'application :

1. Assurez-vous d'avoir Python installé sur votre système.
2. Clonez ce dépôt Git : `git clone https://github.com/ndjieudja/inauconf.git`
3. Accédez au répertoire du projet : `cd mon-projet-python`
4. Installez les dépendances : `pip install -r requirements.txt`
5. Exécutez l'application : 
    ```python
    from inauconf.crypt import EncryptAll

    # crypt function
    EncryptAll.encrypt('inauconf')
    # output: ˫105ɒ110/97Ƞ117W99Ǻ111Ʀ110˯102 .... sample

    # uncrypt function
    EncryptAll.decrypt('Ŷ105ǝ110a97ʙ11799à111̶110ƻ102')
    # output: inauconf

    # crypt & bloc file
    EncryptAll.crypt_file('inauconf.txt')
6. Suivez les instructions à l'écran pour utiliser les différentes fonctionnalités de l'application.

**Note importante** : Lorsque vous utilisez la fonctionnalité de chiffrement ou de déchiffrement de fichiers, assurez-vous que le fichier source et le fichier chiffré/déchiffré portent le même nom, à l'exception de l'extension de fichier. Par exemple, si vous avez un fichier `mon_fichier.txt` que vous souhaitez chiffrer, le fichier chiffré sera `mon_fichier.inc`. Veillez à ne pas séparer les deux fichiers pour garantir le bon fonctionnement de l'application.

## Contribution

Les contributions à ce projet sont les bienvenues ! Si vous souhaitez apporter des modifications ou ajouter de nouvelles fonctionnalités, n'hésitez pas à ouvrir une demande de pull.
Pull requests are welcome. For major changes, please open an [issue](https://github.com/ndjieudja/inauconf/issues) first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Auteurs

- Gabriel Ndjieu dja <gabrielndjieudja@gmail.com>

## License

Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus de détails.