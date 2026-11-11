# Kā REYRUN pārtulkoja Red Dead Redemption 2 latviski

[English](RETROSPECTIVE-en.md) · [Projekta mājaslapa](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/)

Vienā diennaktī 2026. gada 2. novembrī bija sagatavoti melnraksti 32 666 spēles ierakstiem. Tajā pašā diennaktī spēles failā nonāca 8 602 jauni ieraksti. Darbs uzkrājās pēc melnrakstu sagatavošanas. Pirms dot tulkotājiem nākamo uzdevumu, bija jānoskaidro, cik daudz teksta jau gaida galīgo redakciju vai ievietošanu spēlē.

[Izmantot tulkošanas metodi citai spēlei](../skills/reyrun-game-translation-lv/references/GUIDE-lv.md)

## Ko izdevās izmērīt

Visi datumi un laiki tabulā norādīti pēc Rīgas laika. Viens ieraksts ir viens teksta identifikators spēlē. Gan uzraksts uz pogas, gan gara subtitru rinda skaitās viens ieraksts. Projektā uzskaitīja 256 890 identifikatorus. Par 253 073 tekstiem bija jāpieņem redakcionāls lēmums. Vēl 3 817 bija atsevišķi uzskaitīti izņēmumi, tostarp vadības kodi, skaitļi, simboli un tukšas vērtības.

| Pārbaudes laiks 2026. gadā | Kas bija paveikts | Kā lasīt šo skaitli |
|---|---|---|
| 28. oktobra stāvokļa pārbaude | Spēles XML failā bija 119 387 ieraksti. Vecākā progresa atskaitē joprojām bija 118 002. | Tas bija stāvoklis vienā brīdī no 253 073 tulkošanai paredzētajiem ierakstiem. Atsākot darbu pēc novecojušās atskaites, jau pabeigtā daļa būtu apstrādāta vēlreiz. |
| 31. oktobris, pirmās astoņas paralēli apstrādātās pakas | Apmēram 59 sekundēs tapa 128 īsi melnraksti. Gala redakcijā atstāja 45 sākotnējos formulējumus, 72 izlaboja, 11 atlika precizēšanai. | Viena īsu tekstu izlase. Šīs pārbaudes brīdī 117 apstiprinātie teksti vēl gaidīja ievietošanu. |
| No 1. novembra plkst. 22.00 līdz 2. novembra plkst. 22.00 | Melnraksti bija pabeigti 32 666 unikāliem ierakstiem, redakcijas posms pabeigts 32 620 ierakstiem. Desmit pārbaudītos laidienos pievienoja 8 602 ierakstus. Spēles failā to skaits pieauga no 131 617 līdz 140 219. | Pilna diennakts. Viens ieraksts var parādīties vairāku posmu uzskaitē. Spēlē pievienotie teksti aptvēra 341 985 redzamās angļu avota rakstzīmes, neskaitot vadības marķierus. |
| 6. novembris, plkst. 22.29 līdz 22.34 | Datubāzē apstiprināti 198 995 ieraksti. Spēles failā bija 198 238. Visi 198 238 kopīgie teksti precīzi sakrita. | 757 apstiprināti ieraksti gaidīja ievietošanu. Atsevišķā nakts redakcijā no 1 544 ierakstiem 1 411 atzina par gataviem, 133 atlika. No šīs nakts redakcijas spēlē vēl nebija ievietots neviens. |
| 8. novembris, plkst. 23.23 | Spēlē bija 222 065 ieraksti. No 31 008 vēl neievietotajiem 30 960 atrada saglabātu teksta variantu. 2 093 no tiem izdevās atrast tikai sākotnējās saglabātajās atbildēs. 48 ierakstiem pārbaudes brīdī nevarēja droši piesaistīt saglabāto tekstu. | Atrastajam tekstam vēl bija jāpārbauda redakcijas statuss. Pēc darba atsākšanas 9. novembra plkst. 00.28 atskaite fiksēja 1 415 jaunus ievietotus ierakstus. Šajā posmā jaunu tulkošanas API pieprasījumu bija nulle. |
| 9. novembrī plkst. 22.47 un 10. novembrī plkst. 00.21 | Abas pārbaudes uzrādīja 246 024 ievietotus ierakstus. Atlikuši 7 049. | Abas reizes nolasīja esošo stāvokli. Jauns laidiens nevienā no šīm pārbaudēm netapa. |
| 10. novembra gala pārbaude plkst. 23.28 | Visi 253 073 apstiprinātie teksti un to identifikatori sakrita ar spēles XML. Gaidīšanā un redakcijā atlikto skaits bija nulle. Pēdējā labojumā mainīja 29 jau ievietotus tekstus. | Salīdzināts viss apstiprinātais saturs. Burtu attēlojums, subtitru parādīšanās laiks un rindu izvietojums vēl bija jāpārbauda spēlējot. |

