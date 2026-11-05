# Inhalts-Brief: Raketentriebwerke

Gemeinsame fachliche Grundlage für alle Demos und die spätere Website.
Alle Texte auf Deutsch. Zahlen sind gerundete Richtwerte ("ca.").

## Verständnisstufen

| Stufe | Name | Zielgruppe | Ton |
|---|---|---|---|
| 1 | **Einsteiger** | Neugierige ab ca. 10 Jahren | Alltagsanalogien, keine Formeln, kurze Sätze |
| 2 | **Fortgeschritten** | Schüler:innen Oberstufe, Technikinteressierte | Fachbegriffe mit Erklärung, qualitative Physik |
| 3 | **Experte** | Studierende, Ingenieur:innen | Formeln, Kennzahlen, Zyklusvergleiche, Zielkonflikte |

Die Stufe ändert **Text, Beschriftungen und Detailgrad der Animation** (z.B. Stufe 1: Teile grob,
Stufe 3: Turbopumpen, Vorbrenner, Druckwerte eingeblendet).

## Kernprinzip (alle Triebwerke)

- **Stufe 1:** Wie ein Luftballon, den man loslässt: Gas strömt nach hinten raus, die Rakete wird nach vorne
  gedrückt. Je schneller und je mehr Gas rausschießt, desto stärker der Schub. Die Rakete braucht keine Luft
  zum Abstoßen – das funktioniert auch im Weltall.
- **Stufe 2:** Drittes Newtonsches Gesetz (actio = reactio). Treibstoff und Oxidator verbrennen in der
  Brennkammer, das heiße Gas steht unter hohem Druck. Die **Lavaldüse** verengt sich erst (Gas wird
  schneller), erreicht im engsten Querschnitt (**Düsenhals**) Schallgeschwindigkeit und beschleunigt im
  sich erweiternden Teil auf Überschall. Der **spezifische Impuls (Isp)** misst, wie effizient ein Triebwerk
  seinen Treibstoff nutzt.
- **Stufe 3:**
  - Schub: `F = ṁ · vₑ + (pₑ − pₐ) · Aₑ`
  - Spezifischer Impuls: `Isp = vₑ,eff / g₀` (g₀ = 9,80665 m/s²)
  - Raketengleichung (Ziolkowski): `Δv = vₑ · ln(m₀ / m_f)`
  - Lavaldüse: Unterschall konvergent → Ma = 1 im Hals → Überschall divergent; Expansionsverhältnis
    ε = Aₑ / A* bestimmt, auf welchen Umgebungsdruck die Düse optimiert ist.
  - Überexpansion (pₑ < pₐ, auf Meereshöhe) bzw. Unterexpansion (pₑ > pₐ) erzeugt **Stoßdiamanten**
    (Mach-Scheiben) im Abgasstrahl.

## Triebwerkstypen

### 1. Feststofftriebwerk
- **Beispiel:** Space-Shuttle-Booster (SRB), SLS-Booster, Silvesterrakete
- **Stufe 1:** Wie eine riesige Wunderkerze in einem Rohr: Der Treibstoff ist fest und brennt von innen
  nach außen ab. Einmal gezündet, lässt er sich nicht mehr ausschalten.
- **Stufe 2:** Treibstoff (z.B. APCP: Ammoniumperchlorat als Oxidator, Aluminiumpulver, HTPB-Kunststoff als
  Binder) ist als **Treibsatz (Grain)** ins Gehäuse gegossen. Ein Kanal in der Mitte brennt nach außen ab.
  Einfach, lagerfähig, enormer Schub – aber nicht abschaltbar und kaum regelbar.
- **Stufe 3:** Schubverlauf über die **Kanalgeometrie** (Stern-, Zylinder-, Finocyl-Querschnitt) gesteuert,
  da Brennfläche × Abbrandrate den Massenstrom bestimmt. Isp ca. 240–270 s (Vakuum). Abbrandrate
  `r = a · pᶜⁿ` (Saint-Robert/Vieille).
  Shuttle-SRB (je Booster): Schub ca. 12 MN beim Abheben (kurz danach bis ca. 14,7 MN), Isp ca. 242 s
  (Meereshöhe) / ca. 268 s (Vakuum), Kammerdruck ca. 62 bar, Brenndauer ca. 123 s, ca. 500 t Treibstoff.

### 2. Flüssigtriebwerk – Gasgenerator-Zyklus (offener Zyklus)
- **Beispiel:** SpaceX Merlin 1D (RP-1/Kerosin + Flüssigsauerstoff), Saturn-V-F-1
- **Stufe 1:** Zwei flüssige Zutaten werden mit starken Pumpen in eine Kammer gespritzt und verbrannt. Man
  kann das Triebwerk an- und ausschalten und stärker oder schwächer stellen.
- **Stufe 2:** Eine **Turbopumpe** fördert Treibstoff und Oxidator mit hohem Druck zum **Einspritzkopf**.
  Angetrieben wird die Turbine von einem kleinen **Gasgenerator**, der etwas Treibstoff verbrennt. Dessen
  Abgas wird ungenutzt über ein eigenes Rohr abgeleitet (sichtbar als dunkle Abgasfahne neben der Düse).
  Die Düsenwand wird vom Treibstoff gekühlt (**Regenerativkühlung**).
- **Stufe 3:** Offener Zyklus: der Gasgenerator-Massenstrom (einige %) trägt kaum zum Schub bei → Isp-Verlust.
  Merlin 1D: Kammerdruck ca. 100 bar, Schub ca. 850 kN (Meereshöhe), Isp ca. 282 s (Meereshöhe) /
  ca. 311 s (Vakuum). Brennstoffreicher Gasgenerator hält die Turbinentemperatur niedrig.
  Ergänzend: Schub ca. 914 kN (Vakuum), Masse ca. 470 kg (Schub/Gewicht ca. 180), regelbar bis ca. 40 %.

### 3. Flüssigtriebwerk – Hauptstrom-/Stufenverbrennung (geschlossener Zyklus)
- **Beispiel:** RS-25 (Space-Shuttle-Haupttriebwerk, LH2/LOX), SpaceX Raptor (Methan/LOX, Full-Flow)
- **Stufe 1:** Wie der Gasgenerator, aber nichts wird verschwendet: Auch das Gas, das die Pumpen antreibt,
  landet am Ende in der Brennkammer und schiebt mit.
- **Stufe 2:** Ein **Vorbrenner** verbrennt einen Teil der Treibstoffe, treibt damit die Turbine an – und das
  heiße, noch brennbare Gas wird danach in die Hauptbrennkammer geleitet. Höherer Druck, höhere Effizienz,
  aber technisch deutlich schwieriger.
- **Stufe 3:** Full-Flow Staged Combustion (Raptor): **zwei** Vorbrenner – einer brennstoffreich (treibt die
  Methanpumpe), einer sauerstoffreich (treibt die LOX-Pumpe); beide Ströme werden vollständig gasförmig
  eingespritzt → sehr gute Durchmischung. Raptor: Kammerdruck ca. 300 bar, Isp ca. 327 s (Meereshöhe) /
  ca. 350 s (Vakuum-Variante ca. 380 s). RS-25: brennstoffreiche Stufenverbrennung, Isp ca. 366 s (Meereshöhe) /
  ca. 452 s (Vakuum). Herausforderung: oxidatorreiches Heißgas greift Metalle an → Spezialleg­ierungen.
  Ergänzend: Raptor 2 Schub ca. 2260 kN (Meereshöhe), Masse ca. 1,6 t, regelbar ca. 40–100 %.
  RS-25 (109 % Leistungsstufe): Schub ca. 1860 kN (Meereshöhe) / ca. 2280 kN (Vakuum), Kammerdruck ca. 206 bar,
  Masse ca. 3,2 t, regelbar ca. 67–109 %.

### 4. Ionentriebwerk (elektrischer Antrieb)
- **Beispiel:** NASA Dawn (NSTAR), ESA BepiColombo
- **Stufe 1:** Statt Feuer wird Gas elektrisch aufgeladen und mit einem Spannungsgitter extrem schnell nach
  hinten geschossen. Der Schub ist so sanft wie das Gewicht eines Blatt Papiers – aber er hält
  monatelang an.
- **Stufe 2:** Das Edelgas **Xenon** wird durch Elektronenstöße **ionisiert**. Zwei Gitter mit hoher
  Spannung beschleunigen die positiven Ionen auf ca. 30–40 km/s. Ein **Neutralisator** gibt Elektronen in den
  Strahl, damit das Raumfahrzeug nicht elektrisch auflädt. Funktioniert nur im Vakuum.
- **Stufe 3:** Isp ca. 3000 s (NSTAR ca. 3100 s), Schub ca. 0,09 N (NSTAR max. ca. 92 mN) bei ca. 2,3 kW.
  Schub begrenzt durch Raumladung (Child-Langmuir-Gesetz). Dawn sammelte über ca. 11 Jahre ca. 11 km/s Δv.

### 5. Flüssigtriebwerk – Expander-Zyklus (geschlossener Zyklus)
- **Beispiel:** RL10 (Centaur-Oberstufe von Atlas V / Vulcan, Delta-IV- und SLS-Oberstufe; LH2/LOX). Ebenfalls
  nach dem Expander-Prinzip: Vinci (Oberstufe der Ariane 6).
- **Stufe 1:** Hier braucht die Pumpe keinen eigenen kleinen Motor: Der eiskalte Wasserstoff fließt zuerst um die
  heiße Brennkammer herum, wird dabei warm und zu Gas – und dieses Gas dreht die Pumpe wie Wind ein Windrad.
  Danach wird es ganz normal verbrannt.
- **Stufe 2:** Kein Gasgenerator, kein Vorbrenner: Die **Abwärme** von Brennkammer- und Düsenwand verdampft und
  erhitzt den Wasserstoff in den **Kühlkanälen**. Das sich ausdehnende („expandierende“) Gas treibt die
  **Turbine** und strömt danach in die Brennkammer – nichts geht über Bord. Sehr zuverlässig, mehrfach zündbar,
  sehr effizient, aber nur für kleinere Schübe geeignet → typisch für Oberstufen.
- **Stufe 3:** Die Turbinenleistung ist durch die übertragbare Wärme begrenzt: Wärmeeintrag wächst mit der
  Wandfläche (~ L²), der Leistungsbedarf mit Volumen bzw. Schub (~ L³) → „Würfel-Quadrat-Problem“ deckelt Schub
  und Kammerdruck. Wasserstoff passt ideal (hohe Wärmekapazität, verkokt nicht). RL10B-2: Schub ca. 110 kN
  (Vakuum), Isp ca. 465 s (Vakuum), Kammerdruck ca. 44 bar, O/F ca. 5,9, ε ca. 280 (ausfahrbare
  Carbon-Carbon-Düsenverlängerung), Masse ca. 300 kg. RL10C-1 (Centaur, Atlas V): ca. 102 kN, ca. 450 s.
  Reines Vakuumtriebwerk – ein Isp auf Meereshöhe ist nicht sinnvoll.

### 6. Flüssigtriebwerk – druckgefördert, hypergol
- **Beispiel:** AJ10-137 (Haupttriebwerk des Apollo-Service-Moduls, „SPS“; Aerozine 50 + N₂O₄),
  SpaceX Draco (Steuertriebwerke der Dragon-Kapsel; MMH + N₂O₄)
- **Stufe 1:** Keine Pumpen, keine Zündkerze: Die Tanks stehen unter Gasdruck, der die zwei Flüssigkeiten in die
  Kammer drückt – wie bei einer Sprühflasche. Treffen sie sich, fangen sie von selbst Feuer. Deshalb startet so ein
  Triebwerk extrem zuverlässig, immer wieder.
- **Stufe 2:** **Hypergol** heißt: Brennstoff (Hydrazin-Abkömmlinge wie MMH oder Aerozine 50) und Oxidator
  (Distickstofftetroxid N₂O₄) entzünden sich bei Berührung selbst. **Helium** aus Hochdruckflaschen drückt über
  **Druckregler** die Treibstoffe aus den Tanks (**Druckförderung** statt Turbopumpe). Vorteile: wenige bewegte
  Teile, bei Raumtemperatur lagerfähig (nicht kryogen), beliebig oft zündbar. Nachteile: Die Tanks müssen den
  vollen Förderdruck aushalten → schwer; der Kammerdruck bleibt daher niedrig. Die Treibstoffe sind hochgiftig.
