
# Population, Epidemic and Traffic Models

## Përmbledhje

Ky repository përmban implementime referencë të disa **modeleve klasike matematikore dhe numerike** që përdoren për të përshkruar dinamika kolektive në sisteme reale.

Modelet e përfshira në këtë paketë lidhen me tre fusha kryesore:

- **Demografia** – evolucioni i popullatave biologjike
- **Epidemiologjia** – përhapja e sëmundjeve infektive
- **Trafiku rrugor** – dinamika kolektive e automjeteve

Këto modele janë zgjedhur sepse:

- janë **relativisht të thjeshta matematikisht**
- kanë **interpretim fizik dhe biologjik të qartë**
- përdoren gjerësisht në **studime shkencore dhe simulime numerike**

Repository është ndërtuar si pjesë e materialeve të kursit universitar:

**Modelling in Physics**

ku studentët mësojnë të kalojnë nga:

- formulimi matematikor
- tek implementimi numerik
- dhe interpretimi i rezultateve.

---

# Motivimi shkencor

Shumë sisteme reale përbëhen nga **shumë elementë ndërveprues**. Shembuj tipikë janë:

- individët në një popullatë biologjike
- njerëzit gjatë një epidemie
- automjetet në një rrugë

Megjithëse sjellja individuale mund të jetë e thjeshtë, ndërveprimi i shumë elementëve shpesh prodhon **dinamikë kolektive komplekse**.

Modelimi matematikor na lejon të:

- kuptojmë mekanizmat themelorë të sistemit
- analizojmë stabilitetin e tij
- kryejmë simulime numerike
- eksplorojmë skenarë të ndryshëm parametrash

Në këtë repository paraqiten disa nga **modelet më të njohura në literaturën shkencore**.

---

# Struktura e repository

Repository është organizuar në mënyrë modulare për të qenë i lehtë për t’u zgjeruar.

```
population_epidemic_traffic_models/

models/
    population_growth.py
    logistic_growth.py
    sir_model.py
    seir_model.py
    traffic_flow.py

visualization/
    epidemic_curves.py
    phase_plots.py
    traffic_simulation.py

main.py
README.md
requirements.txt
```

Struktura ndjek filozofinë:

- **models/** → formulimi matematikor dhe simulimi
- **visualization/** → funksione për grafika
- **main.py** → ndërfaqe për përdorim nga terminali

---

# Modelet e implementuara

## Modeli i rritjes eksponenciale

Ekuacioni diferencial:

$\frac{dN}{dt} = rN$

Ky model përshkruan rritjen e një popullate kur burimet janë të pakufizuara.

Zgjidhja analitike:

$N(t) = N0 e^(rt)$

---

## Modeli logjistik

Ekuacioni:

$\frac{dN}{dt} = rN (1 - N/K)$

ku:

- $r$ është norma e rritjes
- $K$ është kapaciteti mbajtës

Modeli përshkruan rritjen reale të popullatave ku burimet janë të kufizuara.

---

## Modeli SIR

Popullata ndahet në tre kategori:

- $S$ – susceptible
- $I$ – infected
- $R$ – recovered

Ekuacionet:

$\frac{dS}{dt} = -βSI$
$\frac{dI}{dt} = βSI - γI$
$\frac{dR}{dt} = γI$

Parametrat:

$β$ – norma e infektimit  
$γ$ – norma e shërimit

Numri bazë i riprodhimit:

R0 = β / γ

---

## Modeli SEIR

Ky model përfshin edhe kategorinë:

E – exposed

që përfaqëson individët e infektuar por jo ende infektivë.

S → E → I → R

---

## Modeli i trafikut

Simulon lëvizjen e automjeteve në një rrugë diskrete.

Karakteristikat:

- rruga ndahet në qeliza
- automjetet lëvizin në qeliza bosh
- ndërveprimi është lokal

Ky model është një bazë për modele më të avancuara të trafikut.

---

# Vizualizimi

Grafikat realizohen nga moduli:

visualization/

- epidemic_curves.py
- phase_plots.py
- traffic_simulation.py

---

# Instalimi

Instaloni bibliotekat e nevojshme:

python3 -m pip install -r requirements.txt

Bibliotekat:

numpy
scipy
matplotlib

---

# Përdorimi

Modeli demografik:

python3 main.py --model population

Modeli logjistik:

python3 main.py --model logistic

Modeli SIR:

python3 main.py --model sir

Modeli SEIR:

python3 main.py --model seir

Simulimi i trafikut:

python3 main.py --model traffic

---

# Zgjerime të mundshme

Studentët mund të shtojnë:

### Demografia

- modele migrimi
- modele stokastike
- modele me strukturë moshe

### Epidemiologjia

- modele me vaksinim
- modele me rrjete sociale
- modele hapësinore

### Trafiku

- Optimal Velocity Model
- Intelligent Driver Model
- Nagel–Schreckenberg

---

# Qëllimi pedagogjik

Ky repository synon të ndihmojë studentët të:

1. kuptojnë formulimin matematikor të modeleve
2. implementojnë simulime numerike
3. analizojnë ndikimin e parametrave
4. zhvillojnë kode më të avancuara.

Modelet e paraqitura këtu shërbejnë si **bazë për projekte më të avancuara në modelimin shkencor**.
