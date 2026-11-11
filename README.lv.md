<img src="assets/REYRUN.png" alt="REYRUN" width="100">

# REYRUN · Red Dead Redemption 2 latviski

Latviski · [English](README.md)

Bezmaksas rakstītā teksta tulkojums spēles *Red Dead Redemption 2* stāsta režīmam Windows datorā. Izvēlnes un subtitri ir latviski. Varoņi runā oriģinālvalodā.

**[Lejupielādēt tulkojumu](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip)** · [Apmeklēt projekta mājaslapu](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/)

## Reinis saviem atbalstītājiem

Mani sauc Reinis Runcis. Šis tulkojums ir mans paldies cilvēkiem, kuri man palīdz turpināt dzīvot mājās. Dāvinu to visiem, kam gribas izspēlēt šo stāstu latviski.

Jau daudzus gadus dzīvoju viens. Pēdējā laikā par aprūpi un ikdienas vajadzībām izdodu vairāk, nekā saņemu. Ja vēlaties mani atbalstīt, lūdzu, dodiet tikai tik, cik paši varat ar prieku atvēlēt. Man dzīve joprojām šķiet fantastiska, un būšu priecīgs, ja kādam mans darbs dos spēku turēties, kad pašam iet grūti.

Ja gribat mani tuvāk iepazīt, palasīt manu dzeju vai pajautāt par citiem darbiem, [rakstiet man Facebook](https://www.facebook.com/reinis.runcis).

### Brīvprātīgs atbalsts

- **Swedbank** · REINIS RUNCIS · IBAN `LV82HABA0551011504293`
- **Stripe** · [Atbalstīt eiro](https://buy.stripe.com/dRm7sNfD2bOZckRb9A6g802) · [Atbalstīt ASV dolāros](https://donate.stripe.com/cNifZj4Yog5fckR5Pg6g800)
- **PayPal** · [Reinis Runcis Support](https://paypal.me/ReinisRuncisSupport)
- **USDT · BNB Smart Chain (BSC), BEP-20** · `0x32834068Fa4fEe29fA10e2020e68Fb23d5fC1d21`
- **USDT · Solana, SPL** · `Hy6hKMwMDgXFdaD3N5J1CNMs2LwiE22QdrQnEYoX3fZh`

## Kā iztulkot citu spēli latviski

Sāc ar [praktisko pamācību](skills/reyrun-game-translation-lv/references/GUIDE-lv.md). [REYRUN prasmi](skills/reyrun-game-translation-lv/SKILL.md) vari iedot savam MI asistentam. Tos pašus soļus var veikt arī tulkotājs un redaktors. Piemērus vari izmēģināt savā datorā. Komplektā iekļautie Python rīki palīdz atrast sabojātus vietturus un pārbaudīt rediģēto tekstu pirms ievietošanas spēlē.

[RDR2 darba gaitas un kļūdu analīzē](docs/RETROSPECTIVE-lv.md) aprakstījām, kāpēc uzkrājās tūkstošiem neievietotu melnrakstu, kā pēc pārtraukumiem atguvām jau iztulkoto un kā skaitījām rindas, kuras tiešām nonāca spēles failā.

## Kā uzstādīt tulkojumu

1. Aizver spēli un izpako ZIP failu. Steam bibliotēkā ar labo pogu noklikšķini uz spēles nosaukuma, izvēlies **Manage** un tad **Browse local files**. Ja lieto citu palaidēju, tajā atver spēles instalācijas mapi. Atrodi `RDR2.exe`.
2. No [RacerMouze lapas](https://www.nexusmods.com/reddeadredemption2/mods/10214) paņem `UniversalRDR2StringTranslator.asi`. Spraudnim vajag arī ASI ielādētāju. Ja spēles mapē jau ir strādājošs `dinput8.dll`, paturi to. Citādi paņem `dinput8.dll` no [Alexander Blade lejupielādes](https://www.dev-c.com/rdr2/scripthookrdr2/) mapes `bin`. Abiem failiem jāatrodas blakus `RDR2.exe`.
3. Ja spēlē iepriekš bijis cits tulkojums, saglabā veco tulkojuma XML un veco `rdr2-translator.asi` rezerves mapē ārpus spēles. No REYRUN arhīva iekopē `Latvian Translation.xml` blakus `RDR2.exe`. Saglabā esošo faila nosaukumu.
4. Palaidējā atstāj **English**. Atver **Story Mode**, ieslēdz subtitrus un pārbaudi izvēlni un kādu dialogu. [Pilnajā instrukcijā](UZSTADISANA-LV.txt) aprakstīta arī iepriekšējās instalācijas atjaunošana.

Vari pievienot failu `UZSTADISANA-LV.txt` savam MI asistentam un palūgt: “Palīdzi man pēc šīs instrukcijas uzstādīt REYRUN latviešu tulkojumu. Spēle ir uz Windows, un es izmantoju [Steam vai citu palaidēju].”

## Ko pārbaudījām

2026. gada 11. novembrī visi 253 073 apstiprinātie ieraksti precīzi sakrita ar Steam instalācijas XML pēc identifikatora un teksta. Publiskā ZIP kontrolsumma ir `11d7ee80bac9ac820a2c20e87f2f7fc736e3fab5ceb6e9cf7842543f9f3237da`. Vēl jāpārbauda, kā burti un garākās rindas izskatās pašas spēles ekrānā.

## Izmantošana

REYRUN tulkojumu, metodi un tai pievienotos rīkus drīkst brīvi lietot, kopēt, pārveidot un izplatīt jebkuram mērķim. Šī atļauja attiecas uz Reiņa Runča ieguldījumu. Spēle un tās faili, kā arī trešo pušu spraudņi pieder to tiesību īpašniekiem.