- **Stufe 3:** Tankdruck > Kammerdruck + Verluste (Leitungen, Ventile, Einspritzkopf). Wanddicke eines
  Kugeltanks `s = p · r / (2σ)` → Tankmasse wächst mit dem Druck → niedriges pᶜ, dafür große Düse (hohes ε) für
  gute Vakuum-Isp. AJ10-137: Schub ca. 91 kN (Vakuum), Isp ca. 314 s (Vakuum), Kammerdruck ca. 7 bar,
  ε ca. 62,5. Draco: ca. 400 N, Isp ca. 300 s (Vakuum); SuperDraco (Rettungssystem der Crew Dragon) ca. 70 kN,
  tief regelbar. Lagerfähig → monate- bis jahrelange Missionen ohne Verdampfungsverluste.

### 7. Flüssigtriebwerk – Stufenverbrennung oxidatorreich
- **Beispiel:** RD-180 (NPO Energomasch, Russland; Erststufe der Atlas V, RP-1/LOX), abgeleitet vom
  vierkammrigen RD-170
- **Stufe 1:** Wie beim Raptor oder RS-25 wird nichts verschwendet – aber der kleine Vorbrenner verbrennt viel
  Sauerstoff mit nur ganz wenig Kerosin. So entsteht kein Ruß, der die Turbine verstopfen würde.
  Ein Triebwerk, zwei Düsen.
- **Stufe 2:** (Fast) der gesamte Sauerstoff und ein kleiner Teil des Kerosins gehen durch einen
  **sauerstoffreichen Vorbrenner**. Das heiße, sauerstoffreiche Gas treibt die Turbine und strömt dann in die
  Hauptbrennkammern, wo das restliche Kerosin dazukommt. **Abgrenzung:** RS-25 = brennstoffreich
  (wasserstoffreiches Turbinengas), Raptor = Full-Flow (ein brennstoff- *und* ein sauerstoffreicher Vorbrenner).
  Kerosin eignet sich schlecht für brennstoffreiche Vorbrenner (Ruß, Verkokung), deshalb oxidatorreich. Preis:
  heißes Sauerstoffgas greift fast alle Metalle an. RD-180: zwei Brennkammern und Düsen an einer gemeinsamen
  Turbopumpe.
- **Stufe 3:** Kammerdruck ca. 267 bar – sehr hoch für Kerosin. Schub ca. 3830 kN (Meereshöhe) / ca. 4150 kN
  (Vakuum), Isp ca. 311 s / ca. 338 s, regelbar ca. 47–100 %, Masse ca. 5,5 t, O/F ca. 2,7, ε ca. 37,
  Massenstrom ca. 1250 kg/s. Zyklusvorteil im direkten Vergleich mit Merlin 1D (gleiche Treibstoffe,
  Gasgenerator): Isp ca. 311/338 s statt ca. 282/311 s. Herausforderung: Gefahr von Metallbränden im
  Sauerstoff-Heißgas → Spezialbeschichtungen und -legierungen in Turbine und Heißgasleitungen.

### 8. Hybridtriebwerk
- **Beispiel:** SpaceShipOne (HTPB + Lachgas N₂O, 2004), SpaceShipTwo „VSS Unity“ (RocketMotorTwo, N₂O)
- **Stufe 1:** Halb fest, halb flüssig: Der Brennstoff ist ein Gummiblock mit Löchern – wie eine dicke Kerze.
  Erst wenn flüssiges Lachgas hindurchströmt, brennt er. Dreht man das Lachgas ab, geht das Feuer aus.
- **Stufe 2:** Ein fester **Brennstoffblock (Grain)**, z.B. HTPB (derselbe Kunststoff, der im Feststofftriebwerk als
  Binder dient), sitzt in der Brennkammer. Der **Oxidator** (N₂O, LOX oder Wasserstoffperoxid) wird flüssig oder
  gasförmig über ein Ventil eingespritzt. Die Flamme brennt als **Diffusionsflamme** in einer dünnen Schicht über
  der Oberfläche; deren Hitze verdampft den Brennstoff. N₂O ist **selbstbedrückend** (Dampfdruck ca. 50 bar bei
  20 °C) → keine Pumpe nötig. Vorteile: sicher (Brennstoff und Oxidator getrennt, Block nicht explosiv),
  abschaltbar, prinzipiell regel- und wiederzündbar, einfacher als ein Flüssigtriebwerk. Nachteile: langsamer
  Abbrand → großer Block mit mehreren Kanälen, das Mischungsverhältnis verschiebt sich während des Brennens,
  schlechtere Durchmischung → Isp zwischen Feststoff und Flüssig.
- **Stufe 3:** Abbrandrate hängt vom Oxidator-Massenstrom ab, nicht (wie beim Feststoff) vom Kammerdruck:
  `r = a · G_oⁿ` (G_o = Oxidator-Massenstromdichte im Kanal in kg/(m²·s)). Weitet sich der Kanal, sinkt G_o →
  **O/F-Verschiebung**. SpaceShipOne-Motor: Schub ca. 74–88 kN (nach Leistungssteigerung im Sept. 2004),
  Brenndauer ca. 76–87 s, Isp ca. 250 s; nicht regelbar – der Schub sinkt mit fallendem Tankdruck.

### 9. Steuerdüsen – Monergol (Hydrazin) und Kaltgas
- **Beispiel:** Hydrazin-Triebwerke der 1-N-Klasse (z.B. MR-103) für Satelliten und Raumsonden; Kaltgas mit
  Stickstoff, z.B. Manned Maneuvering Unit (Rückentornister für Astronauten, Shuttle-Ära), CubeSats,
  Lageregelung der Falcon-9-Erststufe bei der Landung
- **Stufe 1:** Kleine Düsen, die einen Satelliten drehen und ausrichten – wie kurze Puster. Kaltgas: eine
  Druckgasflasche mit Ventil, wie eine Spraydose. Hydrazin: eine Flüssigkeit, die an einem Bett aus Metall-Körnchen
  von selbst zu heißem Gas zerfällt – ganz ohne Feuer und ohne zweiten Stoff.
- **Stufe 2:** **Monergol** = ein einziger Treibstoff. **Hydrazin** (N₂H₄) zerfällt am **Katalysator**
  (Iridium auf Aluminiumoxid-Körnchen) zu heißem Ammoniak, Stickstoff und Wasserstoff (ca. 1000 °C). Ein
  **Magnetventil** öffnet und schließt in Millisekunden → kurze Pulse für feine Drehungen. **Kaltgas:** Stickstoff
  aus einem Hochdrucktank strömt über Druckregler und Ventil durch eine kleine Düse – keine Chemie, keine Hitze,
  sauber und sehr einfach, aber wenig effizient. Viele Systeme laufen im **Blowdown-Betrieb**: Der Tankdruck sinkt
  beim Entleeren, damit auch der Schub.
- **Stufe 3:** Hydrazin, MR-103-Klasse: Schub ca. 0,2–1,1 N (je nach Tankdruck), Isp ca. 200–225 s, kleinste
  Impulse ca. 0,01 N·s. Katalysatorbett wird vorgeheizt; Lebensdauer begrenzt durch Verschleiß und Vergiftung des
  Katalysators. Kaltgas Stickstoff: Isp gemessen ca. 73 s (theoretisch ca. 80 s); Manned Maneuvering Unit:
  24 Düsen à ca. 6 N, Stickstoff bei ca. 310 bar. „Grüne“ Alternative zu Hydrazin: LMP-103S
  (Ammoniumdinitramid-Basis), ca. 6 % mehr Isp, weniger giftig.

### 10. Nuklear-thermisches Triebwerk
- **Beispiel:** NERVA / Project Rover (USA, ca. 1955–1973; Prüfstandstriebwerk XE Prime 1968–1969); DRACO
  (DARPA + NASA, 2021–2025, eingestellt)
- **Stufe 1:** Kein Feuer: Ein kleiner Atomreaktor wird superheiß, und flüssiger Wasserstoff strömt hindurch wie
  Wasser durch einen Tauchsieder. Das heiße Gas schießt aus der Düse – etwa doppelt so effizient wie die besten
  chemischen Triebwerke.
- **Stufe 2:** Kernspaltung von Uran im **Reaktorkern** erzeugt Wärme; **Wasserstoff** strömt durch Kanäle in den
  **Brennelementen** und wird auf über 2000 K erhitzt. Keine Verbrennung, kein Oxidator. Vorteil: Wasserstoff ist
  das leichteste Gas → bei gleicher Temperatur viel höhere Ausströmgeschwindigkeit. **Steuertrommeln** am Rand
  regeln die Reaktorleistung, ein **Strahlenschild** schützt Fracht und Crew. Nachteile: schwer, Strahlung,
  extrem aufwendige Tests, Sicherheits- und politische Fragen; nur für den Betrieb im All gedacht.
- **Stufe 3:** `vₑ ~ √(T / M)`: reines H₂ (M ≈ 2 g/mol) gegenüber Verbrennungsprodukten mit deutlich schwereren
  Molekülen (z.B. H₂O 18 g/mol, CO₂ 44 g/mol). Die Temperatur ist durch die Werkstoffe der Brennelemente begrenzt,
  nicht durch chemische Energie. XE Prime: Schub ca. 247 kN, Reaktorleistung ca. 1,1 GW (thermisch),
  Gastemperatur ca. 2270 K, Kammerdruck ca. 39 bar, Masse ca. 18 t (Schub/Gewicht nur ca. 1,4), 28 Starts.
  Isp: laut NASA ca. 825 s mit NERVA-XE am Prüfstand nachgewiesen, ca. 850 s für das NERVA-Flugtriebwerk
  vorgesehen (Vakuum); Sekundärquellen schwanken (ca. 710–841 s). DRACO-Ziel: über 800 s. Bisher ist kein nuklear-thermisches
  Triebwerk geflogen.

### 11. Aerospike-Düse (Düsenbauform, kein Zyklus)
- **Hinweis:** „Aerospike“ beschreibt nur die **Form der Düse**. Der Kreislauf dahinter kann beliebig sein –
  das XRS-2200 nutzte z.B. einen Gasgenerator-Zyklus mit LH2/LOX.
- **Beispiel:** Rocketdyne XRS-2200 (lineare Aerospike für den Technologieträger X-33, um 2000); heute
  Prüfstands- und Testflug-Projekte (z.B. Pangea Aerospace, POLARIS Raumflugzeuge, Stoke Space)
- **Stufe 1:** Eine normale Düse ist ein Trichter mit fester Größe – sie passt nur in einer bestimmten Höhe perfekt.
  Bei der Aerospike strömt das Gas außen an einem Keil oder Zapfen entlang, und die Luft draußen bildet die zweite
  „Wand“. So passt sich der Strahl beim Aufstieg von selbst an.
- **Stufe 2:** Ringförmige (toroidale) oder in einer Reihe angeordnete (lineare) Brennkammern blasen das Gas schräg
  auf einen **Zentralkörper (Spike)**. Innen begrenzt die feste Spike-Wand den Strahl, außen nur der Umgebungsdruck
  → am Boden wird der Strahl zusammengedrückt, in der Höhe dehnt er sich weiter aus = **Höhenkompensation**.
  Eine Glockendüse ist dagegen auf eine Höhe ausgelegt (sonst Über- bzw. Unterexpansion). Ein **abgeschnittener
  Spike** spart Masse. Linear: Brennkammern einzeln regelbar → Lenkung ohne Schwenken. Nachteile: große, zu
  kühlende Spike-Oberfläche, Masse, aufwendige Fertigung, kaum Flugerfahrung.
- **Stufe 3:** Bei der Glocke ist pₑ durch ε und pᶜ fest; die Aerospike hält pₑ ≈ pₐ über einen weiten
  Höhenbereich, bis ihre Auslegungsexpansion erreicht ist – darüber verhält sie sich wie eine Düse mit festem ε.
  XRS-2200: Schub ca. 909 kN (Meereshöhe) / ca. 1184 kN (Vakuum), Isp ca. 339 s / ca. 439 s, Kammerdruck
  ca. 58 bar, ε ca. 58. Status: X-33 im Jahr 2001 eingestellt (u.a. Versagen des Wasserstofftanks aus
  Faserverbund), das XRS-2200 lief nur am Prüfstand. Bis heute (Stand 2026) ist keine Aerospike in
  Serienproduktion; kleine Aerospikes wurden erprobt (z.B. Zündung im Flug bei POLARIS, 2024).

## Funktions-Phasen (Ablauf pro Triebwerkstyp)

Jede Phase wird in der Funktionsansicht einzeln erklärt (Text je Stufe aus den Kernfakten unten formulieren).
Zahlen nur aus diesem Dokument.

### Gasgenerator (Merlin)
1. **Fördern** – Tanks → Turbopumpe; Pumpe erhöht den Druck auf deutlich über Kammerdruck (ca. 100 bar).
2. **Pumpe antreiben** – Gasgenerator verbrennt etwas Treibstoff (brennstoffreich), Heißgas dreht die Turbine;
   Abgas wird ungenutzt abgeleitet (offener Zyklus).
