# TIK BALDAI: paliktas krepšelis ir neužbaigtas atsiskaitymas

Penki dizaino surinkimo maketai Omnisend. Tai dvi atskiros serijos. Dinaminiai produktai dar neprijungti, automatizacijos neaktyvuotos, laiškai neišsiųsti.

| Laiškas | Laikas nuo neveiklumo pradžios | Paskirtis | Pagrindinis native mygtukas |
|---|---|---|---|
| Cart 1 | 1 val. | Trumpas priminimas apie krepšelyje likusias prekes | Grįžti į krepšelį |
| Cart 2 | 24 val. | Aptarnavimo argumentai, tikras atsiliepimas, pristatymo paaiškinimas | Grįžti į krepšelį |
| Cart 3 | 48 val. | DUK apie tinkamumą, pristatymą ir atsiskaitymą | Grįžti į krepšelį |
| Checkout 1 | 1 val. | Tiesus kvietimas užbaigti pradėtą užsakymą | Užbaigti užsakymą |
| Checkout 2 | 24 val. | Paskutinis šios serijos priminimas ir likę patikrinimai | Užbaigti užsakymą |

Laikų interpretacija yra darbinė prielaida, pateikta vartotojui: po pirmo laiško laukimas 23 val., po antro krepšelio laiško dar 24 val. Jei norėti 24 val. tarpai tarp laiškų, pakeisti į 1, 25 ir 49 val. Turinys nuo to nesikeičia. Checkout laikai pritaikyti pagal pirmus du vartotojo nurodytus laikus.

## Siuntimo logika

