# TIK BALDAI welcome laiškai

Vieši trijų laiškų HTML maketai, jų vaizdai ir dabartinės versijos patikros įrodymai.

| Laiškas | Paskirtis | HTML | Kompiuterio peržiūra | Telefono peržiūra |
|---|---|---|---|---|
| Welcome 1 | Susipažinti su TIK BALDAI ir gauti pirmo užsakymo dovaną | [HTML](welcome-01/email.html) | [600 px](welcome-01/responsive-previews/w600.jpg) | [390 px](welcome-01/responsive-previews/w390.jpg) |
| Welcome 2 | Atrasti asortimentą skirtingoms namų erdvėms | [HTML](welcome-02/email.html) | [600 px](welcome-02/responsive-previews/w600.jpg) | [390 px](welcome-02/responsive-previews/w390.jpg) |
| Welcome 3 | Pasitikslinti praktines detales ir apsispręsti prieš užsakant | [HTML](welcome-03/email.html) | [600 px](welcome-03/responsive-previews/w600.jpg) | [390 px](welcome-03/responsive-previews/w390.jpg) |

## Vaizdai laiškuose

Visų laiškų `img src` yra absoliutūs vieši HTTPS adresai `raw.githubusercontent.com` domene. Nuorodos susietos su konkrečiu Git commit, o failų pavadinimai turi turinio hash. GitHub prisijungimo joms nereikia. [Vaizdų patikra](public-assets-check.json) patvirtina HTTP 200, vaizdo tipą ir tikslius failų hash.

Į siuntimo platformą kopijuojant HTML reikia išlaikyti pilnus vaizdų adresus. GitHub failo peržiūros adresas su `/blob/` nėra vaizdo adresas. Kuriant būsimą kampanijos versiją, pridėti naujus vaizdus ir naudoti naujas nuorodas, išsaugant ankstesnę istoriją.

Hero vaizdai yra generuotos studijos ir interjero kompozicijos, parengtos naudojant katalogo produktų referencijas. Kategorijų nuotraukos yra pardavėjo vaizdai.

## Patikra

Kiekvienam HTML patikrinta 15 pločių nuo 320 iki 1440 px, įprastai ir pašalinus head stilius bei fontų nuorodas. Tai 30 naujų renderių vienam laiškui. Vizualiai peržiūrėta po 12 variantų, įskaitant 320, 390, 430 px ir 600 px laišką kompiuterio lange abiem stilių režimais. Ataskaitos susietos su dabartinio HTML ir vaizdų hash.

[Versijų ir patikros indeksas](publication.json). [Interaktyvios peržiūros HTML](responsive-preview.html) veikia atidarius atsisiųstą repo per vietinį HTTP serverį. GitHub failų puslapiai rodo šaltinį, o JPG nuorodos leidžia peržiūrėti laiškus tiesiogiai.

## Prieš siuntimą

Tai dizaino maketai. `SVEIKI10` yra darbinis kodas, jo veikimas ir sąlygos parduotuvėje nepatvirtinti. `{{unsubscribe_url}}` būtina pakeisti konkrečios siuntimo platformos atsisakymo žymeniu. Reikia testinio siuntimo iš naudojamos platformos į Gmail, Outlook ir mobiliuosius klientus. Naršyklės patikra nėra tikro pristatymo patvirtinimas. Automatizacijos neaktyvuotos.