3. **Kühlen** – Kerosin strömt durch Kühlkanäle in der Wand von Düse und Brennkammer (Regenerativkühlung)
   und wird dabei vorgewärmt.
4. **Einspritzen & Zünden** – Einspritzkopf zerstäubt und mischt Kerosin und LOX; Zündung.
5. **Verbrennen** – Brennkammer: ca. 3500 K, Kammerdruck ca. 100 bar.
6. **Beschleunigen** – Lavaldüse: konvergent (Unterschall) → Hals Ma = 1 → Glocke (Überschall).
7. **Schub** – `F = ṁ · vₑ + (pₑ − pₐ) · Aₑ`; ca. 850 kN (Meereshöhe), Isp ca. 282 s / 311 s.

### Stufenverbrennung (Raptor / RS-25)
1. **Fördern** – Tanks → Turbopumpen (Raptor: je eine für Methan und LOX).
2. **Vorverbrennen** – Vorbrenner verbrennen einen Teil der Treibstoffe und treiben die Turbinen
   (Raptor: brennstoffreicher + sauerstoffreicher Vorbrenner).
3. **Heißgas weiterleiten** – das Turbinen-Abgas geht *nicht* über Bord, sondern in die Hauptbrennkammer
   (geschlossener Zyklus).
4. **Einspritzen** – bei Full-Flow beide Ströme gasförmig → sehr gute Durchmischung.
5. **Verbrennen** – Kammerdruck ca. 300 bar (Raptor).
6. **Beschleunigen** – Lavaldüse wie oben.
7. **Schub** – Isp Raptor ca. 327 s / ca. 350 s; RS-25 ca. 366 s / ca. 452 s.

### Feststoff
1. **Zünden** – ein Zünder an der Spitze entflammt die Oberfläche des Innenkanals.
2. **Abbrand** – der Treibsatz brennt von innen nach außen; die Kanalgeometrie bestimmt Brennfläche und damit
   den Schubverlauf.
3. **Druckaufbau** – Verbrennungsgas füllt den Kanal, Kammerdruck baut sich auf (Abbrandrate `r = a · pᶜⁿ`).
4. **Beschleunigen** – Lavaldüse.
5. **Brennschluss** – Treibstoff verbraucht; nicht vorher abschaltbar. Isp ca. 240–270 s (Vakuum).

### Ionentriebwerk
1. **Xenon-Zufuhr** – kleiner Gasstrom aus dem Xenontank in die Ionisationskammer.
2. **Ionisieren** – Elektronen stoßen Xenon-Atome, es entstehen positive Ionen.
3. **Beschleunigen** – Schirm- und Beschleunigungsgitter (ca. 1 kV) schießen die Ionen auf ca. 30–40 km/s.
4. **Neutralisieren** – Neutralisator gibt Elektronen in den Strahl; Raumfahrzeug lädt sich nicht auf.
5. **Schub** – ca. 0,09 N bei ca. 2,3 kW, Isp ca. 3000 s; sanft, aber monatelang.

### Expander (RL10)
1. **Vorkühlen & Fördern** – Leitungen und Pumpen werden vor dem Start mit Treibstoff heruntergekühlt, damit
   nichts vorzeitig verdampft; dann Tanks → Turbopumpe.
2. **Aufheizen** – flüssiger Wasserstoff strömt durch die Kühlkanäle von Brennkammer und Düse, nimmt deren
   Abwärme auf und wird zu heißem Gas.
3. **Pumpe antreiben** – das expandierende Wasserstoffgas dreht die Turbine (kein Gasgenerator, kein Vorbrenner);
   ein Bypassventil an der Turbine regelt, wie viel Leistung sie bekommt.
4. **Einspritzen & Zünden** – Wasserstoffgas und LOX in die Brennkammer; elektrische Funkenzündung.
5. **Verbrennen** – Kammerdruck ca. 44 bar (RL10B-2), vergleichsweise niedrig.
6. **Beschleunigen** – sehr große Düse (ε ca. 280 beim RL10B-2), nur im Vakuum sinnvoll.
7. **Schub** – ca. 110 kN, Isp ca. 465 s (Vakuum); mehrfach wiederzündbar.

### Druckgefördert, hypergol (AJ10-137 / Draco)
1. **Bedrücken** – Helium aus Hochdruckflaschen strömt über Druckregler in die Treibstofftanks.
2. **Fördern** – der Tankdruck allein drückt Brennstoff und Oxidator durch die Leitungen (keine Pumpe).
3. **Ventile öffnen** – Brennstoff- und Oxidatorventil öffnen gleichzeitig.
4. **Selbstzündung** – im Einspritzkopf treffen die hypergolen Treibstoffe aufeinander und entzünden sich sofort.
5. **Verbrennen** – niedriger Kammerdruck (AJ10-137 ca. 7 bar); Kammerwand ablativ bzw. strahlungsgekühlt.
6. **Beschleunigen** – große Düse (ε ca. 62,5 beim AJ10-137).
7. **Schub** – AJ10-137 ca. 91 kN, Isp ca. 314 s (Vakuum); Ventile zu → aus, beliebig oft neu startbar.

### Stufenverbrennung oxidatorreich (RD-180)
1. **Fördern** – Tanks → eine gemeinsame Turbopumpe für Kerosin und LOX.
2. **Vorverbrennen** – sauerstoffreicher Vorbrenner: (fast) der gesamte LOX + wenig Kerosin, Gas bleibt kühl
   genug für die Turbine und rußfrei.
3. **Pumpe antreiben** – sauerstoffreiches Heißgas dreht die Turbine.
4. **Heißgas weiterleiten** – Turbinenabgas strömt in die beiden Hauptbrennkammern (geschlossener Zyklus).
5. **Einspritzen & Verbrennen** – restliches Kerosin (vorher als Kühlmittel durch die Wand) kommt dazu;
   Kammerdruck ca. 267 bar.
6. **Beschleunigen** – zwei Lavaldüsen, je einzeln schwenkbar.
7. **Schub** – ca. 3830 kN (Meereshöhe) / ca. 4150 kN (Vakuum), Isp ca. 311 s / ca. 338 s.

### Hybrid (SpaceShipOne)
1. **Fördern** – selbstbedrückendes N₂O strömt aus dem Tank, Hauptventil öffnet.
2. **Einspritzen** – Oxidator wird in die Kanäle des festen Brennstoffblocks gesprüht.
3. **Zünden** – ein Zünder startet die Flamme an der Oberfläche des Blocks.
4. **Abbrand** – Diffusionsflamme über der Oberfläche verdampft HTPB; Abbrandrate `r = a · G_oⁿ`,
   das O/F-Verhältnis verschiebt sich, während der Kanal größer wird.
5. **Beschleunigen** – Lavaldüse (ablativ gekühlt, wie beim Feststoff).
6. **Abschalten** – Ventil zu → kein Oxidator, Flamme erlischt. SpaceShipOne: ca. 74–88 kN, Isp ca. 250 s.

### Steuerdüsen (Hydrazin / Kaltgas)
1. **Bereithalten** – Treibstoff unter Druck im Tank (Hydrazin: Membrantank; Kaltgas: Stickstoff bei
   mehreren hundert bar); Hydrazin-Katalysatorbett wird vorgeheizt.
2. **Puls auslösen** – Steuerrechner öffnet das Magnetventil für Millisekunden bis Sekunden.
3. **Gas erzeugen** – Hydrazin zerfällt am Katalysator zu heißem Gas (ca. 1000 °C); beim Kaltgas entfällt dieser
   Schritt.
4. **Beschleunigen** – kleine Düse.
5. **Drehen / Ausrichten** – Düsen an gegenüberliegenden Seiten erzeugen ein Drehmoment; Hydrazin ca. 1 N,
   Isp ca. 200–225 s; Kaltgas Stickstoff Isp ca. 73 s.

### Nuklear-thermisch (NERVA)
1. **Fördern** – Turbopumpe bringt flüssigen Wasserstoff auf Druck.
2. **Kühlen** – Wasserstoff kühlt zuerst Düse, Reflektor und Abschirmung und wird dabei gasförmig.
3. **Pumpe antreiben** – ein kleiner Teil heißen Wasserstoffs wird abgezweigt und treibt die Turbine
   (bei NERVA-XE als „Hot-Bleed“-Zyklus erprobt).
4. **Aufheizen im Reaktor** – Wasserstoff strömt durch die Kanäle der Brennelemente, wird auf ca. 2270 K erhitzt;
   Steuertrommeln regeln die Leistung (XE Prime ca. 1,1 GW thermisch).
5. **Beschleunigen** – Lavaldüse; Kammerdruck ca. 39 bar (XE Prime).
6. **Schub** – XE Prime ca. 247 kN; Isp ca. 825 s (Vakuum).

### Aerospike (XRS-2200)
1. **Fördern & Antreiben** – Turbopumpen, angetrieben von einem Gasgenerator (wie beim Merlin).
2. **Verbrennen** – viele kleine Brennkammern in einer Reihe entlang der Spike-Kante; Kammerdruck ca. 58 bar.
3. **Anlegen am Spike** – das Gas strömt schräg auf die gekühlte Rampe (Spike) und beschleunigt an ihr entlang.
4. **Höhenkompensation** – außen begrenzt nur der Umgebungsdruck den Strahl: am Boden eng, in der Höhe breit.
5. **Lenken** – lineare Bauform: Brennkammern einzeln gedrosselt statt Triebwerk geschwenkt.
6. **Schub** – ca. 909 kN (Meereshöhe) / ca. 1184 kN (Vakuum), Isp ca. 339 s / ca. 439 s.

## Bauteile im Detail

Gliederung pro Bauteil: **Aufgabe** · **So funktioniert's** · **Aufbau & Material** · **Kennzahlen** ·
**Herausforderung** · **Beteiligt in Phase**. Stufe 1 zeigt nur Aufgabe + ein Satz „So funktioniert's“
(Analogie), Stufe 2 alle Abschnitte ohne Formeln, Stufe 3 zusätzlich Zahlen/Formeln.

### Flüssigtriebwerke (Merlin, Raptor, RS-25)
- **Tanks** – Aufgabe: Treibstoff und Oxidator lagern. LOX ist bei ca. −183 °C flüssig, flüssiger Wasserstoff
  bei ca. −253 °C, Methan bei ca. −162 °C → Tanks isoliert, Treibstoffe „kryogen“. Tankdruck verhindert,
  dass die Pumpe Dampfblasen ansaugt. Merlin/Raptor bedrücken die Tanks mit verdampftem Treibstoff bzw. Helium.
- **Turbopumpe** – Aufgabe: Treibstoffe von wenigen bar Tankdruck auf deutlich über Kammerdruck bringen.
  Aufbau: Turbine und Kreiselpumpe(n) auf einer gemeinsamen Welle; vor dem Pumpenrad sitzt ein **Inducer**
  (schraubenförmiges Vorlaufrad), der Kavitation (Dampfblasenbildung) verhindert. Drehzahl: zehntausende U/min.
  Herausforderung: auf engstem Raum trifft heißes Turbinengas auf tiefkalte Treibstoffe → Wellendichtungen
  müssen Kraftstoff und Oxidator sicher trennen.
- **Gasgenerator** (offener Zyklus) – kleine Brennkammer, die brennstoffreich verbrennt, damit das Gas kühl genug
  für die Turbinenschaufeln bleibt. Das Abgas trägt kaum zum Schub bei → Effizienzverlust, dafür einfacher
  und robuster.
- **Vorbrenner** (geschlossener Zyklus) – wie ein Gasgenerator, aber das Abgas strömt anschließend in die
  Hauptbrennkammer. RS-25: zwei brennstoffreiche Vorbrenner (je einer pro Hochdruck-Turbopumpe).
  Raptor: ein brennstoffreicher (Methanpumpe) und ein sauerstoffreicher (LOX-Pumpe) Vorbrenner.
  Sauerstoffreiches Heißgas ist extrem aggressiv → Speziallegierungen nötig.
- **Einspritzkopf** – Aufgabe: Treibstoffe zerstäuben und im richtigen Mischungsverhältnis (O/F) mischen.
  Bauarten: viele **Koaxial-Elemente** (Oxidator innen, Brennstoff im Ring außen) oder ein zentraler
  **Pintle-Injektor** (Merlin). Herausforderung: Verbrennungsinstabilitäten (Druckschwingungen) vermeiden –
  beim F-1 der Saturn V ein großes Entwicklungsproblem, gelöst u.a. mit Trennwänden (Baffles) am Einspritzkopf.
