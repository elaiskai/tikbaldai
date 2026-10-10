"""Build three distinct email-safe winback designs using campaign visuals based on authentic catalog product references."""
from pathlib import Path
from html import escape
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import hashlib, json, re, sys

ROOT = Path(__file__).resolve().parent
ASSETS = json.loads((ROOT/'assets.json').read_text())
PAPER, INK, PLUM, WHITE = '#F4F0E8', '#202221', '#38243F', '#FFFFFF'
SANS, SERIF = 'Arial,Helvetica,sans-serif', 'Georgia,Times New Roman,serif'
HOME = 'https://tikbaldai.lt/'
URLS = {'living':HOME+'collections/svetaines-baldai', 'storage':HOME+'collections/spintos-komodos', 'dining':HOME+'collections/virtuves-ir-valgomojo-baldu-komplektai', 'chair':HOME+'products/fotelis-amorinito', 'table':HOME+'collections/kavos-staliukai', 'popular':HOME+'collections/populiariausi', 'sofas':HOME+'collections/sofos-lovos', 'armchairs':HOME+'collections/foteliai-kedes'}
offer_file = ROOT/'offer.json'
OFFER = json.loads(offer_file.read_text()) if offer_file.exists() else {'code':'assugrizau','amount':None,'unit':None,'status':'Amount awaiting user clarification; show code only.'}
NUMBER = '01'

def track(url, content):
    return escape(url+('?' if '?' not in url else '&')+urlencode({'utm_source':'automation','utm_medium':'email','utm_campaign':'winback_'+NUMBER,'utm_content':content}), quote=True)

def p(text, color=INK, size=16, margin='0 0 20px'):
    return f'<p style="margin:{margin};font:{size}px/{size+10}px {SANS};color:{color};">{text}</p>'

def label(text, color='#736874'):
    return f'<p style="margin:0 0 18px;font:11px/18px {SANS};font-weight:bold;letter-spacing:2px;color:{color};">{text}</p>'

def heading(text, color=INK, large=False):
    return f'<h{1 if large else 2} class="{"display" if large else "section-title"}" style="margin:0 0 22px;font:normal {42 if large else 30}px/{46 if large else 37}px {SERIF};letter-spacing:{"-1.2" if large else "-.4"}px;color:{color};">{text}</h{1 if large else 2}>'

def button(text, url, bg=PLUM, color=PAPER):
    return f'''<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{url}" style="height:54px;v-text-anchor:middle;width:320px;" arcsize="0%" stroke="f" fillcolor="{bg}"><w:anchorlock/><center style="font-family:Arial;font-size:15px;font-weight:bold;color:{color};">{text}</center></v:roundrect><![endif]-->
<!--[if !mso]><!--><table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="width:100%;max-width:360px;"><tr><td bgcolor="{bg}"><a class="cta" href="{url}" style="display:block;padding:16px 10px;font:700 15px/22px {SANS};text-align:center;text-decoration:none;background-color:{bg};color:{color};">{text}</a></td></tr></table><!--<![endif]-->'''

def photo(key, alt, url, width=600):
    return f'<a class="photo-link" href="{url}" style="display:block;"><img src="{ASSETS[key]["url"]}" width="{width}" alt="{alt}" style="display:block;width:100%;max-width:{width}px;height:auto;border:0;"></a>'

def section(content, bg=PAPER, pad='34px 24px', align='left', cls='pad'):
    return f'<tr><td class="{cls}" bgcolor="{bg}" align="{align}" style="padding:{pad};background-color:{bg};">{content}</td></tr>'

def row_card(number, title, body, image, alt, url, cta):
    return f'''<table class="product-card" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100%;border-top:1px solid #D7CFC5;"><tr><td style="padding:25px 0;font-size:0;">
<!--[if mso]><table role="presentation" width="520"><tr><td width="250" valign="top"><![endif]--><div class="card-photo" style="display:inline-block;width:100%;vertical-align:top;">{photo(image,alt,url,520)}</div><!--[if mso]></td><td width="270" valign="middle"><![endif]--><div class="card-copy" style="display:inline-block;width:100%;vertical-align:top;"><div class="card-pad" style="padding:20px 0 0;">
{label(number)}<h3 style="margin:0 0 9px;font:normal 28px/34px {SERIF};color:{INK};">{title}</h3>{p(body,size=15,margin='0 0 12px')}<a class="cta" href="{url}" style="display:block;padding:14px 10px;font:700 14px/21px {SANS};text-align:center;text-decoration:none;background-color:{PLUM};color:{PAPER};">{cta}</a></div></div><!--[if mso]></td></tr></table><![endif]--></td></tr></table>'''

