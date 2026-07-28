#!/usr/bin/env python3
"""Generate/merge Pannellum-style "scenes" entries from a folder of 360° images.

Reprend toutes les images d'un dossier (ex: tour/lesCygnes/images) et genere,
pour chaque image, une entree "scene" (id + title = nom du fichier sans
extension) rattachee a un etage ("floor") donne en parametre.

Usage:
    # Affiche uniquement le JSON des scenes generees (a copier/coller)
    python scripts/generate_floor_scenes.py --images-dir tour/lesCygnes/images --floor rez

    # Fusionne directement les nouvelles scenes dans config.json
    # (ajoute les scenes manquantes dans "scenes" et dans floors[floor].scenes,
    #  sans toucher aux scenes deja presentes)
    python scripts/generate_floor_scenes.py --images-dir tour/lesCygnes/images --floor rez \
        --config tour/lesCygnes/config.json --merge
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--images-dir", required=True, type=Path, help="Dossier contenant les images 360°")
    parser.add_argument("--floor", required=True, help="Id de l'etage (floor) a associer aux scenes, ex: rez")
    parser.add_argument("--config", type=Path, default=None, help="Chemin vers config.json a mettre a jour")
    parser.add_argument("--merge", action="store_true", help="Ecrit directement les changements dans --config")
    parser.add_argument("--output", type=Path, default=None, help="Fichier de sortie pour le JSON des scenes (defaut: stdout)")
    parser.add_argument("--panorama-prefix", default=None, help="Chemin utilise dans le champ 'panorama' avant le nom de fichier (defaut: calcule depuis --config, sinon --images-dir)")
    parser.add_argument("--id-prefix", default="", help="Prefixe ajoute a l'id/titre de chaque scene, ex: 'rez_'")
    parser.add_argument("--hfov", type=int, default=110)
    parser.add_argument("--pitch", type=int, default=0)
    parser.add_argument("--yaw", type=int, default=0)
    parser.add_argument("--force", action="store_true", help="Ecrase les scenes existantes portant le meme id (defaut: ignorees)")
    return parser.parse_args()


def find_images(images_dir: Path) -> list[Path]:
    images = sorted(p for p in images_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS)
    if not images:
        raise SystemExit(f"Aucune image trouvee dans {images_dir}")
    return images


def build_scenes(images: list[Path], floor: str, panorama_prefix: str, id_prefix: str, hfov: int, pitch: int, yaw: int) -> dict:
    scenes = {}
    for image in images:
        stem = image.stem
        scene_id = f"{id_prefix}{stem}"
        scenes[scene_id] = {
            "title": scene_id,
            "floor": floor,
            "hfov": hfov,
            "pitch": pitch,
            "yaw": yaw,
            "type": "equirectangular",
            "panorama": f"{panorama_prefix}/{image.name}",
            "hotSpots": [],
            "mapPosition": {"x": 50, "y": 50},
        }
    return scenes


def merge_into_config(config_path: Path, floor: str, new_scenes: dict, force: bool) -> None:
    config = json.loads(config_path.read_text(encoding="utf-8"))

    floor_entry = next((f for f in config.get("floors", []) if f.get("id") == floor), None)
    if floor_entry is None:
        raise SystemExit(f"Floor '{floor}' introuvable dans {config_path}")

    scenes = config.setdefault("scenes", {})
    floor_scene_ids = floor_entry.setdefault("scenes", [])

    added, skipped = [], []
    for scene_id, scene in new_scenes.items():
        if scene_id in scenes and not force:
            skipped.append(scene_id)
        else:
            scenes[scene_id] = scene
            added.append(scene_id)
        if scene_id not in floor_scene_ids:
            floor_scene_ids.append(scene_id)

    config_path.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Scenes ajoutees/mises a jour: {len(added)}", file=sys.stderr)
    if skipped:
        print(f"Scenes deja existantes ignorees (utiliser --force pour ecraser): {len(skipped)} -> {skipped}", file=sys.stderr)


def main() -> None:
    args = parse_args()
    images = find_images(args.images_dir)

    if args.panorama_prefix:
        panorama_prefix = args.panorama_prefix.rstrip("/")
    elif args.config:
        panorama_prefix = args.images_dir.as_posix().rstrip("/")
    else:
        panorama_prefix = args.images_dir.as_posix().rstrip("/")

    new_scenes = build_scenes(images, args.floor, panorama_prefix, args.id_prefix, args.hfov, args.pitch, args.yaw)

    if args.merge:
        if not args.config:
            raise SystemExit("--merge necessite --config")
        merge_into_config(args.config, args.floor, new_scenes, args.force)
    else:
        output_text = json.dumps(new_scenes, indent=2, ensure_ascii=False)
        if args.output:
            args.output.write_text(output_text + "\n", encoding="utf-8")
        else:
            print(output_text)


if __name__ == "__main__":
    main()
