# H8XL

**Lichtgewicht projectplanning in je browser. Geen account, geen server, geen tracking.**
Gemaakt voor iedereen die zijn planning nu in Excel bijhoudt, en daar eigenlijk vanaf wil.

> *English summary below.*

## Wat het doet

- Plan door te slepen: activiteiten verschuiven, verlengen en aan elkaar koppelen. Wat ervan afhangt schuift automatisch mee.
- Rekent in werkdagen, met Nederlandse feestdagen (uit te zetten).
- Fases, activiteiten en subactiviteiten, met mijlpalen als deliverables: wat wordt er opgeleverd, wanneer is dat afgesproken, en past de planning daarbinnen.
- Exporteert naar Excel (met een gekleurde tijdlijn), PDF en PNG. Het Excel-bestand is ook je opslag: je opent het later gewoon weer.
- Leest bestaande planningen in door ze vanuit Excel te plakken of een .xlsx/.csv te openen.
- Nederlands en Engels, licht en donker thema.

## Gebruiken

Open `index.html` in een moderne browser (Chrome, Edge, Firefox of Safari), of gebruik de gehoste versie op `[JOUW-DOMEIN]`.
Er is niets te installeren.

## Privacy, in het kort

Je planning verlaat je computer niet. H8XL heeft geen server en geen database: alles staat in je browser en in de bestanden die je zelf exporteert.
Dat is geen belofte maar een technische afspraak met je browser: de pagina bevat een Content Security Policy met `connect-src 'none'`, waardoor de browser elke poging om data te versturen blokkeert.

- Wat er precies wel en niet gebeurt: [PRIVACY.md](PRIVACY.md)
- Hoe je dat zelf controleert, zonder ons te hoeven geloven: [SECURITY.md](SECURITY.md)

## Technisch

- Eén bestand (`index.html`), geen build-stap, geen afhankelijkheden. Wat in deze repository staat, is letterlijk wat je browser uitvoert.
- Eigen Excel-schrijver en -lezer (xlsx is een zip met XML) en een eigen PDF-schrijver. Alleen voor bestanden die de eigen lezer niet aankan, zoals oude .xls-bestanden, wordt [SheetJS](https://sheetjs.com) geladen. Dat haalt alleen code op en verstuurt niets.
- Ongeveer 25 kB JavaScript (gecomprimeerd).

## Feedback en bijdragen

Ideeën, bugs en vragen zijn welkom via de Feedback-knop in de app of via [Issues](../../issues).
Wil je zelf iets bouwen? Lees eerst [CONTRIBUTING.md](CONTRIBUTING.md).

## Licentie

[EUPL-1.2](https://spdx.org/licenses/EUPL-1.2.html). Je mag H8XL gebruiken, aanpassen en verspreiden. Aangepaste versies die je verspreidt of aanbiedt, moeten onder dezelfde licentie open blijven.

---

## English summary

H8XL is a lightweight, browser-based project planner for people stuck in Excel. Drag to plan, link activities so dependent work shifts automatically, plan in workdays with Dutch public holidays, track deliverables against agreed dates, and export to Excel, PDF or PNG.

There is no account, server or tracking. Your plan stays in your browser and in files you export yourself. A Content Security Policy with `connect-src 'none'` makes the browser block any attempt to send data. See [PRIVACY.md](PRIVACY.md) and how to verify this yourself in [SECURITY.md](SECURITY.md).

Single file, no build step, no dependencies. Licensed under EUPL-1.2.