- **Brennkammer** – Aufgabe: Verbrennung bei hohem Druck (Merlin ca. 100 bar, Raptor ca. 300 bar) und
  ca. 3500 K. Aufbau: Innenwand meist aus **Kupferlegierung** (sehr gute Wärmeleitung) mit eingefrästen
  **Kühlkanälen**, außen ein tragender Mantel. Die Gastemperatur liegt weit über dem Schmelzpunkt der Wand –
  nur die Kühlung hält sie intakt.
- **Kühlkanäle (Regenerativkühlung)** – Treibstoff fließt vor dem Einspritzen durch Kanäle in Brennkammer- und
  Düsenwand, nimmt Wärme auf und bringt sie zurück in den Prozess („regenerativ“). Zusätzlich oft
  Filmkühlung: eine dünne, brennstoffreiche Schicht an der Wand.
- **Düsenhals** – engster Querschnitt A*, hier erreicht das Gas Ma = 1. Höchste Wärmestromdichte im ganzen
  Triebwerk → am stärksten gekühlte Stelle. Der Halsquerschnitt bestimmt zusammen mit dem Kammerdruck den
  Massenstrom.
- **Düsenglocke** – divergenter Teil, beschleunigt auf Überschall. Glockenform statt einfachem Kegel spart
  Länge und Masse. Expansionsverhältnis ε = Aₑ/A*: Merlin 1D (Meereshöhe) ca. 16, RS-25 ca. 69.
  Vakuumdüsen sind viel größer; deren Verlängerung ist oft **strahlungsgekühlt** (z.B. Niob-Legierung,
  glüht im Betrieb orange-rot).
- **Kardanlager (Gimbal)** – lagert das Triebwerk schwenkbar; Hydraulik- oder elektrische Stellzylinder
  schwenken es um wenige Grad und lenken so die Rakete (Schubvektorsteuerung).

### Feststofftriebwerk
- **Gehäuse** – zugleich Brennkammer und Tank. Shuttle-SRB: Stahlsegmente; moderne Motoren oft Faserverbund.
  Innen eine Isolierschicht, damit das Gehäuse nicht durchbrennt.
- **Treibsatz (Grain)** – APCP: Ammoniumperchlorat (Oxidator), Aluminiumpulver (Brennstoff), HTPB (Binder,
  gummiartig). In das Gehäuse gegossen und ausgehärtet. Querschnitt des Kanals (Stern, Zylinder, Finocyl)
  bestimmt die Brennfläche → Schubverlauf.
- **Zünder** – kleiner Treibsatz an der Spitze, der eine Flammenfront in den Kanal schießt.
- **Düse** – meist **ablativ** gekühlt: Kohlefaser-/Phenolharz-Auskleidung trägt beim Abbrand langsam ab und
  nimmt dabei Wärme mit. Lenkung oft über eine schwenkbare Düse (flexibles Lager).

### Ionentriebwerk
- **Xenontank** – Xenon wird unter hohem Druck gespeichert; schwer, chemisch träge, leicht ionisierbar.
- **Ionisationskammer** – Elektronen aus einer **Hohlkathode** stoßen Xenon-Atome und schlagen Elektronen heraus.
  **Magnetringe** zwingen die Elektronen auf längere Bahnen → mehr Stöße, effizientere Ionisation.
- **Gitter** – Schirm- und Beschleunigungsgitter mit tausenden fein ausgerichteten Löchern (NSTAR: Molybdän);
  ca. 1 kV Spannung beschleunigt die Ionen. Lebensdauer begrenzt durch Erosion der Gitter.
- **Neutralisator** – zweite Hohlkathode außen, gibt Elektronen in den Ionenstrahl.
- **Stromversorgung (PPU)** – wandelt Solarstrom (NSTAR ca. 2,3 kW) in die nötigen Spannungen.

Für die folgenden Typen gilt dieselbe Gliederung. Bereits oben beschriebene Bauteile (Tanks, Turbopumpe,
Einspritzkopf, Brennkammer, Kühlkanäle, Düsenhals, Düsenglocke, Kardanlager, Treibsatz, Düse) werden nur
verwiesen – mit ihren Abweichungen.

### Expander (RL10)
- **Kühlmantel als Wärmetauscher** – *Aufgabe:* liefert die Antriebsenergie für die Turbine.
  *So funktioniert's:* wie ein Heizkörper andersherum – die Wand gibt Wärme an den Wasserstoff ab, der dadurch
  zu Gas wird und Druck aufbaut. *Aufbau & Material:* Kühlkanäle wie oben (Regenerativkühlung), aber hier ist die
  aufgenommene Wärme der *einzige* Antrieb der Pumpe. *Kennzahlen:* Wärmeeintrag ~ Wandfläche → begrenzt Schub
  (ca. 100–110 kN) und Kammerdruck (ca. 44 bar). *Herausforderung:* genug Wärme übertragen, ohne die Wand zu
  überhitzen. *Phase:* 2–3.
- **Turbopumpe** – siehe Flüssigtriebwerke; *Abweichung:* angetrieben von gasförmigem, mäßig warmem Wasserstoff
  statt von Verbrennungsgas → schonend für die Turbine, sehr zuverlässig. Beim RL10 treibt die Turbinenwelle
  die Wasserstoffpumpe direkt, die LOX-Pumpe über ein Getriebe. *Phase:* 1, 3.
- **Turbinen-Bypassventil** – *Aufgabe:* Schub einstellen. *So funktioniert's:* ein Teil des Gases wird an der
  Turbine vorbeigeleitet → Pumpe dreht langsamer → weniger Treibstoff, weniger Schub. *Herausforderung:* stabiler
  Start, denn die Turbine bekommt erst Leistung, wenn die Kammer schon heiß ist (Anlauf aus Tankdruck und
  Restwärme). *Phase:* 3.
- **Funkenzünder** – *Aufgabe:* zündet das Gemisch elektrisch; mehrfach verwendbar → viele Wiederzündungen im
  All. *Phase:* 4.
- **Ausfahrbare Düsenverlängerung** – siehe Düsenglocke; *Abweichung:* beim RL10B-2 aus Carbon-Carbon,
  wird erst nach der Stufentrennung ausgefahren → ε ca. 280 bei kompakter Startlänge. *Herausforderung:*
  zuverlässiger Ausfahrmechanismus, Strahlungskühlung. *Phase:* 6.

### Druckgefördert, hypergol (AJ10-137 / Draco)
- **Helium-Druckgasflaschen & Druckregler** – *Aufgabe:* ersetzen die Turbopumpe. *So funktioniert's:* wie die
  Luft in einer Sprühflasche. *Aufbau & Material:* Hochdruckbehälter (oft Titan oder Faserverbund) mit Regler,
  der den Tankdruck konstant hält. *Herausforderung:* Lecks – Helium entweicht durch kleinste Spalte.
  *Phase:* 1–2.
- **Treibstofftanks** – siehe Tanks; *Abweichung:* nicht kryogen, dafür druckfest und damit schwerer; im
  schwerelosen Zustand muss Gas von Flüssigkeit getrennt werden (Membranen, Siebe/Kapillarstrukturen).
  *Phase:* 2.
- **Treibstoffventile** – *Aufgabe:* öffnen Brennstoff und Oxidator gleichzeitig, schnell und dicht.
  *Herausforderung:* zuverlässig über viele Zyklen und lange Lagerzeiten; schon kleine Lecks sind gefährlich, weil
  sich die Treibstoffe selbst entzünden. *Phase:* 3.
- **Einspritzkopf** – siehe oben; *Abweichung:* keine Zündanlage nötig – die Mischung im Einspritzkopf zündet
  selbst. *Phase:* 4.
- **Brennkammer (ablativ / strahlungsgekühlt)** – siehe oben; *Abweichung:* keine Regenerativkühlung durch
  Treibstoff mit hoher Umlaufmenge, sondern ablative Auskleidung (AJ10-137) bzw. eine glühende, strahlungsgekühlte
  Düsenverlängerung. Niedriger Kammerdruck (ca. 7 bar) → geringere Wärmelast. *Phase:* 5–6.

### Stufenverbrennung oxidatorreich (RD-180)
- **Sauerstoffreicher Vorbrenner** – siehe Vorbrenner; *Abweichung:* (fast) der gesamte LOX + wenig Kerosin,
  Gas ist sauerstoffreich und rußfrei. *Herausforderung:* Metallbrand – heißer Sauerstoff kann Turbinenteile
  entzünden → Schutzschichten, Speziallegierungen. *Phase:* 2.
- **Turbopumpe** – siehe oben; *Abweichung:* eine einzige große Turbopumpe versorgt zwei Brennkammern;
  angetrieben von sauerstoffreichem Heißgas mit sehr hohem Druck (Kammerdruck ca. 267 bar).
  *Phase:* 1, 3.
- **Heißgasleitung** – *Aufgabe:* führt das Turbinenabgas zu den Hauptbrennkammern. *Herausforderung:* heißes,
  sauerstoffreiches Gas unter sehr hohem Druck – Dichtungen und Wände müssen beständig sein. *Phase:* 4.
- **Zwei Brennkammern & Düsen** – siehe Brennkammer/Düsenglocke; *Abweichung:* zwei kleinere statt einer großen
  Kammer (beherrschbarere Verbrennungsstabilität), ε ca. 37, beide schwenkbar. *Phase:* 5–6.
- **Chemische Zündung** – *Aufgabe:* eine selbstzündende Startflüssigkeit entflammt das Kerosin-LOX-Gemisch.
  *Phase:* 5.

### Hybridtriebwerk (SpaceShipOne)
- **Oxidatortank** – *Aufgabe:* lagert N₂O flüssig. *So funktioniert's:* wie eine Sahnekapsel – das Lachgas
  drückt sich selbst heraus. *Kennzahlen:* Dampfdruck ca. 50 bar bei 20 °C. *Herausforderung:* Druck und damit
  Schub hängen von der Temperatur ab und fallen beim Entleeren. *Phase:* 1.
- **Hauptventil & Einspritzer** – *Aufgabe:* Oxidator dosieren und verteilen; Ventil zu = Triebwerk aus.
  *Phase:* 2, 6.
- **Brennstoffblock (Grain)** – siehe Treibsatz; *Abweichung:* enthält *keinen* Oxidator, ist darum nicht
  explosiv. SpaceShipOne: HTPB mit vier Kanälen. *Herausforderung:* langsamer Abbrand → viele Kanäle nötig;
  Oberfläche wächst → O/F-Verschiebung. *Phase:* 4.
- **Brennkammer / Gehäuse** – siehe Gehäuse (Feststoff); *Abweichung:* oft mit Vor- und Nachbrennkammer für
  bessere Durchmischung. *Phase:* 3–4.
- **Düse** – siehe Düse (Feststoff), ablativ gekühlt. *Phase:* 5.

### Steuerdüsen (Hydrazin / Kaltgas)
- **Membrantank / Hochdrucktank** – *Aufgabe:* Treibstoff blasenfrei bereitstellen. *So funktioniert's:*
  Hydrazin: eine Gummi- oder Metallmembran trennt Druckgas und Flüssigkeit (Schwerelosigkeit!). Kaltgas:
  Stickstoff bei mehreren hundert bar (MMU ca. 310 bar). *Phase:* 1.
- **Magnetventil** – *Aufgabe:* Puls auslösen. *Kennzahlen:* Millisekunden-Schaltzeiten, kleinste Impulse
  ca. 0,01 N·s (Hydrazin, 1-N-Klasse). *Herausforderung:* über Jahre hunderttausende Schaltspiele dicht bleiben.
  *Phase:* 2.
- **Katalysatorbett** (nur Hydrazin) – *Aufgabe:* zersetzt Hydrazin ohne Zündung. *Aufbau & Material:*
  Aluminiumoxid-Körnchen mit Iridium-Beschichtung, elektrischer Vorheizer. *Kennzahlen:* Zerfallsgas ca. 1000 °C.
  *Herausforderung:* Katalysator verschleißt und kann vergiftet werden → begrenzt die Lebensdauer. *Phase:* 3.
- **Kleine Düse / Düsencluster** – *Aufgabe:* Gas beschleunigen; mehrere Düsen an verschiedenen Seiten erzeugen
  gezielt Drehmomente oder Verschiebungen. *Phase:* 4–5.
- **Druckregler** (Kaltgas) – senkt den Tankdruck auf den Arbeitsdruck der Düse, damit der Schub konstant bleibt.
  *Phase:* 1–2.

