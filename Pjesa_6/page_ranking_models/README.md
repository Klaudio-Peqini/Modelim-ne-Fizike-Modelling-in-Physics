# page_ranking_models

Ky repo përmban versionin **production code** në Python për temën:

**Algoritme të renditjes së faqeve në web**

Materiali është menduar si vazhdim praktik i notebook-ut `06_algoritme_renditjeje.ipynb` dhe i materialit teorik në LaTeX. Qëllimi është që studenti të kalojë nga shpjegimi konceptual te një implementim i strukturuar, i ripërdorshëm dhe i zgjerueshëm.

---

## Ideja kryesore

Në këtë repo, renditja e faqeve nuk trajtohet thjesht si një listë që duhet radhitur, por si një problem shumë më realist i **vlerësimit të rëndësisë së dokumenteve në web**.

Modeli i përdorur këtu është **hibrid**:

- një komponent strukturor nga **PageRank**
- një komponent i **relevancës tekstuale** ndaj pyetjes
- një komponent i **freskisë** së faqes
- një komponent i **cilësisë**
- një komponent i **sinjaleve të përdoruesit**
- dhe një **penalizim për spam-in**

Pra, rezultati final nuk vjen nga një burim i vetëm, por nga kombinimi i disa treguesve.

---

## Struktura e projektit

```text
page_ranking_models/

├── ranking/
│   ├── __init__.py
│   ├── graph_utils.py
│   ├── pagerank.py
│   ├── features.py
│   └── ranking_engine.py
│
├── visualization/
│   ├── plot_scores.py
│   └── graph_plot.py
│
├── examples/
│   └── sample_pages.json
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Përshkrimi i moduleve

### `ranking/graph_utils.py`

Ky modul ndërton matricën e tranzicionit për graf-in e faqeve.

- Çdo faqe përfaqësohet si nyje.
- Çdo hyperlink përfaqësohet si lidhje e drejtuar.
- Nyjet pa dalje trajtohen si **dangling nodes** dhe zëvendësohen me shpërndarje uniforme.

Ky është hapi bazë për ta kthyer problemin e web-it në një problem matematikor të përpunueshëm.

### `ranking/pagerank.py`

Ky modul implementon:

- **PageRank klasik**
- **Personalized PageRank**

Llogaritja bëhet me **metodën e iterimit të fuqisë**, që është mënyra standarde numerike për këtë lloj problemi.

### `ranking/features.py`

Ky modul llogarit disa veçori shtesë:

- relevancën tekstuale të pyetjes ndaj dokumentit
- freskinë në varësi të datës së përditësimit
- normalizimin e veçorive në intervalin `[0,1]`

Ky modul përfaqëson hapin që e bën modelin më realist sesa PageRank-u i pastër.

### `ranking/ranking_engine.py`

Ky është moduli kryesor i renditjes.

Ai kombinon të gjithë komponentët me një formulë të tipit:

```text
score final =
    w_pagerank * PageRank
  + w_relevance * Relevance
  + w_freshness * Freshness
  + w_quality   * Quality
  + w_user      * UserSignal
  - w_spam      * Spam