def coupon(compact=False):
    code=escape(OFFER['code'])
    amount = str(OFFER['amount'])+' '+OFFER['unit'] if OFFER.get('amount') is not None else None
    if compact:
        return label('JŪSŲ SUGRĮŽIMO KODAS', '#D7CBD9')+f'<p style="margin:0 0 10px;font:700 25px/34px {SANS};letter-spacing:2px;color:{PAPER};">{code}</p>'+p((amount+' nuolaida kitam užsakymui. ' if amount else '')+'Kodą įveskite atsiskaitymo metu.', '#E1D8E2',14,'0')
    headline = f'<p class="offer-amount" style="margin:0;font:normal 108px/112px {SERIF};letter-spacing:-5px;color:{PAPER};">{amount}</p>'+p('nuolaida Jūsų kitam užsakymui',PAPER,16,'10px 0 26px') if amount else heading('Gera Jus<br>vėl matyti.',PAPER,True)+p('Jūsų kitam pirkiniui paruošėme<br>sugrįžimo pasiūlymą.', '#DED3E0',16,'0 0 26px')
    return label('PASIŪLYMAS SUGRĮŽTANTIEMS', '#D7CBD9')+headline+f'<table role="presentation" width="100%" style="width:100%;max-width:360px;border:1px solid #8D7793;"><tr><td align="center" style="padding:18px 10px;">{label("JŪSŲ KODAS", "#D7CBD9")}<p style="margin:0;font:700 27px/34px {SANS};letter-spacing:1px;color:{PAPER};">{code}</p></td></tr></table><div style="height:22px;line-height:22px;">&nbsp;</div>'+button('Rinktis su pasiūlymu',track(HOME,'return_offer'),PAPER,PLUM)+p('Kodą įveskite atsiskaitymo metu.','#D7CBD9',12,'16px 0 0')

def footer():
    return section(p('TIK BALDAI · UAB Rancoris', '#CAC9C3',12,'0 0 5px')+p('Partizanų g. 61, 806 patalpa<br>Kaunas, Lietuva','#B7B7B1',11,'0 0 15px')+p('Šį laišką gavote, nes prenumeruojate<br>TIK BALDAI naujienas.','#B7B7B1',11,'0')+f'<a class="cta" href="{{{{unsubscribe_url}}}}" style="display:inline-block;padding:14px 0;font:12px/20px {SANS};color:#D5D3CC;text-decoration:underline;">Atsisakyti naujienlaiškių</a>',INK,'26px 24px 16px','center')

def shell(subject, preheader, content):
    return f'''<!doctype html><html lang="lt" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><meta name="color-scheme" content="light"><meta name="supported-color-schemes" content="light"><title>{subject}</title>
<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
<style>body{{margin:0;padding:0;-webkit-text-size-adjust:100%;}}table{{border-collapse:collapse;}}a[x-apple-data-detectors]{{color:inherit!important;text-decoration:none!important;}}@media(min-width:600px){{.pad{{padding-left:40px!important;padding-right:40px!important;}}.display{{font-size:66px!important;line-height:69px!important;letter-spacing:-2px!important;}}.card-photo{{width:48%!important;}}.card-copy{{width:52%!important;}}.card-pad{{padding:0 0 0 26px!important;}}.offer-amount{{font-size:148px!important;line-height:148px!important;}}.section-title{{font-size:36px!important;line-height:43px!important;}}}}</style></head>
<body style="margin:0;padding:0;width:100%;background:#E6E5E0;-webkit-text-size-adjust:100%;text-size-adjust:100%;"><div style="display:none!important;max-height:0;overflow:hidden;font-size:1px;line-height:1px;color:{PAPER};mso-hide:all;">{preheader}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%;background:#E6E5E0;"><tr><td align="center" style="padding:0;"><!--[if mso]><table role="presentation" width="600"><tr><td><![endif]--><table class="email-shell" role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center" style="width:100%;max-width:600px;border-collapse:collapse;background:{PAPER};">
{section(f'<a href="{track(HOME,"logo")}" style="display:inline-block;padding:8px 0;"><img src="{ASSETS["logo"]["url"]}" width="151" height="27" alt="TIK BALDAI" style="display:block;width:151px;height:auto;border:0;"></a>',INK,'17px 24px','center')}
{content}{footer()}</table><!--[if mso]></td></tr></table><![endif]--></td></tr></table></body></html>'''

