# TIK BALDAI: peržiūrėtos prekės serija

Du Omnisend Product Abandonment laiškų surinkimo maketai. Native produktas neprijungtas. Serija neaktyvuota, laiškai neišsiųsti.

| Laiškas | Siūlomas laikas | Paskirtis | Native CTA |
|---|---|---|---|
| Produktas 1 | Po 2 val. nuo tinkamo peržiūros įvykio | Trumpas kvietimas vėl apžiūrėti prekę ir jos variantus | Apžiūrėti prekę |
| Produktas 2 | Dar po 24 val., bendrai 26 val. | Matmenys, komplektacija ir pristatymo informacija padeda apsispręsti | Apžiūrėti prekę |

Tai siūlomas grafikas. Ši serija skirta produkto puslapį peržiūrėjusiam, bet į krepšelį prekės neįdėjusiam žmogui. Tekstuose nesakoma, kad krepšelis ar užsakymas jau egzistuoja. Nuolaida ir fiktyvus trūkumas nepridedami.

## Įvykiai ir prioritetai

Naudoti Product Abandonment presetą: Viewed Product ir in stock filtras, identifikuotas kontaktas. Prie Placed Order išėjimo pridėti Added product to cart bei Started checkout. Įjungti Skip Contacts aktyvioms cart ir checkout serijoms. Siūlome pakartotinį įėjimą riboti 14 dienų. Pirmas delay 2 val., antras 24 val. Tai dar nesukonfigūruota paskyroje. [Oficiali dokumentacija](https://support.omnisend.com/en/articles/1690227-product-abandonment-automation), patikrinta 2026 m. spalio 10 d.

Pirmenybė: checkout, cart, product. Sąlygas patikrinti prieš abu siuntimus. Naudoti tik siuntimui tinkamus kontaktus; įvykio sekimas ir kanalų nustatymai tikrinami paskyroje. Bendras naršymo priminimas nepridedamas, kol neįvertintas srautas bei šių serijų persidengimas.

## Surinkimas Omnisend

`preview.html` ir pilkas plotas skirti tik maketui. Jų nesiųsti gavėjams. Kiekvieno laiško kataloge yra tema, preheaderis ir du body fragmentai.

1. Nustatyti 600 px email plotį, layout šoninius tarpus 0, išorinį foną #E6E5E0, vidinį #FAFAF8.
2. Custom HTML bloke įdėti `omnisend/01-before-product.html`. Styles lauke naudoti `omnisend/styles.css`.
3. Įterpti vieną native Abandoned Products bloką: nuotrauka, pavadinimas, kaina. Šiame flow jis rodo paskutinę peržiūrėtą prekę, ne visą naršymo istoriją. Palikti vieną native produkto mygtuką „Apžiūrėti prekę“, susietą su produkto puslapiu. Nenaudoti cart recovery URL. [Bloko dokumentacija](https://support.omnisend.com/en/articles/6092208-add-configure-abandoned-products-item).
4. Native blokui parinkti vieną skiltį, mobile stacking, natūralias nuotraukos proporcijas, 24 px šoninius tarpus. Mygtuko fonas #38243F, tekstas #F4F0E8, Arial 16 px bold, 16 px vertikalūs tarpai, visas paviršius paspaudžiamas ir bent 44 px aukščio. Papildomo pirkimo mygtuko HTML fragmentuose nėra.
5. Įdėti `omnisend/02-after-product.html`. Pabaigoje naudoti standartinį Omnisend įmonės ir atsisakymo footer. Temą ir preheaderį paimti iš `metadata.json`.

Abu HTML fragmentai naudoja lenteles ir inline stilius. [Custom HTML taisyklės](https://support.omnisend.com/en/articles/1061866-add-configure-custom-html-item).

## Faktai ir patikra

Taikomas esamas Brand DNA tonas: pagarbus Jūs, konkretus tekstas, jokių brūkšnių gavėjui skirtoje kopijoje. Pristatymo skaičiai, nemokamas pristatymas ar universali gamybos kilmė nežadami. Esamame kliento tyrime pristatymo sąlygos prieštaringos, todėl kviečiama tikrinti konkrečią prekę. Matmenų ir komplektacijos punktai yra praktiniai patarimai, ne teiginiai apie konkretaus modelio savybes.

Naršyklės QA apima statinius fragmentus ir pažymėtą native vietą 600, 320, 390 bei 430 px pločiu, su head stiliais ir be jų. Tikro dinaminio produkto, jo URL bei Omnisend ar pašto kliento pristatymo ši peržiūra nepatvirtina.

Prieš aktyvuojant paskyroje atlikti realų identifikuoto kontakto Viewed Product testą. Patikrinti ilgą prekės pavadinimą, kainą, skirtingų proporcijų nuotrauką, vieną produkto CTA ir jo nuorodą, prieinamumo pokytį bei išėjimą pridėjus į krepšelį, pradėjus checkout ar nupirkus. Tuščio produkto bloko laiško nesiųsti. Tikrinti abu laiškus realiame gavime, ne vien redaktoriaus bendrame testiniame laiške.
