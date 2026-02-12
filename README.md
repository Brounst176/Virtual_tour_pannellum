# Visite Virtuelle Interactive 🏛️

Une page web moderne pour créer des visites virtuelles 360° avec plan de navigation interactif.

## ✨ Fonctionnalités

- 🖼️ Panoramas 360° interactifs avec Pannellum
- 🗺️ Mini-plan en bas à droite avec position en temps réel
- 🏢 Support multi-étages avec navigation intuitive
- 📍 Points cliquables sur le plan pour changer de vue
- 🎨 Interface moderne et élégante
- 📱 Responsive (desktop et mobile)
- ⚡ Page html facile à personnaliser et déployer

## 🚀 Déploiement

### Option 1 : Serveur Web Simple
```bash
# Placez l'ensemble des fichiers dans votre serveur web
# Assurez-vous que les images sont accessibles aux chemins spécifiés
```

### Option 2 : Python (pour tester localement)
```bash
# Dans le dossier contenant virtual-tour.html
python -m http.server 8000
# Ouvrez http://localhost:8000/
```

## 📁 Structure des fichiers

Voici comment organiser tes fichiers :

```
Visite_vitruelle/
├── index.html               # Page d'accueil (liste des visites)
├── virtual-tour-json.html   # Lecteur de visite (avec ?tour_name=)
├── config-editor-v2.html    # Éditeur de configuration
│
├── tours/                   # Dossier des tours
│   ├── heig-vd                # Dossier du tour HEIG-VD
│   │   ├── config.json        # Config du tour
│   │   ├── rez                # Dossier des scènes du rez-de-chaussée et du plan
│   │   │   ├── scene1.jpg
│   │   │   ├── scene2.jpg
│   │   │   └── plan.jpg
│   │   └── ...                # Autres étages et scènes
└── └── ...                  # Tes autres projets

```

## 🛠️ Ajouter des visites virtuelles à la page d'accueil
Pour ajouter une nouvelle visite, il faut modifier le fichier `index.html ` en indicant un nouveau tour dans la partie javascript.
```javascript
const tours = [
            {
                id: "heig-vd",
                title: "HEIG-VD",
                description: "Découvrez le campus de la Haute École d'Ingénierie et de Gestion du Canton de Vaud",
                image: "/tour/heig-vd/icon_titre.jpeg",
                scenes: 5,
                floors: 2,
                badge: "Nouveau"
            },
            {
                id: "mason-circle",
                title: "Bidon",
                description: "Visite bidon",
                image: "/tour/bidon/from-tree.jpg",
                scenes: 2,
                floors: 1,
                badge: null
            },
            // Ajoutez vos visites ici :
            // {
            //     id: "mon-projet",
            //     title: "Mon Projet",
            //     description: "Description de ma visite",
            //     image: "/tour/bidon/from-tree.jpg",
            //     scenes: 10,
            //     floors: 3,
            //     badge: "Nouveau"
            // }
        ];
```

Il faut alors créer le dossier qui contiendra les fichiers de la visite (config.json, images 360°, plans, etc.) et indiquer le bon chemin dans le champ `image` du tour. En principe, le dossier de la visite doit être dans `tours/` et contenir l'image de couverture pour garder la même structure que les visites existantes, mais vous pouvez adapter les chemins à votre organisation.


## 🛠️ Configuration des visites virtuelles

Les visites sont mises dans le dossier `tours/`. Chaque visite a son propre dossier avec un fichier `config.json` et les images nécessaires.

Un page web permet d'éditer facilement les configurations : `config-editor-v2.html`. Vous pouvez ajouter des étages, des scènes en personnalisant les points d'intérêt et position les scènes sur les différents plans d'étage.

### 🎯 Workflow complet

#### Créer une nouvelle visite de A à Z :

1. **Prépare tes images 360°**
   - Photos panoramiques équirectangulaires
   - Format 2:1 (ex: 4096x2048)
   - Place-les dans `/tour/mon-projet/etage`

2. **Prépare ton plan d'étage**
   - Image JPG/PNG ou SVG
   - Place-le dans `/tour/mon-projet/etage/plan.jpg`

3. **Prépare l'image de couverture**
   - Format carré (800x800px)
   - Place-la dans `/tour/mon-projet/icon_titre.jpeg`

