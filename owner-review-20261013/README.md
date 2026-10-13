# TIK BALDAI: atnaujinti laiškai, 2026 10 13

13 maketų pagal savininko pastabas. Tai turinio ir dizaino juodraščiai patvirtinimui, ne aktyvuotos automatizacijos.

## Kas pakeista

* Welcome pasiūlymas yra 35 €. Siūlomas kodas SVEIKI35 dar nesukonfigūruotas ir nepatikrintas. Minimali suma, taikomos prekės, galiojimas ir derinimas su kitomis nuolaidomis turi būti suderinti prieš paleidimą.
* Pagrindiniai statinių laiškų produktai: Gubernator, Gold, Valencia ir Chicago lovų bei čiužinių komplektai. Naudojamos nepakitusios oficialios katalogo nuotraukos. Šaltiniai pateikti assets/manifest.json. Fotelis kliento nurodytu Vera adresu dabar kataloge vadinamas Relax. Jis ir generatoriai palikti papildomose nuorodose.
* Didesnės antraštės ir tekstai, trumpesnė informacija. Aiškiai matomi savininko nurodyti privalumai: nemokamas pristatymas ir atsiskaitymas gavus prekę. Prieš paleidimą būtina patikrinti šių sąlygų ir parduotuvės nustatymų atitiktį bei išimtis.
* assugrizau paliktas be nuolaidos dydžio: kliento pateikto „5“ vienetai nepatvirtinti. Nekeičiame jo į 35 €.
* Atkūrimo laiškuose rodomos gavėjo prekės, ne tik lovos. Nauja nuolaida šioms serijoms nepridėta.

## Siuntimo planas

| Serija | Laikai | Paskirtis |
|---|---|---|
| Welcome, 3 laiškai | iškart, po 2 ir 5 dienų | Prisistatymas bei dovana; komplektų pasirinkimas; pasiūlymo priminimas ir pagalba |
| Peržiūrėta prekė, 2 laiškai | po 2 ir 26 valandų | Priminimas; pirkimo privalumai ir pagalba |
| Krepšelis, 3 laiškai | po 1, 24 ir 48 valandų neveiklumo | Priminimas; pasitikėjimas bei pristatymas; DUK |
| Atsiskaitymas, 2 laiškai | po 1 ir 24 valandų neveiklumo | Užbaigti užsakymą; paskutinis serijos priminimas |
| Winback, 3 laiškai | po 90, 97 ir 104 dienų nuo paskutinio užsakymo | Komplektai; sugrįžimo kodas; pasirinkimas ir kodo priminimas |

Winback 90 dienų pradžia yra siūlomas bandymo taškas, ne iš pardavimų analizės gautas optimalus terminas. Pirkimo intervalų duomenų neturime. Šis lovų turinys skirtas lovomis besidomintiems ankstesniems klientams. Neseniai lovą jau įsigijusius ir vien generatorius pirkusius klientus reikia atskirti. Siūloma lovos pirkėjus iš šios konkrečios serijos pašalinti bent 180 dienų po lovos pirkimo. Jiems reikia atskiro aktualaus papildomo pirkimo turinio. Upsell po mėnesio šiame rinkinyje neparengtas. Trečias winback tik susidomėjusiems, bet dar nepirkusiems, pagal paspaudimą ar svetainės veiklą, ne vien atidarymą.

Visų serijų tinkamumas tikrinamas prieš kiekvieną laišką. Pirkimas stabdo likusius priminimus. Pradėjus checkout, cart stabdomas; įdėjus prekę į krepšelį, product serija stabdoma. Prioritetas checkout, tada cart, tada product. Welcome ir winback neturi dubliuoti aktyvių atkūrimo priminimų. Reikalingas tinkamas rinkodaros sutikimas ir atsisakymo nuoroda.

## Omnisend surinkimas

Septyniuose product, cart ir checkout maketuose pilkas blokas yra tik produkto vietos žymuo. Jo ir demonstracinio mygtuko siųsti negalima. Naudoti atitinkamo laiško omnisend/01-before-products.html, įterpti Omnisend native dinaminį produktų bloką su vienu atitinkamu grįžimo mygtuku, tada omnisend/02-after-products.html. styles.css skirtas papildomam stiliui, o bazinis vaizdas paremtas inline stiliais.

Turi būti rodomos konkretaus gavėjo prekės, variantai, nuotraukos, kainos ir tikras krepšelio, checkout arba prekės adresas. Pakeisti atsisakymo žymenį platformos palaikomu žymeniu. Produktų išnykimą, kainų pokyčius ir jau įvykusį pirkimą patikrinti platformoje. Šio surinkimo ir realaus siuntimo testas dar neatliktas.

## Peržiūra ir patikra

Atidaryti preview.html per vietinį HTTP serverį. manifest.json yra visų laiškų temos, preheader, laikai ir HTML hash. qa-summary.json susieja dabartinius failus su 104 naujais vaizdais: 600, 320, 390 ir 430 px, įprastos bei be head stilių ir fontų nuorodų versijos. Automatinė bei vizualinė naršyklės patikra atlikta. Tai nėra patvirtintas Gmail, Outlook arba Omnisend pristatymas.

Prieš paleidimą: patvirtinti pasiūlymų sąlygas, sukonfigūruoti kodus, segmentus ir siuntimo logiką, surinkti native blokus ir atlikti tikrus testinius siuntimus.
