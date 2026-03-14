# Pjesa_2 – Kalimi nga notebook-u pedagogjik te paketa Python

Ky material përmban **dy paketa Python** të organizuara në mënyrë të thjeshtë, por të pastër, me qëllim që studentët të kuptojnë kalimin:

**notebook demonstrativ → strukturë dosjesh → module Python → ekzekutim nga terminali**

Paketat janë:

1. `biele_manivele_pkg/` – model i mekanizmit **bielë-manivelë**
2. `lavjerresi_dyfishte_pkg/` – model i **lavjerrësit të dyfishtë**

## Ideja pedagogjike

Në notebook, kodi shkruhet zakonisht në mënyrë lineare:
- përkufizohen parametrat,
- nxirren ekuacionet,
- kryhet zgjidhja numerike,
- bëhen grafiqet.

Në një paketë Python, e njëjta punë ndahet në pjesë më të qarta:

- `symbolic_model.py` – derivimi simbolik me `sympy`
- `simulation.py` – modeli numerik dhe integrimi
- `plotting.py` – grafiqet
- `animation.py` – animacionet
- `cli.py` – ndërfaqe e thjeshtë nga terminali

Kjo është një strukturë e vogël, por me frymë **profesionale**, e përshtatshme për mësim.

## Si t'i përdorni

Hyni në secilën paketë dhe ndiqni udhëzimet në `README.md` përkatëse.

## Sugjerim për studentët

Studentët mund të fillojnë duke lexuar:
1. `parameters.py`
2. `simulation.py`
3. `plotting.py`

dhe vetëm më pas të kalojnë te:
- `symbolic_model.py`
- `animation.py`
- `cli.py`

Në këtë mënyrë, ngarkesa konceptuale mbetet e moderuar.