## Kas palēnināja darbu

**Darbinieku skaits un termiņi.** Oktobra desmitajā ciklā bija sagatavoti 12 lokālo darbinieku profili, bet vienlaikus varēja strādāt trīs. No 84 ieplānotajām mazajām pakām nosūtīja 45. Termiņa dēļ 39 pakas ar 179 ierakstiem palika nenosūtītas. Vienā atsūtītajā pakā bija svešs identifikators. Kad redaktori sāka darbu, viņu saņemtajā versijā bija pieejami 90 lokālie melnraksti. Kopā pienāca 264 uzbūves pārbaudi izturējuši teksti, daļa jau pēc redakcijas sākuma. Saglabājām tieši to versiju, ko redaktori bija lasījuši. Kļūdaino ID noraidījām, jo teksta piesaistīšana šķietami pareizajam ID būtu paslēpusi kļūdu. Pārstrādātajā darba kārtībā katram pieprasījumam bija savs termiņš, bet darbu rinda saglabājās un turpināja izsniegt nākamās pakas.

**Galīgā redakcija un ievietošana.** 2. novembrī plkst. 22.04 jau bija 3 286 pārskatīti ieraksti, kas gaidīja importu, un vēl 18 393 bija gatavi galīgajai redakcijai. Pēdējais pabeigtais imports bija plkst. 08.55. Melnrakstu un redakciju darbs turpinājās līdz vakaram. Papildu tulkotājs šīs rindas spēlē ielikt nevarēja. 6. novembrī Steam atjauninājums bija pabeigts un pirmsievietošanas pārbaude izdevās, tomēr iepriekšējais process pēc darba beigām joprojām turēja sev rezervētas tiesības rakstīt datubāzē. Pārbaude pati failus nemainīja. Atsākot darbu, jāpārbauda iepriekšējā procesa stāvoklis, kandidāta un rezerves kopijas atbilstība un jāturpina no pirmā nepabeigtā soļa.

**Atkārtota teksta apstrāde.** 8. novembra auditā četru ar API pieslēgtu redaktoru pēdējo 24 stundu darbā bija 5 650 atskaites ar pakalpojuma sniedzēja tokeniem, kopā 94 683 901 tokeni. Divu posmu plūsma rediģēja un atkārtoti pārbaudīja jau esošus melnrakstus. Audits nenoteica rēķina summu vai izmaksas uz vienu pieņemtu rindu. Tā kā bija saglabātas sākotnējās atbildes, izdevās atgūt 2 093 citur neatrastos tekstus. Citā projektā, redakcijas rindai augot, var apturēt jaunus pieprasījumus, atgūt saglabātās atbildes un atvēlēt turpmāko budžetu konkrētiem neatrisinātiem ierakstiem.

## Kur kļūdījās tulkojumā

Viena lokālā melnraksta variants frāzei “You're right” bija “Tu esi taisnīgs”. Tā latviski raksturo taisnīgu cilvēku. Ja runātājs piekrīt otra teiktajam, doma ir “Tev taisnība”. Citā melnrakstā “maniac” bija pārvērties par “atraitis”. Šādas kļūdas var izturēt gan JSON, gan XML formāta pārbaudi. Tāpēc redakcijā lasīja pilnu oriģinālu kopā ar tulkojumu, pierakstīja, kura nozīme bija pārprasta, un laboto piemēru ar atsauci uz konkrēto avotu izmantoja nākamajā pakā.

Piederība vienai spēles resursu grupai dažreiz palīdzēja saprast domu, bet ID secība nepateica, kurš runā un kura replika seko nākamā. Uzskaitē bija teksta identifikators bez droši zināma runātāja vai ainas. Neskaidros gadījumus atlika atsevišķi, līdzās pierakstot jautājumu redaktoram. Nelielā izmēģinājumā tiem pašiem 24 avotiem salīdzināja instrukciju ar visiem piemēriem un īsāku, atlasītu piemēru kopu. Abos variantos palika būtiskas nozīmes un valodas kļūdas. Atšķīrās arī pieprasījumu secība un kešatmiņas izmantojums, tāpēc no šī mēģinājuma nevarēja secināt, ka īsāka instrukcija paātrinās darbu visā projektā.

