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

Winback 2 perdarytas pagal pateiktą reference: šviesus fonas, Universe sofa ant sidabrinio padėklo, gyva serifinė antraštė ir sugrįžimo kodo blokas. Kategorijų vaizdai welcome 1, welcome 2 ir winback serijoje pakeisti į vientisas šilto akmens aplinkos kompozicijas.

Hero ir atnaujinti kategorijų vaizdai sukurti su AI, naudojant tikrus katalogo produktų vaizdus kaip referencijas. Jie nėra nepakitusios gamintojo nuotraukos. [Vaizdų kilmė ir detalės](visual-refresh-v2/README.md).

## Vieši vaizdai

HTML naudoja absoliučius HTTPS adresus raw.githubusercontent.com domene, susietus su konkrečiu Git commit. Prisijungimo nereikia. [Naujausių vaizdų HTTP ir hash patikra](visual-refresh-v2/public-assets-check.json). Kopijuojant HTML būtina išlaikyti pilnus img src adresus. GitHub blob puslapio adresas nėra vaizdo adresas.

## Patikra

Visi penki šioje redakcijoje keisti laiškai tikrinti 600 px kompiuterio ir 320, 390, 430 px mobiliais pločiais, įprastai ir pašalinus head stilius bei fontų nuorodas. Kiekvienam išsaugotos ir vizualiai peržiūrėtos aštuonios naujos peržiūros. HTML, vaizdų bei screenshot hash susieti su ataskaitomis. Welcome 3 šioje redakcijoje nekeistas, išlaikyta jo ankstesnė patikra.

[Welcome versijų indeksas](publication.json), [Winback patikra](winback/qa-summary.json). Interaktyvios [welcome](responsive-preview.html) ir [winback](winback-preview.html) peržiūros veikia atsisiuntus repo ir paleidus vietinį HTTP serverį. GitHub rodo HTML šaltinį, o JPG nuorodos leidžia iš karto apžiūrėti laiškus.

## Prieš siuntimą

Tai peržiūrėti dizaino maketai. SVEIKI10 yra darbinis kodas. assugrizau yra kliento pateiktas kodas, skaitinė nuolaida neįrašyta, kol nepatikslinta, ar ji procentais, ar eurais. Kodų veikimas ir sąlygos parduotuvėje netestuoti. {{unsubscribe_url}} reikia pakeisti platformos atsisakymo žymeniu. Naršyklės QA nėra patvirtintas Gmail, Outlook ar Omnisend pristatymas. Prieš paleidimą reikalingas platformos testinis siuntimas. Automatizacijos neaktyvuotos, laiškai neišsiųsti.

[Winback siuntimo logika ir failai](winback/README.md).
