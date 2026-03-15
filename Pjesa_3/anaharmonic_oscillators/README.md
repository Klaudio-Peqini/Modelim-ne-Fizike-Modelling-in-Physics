# Pjesa 3 – Versioni i kodit të prodhimit për oshilatorët

Ky folder përmban një version më të strukturuar dhe më të afërt me një **kod prodhimi** të materialit të zhvilluar në notebook-un e pjesës së tretë të kursit **“Modellimi në Fizikë”**. Qëllimi kryesor është që studentët të kalojnë nga një stil eksplorues i tipit Jupyter Notebook drejt një organizimi më të disiplinuar të kodit, ku:

- modelet fizike ndahen nga skripti kryesor i ekzekutimit;
- parametrat kontrollohen nga terminali;
- i njëjti program mund të përdoret për disa modele përmes flag-ut `--model`;
- figurat mund të ruhen automatikisht për përdorim në raporte, prezantime ose materiale mësimore.

---

## Struktura e folderit

```text
anharmonic_oscillators/
├── main.py
├── oscillator_models.py
├── requirements.txt
└── README.md
```

### Përshkrimi i skedarëve

- `main.py`  
  Skripti kryesor. Ky është entry point-i i projektit. Ai lexon argumentet nga rreshti i komandës, zgjedh modelin përkatës, kryen integrimin numerik dhe gjeneron figurat.

- `oscillator_models.py`  
  Përmban modelet fizike në formë funksionesh Python. Të gjitha anët e djathta të ekuacioneve diferenciale janë të grupuara këtu në një skedar të vetëm, në përputhje me kërkesën që modelet të ndodhen në një script të veçantë.

- `requirements.txt`  
  Lista minimale e paketave të nevojshme për ekzekutimin e kodit.

- `README.md`  
  Udhëzues i detajuar për përdorimin, logjikën e organizimit dhe shembujt e ekzekutimit.

---

## Modelet e përfshira

Ky version mbështet pesë modele kryesore:

1. `harmonic`  
   Oshilatori harmonik klasik:
   $\ddot{x} + \omega^2 x = 0$

2. `anharmonic`  
   Oshilatori anharmonik me term kubik:
   \[
   \ddot{x} + \omega^2 x + \alpha x^3 = 0
   \]

3. `duffing`  
   Oshilatori Duffing:
   \[
   \ddot{x} + \delta \dot{x} + \alpha x + \beta x^3 = \gamma \cos(\omega t)
   \]

4. `vdp`  
   Oshilatori van der Pol:
   \[
   \ddot{x} - \mu (1-x^2)\dot{x} + x = 0
   \]

5. `coupled`  
   Dy oshilatorë të lidhur:
   \[
   \ddot{x} + \omega_x^2 x + \epsilon y = 0, \qquad
   \ddot{y} + \omega_y^2 y + \epsilon x = 0
   \]

---

## Instalimi

Krijoni një ambient virtual dhe instaloni varësitë:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Nëse përdorni një ambient ekzistues, mjafton:

```bash
pip install -r requirements.txt
```

---

## Përdorimi bazë

Forma minimale e ekzekutimit është:

```bash
python main.py --model MODEL_NAME
```

ku `MODEL_NAME` mund të jetë një nga:

```text
harmonic
anharmonic
duffing
vdp
coupled
```

---

## Shembuj konkretë

### 1. Oshilatori harmonik

```bash
python main.py --model harmonic --omega 1.0 --tmax 30 --dt 0.01 --phase
```

Ky komandim:
- zgjedh modelin harmonik,
- vendos frekuencën natyrore `omega = 1.0`,
- simulon deri në `t = 30`,
- përdor hapin e vizualizimit `dt = 0.01`,
- vizaton edhe hapësirën fazore.

### 2. Oshilatori anharmonik

```bash
python main.py --model anharmonic --omega 1.0 --alpha 0.8 --tmax 40 --phase
```

Kjo lejon të analizohet efekti i termit jo-linear në deformimin e lëvizjes.

### 3. Oshilatori Duffing

```bash
python main.py --model duffing --delta 0.2 --alpha -1.0 --beta 1.0 --gamma 0.3 --forcing-omega 1.2 --tmax 100 --phase
```

Ky është rasti më interesant për diskutime mbi shumë-stabilitetin, bifurkacionet dhe hyrjen drejt dinamikës kaotike.

