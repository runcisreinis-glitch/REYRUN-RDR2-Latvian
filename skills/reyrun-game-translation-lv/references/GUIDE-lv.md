# Kā ar REYRUN metodi iztulkot spēli latviski

<img src="../assets/REYRUN.png" alt="REYRUN" width="56">

Ja vēlies spēlēt *Red Dead Redemption 2* latviski, gatavais tulkojums un uzstādīšanas instrukcija ir [projekta mājaslapā](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/). Ja pats gribi tulkot vai rediģēt citas spēles tekstu, saglabā visu mapi `reyrun-game-translation-lv`. Tajā ir darba apraksts, pieci mācību piemēri un pārbaudes rīki.

Ja pirmais mēģinājums izdodas, turpini ar [sarežģītāku spēļu tekstu pārbaudēm](ADVANCED-lv.md). Īstus piemērus par pazudušu darbu atgūšanu un to, kur gaidīja jau izrediģētās rindas, atradīsi [RDR2 projekta pieredzes aprakstā](https://github.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/blob/main/docs/RETROSPECTIVE-lv.md).

## Kā sākt vienam vai kopā ar MI

Parastā sarunā pievieno savam MI asistentam `SKILL.md`, šo instrukciju un nelielu avota teksta failu. Ja tavs asistents prot ielādēt prasmes no mapes, iekopē **visu mapi** vietā, kur tavs asistents meklē prasmes. Atjauno prasmju sarakstu un izvēlies `reyrun-game-translation-lv`. Atstāj failus to vietās, lai atvērtos prasmes aprakstā norādītās saites. Tulkojumus var rakstīt arī pats, rediģējot JSONL failus. Pārbaudes veic Python. Vingrinājumam nav vajadzīgs maksas konts.

Pirmajam mēģinājumam pievieno `examples/source.jsonl` un uzraksti asistentam šādu lūgumu:

> Izlasi SKILL.md. Iztulko visus piecus ierakstus latviski. Saglabā visus sākotnējos laukus. Katrai rindai pievieno target, decision un reason. Ja nozīme nav skaidra, atzīmē hold un uzraksti, kas tieši jānoskaidro. Katru ierakstu atgriez atsevišķā rindā kā JSON objektu bez ievada un pēcvārda. Pirms ievietošanas spēlē es tulkojumu pārskatīšu.

Saglabā atbildi UTF-8 kodējumā ar nosaukumu `my-edits.jsonl`. Salīdzini to ar `examples/edited.jsonl`. Vienai replikai var būt vairāki labi tulkojumi. Skaties, vai darbība un tās tonis ir saglabāts, vai pogas kods atrodas pie īstās darbības un vai asistents ir pamanījis neskaidro vārdu.

## Izmēģini vienu partiju

Atver termināli prasmes mapē. Vajadzīgs Python 3.8 vai jaunāks. Dažās Windows instalācijās komandas `python` vietā jālieto `py -3`.

```sh
python scripts/localization_tools.py prepare examples/source.jsonl --output demo-packets --max-rows 2
python scripts/localization_tools.py validate --inputs examples/source.jsonl --edited examples/edited.jsonl --report demo-qa.json
python -B -m unittest discover -s scripts -p "test_*.py"
```

Pirmā komanda izveido trīs pakas. Divās ir pa diviem ierakstiem, trešajā ir viens. Otrā komanda atrod piecus avota ID. Četriem tulkotājs norādījis `ready`, vienam ir `hold`. Rezultātu tabulas rinda sastāv tikai no mainīgajiem un atdalītājiem. Tā paliek tāda pati, tāpēc brīdinājums par sakritību ir pamatots. Atkārto pārbaudi ar savu `my-edits.jsonl` un izvēlies jaunu atskaites nosaukumu. Lai apskatītu kļūdas paziņojumu, testa kopijā izdzēs `~INPUT_INTERACT~` **tikai no tulkojuma**. Rīks nosauks attiecīgo ierakstu un beigs darbu ar kodu 2. Katram mēģinājumam izmanto jaunu izvades mapi vai atskaites nosaukumu, lai saglabātos iepriekšējais rezultāts.

## Sagatavo savas spēles tekstu

Eksportē tekstu ar konkrētās spēles rīku. Saglabā oriģinālfailu, spēles būvējuma numuru, resursa nosaukumu un spēlē izmantoto atslēgu. Vienlaikus apstrādā viena būvējuma resursus, kuros atslēgas ir unikālas. Ja divas resursu grupas izmanto tās pašas atslēgas, pārbaudi grupas atsevišķi. Ievades formāts var būt UTF-8 JSON masīvs vai JSONL ar vienu objektu rindā. Avota kontrolsummu aprēķina no visas atkodētās teksta virknes UTF-8 baitiem, nepievienojot jaunu rindu. Python izteiksme ir `hashlib.sha256(source.encode("utf-8")).hexdigest()`.

| Lauks | Ko tajā ievada |
| --- | --- |
| `id`, `native_id` | Nemainīgu, unikālu darba ieraksta ID un, ja tā zināma, spēles izmantoto atslēgu. Citā spēles versijā rindu secība var mainīties. |
| `source`, `source_sha` | Pilnu avota tekstu ar kodiem, atstarpēm un rindu pārnesumiem, kā arī tā kontrolsummu. |
| `candidate` | Iepriekšējo melnrakstu. Ja tāda vēl nav, ievadi tukšu teksta virkni. |
| `context`, `context_id`, `speaker`, `scene_id`, `branch_id` | Pārbaudītu informāciju par runātāju, ainu un spēlētājam redzamo. Nezināmos laukus izlaid. Secīgi ID vien vēl nepierāda, ka replikas izskan viena pēc otras. |
| `target`, `decision`, `reason` | Latvisko formulējumu, lēmumu un vajadzības gadījumā jautājumu vai pamatojumu. Šos laukus pievieno rediģētajā kopijā. |

Ja tulko vairāki cilvēki vai asistenti, katram piešķir savus ID. Visiem iedod vienu un to pašu apstiprināto tēlu vārdu, vietvārdu un atkārtoto terminu saraksta versiju. Piemēros parādi arī locītās formas. Ja divi tēli kādā ainā pāriet no „jūs” uz „tu”, tēlu piezīmēs norādi šo ainu.

## Rediģē nozīmi un tēla balsi

Šīs frāzes rakstītas mācībām. Tās nav citāti no *Red Dead Redemption 2*.

| Avots un situācija | Iespējamais tulkojums | Ko pārbauda redaktors |
| --- | --- | --- |
| “Resume” pauzes izvēlnē | **Turpināt** | Īss darbības nosaukums, kas ietilpst uz pogas. |
| “Hold `~INPUT_INTERACT~` to open the gate.” | **Turi nospiestu `~INPUT_INTERACT~`, lai atvērtu vārtus.** | Poga jātur nospiesta. Vienreizējs spiediens būtu cita darbība. |
| “I... I didn't take it.” Satraukts liecinieks | **Es… Es to nepaņēmu.** | Saglabā gan vilcināšanos, gan noliegumu. Izrunā repliku balsī. |
| “Can you wait here?” Bērns uzrunā draugu vai darbinieks pieklājīgi uzrunā svešinieku | **Vari te pagaidīt?** / **Vai jūs varētu te pagaidīt?** | Uzrunu nosaka sarunas biedru attiecības. |
| “Charges: {count}” priekšmeta aprakstā ar mainīgu skaitli | **Lādiņu skaits: {count}** | Ja spēle piedāvā vienu teksta lauku, šāds uzraksts der dažādiem skaitļiem. Ja spēlē ir atsevišķas daudzskaitļa formas, iztulko un izmēģini tās ar attiecīgajiem skaitļiem. |
| “Seal” bez ainas vai priekšmeta apraksta | **hold** | Vai runa ir par roni, zīmogu vai aicinājumu kaut ko noslēgt? Atrodi atbildi spēles resursā vai attēlā. |

Pirms apstiprināšanas divreiz izlasi katru pilno avota un tulkojuma pāri. Pirmajā reizē pārbaudi, kurš ko izdarīja, kam tas bija domāts, ko maina noliegums vai nosacījums. Otrajā klausies, vai šis tēls tā teiktu. Pārbaudi locījumus, subtitru garumu un pogu uzrakstus. Vārdnīcā var pārbaudīt vārda formu. Pareizo nozīmi bieži atklāj tikai aina. Saglabā apstiprināto tekstu kopā ar redakcijas pierakstu. Ja tekstu vēlāk pārveido, pārlasi laboto versiju.

## Pārbaudi laidienu un saglabā vietu, no kuras turpināt

Rīks pārbauda avota kontrolsummas, unikālus ID, trūkstošus ierakstus, zināmos konteksta laukus un tukšus tulkojumus ar atzīmi `ready`. Tas salīdzina RDR vadības kodus starp tildēm un to secību, vienkāršus vietturus figūriekavās un biežākos printf formātus. Numurētus printf argumentus var pārvietot atbilstoši latviešu vārdu secībai. Ja argumenti nav numurēti, jāsaglabā to tipu secība. Divi vienādi `%s` joprojām var samainīties nozīmēm, tāpēc redaktoram jāpārbauda, kur ievietojas katra vērtība. Rindu pārnesumu skaita izmaiņas rada brīdinājumu. ICU ziņojumiem ar vairākos līmeņos ievietotiem nosacījumiem, HTML, fontu komandām vai citiem spēlei raksturīgiem kodiem pievieno attiecīgā formāta pārbaudi.

Ar `tm-index` un `tm-suggest` var iegūt ieteikumus no iepriekš apstiprinātiem tulkojumiem. Meklēšanas atslēgā ietilpst spēle, valoda, avota kontrolsumma, konteksta ID un konteksta, redakcijas noteikumu un terminu saraksta versijas. Pievieno redakcijas apliecinājumu un kontrolsummas gan apstiprinātajam tekstam, gan apliecinājuma failam. Ja norādi relatīvu faila ceļu, abas komandas palaid no vienas darba mapes. Ja vienai atslēgai saglabāti dažādi apstiprināti tulkojumi, rīks tos parāda konfliktu sarakstā. Pieejamās komandas parāda `python scripts/localization_tools.py --help`.

Palaid abas komandas prasmes mapē. Pievienotais redakcijas pieraksts attiecas uz pauzes izvēlnes pogu „Turpināt”. Ar tādu pašu konteksta versiju rīks atrod vienu ieteikumu.

```sh
python scripts/localization_tools.py tm-index examples/tm-approved.jsonl --output demo-tm.json
python scripts/localization_tools.py tm-suggest examples/tm-query.jsonl --index demo-tm.json --output demo-suggestions.json
```

Laidienu būvē ar konkrētajai spēlei paredzētu rīku. Tehniskos izņēmumus un neatrisinātos jautājumus reģistrē atsevišķi. Saglabā iepriekšējo failu ārpus spēles mapes. Vienam izpildītājam uztici pārbaudīt būvējumu un ierakstīt apstiprināto laidienu. RDR2 StringTable formāta XML vari pārbaudīt ar šo komandu. Aizstāj piemēra ceļus ar savējiem. Tā salīdzina visu tabulu pēc spēles skaitliskajām atslēgām un precīza atkodētā teksta, kā arī parāda abu failu kontrolsummas. Ierakstu secība vai XML pieraksts var atšķirties arī tad, ja atslēgas un teksti sakrīt.

```sh
python scripts/compare_xml.py "reviewed/Latvian Translation.xml" "installed/Latvian Translation.xml"
```

Atver spēli atbilstošajā režīmā. Apskati izvēlni, ierobežota ilguma dialoga subtitrus, garu priekšmeta nosaukumu un mainīgo ar vairākām vērtībām. Pārbaudi burtus **ā, č, ē, ģ, ī, ķ, ļ, ņ, š, ū, ž**. Par kļūdu pieraksti būvējumu, zināmo ID, avota rindu, pašreizējo tulkojumu un ainu. Pievieno ekrānattēlu. Saglabā iepriekšējo laidienu, lai vajadzības gadījumā varētu to atjaunot.

Katras partijas beigās pieraksti pēdējā uzstādītā faila kontrolsummu, apstiprinātā teksta versiju un ID, kuriem vēl jānoskaidro konteksts. Vienā un tajā pašā laika posmā skaiti gan uzstādītos jaunos ID, gan to avota teksta rakstzīmes. Tulkošanas, rediģēšanas, eksportēšanas un gaidīšanas laiku uzskaiti atsevišķi. Atsākot darbu, salīdzini pēdējo atskaiti ar failu spēles mapē un tikai tad izdali nākamo partiju.

[English](GUIDE-en.md) · [Par Reini un brīvprātīga atbalsta veidiem](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/#ways) · [Raksti Reinim Facebook](https://www.facebook.com/reinis.runcis)
