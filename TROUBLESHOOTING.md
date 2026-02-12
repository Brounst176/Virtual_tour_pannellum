# 🔧 Guide de dépannage - Visite Virtuelle

## Problème : La deuxième image ne s'affiche pas

Tu as ce problème : la première scène fonctionne, mais quand tu changes de scène, l'image ne s'affiche pas (même si les logs disent que c'est chargé).

---

## ✅ Solutions par ordre de priorité

### 🔥 Solution 1 : Utilise `virtual-tour-fixed.html`

J'ai créé une version corrigée avec :
- Durée de transition réduite (500ms au lieu de 1000ms)
- Appel à `viewer.resize()` après chaque changement
- Configuration optimisée

**Test ça en premier !**

---

### 🖼️ Solution 2 : Vérifie le format de tes images

**Pannellum nécessite des images équirectangulaires (panoramas 360°) avec un ratio 2:1**

Vérifie tes images :
```bash
# Linux/Mac
file /images/from-tree.jpg
file /images/bma-0.jpg

# Ou regarde les propriétés dans ton explorateur de fichiers
```

**Dimensions attendues :**
- 4096 x 2048 pixels
- 8192 x 4096 pixels  
- 2048 x 1024 pixels
- etc. (toujours largeur = 2 × hauteur)

**Si tes images ne sont pas au bon format** :
- Elles doivent être des vraies photos 360° prises avec une caméra 360
- Si ce ne sont pas des 360°, Pannellum ne fonctionnera pas correctement

---

### 🧹 Solution 3 : Vide le cache du navigateur

Parfois le navigateur cache une mauvaise version :

**Chrome/Edge :**
- `Ctrl + Shift + R` (force reload)
- Ou : F12 → Onglet Network → Coche "Disable cache" → Recharge

**Firefox :**
- `Ctrl + Shift + R`
- Ou : `Ctrl + Shift + Del` → Vider le cache

---

### 📏 Solution 4 : Réduis la taille des images

Si tes images sont TROP grandes (> 10 MB), le navigateur peut avoir du mal.

**Redimensionne-les :**
```bash
# Avec ImageMagick
convert input.jpg -resize 4096x2048 output.jpg

# Ou utilise un outil en ligne comme :
# - squoosh.app
# - tinypng.com
```

Cible : **2-5 MB par image maximum**

---

### 🔄 Solution 5 : Change l'ordre des scènes

Tu as dit que ça marche quand tu changes l'ordre. Essaie de mettre `house` en premier dans la config :

```javascript
const tourConfig = {
    // ...
    floors: [
        {
            scenes: ["house", "circle"]  // Inverse l'ordre
        }
    ]
};
```

Si ça marche, c'est un problème de préchargement. Dans ce cas, je peux te faire une version qui précharge toutes les images avant de démarrer.

---

### 🌐 Solution 6 : Teste avec des images de test

Pour savoir si c'est un problème d'images ou de code, teste avec des images 360° publiques :

```javascript
scenes: {
    circle: {
        // ...
        panorama: "https://pannellum.org/images/alma.jpg",  // Image de test
    },
    
    house: {
        // ...
        panorama: "https://pannellum.org/images/cerro-toco-0.jpg",  // Image de test
    }
}
```

Si ça marche avec ces images, le problème vient de tes images.

---

### 🆘 Solution 7 : Version alternative sans Pannellum

Si rien ne marche, je peux te créer une version avec une autre bibliothèque (Photo-Sphere-Viewer ou Marzipano).

---

## 🔍 Diagnostic rapide

Réponds à ces questions pour qu'on cible le problème :

1. **Tes images sont-elles de vraies photos 360° ?** (Oui/Non)
2. **Quelle est la taille de tes fichiers ?** (en MB)
3. **Quelles sont les dimensions exactes ?** (ex: 4096x2048)
4. **Est-ce que `virtual-tour-fixed.html` fonctionne mieux ?** (Oui/Non)
5. **Le problème persiste-t-il après avoir vidé le cache ?** (Oui/Non)

---

## 🚀 Action immédiate

1. ✅ Teste `virtual-tour-fixed.html`
2. ✅ Vide le cache (Ctrl+Shift+R)
3. ✅ Vérifie le format de tes images
4. ✅ Dis-moi si ça marche !

Si le problème persiste, donne-moi les infos du diagnostic et je te ferai une solution sur mesure 😊
