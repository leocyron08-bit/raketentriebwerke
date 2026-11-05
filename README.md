# Raketentriebwerke verstehen · interaktiv

Interaktive 3D-Lernseite: Wie funktionieren Raketentriebwerke?
Gleichzeitig Leos Lernprojekt für Claude Code.

**Live:** https://leocyron08-bit.github.io/raketentriebwerke/

- 11 Antriebe in 3D (Feststoff, Gasgenerator, Stufenverbrennung, Expander, Ionen, NERVA, Aerospike …), Bauteile anklickbar
- Drei Verständnisstufen: Einsteiger / Fortgeschritten / Experte
- Lernteil mit Formeln F1–F7, Rechnern, Glossar und Quiz mit Lernpfad
- Vergleich als Duell zweier Antriebe

## Lokal ansehen

`index.html` im Browser öffnen, oder:

```bash
python3 -m http.server 8000   # dann http://127.0.0.1:8000/
```

## Inhalt
- `index.html` – die Website (eine Datei, Three.js 0.170.0 per CDN)
- `docs/inhalt-triebwerke.md` – Fachinhalt (Texte, Zahlen, Formeln, Quiz)
- `explorations/` – Design-Runden (Demos + Feedback), Board z.B. mit
  `python3 -I .claude/skills/design-shotgun/scripts/board_server.py explorations/final-20261103`
- `.claude/skills/design-shotgun/` – Claude-Code-Skill für Demo-Varianten (`/design-shotgun`)
