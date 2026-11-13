# Kā ar REYRUN metodi iztulkot spēli latviski

![REYRUN](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/assets/reyrun.png)

Ja vēlaties spēlēt *Red Dead Redemption 2* latviski, gatavais tulkojums un uzstādīšanas instrukcija ir [projekta mājaslapā](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/). Ja vēlaties tulkot vai rediģēt citas spēles tekstu, saglabājiet visu mapi `reyrun-game-translation-lv`. Tajā ir darba apraksts, pieci mācību piemēri un pārbaudes rīki.

Ja pirmais mēģinājums izdodas, turpiniet ar [sarežģītāku spēļu tekstu pārbaudēm](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/metode/panemieni/). Īstus piemērus par pazudušu darbu atgūšanu un to, kur gaidīja jau izrediģētās rindas, atradīsiet [RDR2 projekta pieredzes aprakstā](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/metode/pieredze/).

## Kā sākt patstāvīgi vai kopā ar MI

Čatā pievienojiet savam MI asistentam `SKILL.md`, šo instrukciju un nelielu avota teksta failu. Ja jūsu asistents prot ielādēt prasmes no mapes, iekopējiet **visu mapi** vietā, kur jūsu asistents meklē prasmes. Atjaunojiet prasmju sarakstu un izvēlieties `reyrun-game-translation-lv`. Atstājiet failus to vietās, lai atvērtos prasmes aprakstā norādītās saites. Tulkojumus varat rakstīt arī paši, rediģējot JSONL failus. Failus pārbauda Python programma. Vingrinājumam nav vajadzīgs maksas konts.

Pirmajam mēģinājumam pievienojiet `examples/source.jsonl` un uzrakstiet asistentam šādu lūgumu:

> Izlasi SKILL.md. Iztulko visus piecus ierakstus latviski. Saglabā visus sākotnējos laukus. Katrai rindai pievieno target, decision un reason. Ja nozīme nav skaidra, atzīmē hold un uzraksti, kas tieši jānoskaidro. Katru ierakstu atgriez atsevišķā rindā kā JSON objektu bez ievada un pēcvārda. Pirms ievietošanas spēlē es tulkojumu pārskatīšu.

Saglabājiet atbildi UTF-8 kodējumā ar nosaukumu `my-edits.jsonl`. Salīdziniet to ar `examples/edited.jsonl`. Vienai replikai var būt vairāki labi tulkojumi. Skatieties, vai darbība un tās tonis ir saglabāts, vai pogas kods atrodas pie īstās darbības un vai asistents ir pamanījis neskaidro vārdu.

## Izmēģiniet piecas spēles teksta rindas

Atveriet termināli prasmes mapē. Vajadzīgs Python 3.8 vai jaunāks. Dažās Windows instalācijās komandas `python` vietā jālieto `py -3`.

    python scripts/localization_tools.py prepare examples/source.jsonl --output demo-packets --max-rows 2
    python scripts/localization_tools.py validate --inputs examples/source.jsonl --edited examples/edited.jsonl --report demo-qa.json
    python -B -m unittest discover -s scripts -p "test_*.py"

Pirmā komanda sagatavo trīs pakas. Divās ir pa diviem ierakstiem, trešajā ir viens. Otrā komanda atrod piecus avota ID. Četriem tulkotājs norādījis `ready`, vienam ir `hold`. Rezultātu tabulas rinda sastāv tikai no mainīgajiem un atdalītājiem. Tā paliek tāda pati, tāpēc brīdinājums par sakritību ir pamatots. Atkārtojiet pārbaudi ar savu `my-edits.jsonl` un izvēlieties jaunu atskaites nosaukumu. Lai apskatītu kļūdas paziņojumu, testa kopijā izdzēsiet `~INPUT_INTERACT~` **tikai no tulkojuma**. Rīks nosauks attiecīgo ierakstu un beigs darbu ar kodu 2. Katram mēģinājumam izmantojiet jaunu izvades mapi vai atskaites nosaukumu, lai saglabātos iepriekšējais rezultāts.

## Sagatavojiet savas spēles tekstu

Eksportējiet tekstu ar konkrētās spēles rīku. Saglabājiet oriģinālfailu, spēles būvējuma numuru, resursa nosaukumu un spēlē izmantoto atslēgu. Vienlaikus apstrādājiet viena būvējuma resursus, kuros atslēgas ir unikālas. Ja divas resursu grupas izmanto tās pašas atslēgas, pārbaudiet grupas atsevišķi. Ievades formāts var būt UTF-8 JSON masīvs vai JSONL ar vienu objektu rindā. Avota kontrolsummu aprēķina no visas atkodētās teksta virknes UTF-8 baitiem, nepievienojot jaunu rindu. Python izteiksme ir `hashlib.sha256(source.encode("utf-8")).hexdigest()`.

