# Visite Virtuelle Interactive 🏛️

Une page web moderne pour créer des visites virtuelles 360° avec plan de navigation interactif.

## ✨ Fonctionnalités

- 🖼️ Panoramas 360° interactifs avec Pannellum
- 🗺️ Mini-plan en bas à droite avec position en temps réel
- 🏢 Support multi-étages avec navigation intuitive
- 📍 Points cliquables sur le plan pour changer de vue
- 🎨 Interface moderne et élégante
- 📱 Responsive (desktop et mobile)
- ⚡ Une seule page HTML - facile à déployer

## 🚀 Déploiement

### Option 1 : Serveur Web Simple
```bash
# Placez le fichier virtual-tour.html dans votre serveur web
# Assurez-vous que les images sont accessibles aux chemins spécifiés
```

### Option 2 : Python (pour tester localement)
```bash
# Dans le dossier contenant virtual-tour.html
python -m http.server 8000
# Ouvrez http://localhost:8000/virtual-tour.html
```

### Option 3 : Node.js
```bash
npx http-server
```

### Option 4 : Netlify / Vercel
Déposez simplement le fichier HTML et vos images dans votre projet.

## 🛠️ Configuration

Toute la configuration se trouve dans l'objet `tourConfig` au début du script :

### 1. Ajouter des étages

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

### 2. Ajouter des scènes 360°

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

### 3. Personnaliser les plans

Vous pouvez utiliser :

**Images (JPG/PNG)** :
```javascript
plan: "/images/plan-etage-1.jpg"
```

**SVG en ligne** (pour des plans vectoriels) :
```javascript
plan: "data:image/svg+xml,%3Csvg...%3C/svg%3E"
```

**Fichier SVG** :
```javascript
plan: "/images/plan.svg"
```

### 4. Positionner les points sur le plan

Les positions sont en pourcentage (0-100) :
- `x: 0` = gauche, `x: 100` = droite
- `y: 0` = haut, `y: 100` = bas

Pour trouver les bonnes coordonnées :
1. Ouvrez la page dans votre navigateur
2. Faites un clic droit sur le plan > "Inspecter"
3. Dans la console, tapez :
```javascript
document.getElementById('floor-plan').addEventListener('click', (e) => {
    const rect = e.target.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width * 100).toFixed(2);
    const y = ((e.clientY - rect.top) / rect.height * 100).toFixed(2);
    console.log(`{ x: ${x}, y: ${y} }`);
});
```
4. Cliquez sur le plan pour obtenir les coordonnées

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
sceneFadeDuration: 1000 // Durée en millisecondes
```

## 🐛 Dépannage

**Les images ne s'affichent pas** :
- Vérifiez que les chemins sont corrects
- Si vous testez en local, utilisez un serveur HTTP (pas file://)

**Le plan ne s'affiche pas** :
- Vérifiez le chemin de l'image
- Pour les SVG en ligne, vérifiez l'encodage URL

**Les points ne sont pas aux bons endroits** :
- Utilisez l'outil de détection des coordonnées (voir section 4)

## 📝 Licence

Code libre d'utilisation pour vos projets personnels et commerciaux.

## 🙏 Crédits

- Pannellum : https://pannellum.org/
- Images d'exemple : Matthew Petroff

---

Bon voyage virtuel ! 🚀