Pradėti nuo Omnisend native Abandoned Cart ir Abandoned Checkout presetų. Krepšelio įvykis: Added product to cart; išeiti po Started Checkout arba Placed Order. Checkout įvykis: Started Checkout; išeiti po Placed Order. Pirmam laiškui naudoti 1 val. inactivity ir nedėti dar vieno 1 val. laukimo. Siųsti tik identifikuotiems, siuntimui tinkamiems kontaktams. Pradėjus checkout, krepšelio seka nebetęsiama. [Oficiali logika](https://support.omnisend.com/en/articles/6659889-abandoned-cart-and-abandoned-checkout-automations).

Prieš paleidimą patikrinti persidengimą su esamais Shopify ir kitais atkūrimo laiškais. Rekomenduojama vienam kontaktui neleisti vienu metu kaupti kelių to paties tipo serijos egzempliorių; pradinė pakartotinio įėjimo riba 7 dienos yra mūsų pasiūlymas. Pirkimas, atsisakymas ar blokavimas stabdo siuntimą. Checkout turi prioritetą prieš cart, o abi atkūrimo serijos prieš bendrą welcome ar winback komunikaciją. Konkrečius segmentus bei prioritetų taisykles patvirtinti paskyroje, jos dar nesukonfigūruotos.

Skubumas kuriamas raginimais grįžti dabar ir užbaigti likusius žingsnius. Nėra fiktyvios rezervacijos, laikmačio, mažo likučio ar nuolaidos termino. Papildoma nuolaida nepridėta.

## Kaip surinkti laišką Omnisend

Kiekvienam laiškui kataloge yra `preview.html`, `preview-stripped.html`, `metadata.json`, `copy.txt` ir `omnisend/` fragmentai. Pilkas plotas ir mygtukas peržiūroje tik iliustruoja native elementų vietą. Peržiūros HTML nesiųsti gavėjams ir neimportuoti kaip baigto dinaminio laiško.

1. Sukurti 600 px pločio template, išorinis fonas `#E6E5E0`, turinio fonas `#FAFAF8`, layout šoniniai tarpai 0.
2. Pirmame Custom HTML bloke įklijuoti `omnisend/01-before-products.html`. Į Styles lauką įkelti `omnisend/styles.css`.
3. Įterpti vieną native Abandoned Products elementą. Jis pakeičia pilką placeholderį. Pasirinkti nuotraukas, pavadinimus ir kainas; ilgų aprašymų nerodyti. Įjungti mobile stacking. Pradinis išdėstymas: viena produktų skiltis, iki 12 produktų, išlaikant natūralias nuotraukų proporcijas.
4. Išjungti kiekvienos prekės Shop Now mygtuką. Šis mygtukas veda į konkrečios prekės puslapį, ne visą krepšelį. Palikti vieną native Button po produktais. Tekstas lentelėje, nuoroda `[[event.raw.abandoned_checkout_url]]`. Violetinis fonas `#38243F`, šviesus tekstas `#F4F0E8`, Arial 16 px bold, vertikalūs tarpai bent 16 px, visas paviršius paspaudžiamas.
5. Toliau įkelti `omnisend/02-after-products.html` į antrą Custom HTML bloką. Pabaigoje naudoti Omnisend standartinę įmonės ir atsisakymo footer dalį.
6. Temą bei preheaderį nukopijuoti iš metadata. Blokų fonas baltas `#FAFAF8`; produktų bei mygtuko šoniniai tarpai 24 px, mygtuko viršus 18 px, apačia 24 px.

Fragmentai turi tik body turinį, lenteles ir inline stilius. Juose nėra netinkamų div, script, iframe, head ar body žymių. [Custom HTML įkėlimas](https://support.omnisend.com/en/articles/1061866-add-configure-custom-html-item).

Vienas native Abandoned Products blokas viename laiške. Dinaminę peržiūrą tikrinti su realiu įvykiu: bendras testinis laiškas neatkuria tikro krepšelio. [Dinaminių produktų dokumentacija](https://support.omnisend.com/en/articles/6092208-add-configure-abandoned-products-item).

## Turinys ir jo pagrindas

Kliento klausimynas pagrindžia pagarbų kreipinį, pagalbą, kainos ir kokybės santykį, atsiskaitymo pasirinkimą. Nežadama, kad kiekvienam krepšeliui prieinami visi mokėjimo būdai, visi produktai lietuviški ar visi pagaminti vietoje.

Cart 2 atsiliepimas: Mantas, 2025 m. rugpjūčio 19 d., viešo komentaro ištrauka apie bendravimą, pristatymą ir baldų kokybę. Šaltinis patikrintas 2026 m. spalio 10 d.: https://rekvizitai.vz.lt/imone/rancoris/atsiliepimai/1/ . Tai individuali patirtis, ne viso katalogo garantija. Nepridėtas išgalvotas bendras žvaigždučių įvertinimas. Platformoje yra ir neigiamų atsiliepimų.

Savininkas patvirtino nemokamą pristatymą ir atsiskaitymą gavus prekę. Šie privalumai aiškiai pateikti prieš dinamines prekes. Konkretus pristatymo terminas tikslinamas pagal pasirinktą prekę.

## Patikra prieš aktyvavimą

Naršyklės patikra vertina tik pateiktus fragmentus ir dinaminės vietos maketą, ne tikrą Omnisend sugeneruotą produktų sąrašą. Galutinė native bloko tipografija ir išdėstymas priklauso nuo Omnisend nustatymų.

Paskyroje patikrinti tikrus scenarijus: viena prekė, kelios skirtingų proporcijų nuotraukos, ilgas pavadinimas, pasirinktas dydis ar spalva, kiekis, pašalinta prekė, pasikeitusi kaina, išparduota prekė, tuščias krepšelis. Nepažadėti, kad prekės likutis rezervuotas. Įsitikinti, kad nuoroda atkuria tinkamo žmogaus teisingus variantus, o ne bendrą parduotuvės krepšelį. Jei native bloke varianto ar kiekio neįmanoma parodyti, tai pažymėti ir tikrinti jų išlaikymą atkurtame krepšelyje. Visiems nepasiekiamiems produktams ištuštėjus blokui, laiško nesiųsti. Didesniam nei 12 eilučių krepšeliui nustatyti atskirą elgesį, nežadėti visų prekių atvaizdavimo.

Atlikti kontroliuojamą realų abandonment testą, exit po checkout pradžios ir po pirkimo bei testinius pristatymus naudojamuose pašto klientuose. Siuntimo teisėtumas ir kontaktų tinkamumas nustatomi paskyroje. Ši užduotis šių veiksmų neaktyvavo.


Aktuali visų pločių patikra: [qa-current](../qa-current/report.json). Senasis qa katalogas istorinis.
