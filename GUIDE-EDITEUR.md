# 🎨 Guide d'utilisation de l'éditeur de configuration

## 🚀 Lancement rapide

1. Ouvre `config-editor.html` dans ton navigateur
2. Charge ton `config.json` existant OU crée une nouvelle config
3. Modifie tes étages, scènes et positions
4. Exporte ton nouveau `config.json`

---

## 📖 Guide détaillé

### 1️⃣ Onglet "Charger Config"

**Charger un fichier existant :**
- Clique sur la zone de téléchargement
- Sélectionne ton fichier `config.json`
- ✅ Tout est chargé automatiquement !

**Créer une nouvelle config :**
- Clique sur "Créer une nouvelle configuration"
- Tu pars d'une config vierge

---

### 2️⃣ Onglet "Étages"

**Ajouter un étage :**
1. Clique sur "+ Ajouter un étage"
2. Remplis les informations :
   - **ID** : identifiant unique (ex: `ground`, `first`, `basement`)
   - **Nom** : nom affiché (ex: "Rez-de-chaussée", "1er étage")
   - **Plan** : chemin vers l'image du plan
     - Peut être une image : `/images/plan.jpg`
     - Ou un SVG inline : `data:image/svg+xml,...`
3. Enregistre !

**Modifier/Supprimer :**
- Utilise les boutons "✏️ Modifier" ou "🗑️ Supprimer" sur chaque carte

---

### 3️⃣ Onglet "Scènes"

**Ajouter une scène 360° :**
1. Clique sur "+ Ajouter une scène"
2. Remplis :
   - **ID** : identifiant unique (ex: `entrance`, `lobby`)
   - **Titre** : nom affiché (ex: "Entrée principale")
   - **Étage** : à quel étage appartient cette scène
   - **Panorama** : chemin vers l'image 360° (ex: `/images/entrance.jpg`)
   - **HFOV** : champ de vision (110 par défaut)
   - **Pitch/Yaw** : orientation initiale de la caméra

**Ajouter des hotspots (points cliquables) :**
1. Dans la scène, clique sur "+ Ajouter un hotspot"
2. Pour chaque hotspot :
   - **Texte** : ce qui s'affiche (ex: "Aller au salon")
   - **Pitch** : hauteur du point (-90 à 90)
   - **Yaw** : rotation du point (-180 à 180)
   - **Scène ID** : vers quelle scène ce hotspot dirige

💡 **Astuce pour trouver Pitch/Yaw :**
- Ouvre ta visite dans le navigateur
- Appuie sur F12 → Console
- Tape : `viewer.getPitch()` et `viewer.getYaw()`
- Note les valeurs quand tu es bien positionné !

---

### 4️⃣ Onglet "Positions Plan" ⭐

C'est ici que la magie opère !

**Positionner tes scènes visuellement :**
1. Sélectionne un étage dans la liste déroulante
2. Le plan de l'étage s'affiche
3. Sélectionne une scène à positionner
4. **Clique sur le plan** là où tu veux placer cette scène
5. ✅ La position est sauvegardée automatiquement !
6. Répète pour toutes les scènes

**Les points apparaissent en rouge avec des numéros.**

---

### 5️⃣ Onglet "Exporter"

**Télécharger ta configuration :**
1. Vérifie l'aperçu JSON
2. Clique sur "📥 Télécharger config.json"
3. Le fichier est téléchargé !
4. Remplace ton ancien `config.json` par celui-ci

---

## 🎯 Workflow recommandé

### Première utilisation :
1. **Étages** : Crée tous tes étages avec leurs plans
2. **Scènes** : Ajoute toutes tes scènes 360°
3. **Hotspots** : Ajoute les liens entre scènes
4. **Positions** : Place visuellement chaque scène sur son plan
5. **Export** : Télécharge ton config.json

