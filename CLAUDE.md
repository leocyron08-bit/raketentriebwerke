# explosion-rocket-engine

Lernprojekt von **Leo Cyron**: Claude Code kennenlernen, indem wir gemeinsam eine interaktive,
animierte 3D-Website bauen, die erklärt, wie Raketentriebwerke funktionieren.

## Wie wir zusammenarbeiten
- Sprache: Deutsch (Code-Bezeichner und Commit-Messages dürfen Englisch sein).
- Leo lernt Claude Code: bei neuen Konzepten (Skills, Subagents, Hooks, Memory, Plan-Mode, Git-Workflow …)
  in 1–2 Sätzen erklären, *was* gerade passiert und *warum* – kurz, nicht dozieren.
- Erst Richtung klären, dann bauen: Design-Entscheidungen laufen über `/design-shotgun`
  (Demos → Board → Feedback), nicht über lange Textbeschreibungen.
- Commits nur auf Anfrage, auf Feature-Branches; `main` bleibt lauffähig.

## Produktziel
- Interaktive 3D-Website mit Motion Design, modern, responsiv.
- **Verständnisstufen umschaltbar:** Einsteiger / Fortgeschritten / Experte – ändern Text, Beschriftungen
  und Detailgrad der Animation.
- **Triebwerkstypen wechselbar** mit animierten Übergängen: Feststoff, Gasgenerator (Merlin),
  Stufenverbrennung (Raptor / RS-25), Ionentriebwerk.
- **Funktionsweise animiert:** Treibstofffluss → Verbrennung → Lavaldüse → Abgasstrahl.

## Struktur
- `docs/inhalt-triebwerke.md` – fachliche Wahrheit (Texte pro Stufe, Zahlen, Glossar, Farbsprache).
  Alle Inhalte kommen von hier; neue Fakten zuerst hier eintragen.
- `explorations/<thema>-<datum>/` – Design-Runden: `variant-*.html`, `board.html`, `variants.json`,
  `feedback.json`, `approved.json`. `explorations/taste.md` = gesammelte Design-Vorlieben.
- `.claude/skills/design-shotgun/` – Projekt-Skill (adaptiert von gstack, MIT).

## Technik (Stand Exploration)
- Kein Node/npm auf dem Rechner. Demos sind einzelne HTML-Dateien, Three.js `0.170.0` per Importmap (jsDelivr).
- Lokal ansehen: `python3 -I .claude/skills/design-shotgun/scripts/board_server.py explorations/<ordner>`
  → http://127.0.0.1:8765/board.html
- Statischer Check (JS-Syntax via macOS JavaScriptCore, CDN-Pinning):
  `python3 -I .claude/skills/design-shotgun/scripts/check_demo.py <datei.html>`
- Der finale Stack (z.B. Vite + Three.js / React Three Fiber) wird nach der Design-Runde entschieden.