### Nuklear-thermisch (NERVA)
- **Reaktorkern & Brennelemente** – *Aufgabe:* Wärmequelle statt Brennkammer. *So funktioniert's:* wie ein
  Tauchsieder mit vielen Röhrchen. *Aufbau & Material:* uranhaltige Graphit-Brennelemente mit Kühlkanälen,
  beschichtet gegen den Angriff von heißem Wasserstoff. *Kennzahlen:* XE Prime ca. 1,1 GW thermisch,
  Gas ca. 2270 K. *Herausforderung:* Erosion und Rissbildung der Brennelemente bei sehr hohen Temperaturen.
  *Phase:* 4.
- **Reflektor & Steuertrommeln** – *Aufgabe:* Reaktorleistung regeln. *So funktioniert's:* drehbare Trommeln
  am Rand haben eine Seite, die Neutronen zurückwirft, und eine, die sie schluckt; Drehen verändert die
  Kettenreaktion. *Phase:* 4.
- **Strahlenschild** – *Aufgabe:* schützt Tanks, Elektronik und Crew vor Neutronen- und Gammastrahlung.
  *Herausforderung:* Masse. *Phase:* (dauernd).
- **Turbopumpe** – siehe oben; *Abweichung:* nur eine Flüssigkeit (Wasserstoff), Antrieb durch heißen,
  abgezweigten Wasserstoff. *Phase:* 1, 3.
- **Düse** – siehe Düsenhals/Düsenglocke; regenerativ durch Wasserstoff gekühlt. *Phase:* 2, 5.

### Aerospike (XRS-2200)
- **Brennkammer-Reihe (Thrust Cells)** – *Aufgabe:* viele kleine Brennkammern statt einer großen, entlang der
  Spike-Kante angeordnet. *Herausforderung:* alle Kammern gleichmäßig versorgen; einzeln drosseln für die
  Lenkung. *Phase:* 2, 5.
- **Spike (Zentralkörper / Rampe)** – *Aufgabe:* innere Wand der Düse. *So funktioniert's:* das Gas „rutscht“
  außen am Keil entlang; die Luft bildet die äußere Wand. *Aufbau & Material:* regenerativ gekühlte Rampe
  (Kühlkanäle wie oben). *Herausforderung:* große heiße Oberfläche → viel Kühlung, viel Masse. *Phase:* 3–4.
- **Abgeschnittene Basis** – *Aufgabe:* spart Länge und Masse; ein Teil des Abgases füllt den Bereich hinter
  der Schnittfläche und erzeugt dort Druck, der mitschiebt. *Phase:* 4.
- **Turbopumpen & Gasgenerator** – siehe Gasgenerator-Zyklus (Merlin). *Phase:* 1.

## Entwicklung & Geschichte (kurz, Stand ca.)
- **Feststoff:** älteste Raketentechnik – Schwarzpulverraketen in China ab ca. 13. Jh. Space-Shuttle-SRB ab 1981;
  SLS-Booster (5 Segmente) erstmals 2022 (Artemis I).
- **Gasgenerator:** F-1 (Saturn V, 1967–1973) mit ca. 6,8 MN Schub das stärkste einkammrige Flüssigtriebwerk
  seiner Zeit. Merlin: Erstflug 2006 (Falcon 1); Merlin 1D fliegt seit 2013 auf Falcon 9 und landet
  wiederverwendbar mit der Erststufe.
- **Stufenverbrennung:** in der Sowjetunion früh perfektioniert (sauerstoffreiche Zyklen, z.B. NK-33, RD-170).
  RS-25: Erstflug 1981 (STS-1), wiederverwendbar; heute auf SLS. Full-Flow-Zyklus lange nur am Prüfstand –
  Raptor flog 2019 erstmals (Starhopper).
- **Ionentriebwerk:** Deep Space 1 (Start 1998) erprobte NSTAR als Hauptantrieb; Dawn (2007–2018) besuchte
  Vesta und Ceres; BepiColombo (Start 2018) fliegt mit Ionentriebwerken zum Merkur.
- **Expander:** RL10 flog erstmals am 27. Nov. 1963 (zwei RL10A-3 an einer Atlas-Centaur) – erstes
  Wasserstoff-Triebwerk im Flug. Bis heute in Varianten im Einsatz (Centaur V / Vulcan, SLS-Oberstufe).
- **Druckgefördert, hypergol:** AJ10-137 flog ab 1966 im Apollo-Service-Modul und brachte die Crews aus dem
  Mondorbit zurück; Abkömmlinge (AJ10-190) dienten im Space Shuttle (OMS) und sitzen heute im Orion-Servicemodul.
  Draco/SuperDraco: SpaceX Dragon (SuperDraco-Test aller acht Triebwerke 2015).
- **Stufenverbrennung oxidatorreich:** sowjetische Stärke (NK-33, RD-170). RD-180 erstmals am 24. Mai 2000
  (Atlas III), seither Erststufe der Atlas V; Lieferstopp aus Russland 2022, Atlas V läuft mit Restbestand aus.
- **Hybrid:** SpaceShipOne erreichte am 21. Juni 2004 über 100 km und gewann am 4. Okt. 2004 den Ansari X Prize.
  SpaceShipTwo „Unity“ erreichte am 13. Dez. 2018 ca. 83 km; letzter Flug Juni 2024.
- **Steuerdüsen:** Kaltgas-Handdüsen schon bei Weltraumausstiegen im Gemini-Programm; Hydrazin-Monergol ist
  seit Jahrzehnten Standard für Satelliten; „grüne“ Ersatzstoffe kommen seit den 2010er-Jahren.
- **Nuklear-thermisch:** Rover/NERVA ab ca. 1955, XE Prime 1968–1969 am Prüfstand, Programmende Januar 1973 –
  nie geflogen. DRACO (DARPA + NASA, ab 2021, Flug ab 2027 geplant) wurde 2025 eingestellt (u.a. wegen stark
  gesunkener Startkosten).
- **Aerospike:** Prüfstandsversuche ab den 1960er-Jahren (Rocketdyne); XRS-2200 für X-33, Programmabbruch 2001.
  Seitdem nur Klein- und Prüfstandsversuche (Stand 2026).

## Bauteile-Glossar (für Beschriftungen / Hover)

| Bauteil | Kurz (Stufe 1) | Fachlich (Stufe 2/3) |
|---|---|---|
| Tank | Hier ist der Treibstoff drin | Kryogene Lagerung, Tankdruck, Autogen-Bedrückung |
| Turbopumpe | Supersaugstarke Pumpe | Turbine + Kreiselpumpe, zehntausende U/min |
| Gasgenerator / Vorbrenner | Kleiner Motor für die Pumpe | Brennstoff- oder oxidatorreiche Teilverbrennung |
| Einspritzkopf | Duschkopf für Treibstoff | Koaxial- / Pintle-Injektor, Zerstäubung & Mischung |
| Brennkammer | Hier brennt es | Kammerdruck pᶜ, Verbrennungstemperatur ca. 3500 K |
| Düsenhals | Engste Stelle | Ma = 1, kritischer Querschnitt A* |
| Düsenglocke | Trichter, der das Gas lenkt | Divergenter Teil, Expansionsverhältnis ε |
| Kühlkanäle | Kühlt die heiße Wand | Regenerativkühlung durch Treibstoff |
| Treibsatz (Grain) | Fester Treibstoff | APCP, Kanalgeometrie bestimmt Schubverlauf |
| Gitter (Ionen) | Elektrische Schleuder | Schirm- und Beschleunigungsgitter, ca. 1 kV |
| Kühlmantel (Expander) | Heizt den Treibstoff auf | Abwärme der Wand treibt die Turbine (Expander-Zyklus) |
| Turbinen-Bypassventil | Gaspedal | Leitet Gas an der Turbine vorbei → regelt Pumpenleistung und Schub |
| Ausfahrbare Düsenverlängerung | Ausziehbarer Trichter | Carbon-Carbon, erst nach Stufentrennung ausgefahren (RL10B-2, ε ca. 280) |
| Helium-Druckgasflasche | Druckluftflasche | Druckförderung statt Turbopumpe, Druckregler hält Tankdruck konstant |
| Hypergoler Treibstoff | Zündet von selbst | MMH / Aerozine 50 + N₂O₄, Selbstzündung bei Kontakt, giftig, lagerfähig |
| Sauerstoffreicher Vorbrenner | Kleiner Sauerstoff-Brenner für die Pumpe | Oxidatorreiche Teilverbrennung, rußfrei, Metallbrand-Gefahr |
| Heißgasleitung | Rohr für heißes Gas | Führt Turbinenabgas in die Hauptbrennkammer |
| Brennstoffblock (Hybrid) | Gummiblock, der brennt | HTPB-Grain ohne Oxidator, Abbrand `r = a · G_oⁿ` |
| Oxidatortank (N₂O) | Lachgas-Flasche | Selbstbedrückend, Dampfdruck ca. 50 bar bei 20 °C |
| Katalysatorbett | Macht aus Flüssigkeit Gas | Iridium auf Aluminiumoxid, zersetzt Hydrazin bei ca. 1000 °C |
| Magnetventil | Schalter für Puster | Millisekunden-Pulse, kleinste Impulsbits |
| Membrantank | Tank mit Gummihaut | Trennt Druckgas und Flüssigkeit in Schwerelosigkeit |
| Reaktorkern / Brennelemente | Superheißer Tauchsieder | Uran-Graphit-Brennelemente mit H₂-Kanälen, ca. 2270 K |
| Steuertrommeln | Drehknopf für den Reaktor | Reflektor-/Absorberseite regelt die Kettenreaktion |
| Strahlenschild | Schutzschild | Abschirmung von Neutronen- und Gammastrahlung |
| Spike (Aerospike) | Keil, an dem das Gas entlangströmt | Zentralkörper, Höhenkompensation, regenerativ gekühlt |

## Farbsprache (Vorschlag, für alle Demos)
- Brennstoff (Kerosin/Methan/Wasserstoff): warmes Orange/Rot
- Oxidator (LOX): kaltes Cyan/Blau
- Heißgas / Verbrennung: Weiß → Gelb → Orange
- Elektrisch / Ionen: Violett/Blau
- Ergänzung (Vorschlag): hypergole Treibstoffe Gelbgrün (Warnfarbe, giftig); Kaltgas/Druckgas Hellgrau;
  Reaktorwärme (nuklear) Grün; Wasserstoff im Reaktor wie Brennstoff (warm), sobald er erhitzt ist.

## Vergleichsdaten (alle Triebwerke)

Datenbasis für Vergleichs-Visualisierungen (z.B. Schub vs. Isp). Konventionen: **alle Werte sind gerundete
Richtwerte (ca.)**, Dezimalpunkt statt Komma, Bereiche als `a–b`, `–` = nicht sinnvoll oder nicht belegt.
Einheiten stehen im Spaltenkopf. Masse = Trockenmasse des Triebwerks. Steuerdüsen (Typ 9) sind in zwei Zeilen
aufgeteilt (Hydrazin / Kaltgas), daher 13 Zeilen.

