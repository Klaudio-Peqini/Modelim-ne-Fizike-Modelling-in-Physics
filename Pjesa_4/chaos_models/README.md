# Pjesa 4 — Kaosi dhe sistemet kaotike

Ky folder përmban **versionin production code** të materialit të Pjesës 4 të kursit **Modelim në Fizikë**. Qëllimi pedagogjik është kalimi nga qasja eksploruese në **Jupyter notebook** te një strukturë më e rregullt, e afërt me praktikën e kërkimit shkencor dhe të zhvillimit të kodeve të ripërdorshme.

Në këtë pjesë trajtohen disa nga konceptet më themelore të dinamikës jolineare dhe të kaosit determinist:

- ndjeshmëria ndaj kushteve fillestare,
- tranzicioni drejt kaosit përmes bifurkacioneve,
- harta logjistike si model diskret paradigmatik,
- eksponenti i Ljapunovit si tregues i divergjencës lokale të trajektoreve,
- sistemi i Lorencit si shembull klasik i një atraktori të çuditshëm.

## Struktura e projektit

```text
chaos_models/
│
├── models/
│   ├── logistic_map.py
│   ├── lorenz_system.py
│   └── lyapunov.py
│
├── visualization/
│   ├── bifurcation.py
│   └── phase_space.py
│
├── output/
│
├── main.py
├── requirements.txt
└── README.md
```

## Ideja themelore e organizimit

Struktura është ndërtuar sipas një parimi të thjeshtë dhe të dobishëm për studentët:

