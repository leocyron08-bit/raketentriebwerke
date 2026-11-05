---
name: design-shotgun
description: |
  Interaktive Design-Exploration: erzeugt mehrere (Standard 4) grundverschiedene, lauffähige
  HTML/WebGL-Demos parallel über Subagents, öffnet sie in einem Vergleichsboard im Browser,
  sammelt strukturiertes Feedback (Sterne, Notizen, Favorit, Kombinieren) und iteriert.
  Nutzen bei: "zeig mir Optionen", "Design-Varianten", "neue Richtungen", "gefällt mir nicht",
  "nächste Runde", oder wenn ein UI-/Animationsthema beschrieben wird, das noch niemand gesehen hat.
---

# /design-shotgun – interaktive Demo-Varianten

Adaptiert von gstack `design-shotgun` (MIT, © 2026 Garry Tan, github.com/garrytan/gstack).
Unterschied zum Original: statt KI-Bild-Mockups entstehen **echte, klickbare Demos**
(HTML + Three.js/WebGL/Canvas/SVG), weil es in diesem Projekt um Interaktion und Motion Design geht.
Keine gstack-Binaries, keine OpenAI-API nötig – nur Python 3 (Systemversion reicht).

Du bist Design-Sparringspartner, kein Reviewer. Ziel: schnell sichtbar machen, was möglich ist,
und dann mit dem Feedback des Users eine Richtung festzurren.

## Schritt 0: Vorherige Runden prüfen

```bash
ls -d explorations/*/ 2>/dev/null; cat explorations/taste.md 2>/dev/null
find explorations -name approved.json -maxdepth 2 2>/dev/null | sort -r | head -5
```

Gibt es frühere Runden: kurz zusammenfassen (Datum, Thema, Favorit, Kernfeedback) und fragen, ob
weiter iteriert (neue Runde im selben Thema) oder neu exploriert werden soll.

## Schritt 1: Kontext (max. 2 Rückfragerunden)

Zuerst selbst lesen: `CLAUDE.md`, `docs/inhalt-triebwerke.md` (fachliche Wahrheit), `DESIGN.md` falls vorhanden,
`explorations/taste.md`. Dann fehlende Punkte in **einer** AskUserQuestion bündeln:
Zielgruppe, Kernaufgabe der Seite, Muss-Features, Geräte, Anzahl Varianten (Standard 4, max. 6).
Hat der User das alles schon gesagt: nicht nachfragen, Annahmen notieren.

## Schritt 2: Geschmacks-Gedächtnis

`explorations/taste.md` sammelt rundenübergreifend, was der User mag / ablehnt (Schriften, Farben,
Interaktionsmuster, Tempo). Neue Konzepte daran ausrichten, aber nicht blind kopieren – mindestens
eine Variante darf bewusst dagegen wetten (als solche kennzeichnen).

## Schritt 3: Varianten erzeugen

### 3a Konzepte
Ordner: `explorations/<thema>-<YYYYMMDD>/` (bei weiteren Runden am selben Tag `-r2`, `-r3`).
Formuliere N Konzepte als Liste `A) "Name" – ein Satz`. **Anti-Konvergenz:** jede Variante unterscheidet sich in
mindestens drei Achsen: Farbwelt (hell/dunkel), Typografie, Layout, **Interaktionsmodell**
(scrollen / frei erkunden / Regler / geführte Sequenz) und Motion-Stil.
Test: Könnte man die Überschriften zweier Varianten tauschen, ohne dass es auffällt → zu ähnlich, überarbeiten.

### 3b Bestätigen
Konzepte per AskUserQuestion bestätigen lassen (Generieren / ändern / mehr / weniger).
**Überspringen**, wenn der User ausdrücklich direkt Demos sehen will – dann Konzepte nur im Text nennen.

### 3c Parallel generieren
Pro Variante **einen Subagent** (Agent-Tool, `run_in_background: true`, alle in einer Nachricht).
Jeder Prompt enthält: (1) den gemeinsamen Block unten, (2) die eigene Richtung ausführlich
(Farben, Schriften, Layout, Interaktion, Übergänge, Signature-Moment), (3) den Hinweis, dass andere Agents
andere Richtungen bauen.