| id | Name/Beispiel | Typ | Familie | Treibstoffe | Schub Meereshöhe [kN] | Schub Vakuum [kN] | Isp Meereshöhe [s] | Isp Vakuum [s] | Kammerdruck [bar] | Masse [kg] | Wiederzündbar | Regelbar | Einsatz | Reifegrad | Bemerkung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| srb | Space-Shuttle-SRB | Feststoff | fest | APCP (AP + Al + HTPB) | 12000–14700 | – | 242 | 268 | 62 | – | nein | nein | Booster | geflogen | Schubverlauf über Kanalgeometrie; 1981–2011 |
| merlin-1d | Merlin 1D | Gasgenerator | flüssig | RP-1 / LOX | 845 | 914 | 282 | 311 | 100 | 470 | ja | ja | Erststufe | fliegt | regelbar bis ca. 40 % |
| raptor-2 | Raptor 2 | Stufenverbrennung Full-Flow | flüssig | CH4 / LOX | 2260 | – | 327 | 350 | 300 | 1630 | ja | ja | Erststufe, Oberstufe | fliegt | Starship-Testflüge; Vakuumvariante Isp ca. 380 s |
| rs-25 | RS-25 | Stufenverbrennung brennstoffreich | flüssig | LH2 / LOX | 1860 | 2280 | 366 | 452 | 206 | 3180 | nein | ja | Erststufe | fliegt | 109 % Leistungsstufe; regelbar 67–109 % |
| nstar | NSTAR (Dawn) | Ionentriebwerk | elektrisch | Xenon | – | 0.000092 | – | 3100 | – | – | ja | ja | Raumsonde | geflogen | 92 mN bei ca. 2.3 kW |
| rl10b-2 | RL10B-2 | Expander | flüssig | LH2 / LOX | – | 110 | – | 465 | 44 | 300 | ja | nein | Oberstufe | fliegt | RL10C-1: ca. 102 kN / 450 s; Serien-RL10 nicht regelbar |
| aj10-137 | AJ10-137 (Apollo SPS) | Druckgefördert, hypergol | flüssig | Aerozine 50 / N2O4 | – | 91 | – | 314 | 7 | – | ja | nein | Raumschiff-Hauptantrieb | geflogen | Draco: ca. 0.4 kN / ca. 300 s (MMH / N2O4), fliegt |
| rd-180 | RD-180 | Stufenverbrennung oxidatorreich | flüssig | RP-1 / LOX | 3830 | 4150 | 311 | 338 | 267 | 5480 | nein | ja | Erststufe | fliegt | Atlas V, auslaufend; regelbar 47–100 % |
| ss1-hybrid | SpaceShipOne-Motor | Hybrid | Sonderform | HTPB / N2O | – | 74–88 | – | 250 | – | – | nein | nein | Suborbital | geflogen | Schub/Isp ohne Bezugsdruck angegeben; 2004 |
| mr-103 | Hydrazin-Düse 1-N-Klasse (MR-103) | Monergol | flüssig | Hydrazin (N2H4) | – | 0.0002–0.0011 | – | 200–225 | – | 0.33 | ja | begrenzt | Lageregelung | fliegt | Schub sinkt mit Tankdruck (Blowdown) |
| coldgas-n2 | Kaltgas-Düse Stickstoff (z.B. MMU) | Kaltgas | Sonderform | Stickstoff (N2) | – | 0.006 | – | 73 | – | – | ja | nein | Lageregelung | fliegt | Isp theoretisch ca. 80 s; MMU-Düse ca. 6 N |
| nerva-xe | NERVA XE Prime | Nuklear-thermisch | nuklear | LH2 (Reaktorheizung) | – | 247 | – | 825 | 39 | 18100 | ja | – | Oberstufe, interplanetar (geplant) | nur Prüfstand | 28 Starts am Prüfstand; Flugtriebwerk-Auslegung 850 s |
| xrs-2200 | XRS-2200 (X-33) | Aerospike-Düse (Gasgenerator) | Sonderform | LH2 / LOX | 909 | 1184 | 339 | 439 | 58 | – | – | – | Erststufe (geplant) | nur Prüfstand | Düsenbauform, kein Zyklus |

## Formeln & Rechenbeispiele (Lernteil)

Zielgruppe: Grundlagen Raumfahrttechnik; Darstellung pro Stufe abgestuft (Stufe 1 anschaulich ohne Formel,
Stufe 2 qualitativ + einfache Formel, Stufe 3 vollständig). Konstante: g₀ = 9,80665 m/s². Alle Beispiele mit
python3 nachgerechnet und gerundet; Eingangswerte stammen aus diesem Dokument, Annahmen sind als solche markiert.

### F1 – Spezifischer Impuls ↔ effektive Ausströmgeschwindigkeit
- **Stufe 1:** Der Isp sagt, wie „sparsam“ ein Triebwerk ist: Je höher, desto länger schiebt ein Kilo Treibstoff.
- **Stufe 2:** Isp und Ausströmgeschwindigkeit sind dasselbe in anderer Einheit: `vₑ = Isp · g₀`
  (grob: Isp in s × 10 ≈ vₑ in m/s).
- **Stufe 3:** `vₑ,eff = Isp · g₀ = F / ṁ`. Die *effektive* Ausströmgeschwindigkeit enthält den Druckterm der
  Schubgleichung.
- **Größen:** Isp [s], vₑ,eff [m/s], g₀ [m/s²] (Normfallbeschleunigung, reine Umrechnungskonstante), F [N], ṁ [kg/s].
- **Denkfehler:** g₀ ist *nicht* die örtliche Schwerkraft – ein Triebwerk hat auf dem Mars denselben Isp. Und:
  Isp in Sekunden ist keine Brenndauer.
- **Beispiel:** Merlin 1D (Vakuum, 311 s) → ca. 3050 m/s; RL10B-2 (465 s) → ca. 4560 m/s;
  NSTAR (3100 s) → ca. 30 400 m/s (passt zu den ca. 30–40 km/s Ionengeschwindigkeit oben).

### F2 – Raketengleichung (Ziolkowski)
- **Stufe 1:** Eine Rakete wird schneller, indem sie Masse nach hinten wirft. Wie viel schneller, hängt davon ab,
  wie schnell sie das Gas wegschleudert und wie viel ihrer Masse Treibstoff ist.
- **Stufe 2:** `Δv = vₑ · ln(m₀ / m_f)` – doppelte Ausströmgeschwindigkeit = doppeltes Δv; doppelte
  Treibstoffmenge bringt dagegen *weniger* als das Doppelte (Logarithmus).
- **Stufe 3:** `Δv = Isp · g₀ · ln(m₀ / m_f)`; umgestellt `m₀ / m_f = exp(Δv / vₑ)`, Treibstoffanteil
  `m_T / m₀ = 1 − exp(−Δv / vₑ)`. Gilt ohne äußere Kräfte (keine Schwerkraft- und Luftwiderstandsverluste).
- **Größen:** Δv [m/s], vₑ [m/s], m₀ Startmasse [kg], m_f Masse nach Brennschluss [kg], m_T Treibstoffmasse [kg].
- **Denkfehler:** Δv ist nicht die Endgeschwindigkeit im Schwerefeld (Gravitations- und Luftverluste kommen
  dazu); m_f ist die *Leermasse inkl. Nutzlast*, nicht die Treibstoffmasse.
- **Beispiel A (gleiches Massenverhältnis m₀/m_f = 3):** Merlin-Vakuumwert (vₑ ca. 3050 m/s) → Δv ca. 3350 m/s;
  Ionentriebwerk (vₑ ca. 30 400 m/s) → Δv ca. 33 400 m/s – zehnmal mehr.
- **Beispiel B (Δv = 11 km/s wie Dawn):** mit vₑ ca. 3050 m/s wäre m₀/m_f ca. 37 nötig (ca. 97 % der Startmasse
  Treibstoff); mit dem Ionentriebwerk nur ca. 1,44 (ca. 30 % Treibstoff). (Chemischer Fall als
  Gedankenexperiment, ohne Stufung.)

### F3 – Schubgleichung (mit Druckterm)
- **Stufe 1:** Schub entsteht, weil Gas nach hinten rausschießt. Luft außen bremst das Gas eher – im Weltall
  schiebt ein Triebwerk sogar etwas stärker.
- **Stufe 2:** Schub = Massenstrom × Ausströmgeschwindigkeit, plus ein Druckanteil an der Düsenöffnung.
  Deshalb ist der Schub im Vakuum höher als auf Meereshöhe.
- **Stufe 3:** `F = ṁ · vₑ + (pₑ − pₐ) · Aₑ`. Zwischen Meereshöhe und Vakuum ändert sich nur pₐ:
  `F_vak − F_MH = p₀ · Aₑ` (p₀ = 101 325 Pa).
- **Größen:** F [N], ṁ [kg/s], vₑ Strahlgeschwindigkeit am Düsenaustritt [m/s], pₑ Austrittsdruck [Pa],
  pₐ Umgebungsdruck [Pa], Aₑ Düsenaustrittsfläche [m²].
- **Denkfehler:** „Die Rakete stößt sich an der Luft ab“ – falsch, die Luft verringert den Schub (pₐ > 0).
- **Beispiel RD-180:** ṁ ca. 1250 kg/s, F_vak ca. 4150 kN → vₑ,eff = F/ṁ ca. 3320 m/s → Isp ca. 339 s
  (passt zu 338 s). Aus der Schubdifferenz (4150 − 3830) kN = 320 kN folgt Aₑ ≈ 320 000 / 101 325 ca. 3,2 m²
  für beide Düsen, also ca. 1,6 m² bzw. ca. 1,4 m Durchmesser je Düse (rechnerische Schätzung).

### F4 – Massenstrom
- **Stufe 1:** Wie viel Treibstoff pro Sekunde durch das Triebwerk rauscht.
- **Stufe 2:** `ṁ = F / vₑ` – viel Schub bei kleiner Ausströmgeschwindigkeit braucht viel Treibstoff.
- **Stufe 3:** `ṁ = F / (Isp · g₀)`; außerdem gilt am Düsenhals (gedrosselte Strömung) `ṁ ~ pᶜ · A* / √Tᶜ` –
  Kammerdruck und Halsquerschnitt bestimmen den Massenstrom.
- **Größen:** ṁ [kg/s], F [N], Isp [s], pᶜ [Pa], A* [m²], Tᶜ [K].
- **Denkfehler:** Schub und Isp aus *demselben* Betriebspunkt nehmen (Meereshöhe mit Meereshöhe, Vakuum mit Vakuum).
- **Beispiel:** Merlin 1D Meereshöhe: 845 kN / (282 s · g₀) ca. 306 kg/s. NSTAR: 0,092 N / (3100 s · g₀)
  ca. 3,0 · 10⁻⁶ kg/s = ca. 3 mg/s ≈ ca. 0,26 kg pro Tag.

### F5 – Brenndauer
- **Stufe 1:** Wie lange der Tank reicht: viel Treibstoff und sparsamer Verbrauch = lange Brenndauer.
- **Stufe 2:** `t = m_T / ṁ`.
- **Stufe 3:** `t = m_T · Isp · g₀ / F` (konstanter Schub vorausgesetzt).
- **Größen:** t [s], m_T nutzbare Treibstoffmasse [kg], ṁ [kg/s].
- **Denkfehler:** Triebwerke laufen oft gedrosselt oder in Pausen, und ein Rest Treibstoff ist nicht nutzbar →
  reale Brenndauern weichen ab.
- **Beispiel:** RL10B-2: ṁ = 110 kN / (465 s · g₀) ca. 24,1 kg/s; mit angenommen 30 t Treibstoff →
  t ca. 1240 s ≈ ca. 21 min. NSTAR mit angenommen 100 kg Xenon bei ca. 3 mg/s → ca. 3,3 · 10⁷ s ≈ ca. 380 Tage.

### F6 – Schub-Gewichts-Verhältnis
- **Stufe 1:** Ist der Schub größer als das Gewicht, hebt die Rakete ab. Ist er kleiner, bleibt sie stehen.
- **Stufe 2:** `T/W = F / (m · g)`; > 1 nötig zum Abheben vom Boden, im Orbit reicht auch ein winziger Wert.
- **Stufe 3:** Anfangsbeschleunigung beim Senkrechtstart `a = F / m − g`. Zu unterscheiden: T/W des *Triebwerks*
  (Schub / Triebwerksmasse, Maß für Leichtbau) und T/W des *Fahrzeugs*.
- **Größen:** F [N], m [kg], g örtliche Fallbeschleunigung [m/s²] (Erde g₀, Mond ca. 1,62, Mars ca. 3,71).
- **Denkfehler:** T/W < 1 heißt nicht „nutzlos“ – Ionentriebwerke funktionieren im All hervorragend. Und für den
  Start zählt der Schub auf Meereshöhe, nicht der Vakuumschub.
- **Beispiel Triebwerk:** Merlin 1D 845 kN / (470 kg · g₀) ca. 183; RD-180 (Meereshöhe) ca. 71; RL10B-2 (Vakuum)
  ca. 37; NERVA XE Prime ca. 1,4.
- **Beispiel Fahrzeug:** 50-t-Rakete mit einem Merlin 1D: T/W ca. 1,7 → hebt ab (a ca. 7,1 m/s²);
  1000-kg-Sonde mit NSTAR: T/W ca. 9 · 10⁻⁶.

### F7 – Expansionsverhältnis & Düse
- **Stufe 1:** Die Düse ist ein Trichter, der heißes Gas in einen schnellen Strahl verwandelt. Ein größerer
  Trichter holt im Weltall mehr heraus – am Boden wäre er zu groß.
- **Stufe 2:** `ε = Aₑ / A*`. Großes ε → Gas dehnt sich stärker aus, wird kälter und schneller, pₑ sinkt.
  Ideal ist pₑ = pₐ: am Boden kleines ε (Merlin ca. 16), im Vakuum großes ε (RL10B-2 ca. 280). Zu großes ε
  am Boden → Strömungsablösung, Stoßdiamanten, Schubverlust (vgl. Aerospike: passt sich selbst an).
- **Stufe 3:** Flächen-Mach-Beziehung (isentrop):
  `ε = (1/Ma) · [ (2/(γ+1)) · (1 + (γ−1)/2 · Ma²) ]^((γ+1)/(2(γ−1)))`.
  Ideale Austrittsgeschwindigkeit aus Kammerbedingungen:
  `vₑ = √( 2γ/(γ−1) · (R_u / M) · Tᶜ · [1 − (pₑ/pᶜ)^((γ−1)/γ)] )`.
