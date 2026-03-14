# biele_manivele_pkg

Paketë e thjeshtë Python për modelimin e mekanizmit **bielë-manivelë**.

Qëllimi i saj është ilustrativ: studenti të shohë si organizohet një projekt i vogël Python kur kalojmë nga notebook-u te një strukturë më e rregullt.

## Struktura

```text
biele_manivele_pkg/
├── README.md
├── pyproject.toml
├── requirements.txt
├── scripts/
│   └── run_demo.py
└── src/
    └── biele_manivele_pkg/
        ├── __init__.py
        ├── parameters.py
        ├── symbolic_model.py
        ├── simulation.py
        ├── plotting.py
        ├── animation.py
        └── cli.py
```

## Çfarë bën paketa?

- llogarit pozicionin, shpejtësinë dhe përshpejtimin e pistonit;
- përdor `sympy` për formulat simbolike;
- përdor `numpy` për llogaritje numerike;
- përdor `matplotlib` për grafikë dhe animacion.

## Instalimi

Nga kjo dosje, ekzekutoni:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Ekzekutimi i një demonstrimi të thjeshtë

```bash
python scripts/run_demo.py
```

Ky komandim:
- gjeneron një simulim të thjeshtë,
- shfaq grafikët kryesorë,
- dhe krijon animacionin në dritaren e `matplotlib`.

## Përdorimi nga terminali me CLI

### Grafikët

```bash
python -m biele_manivele_pkg.cli plot --r 0.05 --l 0.18 --omega 12.0 --duration 2.0
```

### Animacioni

```bash
python -m biele_manivele_pkg.cli animate --r 0.05 --l 0.18 --omega 12.0 --duration 2.0
```

### Shfaqja e formulave simbolike

```bash
python -m biele_manivele_pkg.cli symbolic
```

## Vërejtje pedagogjike

Në këtë paketë, nuk kemi ndërtuar një model dinamik me çift rrotullues dhe masë të shpërndarë në mënyrë të plotë. Këtu fokusi është te:

- **kinematika e mekanizmit**,
- organizimi i kodit,
- dhe ndarja e funksioneve sipas rolit të tyre.

Pra, kjo paketë është e përshtatshme për hyrje në programim shkencor.