4. **Crée la configuration**
   - Ouvre `config-editor-v2.html`
   - Crée tes étages (avec le chemin vers ton plan)
   - Crée tes scènes (avec les chemins vers tes 360°)
   - Place les hotspots visuellement
   - Place les scènes sur le plan visuellement
   - Exporte → `config.json`
   - Place-le dans `/tour/mon-projet/`

5. **Ajoute à la page d'accueil**
   - Édite `index.html`
   - Ajoute ton objet dans l'array `tours`

6. **Teste !**
   - Ouvre `http://localhost:8000/`
   - Clique sur ta visite
   - Ça fonctionne ! 🎉

---

### 🛠️ Procédure manuelle du fichier config.json
#### 1. Ajouter des étages

```javascript
floors: [
    {
        id: "ground",           // ID unique
        name: "Rez-de-chaussée", // Nom affiché
        plan: "plan-rdc.jpg",   // Chemin vers l'image du plan
        scenes: ["circle", "house"] // IDs des scènes de cet étage
    },
    {
        id: "first",
        name: "Premier étage",
        plan: "plan-etage1.jpg",
        scenes: ["room1", "room2", "corridor"]
    }
]
```

#### 2. Ajouter des scènes 360°

```javascript
scenes: {
    circle: {
        title: "Mason Circle",
        floor: "ground",              // Étage de la scène
        hfov: 110,                    // Champ de vision
        pitch: -3,                    // Inclinaison initiale
        yaw: 117,                     // Rotation initiale
        type: "equirectangular",      // Type de panorama
        panorama: "/images/from-tree.jpg", // Chemin de l'image 360°
        mapPosition: { x: 31.25, y: 58.3 }, // Position sur le plan (en %)
        hotSpots: [                   // Points cliquables dans le 360°
            {
                pitch: -2.1,
                yaw: 132.9,
                type: "scene",
                text: "Aller à Spring House",
                sceneId: "house"
            }
        ]
    }
}
```

#### 3. Personnaliser les plans

Vous pouvez utiliser des images JPG/PNG ou des SVG pour les plans. Les SVG permettent une meilleure qualité et peuvent être interactifs. Par principe, ils sont mis dans le dossier des étages, mais vous pouvez les stocker ailleurs tant que le chemin est correct.


#### 4. Positionner les points sur le plan

Les positions sont en pourcentage (0-100) :
- `x: 0` = gauche, `x: 100` = droite
- `y: 0` = haut, `y: 100` = bas



## 🎨 Personnalisation du style

Les couleurs et styles sont dans la balise `<style>`. Quelques variables utiles :

```css
/* Couleur des points actifs */
.map-point.active {
    background: #ef4444; /* Rouge par défaut */
}

/* Couleur des points normaux */
.map-point {
    background: #3b82f6; /* Bleu par défaut */
}

/* Arrière-plan des panneaux */
background: rgba(0, 0, 0, 0.7); /* Noir semi-transparent */
```

## 📸 Format des images

### Images 360°
- Format : Equirectangulaire (2:1)
- Résolution recommandée : 4096x2048px ou plus
- Format : JPG (optimisé pour le web)

### Plans
- Format : JPG, PNG ou SVG
- Taille recommandée : 800-1200px de large
- Le SVG est idéal pour des plans architecturaux nets

## 🔧 Fonctionnalités avancées

### Ajouter des infobulles personnalisées

```javascript
hotSpots: [
    {
        pitch: -2.1,
        yaw: 132.9,
        type: "info",
        text: "Cette pièce date de 1850",
        URL: "https://example.com/info" // Optionnel
    }
]
```

### Changer l'animation de transition

```javascript
sceneFadeDuration: 500 // Durée en millisecondes
```

## 🐛 Dépannage

**Les images ne s'affichent pas** :
- Vérifiez que les chemins sont corrects
- Si vous testez en local, utilisez un serveur HTTP (pas file://)

**Le plan ne s'affiche pas** :
- Vérifiez le chemin de l'image
- Pour les SVG en ligne, vérifiez l'encodage URL



## 📝 Licence

Code libre d'utilisation pour vos projets personnels et commerciaux.

## 🙏 Crédits

- Pannellum : https://pannellum.org/

---

Bon voyage virtuel ! 🚀