| Lauks                                                       | Ko tajā ievada                                                                                                                                                 |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`, `native_id`                                           | Nemainīgu, unikālu darba ieraksta ID un, ja tā zināma, spēles izmantoto atslēgu. Citā spēles versijā rindu secība var mainīties.                               |
| `source`, `source_sha`                                      | Pilnu avota tekstu ar kodiem, atstarpēm un rindu pārnesumiem, kā arī tā kontrolsummu.                                                                          |
| `candidate`                                                 | Iepriekšējo melnrakstu. Ja tāda vēl nav, ievadiet tukšu teksta virkni.                                                                                         |
| `context`, `context_id`, `speaker`, `scene_id`, `branch_id` | Pārbaudītu informāciju par runātāju, ainu un spēlētājam redzamo. Nezināmos laukus izlaidiet. Secīgi ID vien vēl nepierāda, ka replikas izskan viena pēc otras. |
| `target`, `decision`, `reason`                              | Latvisko formulējumu, lēmumu un vajadzības gadījumā jautājumu vai pamatojumu. Šos laukus pievienojiet rediģētajā kopijā.                                       |

Ja tulko vairāki cilvēki vai asistenti, katram piešķiriet savus ID. Visiem iedodiet vienu un to pašu apstiprināto tēlu vārdu, vietvārdu un atkārtoto terminu saraksta versiju. Piemēros parādiet arī locītās formas. Ja divi tēli kādā ainā pāriet no „jūs” uz „tu”, tēlu piezīmēs norādiet šo ainu.

## Pārbaudiet, ko tēls saka un kā viņš runā

Šīs frāzes rakstītas mācībām. Tās nav citāti no *Red Dead Redemption 2*.

| Avots un situācija                                                                   | Iespējamais tulkojums                                      | Ko pārbauda redaktors                                                                                                                                                            |
|--------------------------------------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “Resume” pauzes izvēlnē                                                              | **Turpināt**                                               | Īss darbības nosaukums, kas ietilpst uz pogas.                                                                                                                                   |
| “Hold `~INPUT_INTERACT~` to open the gate.”                                          | **Turi nospiestu `~INPUT_INTERACT~`, lai atvērtu vārtus.** | Poga jātur nospiesta. Vienreizējs spiediens būtu cita darbība.                                                                                                                   |
| “I... I didn't take it.” Satraukts liecinieks                                        | **Es… Es to nepaņēmu.**                                    | Saglabājiet gan vilcināšanos, gan noliegumu. Izrunājiet repliku balsī.                                                                                                           |
| “Can you wait here?” Bērns uzrunā draugu vai darbinieks pieklājīgi uzrunā svešinieku | **Vari te pagaidīt?** / **Vai jūs varētu te pagaidīt?**    | Uzrunu nosaka sarunas biedru attiecības.                                                                                                                                         |
| “Charges: {count}” priekšmeta aprakstā ar mainīgu skaitli                            | **Lādiņu skaits: {count}**                                 | Ja spēle piedāvā vienu teksta lauku, šāds uzraksts der dažādiem skaitļiem. Ja spēlē ir atsevišķas daudzskaitļa formas, iztulkojiet un izmēģiniet tās ar attiecīgajiem skaitļiem. |
| “Seal” bez ainas vai priekšmeta apraksta                                             | **hold**                                                   | Vai runa ir par roni, zīmogu vai aicinājumu kaut ko noslēgt? Atrodiet atbildi spēles resursā vai attēlā.                                                                         |

Pirms apstiprināšanas divreiz izlasiet katru pilno avota un tulkojuma pāri. Pirmajā reizē pārbaudiet, kurš ko izdarīja, kam tas bija domāts, ko maina noliegums vai nosacījums. Otrajā ieklausieties, vai šis tēls tā teiktu. Pārbaudiet locījumus, subtitru garumu un pogu uzrakstus. Vārdnīcā var pārbaudīt vārda formu. Pareizo nozīmi bieži atklāj tikai aina. Saglabājiet apstiprināto tekstu kopā ar redakcijas pierakstu. Ja tekstu vēlāk pārveidojat, pārlasiet laboto versiju.

## Pārbaudiet spēles failu un pierakstiet, kur turpināt

Rīks pārbauda avota kontrolsummas, unikālus ID, trūkstošus ierakstus, zināmos konteksta laukus un tukšus tulkojumus ar atzīmi `ready`. Tas salīdzina RDR vadības kodus starp tildēm un to secību, vienkāršus vietturus figūriekavās un biežākos printf formātus. Numurētus printf argumentus var pārvietot atbilstoši latviešu vārdu secībai. Ja argumenti nav numurēti, jāsaglabā to tipu secība. Divi vienādi `%s` joprojām var samainīties nozīmēm, tāpēc redaktoram jāpārbauda, kur ievietojas katra vērtība. Rindu pārnesumu skaita izmaiņas rada brīdinājumu. ICU ziņojumiem ar vairākos līmeņos ievietotiem nosacījumiem, HTML, fontu komandām vai citiem spēlei raksturīgiem kodiem pievienojiet attiecīgā formāta pārbaudi.

Ar `tm-index` un `tm-suggest` var iegūt ieteikumus no iepriekš apstiprinātiem tulkojumiem. Meklēšanas atslēgā ietilpst spēle, valoda, avota kontrolsumma, konteksta ID un konteksta, redakcijas noteikumu un terminu saraksta versijas. Pievienojiet redakcijas apliecinājumu un kontrolsummas gan apstiprinātajam tekstam, gan apliecinājuma failam. Ja norādāt relatīvu faila ceļu, abas komandas palaidiet no vienas darba mapes. Ja vienai atslēgai saglabāti dažādi apstiprināti tulkojumi, rīks tos parāda konfliktu sarakstā. Pieejamās komandas parāda `python scripts/localization_tools.py --help`.

Palaidiet abas komandas prasmes mapē. Pievienotais redakcijas pieraksts attiecas uz pauzes izvēlnes pogu „Turpināt”. Ar tādu pašu konteksta versiju rīks atrod vienu ieteikumu.

    python scripts/localization_tools.py tm-index examples/tm-approved.jsonl --output demo-tm.json
    python scripts/localization_tools.py tm-suggest examples/tm-query.jsonl --index demo-tm.json --output demo-suggestions.json

Laidienu veidojiet ar konkrētajai spēlei paredzētu rīku. Tehniskos izņēmumus un neatrisinātos jautājumus reģistrējiet atsevišķi. Saglabājiet iepriekšējo failu ārpus spēles mapes. Vienam izpildītājam uzticiet pārbaudīt būvējumu un ierakstīt apstiprināto laidienu. RDR2 StringTable formāta XML varat pārbaudīt ar šo komandu. Aizstājiet piemēra ceļus ar savējiem. Tā salīdzina visu tabulu pēc spēles skaitliskajām atslēgām un precīza atkodētā teksta, kā arī parāda abu failu kontrolsummas. Ierakstu secība vai XML pieraksts var atšķirties arī tad, ja atslēgas un teksti sakrīt.

    python scripts/compare_xml.py "reviewed/Latvian Translation.xml" "installed/Latvian Translation.xml"

Atveriet spēli atbilstošajā režīmā. Apskatiet izvēlni, ierobežota ilguma dialoga subtitrus, garu priekšmeta nosaukumu un mainīgo ar vairākām vērtībām. Pārbaudiet burtus **ā, č, ē, ģ, ī, ķ, ļ, ņ, š, ū, ž**. Par kļūdu pierakstiet būvējumu, zināmo ID, avota rindu, pašreizējo tulkojumu un ainu. Pievienojiet ekrānattēlu. Saglabājiet iepriekšējo laidienu, lai vajadzības gadījumā varētu to atjaunot.

Katras partijas beigās pierakstiet pēdējā uzstādītā faila kontrolsummu, apstiprinātā teksta versiju un ID, kuriem vēl jānoskaidro konteksts. Vienā un tajā pašā laika posmā skaitiet gan uzstādītos jaunos ID, gan to avota teksta rakstzīmes. Tulkošanas, rediģēšanas, eksportēšanas un gaidīšanas laiku uzskaitiet atsevišķi. Atsākot darbu, salīdziniet pēdējo atskaiti ar failu spēles mapē un tikai tad izdaliet nākamo partiju.

[English](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/method/) · [Par Reini un brīvprātīga atbalsta veidiem](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/#ways) · [Rakstiet Reinim Facebook](https://www.facebook.com/reinis.runcis)