- **Größen:** ε [–], Aₑ, A* [m²], Ma Machzahl [–], γ Isentropenexponent [–], R_u = 8,314 J/(mol·K),
  M molare Masse des Abgases [kg/mol], Tᶜ Kammertemperatur [K], pₑ/pᶜ Druckverhältnis [–].
- **Denkfehler:** „Die Düse beschleunigt das Gas immer“ – im Unterschall beschleunigt der *verengende* Teil,
  erst ab Ma = 1 der erweiternde. Und: mehr Expansion bringt immer weniger Zusatzgewinn.
- **Beispiel (Modellannahmen, keine Messwerte):** γ = 1,2 → Ma = 3 braucht ε ca. 6,7, Ma = 4 ca. 28.
  Kerosin/LOX-ähnlich mit Tᶜ = 3500 K, *angenommen* M = 22 g/mol, γ = 1,2, pₑ/pᶜ = 0,007 → vₑ ca. 2990 m/s
  (Isp ca. 305 s; Größenordnung Merlin-Vakuumwert). Bei pₑ/pᶜ = 0,0007 → ca. 3340 m/s (ca. 340 s).
  Nuklear-thermisch mit reinem H₂: Tᶜ = 2270 K, M = 2 g/mol, *angenommen* γ = 1,4, pₑ/pᶜ = 0,001 →
  vₑ ca. 7540 m/s (Isp ca. 770 s) – trotz kühlerem Gas mehr als das Doppelte, wegen der kleinen Molmasse.

### Spezifikation interaktiver Rechner
Presets = Triebwerke aus der Vergleichstabelle (`id`); Eingaben als Slider + Zahlenfeld, Ausgabe live.

1. **Isp ↔ vₑ-Umrechner**
   - Eingaben: Isp 50–10 000 s (Standard 311, Merlin Vakuum) *oder* vₑ 0,5–100 km/s; Preset-Auswahl.
   - Ausgaben: vₑ [m/s, km/s] bzw. Isp [s]; Balken mit allen Triebwerken zum Vergleich.
   - Formel: `vₑ = Isp · g₀`.
2. **Δv-Rechner (Ziolkowski)**
   - Eingaben: Isp 50–10 000 s (Standard 311) oder Preset; Startmasse m₀ 1–3 000 000 kg (Standard 1000);
     Treibstoffmasse m_T 0 bis 0,99 · m₀ (Standard 500). Umkehrmodus: Ziel-Δv 0–20 000 m/s (Standard 11 000).
   - Ausgaben: Δv [m/s], Massenverhältnis m₀/m_f; im Umkehrmodus nötiger Treibstoffanteil [%].
   - Formel: `Δv = Isp · g₀ · ln(m₀ / (m₀ − m_T))`; Umkehrung `m_T/m₀ = 1 − exp(−Δv / (Isp · g₀))`.
3. **Brenndauer- & Massenstrom-Rechner**
   - Eingaben: Schub F 0,00001–5000 kN (logarithmischer Slider, Standard 845) oder Preset; Isp 50–10 000 s
     (Standard 282); Treibstoffmasse 0,1–1 000 000 kg (Standard 100 000).
   - Ausgaben: ṁ [kg/s bzw. mg/s], Brenndauer t (automatisch in s / min / Tagen).
   - Formel: `ṁ = F / (Isp · g₀)`, `t = m_T / ṁ`.
4. **Schub-Gewichts-Rechner**
   - Eingaben: Schub F (Meereshöhe) 0,00001–50 000 kN (Standard 845) oder Preset; Anzahl Triebwerke 1–40
     (Standard 1); Fahrzeugmasse 1–5 000 000 kg (Standard 50 000); Himmelskörper Erde 9,80665 / Mond 1,62 /
     Mars 3,71 m/s².
   - Ausgaben: T/W [–], Anfangsbeschleunigung `a = n · F / m − g` [m/s²], Anzeige „hebt ab / hebt nicht ab“.
   - Formel: `T/W = n · F / (m · g)`.
5. *(optional, Stufe 3)* **Düsen-Rechner**
   - Eingaben: Tᶜ 1000–4000 K (Standard 3500), M 2–30 g/mol (Standard 22), γ 1,1–1,67 (Standard 1,2),
     pₑ/pᶜ 0,0001–0,5 (Standard 0,007).
   - Ausgaben: ideale vₑ [m/s], Isp [s], Austritts-Machzahl, ε (numerisch aus Flächen-Mach-Beziehung).
   - Formeln: siehe F7; Hinweis „ideale Werte, reale Triebwerke liegen darunter“.

## Quiz (Lernteil)

Ein Block „Teste dich“ am Ende jedes Lern-Abschnitts (Grundlagen, F1–F7). Pro Abschnitt 6 Fragen:
4 für alle Stufen, eine nur für Einsteiger/Fortgeschritten (`St. 1–2`), eine nur für Experte (`St. 3`,
meist eine zusätzliche Rechenaufgabe) – jede Stufe sieht also 5 Fragen. **Bestanden** ab 4 von 5 richtig.
Fragetypen: **MC** (Multiple Choice, genau eine richtige Antwort ✓), **W/F** (wahr/falsch), **Zahl**
(Zahleneingabe; richtig, wenn die Abweichung höchstens die angegebene Toleranz in % beträgt).
Alle Antworten stammen aus diesem Dokument; Rechenaufgaben mit g₀ = 9,80665 m/s² und python3 nachgerechnet.
Rechenaufgaben zu F5 und F6 sind mit exaktem g₀ und Toleranz formuliert. „Nachlesen“ verweist auf die angegebene Stelle.

### Quiz Grundlagen (Kernprinzip, Antriebe ohne Verbrennung)
1. **MC · alle:** Warum funktioniert eine Rakete auch im Weltall? – Sie stößt sich an der Luft ab · ✓ Sie wirft Gas
   nach hinten, der Rückstoß drückt sie nach vorn · Die Erdanziehung zieht sie mit · Sie saugt Luft als Oxidator an.
   *Erklärung:* Actio = reactio – die Rakete braucht keine Luft zum Abstoßen. *Nachlesen:* Kernprinzip.
2. **MC · alle:** Wo erreicht das Gas in der Lavaldüse Schallgeschwindigkeit? – In der Brennkammer · ✓ Im Düsenhals ·
   Am Düsenaustritt · Erst im Abgasstrahl. *Erklärung:* Die Düse verengt sich bis zum engsten Querschnitt
   (Düsenhals, Ma = 1) und beschleunigt danach im erweiternden Teil auf Überschall. *Nachlesen:* Kernprinzip.
3. **W/F · alle:** „Ein Ionentriebwerk verbrennt Xenon.“ – ✓ falsch. *Erklärung:* Xenon wird ionisiert, zwei Gitter
   beschleunigen die Ionen elektrisch; ein Neutralisator gleicht die Ladung aus. *Nachlesen:* Ionentriebwerk (Typ 4).
4. **MC · alle:** Warum ist ein nuklear-thermisches Triebwerk so effizient? – ✓ Reiner Wasserstoff hat eine sehr
   kleine Molmasse (ca. 2 g/mol) → höhere Ausströmgeschwindigkeit · Wasserstoff verbrennt im Reaktor besonders heiß ·
   Es braucht keine Düse · Es stößt Uran aus. *Erklärung:* `vₑ ~ √(T / M)`; keine Verbrennung, kein Oxidator.
   *Nachlesen:* Nuklear-thermisch (Typ 10).
5. **W/F · St. 1–2:** „Hydrazin braucht in einer Steuerdüse einen zweiten Stoff, um zu zünden.“ – ✓ falsch.
   *Erklärung:* Hydrazin ist ein Monergol und zerfällt am Katalysator von selbst zu heißem Gas.
   *Nachlesen:* Steuerdüsen (Typ 9).
6. **Zahl · St. 3:** Wievielmal so hoch ist der Isp von Hydrazin (Mitte von 200–225 s, also 212,5 s) wie der von
   Kaltgas-Stickstoff (ca. 73 s)? – ✓ ca. 2,91 (Toleranz 3 %). *Erklärung:* 212,5 s / 73 s ≈ 2,9 – Kaltgas ist
   einfach, aber wenig effizient. *Nachlesen:* Steuerdüsen (Typ 9).

### Quiz F1 – Spezifischer Impuls ↔ Ausströmgeschwindigkeit
1. **MC · alle:** Was beschreibt der Isp? – ✓ Wie sparsam ein Triebwerk seinen Treibstoff nutzt · Wie lange es
   brennt · Schub pro Kilogramm Triebwerk · Die Zeit bis Ma = 1. *Erklärung:* Je höher der Isp, desto länger schiebt
   ein Kilo Treibstoff. *Nachlesen:* F1.
2. **W/F · alle:** „Auf dem Mars hat ein Triebwerk einen kleineren Isp, weil die Schwerkraft kleiner ist.“ – ✓ falsch.
   *Erklärung:* g₀ ist eine reine Umrechnungskonstante, nicht die örtliche Schwerkraft. *Nachlesen:* F1, Denkfehler.
3. **W/F · alle:** „Ein Isp von 311 s heißt: Das Triebwerk brennt 311 Sekunden.“ – ✓ falsch. *Erklärung:* Isp in
   Sekunden ist keine Brenndauer, sondern vₑ / g₀. *Nachlesen:* F1, Denkfehler.
4. **Zahl · alle:** RL10B-2 hat einen Isp von ca. 465 s. Wie groß ist vₑ = Isp · g₀ in m/s? – ✓ ca. 4560 m/s
   (Toleranz 3 %, die Faustregel „× 10“ liegt mit 4650 noch darin). *Erklärung:* 465 s · 9,80665 m/s² ≈ 4560 m/s.
   *Nachlesen:* F1, Beispiel.
5. **MC · St. 1–2:** Welches Triebwerk stößt sein Gas am schnellsten aus? – Merlin 1D (311 s) · RL10B-2 (465 s) ·
   NERVA XE Prime (825 s) · ✓ NSTAR (3100 s). *Erklärung:* Höchster Isp = höchste Ausströmgeschwindigkeit, bei NSTAR
   ca. 30 km/s. *Nachlesen:* F1, Beispiel.
6. **Zahl · St. 3:** NSTAR hat einen Isp von ca. 3100 s. Wie groß ist vₑ in km/s? – ✓ ca. 30,4 km/s (Toleranz 2 %).
   *Erklärung:* 3100 s · 9,80665 m/s² ≈ 30 400 m/s – passt zu den ca. 30–40 km/s Ionengeschwindigkeit.
   *Nachlesen:* F1, Beispiel.

### Quiz F2 – Raketengleichung (Ziolkowski)
1. **MC · alle:** Was bringt die doppelte Ausströmgeschwindigkeit (gleiches Massenverhältnis)? – ✓ Doppeltes Δv ·
   Mehr als doppeltes Δv · Weniger als doppeltes Δv · Gar nichts. *Erklärung:* Δv = vₑ · ln(m₀/m_f) ist linear in vₑ.
   *Nachlesen:* F2.
2. **W/F · alle:** „Doppelt so viel Treibstoff bringt doppelt so viel Δv.“ – ✓ falsch. *Erklärung:* Wegen des
   Logarithmus bringt doppelte Treibstoffmenge weniger als das Doppelte. *Nachlesen:* F2.
3. **MC · alle:** Was ist m_f in der Raketengleichung? – Die Treibstoffmasse · Die Startmasse · ✓ Die Leermasse
   inkl. Nutzlast nach Brennschluss · Die Masse des Triebwerks. *Erklärung:* m_f ist die Masse nach Brennschluss.
   *Nachlesen:* F2, Denkfehler.
4. **Zahl · alle:** vₑ = 3050 m/s (Merlin-Vakuumwert), m₀/m_f = 3 (ln 3 ≈ 1,1). Wie groß ist Δv in m/s? –
   ✓ ca. 3350 m/s (Toleranz 2 %). *Erklärung:* 3050 m/s · ln 3 ≈ 3350 m/s. *Nachlesen:* F2, Beispiel A.
5. **W/F · St. 1–2:** „Mit demselben Massenverhältnis kommt ein Ionentriebwerk etwa zehnmal so weit wie ein
   Merlin.“ – ✓ wahr. *Erklärung:* vₑ ca. 30 400 statt ca. 3050 m/s → Δv ca. 33 400 statt ca. 3350 m/s.
   *Nachlesen:* F2, Beispiel A.
