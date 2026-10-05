# Bijdragen aan H8XL

Fijn dat je wilt helpen. H8XL heeft een paar harde uitgangspunten; een wijziging die daartegen ingaat, wordt niet opgenomen, hoe handig ook.

## Uitgangspunten

1. **Geen netwerkverkeer met gebruikersdata.** De Content Security Policy blijft `connect-src 'none'`. Geen analytics, geen externe API's, geen formulierdiensten.
2. **Eén bestand, geen bouwstap.** Wat in `index.html` staat, is wat de browser draait. Dat maakt de privacyclaim controleerbaar.
3. **Geen afhankelijkheden** zonder voorafgaand overleg in een issue. Elke kilobyte telt.
4. **Excel blijft de uitwisseling.** Wat je exporteert, moet weer in te lezen zijn zonder verlies.

## Werkwijze

1. Open eerst een issue en beschrijf wat je wilt veranderen.
2. Pas `index.html` aan.
3. Werk de beveiligingshash bij, anders weigert de browser het script:
   ```sh
   python3 tools/update-csp.py
   ```
4. Test minimaal: een planning maken, slepen en koppelen, exporteren naar Excel en dat bestand weer openen. De planning moet identiek terugkomen.
5. Open een pull request.

## Configuratie

Bovenaan het script staat een `H8XL`-object met het contactadres en de repository-link. Pas die aan als je je eigen versie host.