def build_one():
    return section(label('JŪSŲ NAMŲ TĘSINYS')+heading('Namai keičiasi.<br>Kartu su Jumis.',large=True)+p('Jau rinkotės TIK BALDAI. Gal dabar namams trūksta patogaus fotelio, talpios komodos ar valgomojo stalo? Peržiūrėkite kategorijas ir išsirinkite kitą savo baldą.'))+section(label('NUO KO NORĖTUMĖTE PRADĖTI?')+row_card('01 / JŪSŲ POILSIUI','Sofos ir foteliai.','Patogiam vakarui su knyga ar tiesiog ramiai valandai po dienos darbų.','living','Šviesi Universe sofa svetainės interjere',track(URLS['living'],'category_living'),'Žiūrėti svetainės baldus')+row_card('02 / JŪSŲ TVARKAI','Spintos ir komodos.','Komoda ar spinta gali padėti atrasti daugiau vietos tam, ką mėgstate.','storage','Alyvuogių spalvos komoda namų interjere',track(URLS['storage'],'category_storage'),'Žiūrėti spintas ir komodas')+row_card('03 / JŪSŲ LAIKUI KARTU','Valgomojo komplektai.','Kasdieniams pusryčiams, pokalbiams ir vakarienei, kuri neskuba baigtis.','dining','Valgomojo stalas su keturiomis šviesiomis kėdėmis',track(URLS['dining'],'category_dining'),'Žiūrėti valgomojo komplektus'),pad='32px 24px 12px')+section(heading('Nuo vieno gero<br>pasirinkimo.',PAPER)+p('Peržiūrėkite modelius, išsirinkite tinkamą ir užsisakykite internetu.','#D7CDD9')+button('Žiūrėti populiariausius',track(URLS['popular'],'browse_popular'),PAPER,PLUM),PLUM,'34px 24px 38px')

def build_two():
    ivory='#F8F6F0'
    amount=str(OFFER['amount'])+' '+OFFER['unit']+' nuolaida kitam užsakymui.' if OFFER.get('amount') is not None else 'Pasiūlymas Jūsų kitam užsakymui.'
    offer=f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%;border-top:1px solid #CEC6BC;border-bottom:1px solid #CEC6BC;"><tr><td align="center" style="padding:27px 0;">{label("JUMS, SUGRĮŽTANTIEMS")}{p(amount,INK,17,"0 0 14px")}<p style="margin:0 0 21px;font:700 29px/36px {SANS};letter-spacing:2px;color:{PLUM};">{escape(OFFER["code"])}</p>{button("Rinktis baldus su kodu",track(URLS["popular"],"return_offer"))}{p("Kodą įveskite atsiskaitymo metu.","#736874",12,"15px 0 0")}</td></tr></table>'
    return section(label('GERA JUS VĖL MATYTI')+heading('Jūsų namams.<br><i>Su malonumu.</i>',large=True),ivory,'40px 24px 0','center')+section(photo('tray','Universe sofa ant sidabrinio padėklo, kūrybinė TIK BALDAI kompozicija',track(URLS['living'],'hero_tray')),ivory,'0',cls='')+section(p('Kviečiame išsirinkti kitą baldą savo namams. Peržiūrėkite modelius, įsidėkite patikusį į krepšelį ir atsiskaitydami panaudokite sugrįžimo kodą.',INK,17,'0 0 28px')+offer,ivory,'8px 24px 36px')+section(label('KITA GERA IDĖJA JŪSŲ NAMAMS')+row_card('01 / LAIKUI KARTU','Valgomojo komplektai.','Valgomojo baldai kasdieniams susitikimams prie vieno stalo.','dining','Valgomojo stalas su keturiomis šviesiomis kėdėmis šiltame interjere',track(URLS['dining'],'category_dining'),'Žiūrėti valgomojo komplektus')+row_card('02 / KASDIENEI TVARKAI','Spintos ir komodos.','Spintos ir komodos tam, ką norite laikyti tvarkingai ir patogiai.','storage','Alyvuogių spalvos komoda šviesiame interjere',track(URLS['storage'],'category_storage'),'Žiūrėti spintas ir komodas'),ivory,'12px 24px 20px')+section(button('Žiūrėti populiariausius',track(URLS['popular'],'browse_popular'))+p('Prireikus padėsime pasitikslinti matmenis, medžiagas ar komplektaciją.','#665F66',14,'22px 0 0'),ivory,'8px 24px 36px')

def question(number, title, body):
    return f'<table role="presentation" width="100%" style="width:100%;border-top:1px solid #D7CFC5;"><tr><td width="42" valign="top" style="width:42px;padding:22px 12px 22px 0;font:normal 25px/32px {SERIF};color:#86698D;">{number}</td><td style="padding:22px 0;"><h3 style="margin:0 0 8px;font:normal 25px/31px {SERIF};color:{INK};">{title}</h3>{p(body,size=15,margin="0")}</td></tr></table>'

def shop_choice(title, body, destination, content, cta):
    return f'<table class="shop-choice" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100%;border-top:1px solid #D7CFC5;"><tr><td style="padding:23px 0;">'+heading(title)+p(body,size=15,margin='0 0 17px')+button(cta,track(destination,content))+'</td></tr></table>'