6. **Zahl · St. 3:** Δv = 11 km/s (wie Dawn) mit vₑ = 30 400 m/s: Welcher Treibstoffanteil m_T/m₀ in % ist nötig? –
   ✓ ca. 30 % (exakt 30,4 %; Toleranz 5 %). *Erklärung:* 1 − exp(−11 000 / 30 400) ≈ 0,30. *Nachlesen:* F2, Beispiel B.

### Quiz F3 – Schubgleichung mit Druckterm
1. **W/F · alle:** „Die Rakete stößt sich an der Luft ab.“ – ✓ falsch. *Erklärung:* Die Luft verringert den Schub
   sogar (pₐ > 0). *Nachlesen:* F3, Denkfehler.
2. **MC · alle:** Wo hat dasselbe Triebwerk mehr Schub? – Auf Meereshöhe · ✓ Im Vakuum · Überall gleich · Nur der
   Treibstoff entscheidet. *Erklärung:* Ohne Umgebungsdruck fällt der bremsende Druckanteil weg. *Nachlesen:* F3.
3. **MC · alle:** Woraus setzt sich der Schub zusammen? – ✓ Massenstrom × Ausströmgeschwindigkeit plus Druckanteil
   an der Düsenöffnung · Nur aus dem Kammerdruck · Gewicht × g · Isp × Triebwerksmasse. *Erklärung:*
   `F = ṁ · vₑ + (pₑ − pₐ) · Aₑ`. *Nachlesen:* F3.
4. **Zahl · alle:** RD-180: ca. 3830 kN auf Meereshöhe, ca. 4150 kN im Vakuum. Um wie viel kN ist der Vakuumschub
   höher? – ✓ 320 kN (Toleranz 1 %). *Erklärung:* 4150 − 3830 = 320 kN – so viel kostet der Luftdruck.
   *Nachlesen:* F3, Beispiel RD-180.
5. **MC · St. 1–2:** Was ändert sich zwischen Meereshöhe und Vakuum? – ✓ Nur der Umgebungsdruck pₐ · Die Treibstoff-
   menge · Die Düsengröße · Die Schwerkraft. *Erklärung:* Darum ist F_vak − F_MH = p₀ · Aₑ. *Nachlesen:* F3.
6. **Zahl · St. 3:** Aus ΔF = 320 kN und p₀ = 101 325 Pa: Wie groß ist die Austrittsfläche Aₑ beider Düsen in m²? –
   ✓ ca. 3,2 m² (exakt 3,16; Toleranz 3 %). *Erklärung:* Aₑ = 320 000 N / 101 325 Pa. *Nachlesen:* F3, Beispiel RD-180.

### Quiz F4 – Massenstrom
1. **MC · alle:** Was ist der Massenstrom ṁ? – ✓ Treibstoffmasse pro Sekunde durch das Triebwerk · Schub pro Sekunde ·
   Gasgeschwindigkeit · Masse des Triebwerks. *Erklärung:* Einheit kg/s. *Nachlesen:* F4.
2. **W/F · alle:** „Für ṁ = F / (Isp · g₀) darf man Vakuumschub mit dem Isp auf Meereshöhe kombinieren.“ – ✓ falsch.
   *Erklärung:* Schub und Isp aus demselben Betriebspunkt nehmen. *Nachlesen:* F4, Denkfehler.
3. **Zahl · alle:** Merlin 1D auf Meereshöhe: F = 845 kN, Isp = 282 s. Wie groß ist ṁ in kg/s? – ✓ ca. 306 kg/s
   (Toleranz 2 %). *Erklärung:* 845 000 N / (282 s · 9,80665 m/s²) ≈ 306 kg/s. *Nachlesen:* F4, Beispiel.
4. **MC · alle:** Gleicher Schub, aber kleinere Ausströmgeschwindigkeit – was folgt? – ✓ Mehr Massenstrom ·
   Weniger Massenstrom · Gleicher Massenstrom · Kein Schub. *Erklärung:* ṁ = F / vₑ. *Nachlesen:* F4.
5. **W/F · St. 1–2:** „Ein Ionentriebwerk wie NSTAR verbraucht nur rund 0,26 kg Xenon pro Tag.“ – ✓ wahr.
   *Erklärung:* ca. 3 mg/s × 86 400 s ≈ 0,26 kg. *Nachlesen:* F4, Beispiel.
6. **Zahl · St. 3:** NSTAR: F = 0,092 N, Isp = 3100 s. Wie groß ist ṁ in mg/s? – ✓ ca. 3,0 mg/s (Toleranz 3 %).
   *Erklärung:* 0,092 / (3100 · 9,80665) ≈ 3,0 · 10⁻⁶ kg/s. *Nachlesen:* F4, Beispiel.

### Quiz F5 – Brenndauer
1. **MC · alle:** Wie berechnet man die Brenndauer? – ✓ Treibstoffmasse ÷ Massenstrom · Schub ÷ Masse · Isp × g₀ ·
   Massenstrom ÷ Treibstoffmasse. *Erklärung:* `t = m_T / ṁ`. *Nachlesen:* F5.
2. **W/F · alle:** „Reale Brenndauern weichen von t = m_T / ṁ ab, weil Triebwerke gedrosselt laufen und ein Rest
   Treibstoff nicht nutzbar ist.“ – ✓ wahr. *Nachlesen:* F5, Denkfehler.
3. **Zahl · alle:** 100 000 kg Treibstoff (Standardwert des Rechners) für ein Merlin 1D mit ca. 306 kg/s. Wie lange
   brennt es in s? – ✓ ca. 327 s (Toleranz 3 %). *Erklärung:* 100 000 kg / 306 kg/s ≈ 327 s ≈ 5,5 min.
   *Nachlesen:* F5 und Rechner 3.
4. **MC · alle:** Gleicher Schub, gleiche Treibstoffmenge, aber höherer Isp – was passiert? – ✓ Längere Brenndauer ·
   Kürzere Brenndauer · Keine Änderung · Mehr Schub. *Erklärung:* `t = m_T · Isp · g₀ / F`. *Nachlesen:* F5.
5. **MC · St. 1–2:** Wie lange reichen angenommen 100 kg Xenon für NSTAR (ca. 3 mg/s)? – ca. 4 Tage · ca. 38 Tage ·
   ✓ ca. 380 Tage · ca. 3800 Tage. *Erklärung:* 100 kg / 3 mg/s ≈ 3,3 · 10⁷ s ≈ 380 Tage. *Nachlesen:* F5, Beispiel.
6. **Zahl · St. 3:** RL10B-2: F = 110 kN, Isp = 465 s, angenommen 30 000 kg Treibstoff. t = m_T · Isp · g₀ / F in s
   (g₀ = 9,80665 m/s²)? – ✓ ca. 1244 s ≈ 21 min (Toleranz 2 %). *Nachlesen:* F5.

### Quiz F6 – Schub-Gewichts-Verhältnis
1. **MC · alle:** Wann hebt eine Rakete vom Boden ab? – ✓ Wenn T/W größer als 1 ist · Wenn T/W kleiner als 1 ist ·
   Bei T/W = 0 · Immer, wenn sie zündet. *Nachlesen:* F6.
2. **W/F · alle:** „Ein Ionentriebwerk mit T/W weit unter 1 ist nutzlos.“ – ✓ falsch. *Erklärung:* Im Orbit reicht
   ein winziger Wert; Ionentriebwerke funktionieren im All hervorragend. *Nachlesen:* F6, Denkfehler.
3. **W/F · alle:** „Für den Start vom Boden zählt der Vakuumschub.“ – ✓ falsch. *Erklärung:* Es zählt der Schub auf
   Meereshöhe. *Nachlesen:* F6, Denkfehler.
4. **Zahl · alle:** 50-t-Rakete mit einem Merlin 1D (845 kN): T/W = F / (m · g₀)? – ✓ ca. 1,7 (exakt 1,72;
   Toleranz 3 %). *Nachlesen:* F6, Beispiel Fahrzeug.
5. **MC · St. 1–2:** Welches Triebwerk hat das höchste T/W des Triebwerks (Leichtbau)? – ✓ Merlin 1D (ca. 183) ·
   RD-180 (ca. 71) · RL10B-2 (ca. 37) · NERVA XE Prime (ca. 1,4). *Nachlesen:* F6, Beispiel Triebwerk.
6. **Zahl · St. 3:** Dieselbe Rakete: Anfangsbeschleunigung a = F / m − g₀ in m/s² (g₀ = 9,80665)? – ✓ ca. 7,1 m/s²
   (exakt 7,09; Toleranz 3 %). *Nachlesen:* F6.

### Quiz F7 – Expansionsverhältnis & Düse
1. **MC · alle:** Was ist das Expansionsverhältnis ε? – ✓ Austrittsfläche ÷ Halsfläche (Aₑ / A*) · Kammerdruck ÷
   Umgebungsdruck · Schub ÷ Gewicht · Länge ÷ Durchmesser der Düse. *Nachlesen:* F7.
2. **MC · alle:** Welche Düse hat das größere ε? – Merlin 1D am Boden · ✓ RL10B-2 im Vakuum · Beide gleich ·
   ε hängt nur vom Treibstoff ab. *Erklärung:* Merlin ca. 16, RL10B-2 ca. 280 – ideal ist pₑ = pₐ. *Nachlesen:* F7.
3. **W/F · alle:** „Im Unterschall beschleunigt der erweiternde Teil der Düse das Gas.“ – ✓ falsch. *Erklärung:* Im
   Unterschall beschleunigt der verengende Teil, erst ab Ma = 1 der erweiternde. *Nachlesen:* F7, Denkfehler.
4. **MC · alle:** Was passiert mit einer zu großen Düse (zu großes ε) am Boden? – ✓ Strömungsablösung, Stoßdiamanten,
   Schubverlust · Mehr Schub · Nichts · Die Düse schmilzt sofort. *Nachlesen:* F7.
5. **Zahl · St. 1–2:** Wievielmal größer ist ε beim RL10B-2 (ca. 280) als beim Merlin (ca. 16)? – ✓ ca. 17,5
   (Toleranz 3 %). *Nachlesen:* F7.
6. **Zahl · St. 3:** Flächen-Mach-Beziehung mit γ = 1,2: Welches ε braucht Ma = 3? – ✓ ca. 6,7 (Toleranz 3 %).
   *Nachlesen:* F7, Beispiel (Modellannahmen).

## Quellen
- RL10: https://en.wikipedia.org/wiki/RL10 · L3Harris: https://www.l3harris.com/all-capabilities/rl10-engine
- RL10B-2 Kammerdruck (633 psi): https://www.nap.edu/read/11780/chapter/13
- RL10A-3-3A / Expander-Grundlagen (NASA): https://ntrs.nasa.gov/api/citations/19950017370/downloads/19950017370.pdf
- AJ10 / Apollo SPS: https://en.wikipedia.org/wiki/AJ10
- Apollo SPS Leistungsdaten (NASA): https://www.nasa.gov/wp-content/uploads/static/history/afj/ap12fj/pdf/a12-mr-sps-eval-19740077562.pdf
- Draco / SuperDraco: https://en.wikipedia.org/wiki/Draco_(rocket_engine_family)
- RD-180: https://en.wikipedia.org/wiki/RD-180
- SpaceShipOne: https://en.wikipedia.org/wiki/SpaceShipOne · SpaceShipTwo: https://en.wikipedia.org/wiki/SpaceShipTwo
- Hybridtriebwerke: https://en.wikipedia.org/wiki/Hybrid-propellant_rocket
- Monergol / Hydrazin: https://en.wikipedia.org/wiki/Monopropellant_rocket
- Hydrazin-Triebwerke (L3Harris Datenblatt): https://www.l3harris.com/sites/default/files/2025-10/l3harris-ar-monopropellant-rocket-engines.pdf
- Kaltgas: https://en.wikipedia.org/wiki/Cold_gas_thruster
- NERVA / Rover: https://en.wikipedia.org/wiki/NERVA
- NERVA-XE Isp 825–850 s (NASA): https://ntrs.nasa.gov/api/citations/20190033337/downloads/20190033337.pdf
- DRACO: https://en.wikipedia.org/wiki/Demonstration_Rocket_for_Agile_Cislunar_Operations
- DRACO Einstellung: https://breakingdefense.com/2025/06/darpas-draco-nuclear-propulsion-project-roars-no-more/
- Aerospike: https://en.wikipedia.org/wiki/Aerospike_engine · XRS-2200: https://en.wikipedia.org/wiki/XRS-2200
- Merlin: https://en.wikipedia.org/wiki/SpaceX_Merlin · Raptor: https://en.wikipedia.org/wiki/SpaceX_Raptor
- RS-25: https://en.wikipedia.org/wiki/RS-25 · Shuttle-SRB: https://en.wikipedia.org/wiki/Space_Shuttle_Solid_Rocket_Booster