- **models/** përmban formulimin matematikor dhe algoritmet bazë numerike;
- **visualization/** përmban funksionet e vizualizimit;
- **main.py** shërben si pikë hyrjeje nga terminali, duke lejuar zgjedhjen e modelit përmes flag-ut `--model`;
- **output/** ruan figurat e gjeneruara.

Kjo ndarje i ndihmon studentët të kuptojnë se në praktikën shkencore modeli fizik, llogaritja numerike dhe vizualizimi nuk duhen përzier pa kriter në një skript të vetëm.

## Instalimi

Këshillohet përdorimi i një mjedisi virtual Python.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Përdorimi bazë

### 1. Orbita e hartës logjistike

```bash
python3 main.py --model logistic --r 3.7 --x0 0.2 --n_steps 150
```

Kjo komandë gjeneron evolucionin diskret të vargut \$x_n$ për një vlerë të caktuar të parametrit $r$.

### 2. Portreti diskret i fazës për hartën logjistike

```bash
python3 main.py --model logistic_phase --r 3.9 --x0 0.21 --n_steps 400
```

Kjo komandë vizaton $x_n$ kundrejt $x_{n+1}$, gjë që ndihmon në kuptimin gjeometrik të dinamikës diskrete.

### 3. Diagrami i bifurkacionit

```bash
python3 main.py --model bifurcation --r_min 2.5 --r_max 4.0 --n_r 1800 --discard 1200 --keep_last 200
```

Kjo është një nga analizat më të rëndësishme të Pjesës 4, pasi tregon kalimin nga pikë fikse te orbitat periodike dhe më tej te regjimet kaotike.

### 4. Eksponenti i Ljapunovit për një vlerë të vetme të $r$

```bash
python3 main.py --model lyapunov --r 3.95 --x0 0.2 --n_steps 5000 --discard 1000
```

Në dalje, programi raporton vlerën e $(\lambda)$ dhe jep një interpretim të shkurtër fizik.

### 5. Skanimi i eksponentit të Ljapunovit

```bash
python3 main.py --model lyapunov_scan --r_min 2.5 --r_max 4.0 --n_r 1000
```

Kjo komandë gjeneron figurën ku shihet se në cilat intervale të parametrit $r$ sistemi ka $\lambda > 0$, pra sjellje kaotike.

### 6. Atraktori i Lorencit

```bash
python3 main.py --model lorenz --t_max 40 --dt 0.01 --sigma 10 --rho 28 --beta 2.6666666667
```

Ky është shembulli klasik i kaosit në një sistem kontinual tridimensional.

### 7. Projeksioni $(x, y)$ i atraktorit të Lorencit

```bash
python3 main.py --model lorenz_xy --t_max 40 --dt 0.01
```

### 8. Ndjeshmëria ndaj kushteve fillestare në sistemin e Lorencit

```bash
python3 main.py --model lorenz_sensitivity --delta0 1e-8 --t_max 20 --dt 0.01
```

Kjo komandë vizaton rritjen e distancës mes dy trajektoreve që nisin shumë pranë njëra-tjetrës.

## Interpretim fizik i pjesëve kryesore

### Harta logjistike

Harta logjistike është modeli më i thjeshtë ku studentët mund të shohin se si një rregull determinist shumë elementar prodhon sjellje tepër të ndërlikuar. Pikërisht kjo e bën atë një pikë hyrjeje ideale në temën e kaosit.

### Diagrami i bifurkacionit

Diagrami i bifurkacionit nuk është thjesht një figurë estetike. Ai përmbledh strukturën globale të dinamikës së sistemit në varësi të parametrit të kontrollit. Pedagogjikisht, kjo figurë është shumë e rëndësishme sepse tregon se si ndryshimi i vogël i një parametri mund të transformojë cilësisht sjelljen e sistemit.

### Eksponenti i Ljapunovit

Eksponenti i Ljapunovit është treguesi më i drejtpërdrejtë sasior i ndjeshmërisë ndaj kushteve fillestare. Kur ai del pozitiv, perturbimet e vogla rriten mesatarisht në mënyrë eksponenciale, gjë që e bën parashikueshmërinë afatgjatë të kufizuar.

### Sistemi i Lorencit

Sistemi i Lorencit është i një rëndësie të veçantë sepse tregon se kaosi nuk është një veçori vetëm e sistemeve diskrete. Edhe në ekuacionet diferenciale ordinare, një model relativisht i thjeshtë mund të gjenerojë një atraktor të çuditshëm dhe humbje të parashikueshmërisë praktike.

## Zgjerime të mundshme për studentët

Ky production code mund të zgjerohet më tej në disa drejtime:

1. shtimi i **hartës së tendës** dhe krahasimi me hartën logjistike;
2. shtimi i **sistemit Rössler** si shembull tjetër i atraktorit kaotik;
3. llogaritja më e avancuar e eksponentit maksimal të Ljapunovit për sisteme kontinuale;
4. ndërtimi i **Poincaré sections** për sisteme të përshtatshme;
5. shtimi i animacioneve ose i ruajtjes së rezultateve në skedarë CSV.

## Koment pedagogjik

Qëllimi i këtij versioni production code nuk është të zëvendësojë notebook-un, por të plotësojë atë. Notebook-u është shumë i dobishëm për mësimdhënie, eksplorim dhe komentim interaktiv. Në anën tjetër, versioni production code u mëson studentëve:

- organizimin e kodit në module,
- ripërdorimin e funksioneve,
- kontrollin e parametrave nga terminali,
- ndarjen midis modelit fizik dhe vizualizimit,
- kalimin gradual drejt praktikave më profesionale të llogaritjes shkencore.

## Sugjerim për përdorim në mësim

Një rrjedhë shumë e mirë pedagogjike do të ishte kjo:

1. së pari të prezantohet ideja në notebook,
2. pastaj studentët të riprodhojnë figurat me `main.py`,
3. më pas të modifikojnë parametrat,
4. dhe në fund të shtojnë vetë një model të ri ose një vizualizim të ri.

Në këtë mënyrë, Pjesa 4 bëhet jo vetëm një hyrje teorike në kaos, por edhe një ushtrim shumë i mirë në **programim shkencor të strukturuar**.