```

Peshat mund të ndryshohen sipas qëllimit të eksperimentit.

### `visualization/plot_scores.py`

Krijon grafik kolonash për rezultatin final të faqeve.

### `visualization/graph_plot.py`

Vizaton vetë graf-in e faqeve dhe lidhjeve me `networkx`.

### `examples/sample_pages.json`

Një dataset i vogël demonstrativ me:

- tituj
- përmbajtje
- etiketa
- lidhje mes faqeve
- datë përditësimi
- score cilësie
- sinjal përdoruesi
- score spam-i

Ky skedar mund të zëvendësohet me shembuj të tjerë nga studentët.

---

## Instalimi

Krijo mjedisin virtual nëse dëshiron:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Nëse nuk përdor mjedis virtual, mjafton të kesh të instaluara varësitë.

---

## Ekzekutimi bazë

Nga dosja kryesore e projektit:

```bash
python3 main.py
```

Kjo do të përdorë automatikisht:

- dataset-in `examples/sample_pages.json`
- pyetjen `fizike algoritme`
- vlerën `alpha = 0.85`

---

## Shembuj përdorimi

### 1. Ekzekutim i thjeshtë

```bash
python3 main.py
```

### 2. Me pyetje të personalizuar

```bash
python3 main.py --query "pagerank web algoritme"
```

### 3. Me personalized PageRank sipas një teme

```bash
python3 main.py --query "fizike modelim" --topic "fizike"
```

### 4. Me një vlerë tjetër të faktorit të amortizimit

```bash
python3 main.py --alpha 0.90
```

### 5. Me grafikë

```bash
python3 main.py --plot
```

Kjo krijon:

- `ranking_scores.png`
- `web_graph.png`

---

## Çfarë e bën këtë model më realist?

Në shumë ushtrime pedagogjike, PageRank paraqitet në formën e tij më të thjeshtë, gjë që është shumë e vlefshme për të kuptuar idenë bazë. Megjithatë, një motor kërkimi real nuk vendos renditjen vetëm nga struktura e lidhjeve.

Ky implementim përpiqet ta zgjerojë modelin në disa drejtime:

### 1. Relevanca tekstuale

Një faqe shumë autoritative nuk është domosdoshmërisht përgjigjja më e mirë për pyetjen aktuale. Për këtë arsye, pyetja e përdoruesit krahasohet me:

- titullin
- përmbajtjen
- etiketat

### 2. Freskia

Në shumë raste, dokumentet më të reja janë më të dobishme. Për këtë arsye, përdoret një faktor eksponencial që bie me kalimin e kohës.

### 3. Cilësia

Faqet me përmbajtje më serioze, më të plota ose më të besueshme mund të marrin një bonus.

### 4. Sinjalet e përdoruesit

Në një model të thjeshtuar, mund të përfshihet një tregues që lidhet me angazhimin e përdoruesve.

### 5. Penalizimi i spam-it

Faqet që duken të manipuluara ose me cilësi të ulët nuk duhet të favorizohen vetëm sepse kanë lidhje.

---

## Formula e përgjithshme

Në këtë repo përdoret logjika:

```text
S_i = wP * P_i + wR * R_i + wF * F_i + wQ * Q_i + wU * U_i - wS * Sp_i
```

ku:

- `P_i` = PageRank
- `R_i` = relevanca tekstuale
- `F_i` = freskia
- `Q_i` = cilësia
- `U_i` = sinjal përdoruesi
- `Sp_i` = spam score

Të gjitha veçoritë normalizohen para kombinimit.

---

## Sugjerime për zgjerim

Studentët mund ta zgjerojnë projektin në disa mënyra:

1. Të implementojnë **Weighted PageRank**
2. Të shtojnë një model më të mirë relevance, si p.sh. **TF-IDF** ose **BM25**
3. Të përdorin të dhëna reale nga një mini-koleksion faqesh
4. Të ndryshojnë peshat e modelit dhe të studiojnë ndjeshmërinë e renditjes
5. Të ndërtojnë një version me **mësim makinerik**, ku peshat mësohen nga të dhënat
6. Të shtojnë filtra për gjuhë, temë ose domen
7. Të krijojnë një ndërfaqe të vogël web për testim interaktiv

---

## Vlera pedagogjike

Ky projekt është shumë i përshtatshëm për studentët, sepse lidh disa fusha të rëndësishme:

- teori e grafeve
- algjebër lineare
- probabilitet
- modelim numerik
- përpunim teksti
- analiza e sistemeve reale

Pra, ai shërben si shembull shumë i mirë se si një ide matematikore e pastër mund të zgjerohet në drejtim të një sistemi më realist dhe më afër aplikimeve reale.

---

## Rezultati i pritur

Pas ekzekutimit, studenti merr:

- një listë të renditur faqesh
- score final për secilën faqe
- komponentët kryesorë që ndikuan në renditje
- grafikë ndihmës për interpretim

Kjo i lejon studentit të kuptojë jo vetëm **çfarë** renditje doli, por edhe **pse** doli ajo renditje.

---

## Komandat kryesore

```bash
python3 main.py
python3 main.py --query "fizike algoritme"
python3 main.py --query "pagerank web" --topic "web"
python3 main.py --alpha 0.9 --plot
```

---

## Përfundim

Ky production code është menduar si bazë e fortë për laborator, diskutim në klasë dhe zgjerime të mëtejshme. Ai nuk synon të riprodhojë plotësisht një motor kërkimi industrial, por të japë një version të qartë, të organizuar dhe mjaftueshëm realist për të treguar se si ndërtohet një algoritëm modern renditjeje.

