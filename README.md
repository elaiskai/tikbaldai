# TIK BALDAI laiškai

Vieši welcome ir winback HTML maketai, vaizdai ir dabartinių versijų patikros įrodymai.

| Laiškas | HTML | Kompiuterio peržiūra | Telefono peržiūra |
|---|---|---|---|
| Welcome 1 | [HTML](welcome-01/email.html) | [600 px](welcome-01/responsive-previews/w600.jpg) | [390 px](welcome-01/responsive-previews/w390.jpg) |
| Welcome 2 | [HTML](welcome-02/email.html) | [600 px](welcome-02/responsive-previews/w600.jpg) | [390 px](welcome-02/responsive-previews/w390.jpg) |
| Welcome 3 | [HTML](welcome-03/email.html) | [600 px](welcome-03/responsive-previews/w600.jpg) | [390 px](welcome-03/responsive-previews/w390.jpg) |
| Winback 1 | [HTML](winback/email-01.html) | [600 px](winback/qa/e01-w600.jpg) | [390 px](winback/qa/e01-w390.jpg) |
| Winback 2 | [HTML](winback/email-02.html) | [600 px](winback/qa/e02-w600.jpg) | [390 px](winback/qa/e02-w390.jpg) |
| Winback 3 | [HTML](winback/email-03.html) | [600 px](winback/qa/e03-w600.jpg) | [390 px](winback/qa/e03-w390.jpg) |

## Naujausia versija

Winback 2 tarpas tarp antraštės ir sofos sumažintas maždaug perpus, sutrumpinus hero tuščią viršų. Nauji aštuoni šio laiško vaizdai ir tikslus HTML hash: [tarpo patikra](winback-spacing/qa-summary.json). Ankstesnė CTA redakcijos patikra Winback 2 atveju yra istorinė.

Visuose šešiuose laiškuose sustiprinti prekių pasirinkimo ir pirkimo kvietimai. Mygtukai aiškiai įvardija kategorijas ir veda tiesiai į prekių sąrašus. Konsultacija yra papildoma nuoroda. Winback 3 siūlo sofas lovas, fotelius ir kavos staliukus bei primena sugrįžimo kodą.

Winback 3 hero yra naujas redakcinis koliažas su tikbaldai.lt oranžinės sofos ir balto apvalaus kavos staliuko referencijomis. Kiti elementai yra dekoratyvinis rekvizitas. [Hero kilmė](winback/hero-v3/provenance.json). Kitų laiškų vaizdai šioje redakcijoje išlaikyti. Kampanijos kompozicijos kurtos su AI pagal katalogo referencijas, jos nėra nepakitusios gamintojo nuotraukos.

## Vieši vaizdai

HTML naudoja absoliučius HTTPS adresus raw.githubusercontent.com domene, susietus su konkrečiu Git commit. Prisijungimo nereikia. [Naujausių vaizdų HTTP ir hash patikra](visual-refresh-v2/public-assets-check.json). Kopijuojant HTML būtina išlaikyti pilnus img src adresus. GitHub blob puslapio adresas nėra vaizdo adresas.

## Patikra

Visi šeši dabartiniai HTML tikrinti 600 px kompiuterio ir 320, 390, 430 px mobiliais CSS pločiais, įprastai ir pašalinus head stilius bei fontų nuorodas. Išsaugotos ir vizualiai peržiūrėtos 48 naujos peržiūros. Fiksuoto pločio iframe užtikrina tikslų laiško CSS plotį; iš pilnų naršyklės nuotraukų iškirptas tik peržiūros rėmelis. HTML ir nuotraukų hash susieti [dabartinėje QA ataskaitoje](cta-refresh/qa-summary.json). Ankstesnis visual-refresh-v2 katalogas yra istorinė vaizdų atnaujinimo patikra.

[Welcome versijų indeksas](publication.json), [Winback patikra](winback/qa-summary.json). Interaktyvios [welcome](responsive-preview.html) ir [winback](winback-preview.html) peržiūros veikia atsisiuntus repo ir paleidus vietinį HTTP serverį. GitHub rodo HTML šaltinį, o JPG nuorodos leidžia iš karto apžiūrėti laiškus.

## Prieš siuntimą

Tai peržiūrėti dizaino maketai. SVEIKI10 yra darbinis kodas. assugrizau yra kliento pateiktas kodas, skaitinė nuolaida neįrašyta, kol nepatikslinta, ar ji procentais, ar eurais. Kodų veikimas ir sąlygos parduotuvėje netestuoti. {{unsubscribe_url}} reikia pakeisti platformos atsisakymo žymeniu. Naršyklės QA nėra patvirtintas Gmail, Outlook ar Omnisend pristatymas. Prieš paleidimą reikalingas platformos testinis siuntimas. Automatizacijos neaktyvuotos, laiškai neišsiųsti.

[Winback siuntimo logika ir failai](winback/README.md).

## Krepšelio ir checkout serijos

Parengti trys abandoned cart ir du abandoned checkout dizaino maketai su atskirais Omnisend Custom HTML fragmentais. [Planas ir surinkimas](recovery/README.md), [interaktyvi peržiūra](recovery-preview.html), [40 dabartinių naršyklės peržiūrų patikra](recovery/qa-summary.json). Tai surinkimo juodraščiai: native dinaminės prekės dar neprijungtos, automatizacijos neaktyvuotos. Pilkos produktų vietos nėra siuntimui.

| Laiškas | Kompiuteris | Telefonas | Fragmentai |
|---|---|---|---|
| cart-01 | [600 px](recovery/qa/cart-01-w600-crop.jpg) | [390 px](recovery/qa/cart-01-w390-crop.jpg) | [Omnisend](recovery/cart-01/omnisend) |
| cart-02 | [600 px](recovery/qa/cart-02-w600-crop.jpg) | [390 px](recovery/qa/cart-02-w390-crop.jpg) | [Omnisend](recovery/cart-02/omnisend) |
| cart-03 | [600 px](recovery/qa/cart-03-w600-crop.jpg) | [390 px](recovery/qa/cart-03-w390-crop.jpg) | [Omnisend](recovery/cart-03/omnisend) |
| checkout-01 | [600 px](recovery/qa/checkout-01-w600-crop.jpg) | [390 px](recovery/qa/checkout-01-w390-crop.jpg) | [Omnisend](recovery/checkout-01/omnisend) |
| checkout-02 | [600 px](recovery/qa/checkout-02-w600-crop.jpg) | [390 px](recovery/qa/checkout-02-w390-crop.jpg) | [Omnisend](recovery/checkout-02/omnisend) |

## Peržiūrėta prekė

Du Product Abandonment laiškai: trumpas priminimas ir pagalba įvertinti tinkamumą. [Planas ir Omnisend surinkimas](product-abandonment/README.md), [peržiūra](product-abandonment-preview.html), [16 dabartinių peržiūrų QA](product-abandonment/qa-summary.json). Native produktai dar neprijungti, maketų placeholderių nesiųsti.