### 4. Oshilatori van der Pol

```bash
python main.py --model vdp --mu 3.0 --tmax 60 --phase
```

Ky shembull është i përshtatshëm për të vizualizuar ciklin limit.

### 5. Dy oshilatorë të lidhur

```bash
python main.py --model coupled --wx 1.0 --wy 1.2 --eps 0.3 --x0 1.0 --v0 0.0 --y0 0.5 --vy0 0.0 --tmax 50 --phase
```

Ky rast ilustron shkëmbimin e energjisë ndërmjet dy shkallëve të lirisë.

---

## Ruajtja automatike e figurave

Nëse dëshironi që figurat të ruhen në disk, përdorni flag-un `--savefig`:

```bash
python main.py --model duffing --phase --savefig --outdir figures
```

Kjo do të krijojë dosjen `figures/` dhe do të ruajë aty figurat përkatëse, p.sh.:

- `duffing_time_series.png`
- `duffing_phase.png`

Mund të ndryshohet edhe rezolucioni:

```bash
python main.py --model vdp --phase --savefig --dpi 200
```

---

## Parametrat kryesorë të disponueshëm

### Parametra të përgjithshëm

- `--model` : zgjedh modelin
- `--tmin` : koha fillestare
- `--tmax` : koha përfundimtare
- `--dt` : hapi kohor për `t_eval`
- `--method` : metoda numerike e `solve_ivp`

### Kushte fillestare

- `--x0`, `--v0` : për modelet një-dimensionale
- `--y0`, `--vy0` : shtesë për modelin `coupled`

### Parametra fizikë

- `--omega` : frekuenca natyrore për modelin harmonik/anharmonik
- `--alpha` : parametër jo-linear
- `--delta`, `--beta`, `--gamma`, `--forcing-omega` : për Duffing
- `--mu` : për van der Pol
- `--wx`, `--wy`, `--eps` : për modelin e lidhur

### Vizualizimi

- `--phase` : vizaton portretin fazor
- `--savefig` : ruan figurat
- `--outdir` : dosja e figurave
- `--dpi` : rezolucioni i figurave

---

## Logjika pedagogjike e këtij organizimi

Ky organizim është i rëndësishëm edhe nga pikëpamja mësimore. Në notebook studentët shohin procesin eksplorues: provohen ide, ndryshohen parametra, bëhen grafika. Në versionin e prodhimit, i njëjti problem ristrukturohet në një formë më profesionale:

1. **ndarje e përgjegjësive**  
   Modelet janë të ndara nga ekzekutimi.

2. **ripërdorshmëri**  
   I njëjti skript mund të përdoret për disa modele.

3. **kontroll nga terminali**  
   Parametrat nuk ndryshohen më brenda kodit, por nga jashtë.

4. **afrim me praktikën reale shkencore**  
   Kjo strukturë i ngjan më shumë mënyrës si organizohen projektet numerike në fizikë, inxhinieri dhe shkencë kompjuterike.

---

## Sugjerime për zgjerim të mëtejshëm

Ky version mund të zgjerohet në disa drejtime:

- shtimi i animacioneve;
- ruajtja e të dhënave numerike në CSV;
- shtimi i një moduli për analizë energjie;
- ndërtimi i seksioneve Poincaré për modelin Duffing;
- llogaritja e eksponentit të Lyapunov-it për raste të zgjedhura;
- ndarja e vizualizimit në një modul më vete, nëse projekti rritet.

---

## Komanda të shpejta të rekomanduara

```bash
python main.py --model harmonic --phase
python main.py --model anharmonic --alpha 1.0 --phase
python main.py --model duffing --alpha -1 --beta 1 --delta 0.2 --gamma 0.3 --forcing-omega 1.2 --tmax 100 --phase
python main.py --model vdp --mu 3.0 --phase
python main.py --model coupled --wx 1.0 --wy 1.2 --eps 0.3 --phase
```

---

## Përmbyllje

Ky folder përfaqëson kalimin nga një material demonstrues drejt një **baze të strukturuar kodesh** për simulimin e oshilatorëve linearë dhe jo-linearë. Ai mund të përdoret:

- si material mësimor për studentët,
- si pikënisje për ushtrime laboratorike,
- si bazë për zgjerime të mëtejshme në temat e bifurkacioneve dhe kaosit.

