# lavjerresi_dyfishte_pkg

Paketë e thjeshtë Python për modelimin e **lavjerrësit të dyfishtë**.

Kjo paketë ruan një strukturë të vogël, por të rregullt, që studenti të shohë si ndahet kodi sipas roleve:

- parametra,
- model simbolik,
- simulim numerik,
- grafikë,
- animacion,
- ekzekutim nga terminali.

## Struktura

```text
lavjerresi_dyfishte_pkg/
├── README.md
├── pyproject.toml
├── requirements.txt
├── scripts/
│   └── run_demo.py
└── src/
    └── lavjerresi_dyfishte_pkg/
        ├── __init__.py
        ├── parameters.py
        ├── symbolic_model.py
        ├── simulation.py
        ├── plotting.py
        ├── animation.py
        └── cli.py
```

## Çfarë bën paketa?

- zgjidh numerikisht ekuacionet e lavjerrësit të dyfishtë;
- vizaton këndet dhe shpejtësitë këndore në funksion të kohës;
- jep një animacion të lëvizjes;
- shfaq edhe formulimin simbolik bazë me `sympy`.

## Instalimi

Nga kjo dosje, ekzekutoni:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Ekzekutimi i demonstrimit

```bash
python scripts/run_demo.py
```

## Përdorimi me CLI

### Grafikët

```bash
python -m lavjerresi_dyfishte_pkg.cli plot --theta1 0.6 --theta2 0.2 --duration 10.0
```

### Animacioni

```bash
python -m lavjerresi_dyfishte_pkg.cli animate --theta1 0.6 --theta2 0.2 --duration 10.0
```

### Shfaqja e përshkrimit simbolik

```bash
python -m lavjerresi_dyfishte_pkg.cli symbolic
```

## Vërejtje pedagogjike

Këtu lavjerrësi i dyfishtë përdoret si shembull i një sistemi jo-linear me dy shkallë lirie. Në këtë version:

- fokusi është te programimi dhe struktura,
- jo te analiza e plotë teorike,
- dhe nuk diskutohet ende natyra kaotike e sistemit.
