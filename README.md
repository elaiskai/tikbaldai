# TIK BALDAI laiškai

Dabartiniai 13 laiškų ir vieši paveikslėliai įkėlimui į Omnisend. Atnaujinta 2026 m. spalio 16 d.

SVEIKI25: 25 € pirmam užsakymui, savininkas patvirtino, kad kodas aktyvus. assugrizau: 5 % visam pirkinių krepšeliui.

| Laiškas | HTML arba maketas | 600 px | 390 px |
|---|---|---|---|
| Welcome 1 | [HTML](welcome-01/email.html) | [Kompiuteris](qa-current/welcome-01-600.jpg) | [Telefonas](qa-current/welcome-01-390.jpg) |
| Welcome 2 | [HTML](welcome-02/email.html) | [Kompiuteris](qa-current/welcome-02-600.jpg) | [Telefonas](qa-current/welcome-02-390.jpg) |
| Welcome 3 | [HTML](welcome-03/email.html) | [Kompiuteris](qa-current/welcome-03-600.jpg) | [Telefonas](qa-current/welcome-03-390.jpg) |
| Winback 1 | [HTML](winback/email-01.html) | [Kompiuteris](qa-current/winback-01-600.jpg) | [Telefonas](qa-current/winback-01-390.jpg) |
| Winback 2 | [HTML](winback/email-02.html) | [Kompiuteris](qa-current/winback-02-600.jpg) | [Telefonas](qa-current/winback-02-390.jpg) |
| Winback 3 | [HTML](winback/email-03.html) | [Kompiuteris](qa-current/winback-03-600.jpg) | [Telefonas](qa-current/winback-03-390.jpg) |
| Paliktas krepšelis 1 | [HTML](recovery/cart-01/preview.html) | [Kompiuteris](qa-current/cart-01-600.jpg) | [Telefonas](qa-current/cart-01-390.jpg) |
| Paliktas krepšelis 2 | [HTML](recovery/cart-02/preview.html) | [Kompiuteris](qa-current/cart-02-600.jpg) | [Telefonas](qa-current/cart-02-390.jpg) |
| Paliktas krepšelis 3 | [HTML](recovery/cart-03/preview.html) | [Kompiuteris](qa-current/cart-03-600.jpg) | [Telefonas](qa-current/cart-03-390.jpg) |
| Neužbaigtas atsiskaitymas 1 | [HTML](recovery/checkout-01/preview.html) | [Kompiuteris](qa-current/checkout-01-600.jpg) | [Telefonas](qa-current/checkout-01-390.jpg) |
| Neužbaigtas atsiskaitymas 2 | [HTML](recovery/checkout-02/preview.html) | [Kompiuteris](qa-current/checkout-02-600.jpg) | [Telefonas](qa-current/checkout-02-390.jpg) |
| Peržiūrėta prekė 1 | [HTML](product-abandonment/product-01/preview.html) | [Kompiuteris](qa-current/product-01-600.jpg) | [Telefonas](qa-current/product-01-390.jpg) |
| Peržiūrėta prekė 2 | [HTML](product-abandonment/product-02/preview.html) | [Kompiuteris](qa-current/product-02-600.jpg) | [Telefonas](qa-current/product-02-390.jpg) |

## Įkėlimas

Vadovas ir failų paskirtys: [OMNISEND.txt](OMNISEND.txt). Welcome bei Winback yra pilni HTML. Cart, checkout ir product serijoms naudoti jų omnisend katalogų fragmentus, tarp kurių įterpiamas native dinaminis produktų blokas. preview.html ir pilkos vietos nėra siuntimui.

Visi img src yra vieši absoliutūs HTTPS adresai. Nauji GitHub vaizdai susieti su konkrečiu commit. Pilnuose HTML naudojamas [[unsubscribe_link]].

## Dabartinė patikra

[104 šviežių peržiūrų ataskaita](qa-current/report.json): 600, 320, 390 ir 430 px, įprastai ir be head stilių bei fontų nuorodų. Kiekvienas HTML ir vaizdas susieti SHA256. Vizualiai peržiūrėti tekstai, prekių eilė, nuotraukos, tarpai bei mygtukai.

Tai naršyklės QA. Omnisend dinaminės prekės, grąžinimo į krepšelį nuorodos ir tikras pristatymas dar netestuoti. Automatizacijos dar neįjungtos.

Ankstesni cta-refresh, visual-refresh-v2, winback-spacing ir senieji qa katalogai yra istorinis archyvas. Aktualius maketus ir įrodymus rinktis iš šios lentelės ir qa-current.