def build_three():
    ivory='#FAFAF8'
    choices=shop_choice('Sofos lovos','Palyginkite dydžius, spalvas ir miegamosios dalies sprendimus.',URLS['sofas'],'category_sofas','Žiūrėti sofas lovas')+shop_choice('Foteliai','Raskite patogią vietą knygai, filmui ar ramiam vakarui.',URLS['armchairs'],'category_armchairs','Žiūrėti fotelius')+shop_choice('Kavos staliukai','Išsirinkite prie sofos ir Jūsų erdvės derantį staliuką.',URLS['table'],'category_tables','Žiūrėti kavos staliukus')
    return section(photo('moodboard','Kaip derinti oranžinę sofą. TIK BALDAI oranžinė sofa ir baltas apvalus kavos staliukas spalvų koliaže',track(URLS['living'],'hero_styling')),ivory,'0',cls='')+section(label('IŠSIRINKITE SAVO SVETAINEI')+heading('Kitas geras<br>pasirinkimas<br>Jūsų namams.',large=True)+p('Patogi sofa, mėgstamas fotelis ar naujas kavos staliukas. Peržiūrėkite modelius ir išsirinkite tai, ko dabar trūksta Jūsų svetainei.'),ivory,'32px 24px 16px')+section(choices,ivory,'0 24px 10px')+section(heading('Išsirinkote?')+p('Prieš užsakydami palyginkite baldo matmenis su vieta namuose ir patikrinkite konkretaus modelio medžiagas bei funkcijas.',size=15,margin='0 0 8px')+f'<a class="cta" href="mailto:info@tikbaldai.lt" style="display:inline-block;padding:13px 0;font:14px/22px {SANS};color:{PLUM};text-decoration:underline;">Kilo klausimas apie prekę? Parašykite.</a>',ivory,'14px 24px 28px')+section(heading('Išsirinkite baldą.<br>Panaudokite kodą.',PAPER)+coupon(True)+'<div style="height:22px;line-height:22px;">&nbsp;</div>'+button('Rinktis baldus su kodu',track(URLS['popular'],'return_offer'),PAPER,PLUM),PLUM,'34px 24px 38px')


SUBJECTS = {'01':('Ką norėtumėte atnaujinti savo namuose?','Vieta poilsiui, bendriems vakarams ar daugiau tvarkos. Atraskite savo kitą pasirinkimą.'),'02':('Jūsų kitam pirkiniui turime pasiūlymą','Sugrįžkite su kodu assugrizau ir išsirinkite tai, ko dabar reikia Jūsų namams.'),'03':('Ko dabar trūksta Jūsų svetainei?','Peržiūrėkite sofas, fotelius ir kavos staliukus. Kitam užsakymui panaudokite kodą assugrizau.')}

if __name__=='__main__':
    for NUMBER, builder in [('01',build_one),('02',build_two),('03',build_three)]:
        if len(sys.argv)>1 and NUMBER!=sys.argv[1]: continue
        subject, preheader=SUBJECTS[NUMBER]
        html=shell(subject,preheader,builder())
        stripped=re.sub(r'<style\b[^>]*>.*?</style>|<link\b[^>]*>','',html,flags=re.S|re.I)
        (ROOT/f'email-{NUMBER}.html').write_text(html)
        (ROOT/f'email-{NUMBER}-stripped.html').write_text(stripped)
        soup=BeautifulSoup(html,'html.parser')
        for t in soup(['style','script']):t.decompose()
        copy=soup.get_text(' ',strip=True)+' '.join(i.get('alt','') for i in soup.find_all('img'))
        assert not re.search(r'[-\u2010-\u2015\u2212]',copy), 'Dash punctuation in copy'
        meta={'version':4 if NUMBER in ('02','03') else 3,'date':'2026-10-10','subject':subject,'preheader':preheader,'day_from_last_order':{'01':180,'02':187,'03':194}[NUMBER],'audience':'Existing furniture customers, general fallback design. Generator-only buyers excluded.','send_rule':'Eligible nonbuyers; email3 requires recent click or known site visit.' if NUMBER=='03' else 'Eligible prior customers without newer purchase.','personalization':'Generic fallback. Dynamic category selection not connected.','offer':OFFER if NUMBER!='01' else None,'html_sha256':hashlib.sha256(html.encode()).hexdigest(),'stripped_sha256':hashlib.sha256(stripped.encode()).hexdigest(),'platform_delivery_verified':False,'status':'design_draft','image_urls':sorted({i['src'] for i in soup.find_all('img')})}
        (ROOT/f'email-{NUMBER}.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
        (ROOT/f'email-{NUMBER}-copy.txt').write_text(subject+'\n'+preheader+'\n\n'+soup.get_text('\n',strip=True))
        print(NUMBER,meta['html_sha256'],len(html.encode()))