Gemeinsamer Block (anpassen, aber diese Punkte immer drin):
- genau eine selbständige Datei `variant-<x>.html` im Explorationsordner, sonst nichts im Repo anfassen
- Inhalte aus `docs/inhalt-triebwerke.md`, keine erfundenen Zahlen; UI auf Deutsch
- Pflicht-Features des Projekts (siehe CLAUDE.md: Verständnisstufen-Umschalter, Triebwerkswechsel mit
  animiertem Übergang, Funktionsanimation)
- Three.js `0.170.0` per Importmap von `cdn.jsdelivr.net`, optional GSAP `3.12.5` von `cdnjs.cloudflare.com`,
  Fonts nur von Google Fonts, Geometrie prozedural, keine Build-Tools
- responsive bis 390 px, pixelRatio ≤ 2, Render-Loop pausiert im Hintergrund-Tab, `prefers-reduced-motion`
- Badge „Variante X · Name“ in einer Ecke
- Bekannte Falle: Bei transparentem Canvas (`alpha: true`) über CSS-Hintergrund müssen additive Shader
  (Flammen, Partikel) Alpha **0.0** schreiben, sonst entstehen dunkle Quadrate (Runde 3 gefunden)
- Text/Labels flackerfrei: keine Seiten-/Sortierentscheidung pro Frame, gedämpft, ganze Pixel, DOM nur bei Änderung
- **Pflicht-Check** vor Abschluss: `python3 -I .claude/skills/design-shotgun/scripts/check_demo.py <datei>` muss OK melden
- Abschlussbericht max. 12 Zeilen inkl. Unsicherheiten

Während die Agents laufen: `variants.json` schreiben (`title`, `round`, `variants[{id,name,file,idea}]`)
und `assets/board.html` als `board.html` in den Ordner kopieren.

## Schritt 4: Board + Feedback-Schleife

Nach Abschluss aller Agents:
```bash
python3 -I .claude/skills/design-shotgun/scripts/check_demo.py explorations/<ordner>/*.html
```
Dann Server im Hintergrund starten (Bash `run_in_background: true`) und Board öffnen:
```bash
python3 -I .claude/skills/design-shotgun/scripts/board_server.py explorations/<ordner> 8765
open http://127.0.0.1:8765/board.html
```
Port belegt → 8766 usw. Dem User sagen: jede Variante ausprobieren, Sterne + Notizen vergeben,
„Feedback an Claude senden“ klicken. Der Server schreibt `feedback.json` und meldet `FEEDBACK_RECEIVED`.
Fallback: „Als Text kopieren“ und ins Terminal einfügen.

Wenn möglich zusätzlich selbst prüfen (Claude in Chrome / eingebauter Browser, falls verfügbar):
jede Variante laden, Konsole auf Fehler prüfen, Screenshot ansehen. Sonst ehrlich sagen, dass nur statisch geprüft wurde.

## Schritt 5: Feedback bestätigen

`feedback.json` lesen und zusammenfassen:
```
FAVORIT: B
WERTUNG: A 3/5 · B 5/5 · C 4/5 · D 2/5
NOTIZEN: …
KOMBINIEREN: …
NÄCHSTE RICHTUNG: …
```
Per AskUserQuestion bestätigen lassen, bevor gespeichert wird.

## Schritt 6: Speichern & weiter

- `approved.json` in den Rundenordner: `{favorite, ratings, decisions[], next_steps[], date}`
- `explorations/taste.md` ergänzen (Gefallen / Abgelehnt / Offene Fragen), knapp halten
- Nächste Schritte anbieten: (A) neue Runde – Favorit verfeinern bzw. Elemente kombinieren,
  (B) Richtung festschreiben → `DESIGN.md` anlegen und Umsetzung planen, (C) Pause

## Regeln

1. Alles bleibt im Repo unter `explorations/` – nachvollziehbar und lernbar.
2. Varianten müssen sich wie von verschiedenen Studios gemacht anfühlen.
3. Feedback immer zurückspiegeln, bevor gespeichert wird.
4. Höchstens 2 Rückfragerunden zum Kontext, dann mit Annahmen arbeiten.
5. Nichts als „funktioniert“ melden, was nur statisch geprüft wurde.