### Modification d'une config existante :
1. **Charger** : Charge ton config.json
2. Modifie ce que tu veux dans les onglets
3. **Export** : Télécharge la version mise à jour

---

## 💡 Astuces

### Trouver les coordonnées Pitch/Yaw pour les hotspots :

**Méthode 1 : Console navigateur**
```javascript
// Dans la console F12, quand tu regardes dans la bonne direction :
viewer.getPitch()  // Note cette valeur
viewer.getYaw()    // Note cette valeur
```

**Méthode 2 : Approximation**
- Pitch = 0 : horizon
- Pitch = -30 : vers le bas
- Pitch = 30 : vers le haut
- Yaw = 0 : devant
- Yaw = 90 : droite
- Yaw = -90 : gauche
- Yaw = 180 : derrière

### Plans d'étage :

**Format recommandé :**
- JPG/PNG pour des photos de plans
- SVG pour des plans vectoriels (plus nets au zoom)

**Taille recommandée :**
- 800-1200px de large
- Pas trop lourde (< 500 KB)

### Organisation des IDs :

**Bonne pratique :**
```
Étages :
- ground
- first  
- second

Scènes :
- ground_entrance
- ground_lobby
- first_room1
- first_room2
```

Ça aide à s'y retrouver !

---

## 🔧 Dépannage

**"Mon plan ne s'affiche pas"**
→ Vérifie que le chemin de l'image est correct
→ Lance un serveur HTTP (php -S localhost:8000)

**"Je ne vois pas mes scènes dans l'onglet Positions"**
→ Vérifie que tes scènes sont bien assignées à un étage
→ Recharge l'onglet Positions

**"Mon JSON ne se télécharge pas"**
→ Vérifie qu'il n'y a pas d'erreurs dans la console (F12)
→ Essaie avec un autre navigateur

---

## 📸 Captures d'écran (ce que tu devrais voir)

### Onglet Étages :
```
┌─────────────────────┐
│ Rez-de-chaussée     │
│ ID: ground          │
│ Scènes: 3           │
│ [Modifier] [Suppr.] │
└─────────────────────┘
```

### Onglet Positions :
```
[Plan de l'étage]
    🔴 1  ← Scène 1
  🔴 2    ← Scène 2
```

Clique sur le plan pour placer les points !

---

## 🎓 Exemple complet

Imaginons une maison avec 2 étages et 4 pièces :

**1. Crée les étages :**
- ID: `ground`, Nom: "Rez-de-chaussée", Plan: `/images/plan-rdc.jpg`
- ID: `first`, Nom: "1er étage", Plan: `/images/plan-etage1.jpg`

**2. Crée les scènes :**
- ID: `entrance`, Titre: "Entrée", Étage: `ground`, Panorama: `/images/360-entrance.jpg`
- ID: `living`, Titre: "Salon", Étage: `ground`, Panorama: `/images/360-living.jpg`
- ID: `bedroom1`, Titre: "Chambre 1", Étage: `first`, Panorama: `/images/360-bedroom1.jpg`
- ID: `bedroom2`, Titre: "Chambre 2", Étage: `first`, Panorama: `/images/360-bedroom2.jpg`

**3. Ajoute des hotspots :**
- Dans `entrance` : hotspot vers `living` (pitch: 0, yaw: 90)
- Dans `living` : hotspot vers `entrance` (pitch: 0, yaw: -90)

**4. Positionne sur les plans :**
- Sélectionne "Rez-de-chaussée"
- Positionne `entrance` et `living`
- Sélectionne "1er étage"  
- Positionne `bedroom1` et `bedroom2`

**5. Exporte !**
→ Tu as ton `config.json` prêt à utiliser !

---

## 🆘 Besoin d'aide ?

L'éditeur sauvegarde tout dans la mémoire du navigateur pendant ta session. Si tu rafraîchis la page, tu perds tes modifications non exportées. Pense à exporter régulièrement !

---

Bon montage de visite virtuelle ! 🚀
