# Privacy

Deze pagina beschrijft precies welke gegevens H8XL gebruikt en waar die blijven. Als er iets verandert, verandert deze pagina mee, en is de wijziging terug te zien in de geschiedenis van deze repository.

## Je planning

- **Waar staat je planning?** In de lokale opslag (`localStorage`) van je eigen browser, op je eigen computer. En in de bestanden die je zelf exporteert (Excel, PDF, PNG).
- **Wie kan erbij?** Alleen jij, op dat apparaat, in die browser. H8XL heeft geen server, geen database en geen accounts.
- **Wordt je planning ergens heen gestuurd?** Nee. De pagina bevat een Content Security Policy met `connect-src 'none'`. Daarmee weigert de browser zelf elk verzoek waarmee data verstuurd zou kunnen worden (fetch, XMLHttpRequest, beacons, websockets). Ook afbeeldingen van externe adressen worden geblokkeerd, zodat data niet via een omweg weg kan.
- **Let op:** lokale browseropslag kan door jou, je browser of je organisatie worden gewist. Sla belangrijke planningen daarom op als Excel-bestand.

## Wat er wél over het netwerk gaat

Eerlijkheid gaat voor een mooie claim. Dit zijn alle verzoeken die H8XL kan doen, en geen enkel verzoek bevat je planning:

| Verzoek | Wanneer | Wat de ander ziet |
|---|---|---|
| Het laden van de pagina zelf | Bij openen van de gehoste versie | Je IP-adres en browser, zoals bij elke website. Dit ziet de hostingpartij, Cloudflare. H8XL zet bij Cloudflare geen analytics of extra scripts aan. Gebruik je een lokale kopie van `index.html`, dan gebeurt dit niet. |
| Lettertype (Google Fonts) | Bij openen | Je IP-adres en browser. *Gepland: het lettertype wordt in een volgende versie meegeleverd, zodat dit verzoek verdwijnt.* |
| SheetJS (cdnjs.cloudflare.com) | Alleen als je een Excel-bestand opent dat de eigen lezer niet aankan, zoals een oud .xls-bestand | Je IP-adres en browser. Er wordt alleen code opgehaald; je bestand blijft in je browser. |

## Feedback

De Feedback-knop opent je eigen mailprogramma met een kant-en-klaar bericht, of een pagina op GitHub. H8XL verstuurt zelf niets. Je planning wordt nooit meegestuurd; alleen als je dat aanvinkt, gaan je browserversie en de versie van H8XL mee in de tekst, zodat je die vóór het versturen kunt lezen.

## Geen tracking

Geen cookies, geen analytics, geen advertenties, geen fingerprinting.