## Kā spēlē nonāca pēdējie 7 049 ieraksti

Vispirms atguva 1 348 agrāk izrediģētus ierakstus. Pārējiem 5 701 pārbaudīja jaunākos redakcijas lēmumus 104 pakās. Redaktori 377 formulējumiem apzināti saglabāja oriģinālrakstību, tostarp taustiņu nosaukumiem, zīmoliem un tēlu replikām svešvalodā. Noteikums vēlreiz tulkot ikvienu ierakstu, kurš sakrīt ar avotu, būtu atsācis jau pabeigtu darbu.

Laidienu vienlaikus ierakstīja viens izpildītājs. Tas pārbaudīja sagatavoto tekstu, sagatavoja importu, izmēģināja to datubāzes kopijā, ievietoja apstiprināto tekstu darba datubāzē, izveidoja XML, pārbaudīja mērķa instalāciju un ievietoja failu spēlē. Pēc tam instalēto XML atvēra vēlreiz un salīdzināja visus ID un tekstus. Visiem 246 024 ierakstiem, kas spēlē atradās pirms šī darba, formulējumi saglabājās. Pēc tam 29 jaunpievienotajos tekstos precizēja formulējumu, tāpēc kopējais ierakstu skaits nemainījās.

Citai spēlei tajā pašā laika intervālā pieraksti, cik melnrakstu pabeigti, cik tekstiem pieņemta gala redakcija un cik jaunu ID pārbaudīti tieši spēles failā. Pievieno redzamo avota rakstzīmju skaitu un pagājušo laiku. Jau ievietota teksta labojumus, apzināti saglabāto oriģinālrakstību un neatbildētos jautājumus uzskaiti atsevišķi. Tad darba turpinātājs redzēs, vai vajadzīgs tulkojums, redaktora lēmums vai jau gatava faila ievietošana.

## Ko redzēja spēlētājs

Reinis 11. novembrī iemūžināja spēles versiju 1491.50 septiņos ekrānattēlos. Pauzes izvēlnē redzami „Karte” un „Iestatījumi”, vadības sadaļā „Taustiņu piesaiste”. Jāšanas norādē pie teksta ir īstā taustiņa simbols. Ievada ainās latviski redzami dialoga subtitri un veidotāju amatu nosaukumi. Nodaļas nosaukuma tulkojums parādās zem oriģinālā grafiskā uzraksta.

Trīs kadrus var piesaistīt precīziem publiskā XML ierakstiem. „Bet mēs zaudējām dažus cilvēkus.” ir `0xFCD0E439`. Jāšanas pamācība ar īsu taustiņa spiedienu ir `0x9D9BAF33`. Vadības izvēlnes skaidrojums „Pielāgo tastatūras un peles taustiņu piesaistes.” ir `0x94B26056`. Tas ļauj redaktoram atrast konkrētu formulējumu nākamajam labojumam. Misijas mērķi, spēlēšanas laikā dzirdēta dialoga subtitrus un darbību sarakstu atvērtā taustiņu piesaistes izvēlnē var pārbaudīt atsevišķi. [Spēles pārbaudes pamācība](INSTALL-AI-lv.md)

### Pārbaudes avoti

Skaitļi ņemti no projekta 28. oktobra instalācijas stāvokļa pārbaudes, 31. oktobra 9. un 10. cikla kontrolpunktiem un plkst. 23.35 atskaites, 2. novembra diennakts atskaites, 6. novembra instalācijas audita, 8. novembra apturēšanas un atkopšanas audita un tam sekojošā laidiena atskaites, abām tabulā minētajām novembra stāvokļa pārbaudēm un 10. novembra gala instalācijas un labojumu pārbaudēm. Redakcijas datubāzes salīdzināšanu veica projekta datorā. Ikviens var patstāvīgi pārskaitīt publiskā XML unikālos ID un pārbaudīt faila SHA-256. Atverot 11. novembra laidiena ZIP un nolasot XML, atkārtoti apstiprinājām šo kontrolsummu un visus 253 073 unikālos ID.

`c72337da664b3999ca4fc2de2600c1e79c551b29fa1e69d79d1330485aef5045`

[Lejupielādēt tulkojumu](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip) · [Atbalstīt Reini](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/#ways) · [Iepazīt Reini Facebook](https://www.facebook.com/reinis.runcis)

<p align="right"><img src="../assets/REYRUN.png" alt="REYRUN" width="64"></p>
