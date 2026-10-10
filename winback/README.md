# TIK BALDAI winback laiškai

Trys atskiri HTML dizaino maketai esamiems baldų pirkėjams. Versija 2, 2026 m. spalio 10 d.

| Laiškas | Paskirtis | Siūlomas laikas |
|---|---|---|
| [1](email-01.html) | Sugrįžti su nauju poreikiu namams, pasirinkti kategoriją | 180 dieną nuo paskutinio užsakymo |
| [2](email-02.html) | Sugrįžimo pasiūlymas ir kategorijų atranka | 187 dieną, jei nepirko |
| [3](email-03.html) | Pasitarti dėl dominančio baldo ir užbaigti pasirinkimą | 194 dieną, jei nepirko ir paspaudė laiške ar patikimai užfiksuotas apsilankymas |

## Turinys

Naujose kampanijos kompozicijose naudojamos tikrų katalogo produktų referencijos. Aplinka, šviesa ir Winback 2 sofa ant sidabrinio padėklo sukurta su AI. Tai nėra nepakitusios gamintojo nuotraukos. Kategorijos turi vientisą šiltą akmens foną. Pirmasis laiškas yra bendras variantas, kai nežinoma aktuali gavėjo kategorija. Dinaminis pasirinkimas pagal ankstesnį pirkimą ar paspaudimą dar neprijungtas. Generatorius pirkusiems kontaktams, kurių baldų interesas nežinomas, ši serija neskirta.

Kliento kodas `assugrizau` rodomas antrame ir trečiame laiškuose. Skaitinė nuolaida neįrašyta, kol nepatikslinta, ar turimi omenyje 5 procentai, ar 5 eurai. Kodo veikimas, sąlygos ir galiojimas parduotuvėje netestuoti. Fiktyvaus termino ar didėjančios nuolaidos nėra.

## Siuntimo taisyklės

Reikalingas įvykdytas, neatšauktas ir ne visiškai grąžintas ankstesnis užsakymas bei galiojantis rinkodaros statusas. Prieš kiekvieną laišką tikrinti naują užsakymą, prenumeratos atsisakymą, blokavimą ir žinomą neišspręstą aptarnavimo problemą. Naujas užsakymas arba aktyvuota checkout priminimų serija nutraukia likusį winback ciklą. Tarp rinkodaros laiškų bent 48 valandos. Nepirkęs gavėjas po šios serijos į ją automatiškai negrąžinamas. Laikai yra pradinė hipotezė, koreguotina pagal pardavimų duomenis.

## Patikra ir integracija

Kiekvienam dabartiniam HTML išsaugomos aštuonios peržiūros: 600 px desktop ir 320, 390, 430 px mobile, įprastai ir pašalinus head stilius bei fontų nuorodas. `qa-summary.json` ir `qa/visual-*.json` susieja automatinius ir vizualinius rezultatus su HTML bei screenshot SHA256. Peržiūros sukurtos naršyklėje, ne Gmail ar Outlook kliente.

Vaizdai naudoja viešus HTTPS adresus, susietus su konkrečiu Git commit. Šaltinių atitikmenys yra `assets.json`. Prieš realų siuntimą reikia patvirtinti pasiūlymą, pakeisti `{{unsubscribe_url}}` platformos atsisakymo žymeniu, sujungti siuntimo bei segmentavimo taisykles ir atlikti testinį platformos siuntimą. Automatizacija neaktyvuota ir jokie laiškai neišsiųsti.

`email-*.json` saugo temas ir preheaderius, `email-*-copy.txt` tekstus. `build.py` atkuria HTML. Pakeitus jį, dabartinė QA nebegalioja.
