"""Crée un aperçu .jpg (page 1) pour chaque PDF du dossier, avec le même nom.

Utilisation :
  1. pip install pymupdf
  2. Place ce fichier dans le dossier de tes PDF renommés
  3. python apercus.py
  4. Dépose les .jpg créés dans le dépôt GitHub, à côté des PDF.
"""
import glob
import os

import fitz  # PyMuPDF

LARGEUR = 720  # largeur de l'aperçu en pixels

for pdf in sorted(glob.glob("*.pdf")):
    if os.path.basename(pdf).lower() == "cv.pdf":
        continue
    page = fitz.open(pdf)[0]
    zoom = LARGEUR / page.rect.width
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    sortie = os.path.splitext(pdf)[0] + ".jpg"
    pix.save(sortie, jpg_quality=80)
    print("OK", sortie)
