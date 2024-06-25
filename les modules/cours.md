## Les modules en Python

Il s'agit d'un fichier Python (ou plusieurs) dans une même Application.

Pour utiliser un module dans un fichier Python, il suffit d'utiliser un **import**
Une fois importer, les fonctions de ce fichier sont utilisable dans le fichier qui importe.

**Exemple :** 
* Je crée un fichier main.py et un autre fichiers utilitaires.py.
* Dans utilitaires, je mets les fonctions utiles de mon projet.
* Dans main, je mets juste le contenu de mon application.
```import utilitaires```

Utiliser une fonction : 
```utilitaires.mafonction()```

Il faut que j'importe **utilitaires.py** dans **main.py** afin de pouvoir les utiliser.

Si nécessaire, je peux choisir de n'**importer que les fonctions dont j'ai besoin** dans mon application.
```from 'mon fichier' import 'ma fonction'```

Je peux aussi importer via les **chemins relatifs** : 
```from './helpers/utilitaires'```

# Les modules natifs au language Python 

Depuis le site officiel Python, il y a plusieurs modules deja importable nativement dans le language.
```import 'nom_du_module'```

# Les modules communautaires Python

Comme dans beaucoup de languages, Python bénéficie d'une grande communauté qui publie des modules.
Il est possible d'importer des modules communautaires dans son projet.

Pour installer un module communautaire, il faut saisir : 
```python -m pip install 'mon_paquet'```

Une fois installer, il faut l'importer comme vue précédemment.

Le mot clé **with** permet depuis Python 3 de fermé le flux dans lequel se situe ce mot clé.

Les fontions **.open()** et **.write()** permettent de modifier le fichier **data.txt**
**.open()** prends deux parametres : 
* Le nom du fichier
* Les autorisations/actions sur ce fichier (r : read, w : write, a : authorization)
Exemple : 
```mon_fichier.open(mon_fichier_ouvrir, 'a') as fichier:```

Exemple avec le module **datetime** : 

```import os
import datetime from datetime

mon_fichier = data.txt

def ajouter_une_ligne(ligne) :
    if os.path.exists(nom_fichier) : 
        with open(mon_fichier, 'a') as fichier: 
            fichier.write(f"{ligne}\n")
    else : 
        with open(mon_fichier, 'w') as fichier :
            fichier.write(f"{ligne}\n")

ajouter_une_ligne("Lapremiere)```
