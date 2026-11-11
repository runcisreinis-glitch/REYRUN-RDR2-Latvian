# Kā pārbaudīt spēles tulkojumu ainā, izvēlnē un otrā dzinējā

[English](ADVANCED-en.md) · [Pirmie pieci piemēri](GUIDE-lv.md)

Sāc ar vienu ainu, kuru vari atkārtoti atvērt. Saglabā spēles versiju, saglabājuma vietu, runātāju, sarunas biedru, spēlētāja iepriekšējo izvēli un teksta atslēgu. Zemāk rādītā Godot mācību spēle ir atsevišķs, brīvi izmantojams piemērs. RDR2 piemēri ņemti no publiskā REYRUN tulkojuma.

## Kad viena angļu rinda nozīmē divas dažādas lietas

Inventārā **Open** uz konteinera atvēršanas pogas ir **Atvērt**. Tas pats vārds blakus lauka nosaukumam **Konteiners** var būt stāvoklis **Atvērts**. Ja blakus rakstīts **Lāde**, vajag sieviešu dzimti **Atvērta**. Saglabā atšķirīgās atslēgas un pievieno lietvārdu pie katra stāvokļa. Tulkošanas atmiņā šo izvēli sasaisti ar funkciju un kontekstu.

| Materiāls | Ko noskaidrot pirms tulkošanas | Kā redaktors pārbauda rezultātu |
| --- | --- | --- |
| Saruna ar izvēlēm | Runātājs, adresāts, aina, atzars, iepriekšējā un nākamā replika tajā pašā atzarā. Norādi, no kurienes tas zināms. | Izspēlē abas atbildes. Vai pēc atteikuma tēls joprojām izsaka atteikumu? Vai “tu” un “jūs” atbilst attiecībām? |
| Uzdevuma mērķis | Kurš ko dara, kam seko vai ko nes, kur, līdz kuram brīdim. Atrodi sākuma, progresa, sekmīgas pabeigšanas un neveiksmes rindas. | Izpildi vienu soli, atver žurnālu un salīdzini ar uzrakstu spēles skatā. Pārbaudi, vai darbība un mērķis atbilst abās vietās. |
| Taustiņa norāde | Vai taustiņš jānospiež vienreiz, atkārtoti, jāpatur vai jāatlaiž. Nosaki, ko zīmes vietā uzzīmē spēle. | Atkārto to pašu ainu ar noklusēto un pārsieto taustiņu. Izmēģini arī vadības pulti, ja spēle to atbalsta. |
| Dialogs ar noteiktu ilgumu | Precīzs laiks, kurā teksts redzams. Piefiksē pārtraukumu, runātāja maiņu, divas balsis vienlaikus vai tekstu attēlā. | Noskaties ar sākotnējo balsi un vēlreiz ar izslēgtu skaņu. Pārbaudi, vai līdz nākamajai replikai var nolasīt domu un saprast runātāju. |

Ja paredzamā secība nav atrodama scenārijā, dialoga datos vai ierakstā, sagatavo jautājumu konkrētajai rindai. Piemēram, **“Vai spēlētājs ar šo pogu atver lādi, vai logs rāda lādes pašreizējo stāvokli?”** Turpini ar rindām, kuru nozīme ir zināma. Spēļu lokalizācijas nozares rokasgrāmata sniedz plašāku kontekstu. [IGDA Localization SIG](https://igda.org/resources-archive/best-practices-for-game-localization/)

## Kas jāatstāj spēlei

Šos trīs ierakstus var atrast 2026. gada 11. novembra failā `Latvian Translation.xml`. Atver XML teksta redaktorā un meklē norādīto ID. [Lejupielādēt REYRUN tulkojumu](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip)

| XML identifikators | Precīzs teksts failā | Ko var pārbaudīt |
| --- | --- | --- |
| `0x9D9BAF33` | `Īsi spiediet ~INPUT_HORSE_SPRINT\|PromptId=INPUT_WNT1_SPEEDUP~, lai jātu ātrāk` | Saglabā visu marķieri, ieskaitot daļu aiz vertikālās svītras. Spēle norādes vidū rāda taustiņa zīmi. |
| `0x046E5281` | `Turiet ~INPUT_HORSE_SPRINT\|PromptId=INPUT_WNT1_SPEEDUP~, lai jātu ātrāk` | Marķieris ir tas pats, bet darbība atšķiras. Kopējot gatavu tulkojumu, šīs divas rindas viegli sajaukt. |
| `0x1C4EF867` | `Seko ~o~Dačam~s~` | Saglabā mērķa nosaukuma izcēluma robežas. Atrodi personvārdu vajadzīgajā locījumā. Šis ir viens no vairākiem ID ar tādu pašu tekstu. |

Pārbaudot ar tastatūru, pieraksti sākotnējo piesaisti un atver ainu. Pārsien darbību uz kādu brīvu taustiņu, vēlreiz atver norādi un nospied jauno taustiņu. Salīdzini **vadības izvēlni → zīmi norādē → faktisko darbību**. Beigās atjauno sākotnējo piesaisti. Veic to pašu pārbaudi katrai atbalstītajai ievades ierīcei, par kuru publicē pārbaudes rezultātu. [Microsoft XAG 107](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107)

## Subtitri un burti, kurus patiešām var izlasīt

Izvēlies ainu ar īsu izsaucienu, garu atbildi un citu runātāju ārpus kadra. Saglabā sākuma un beigu laiku, redzamo tekstu un rindas lūzumu. Lai atlasītu saspringtas vietas, sadali redzamo rakstzīmju skaitu ar sekundēm ekrānā. Piemēram, 42 rakstzīmes 2,1 sekundē dod 20 rakstzīmes sekundē. Šis skaitlis palīdz izvēlēties, ko skatīties vispirms. Pieņemšanas lēmumu pamato ar atskaņošanu reālā ātrumā, fonta izmēru un spēles skatu. Ja maina tikai teksta failu, saīsini liekvārdību, saglabājot noliegumu, adresātu, mērķi un nosacījumu.

Pārbaudi mazāko atbalstīto logu, parasto spēles izšķirtspēju un lielāko pieejamo subtitru izmēru. Vai darbības mērķis, izvēles atbildes vai spēles padoms aizsedz subtitrus? Ja titrēts uzraksts ir daļa no grafikas, pieraksti abus slāņus atsevišķi. Piemēram, RDR2 nodaļas sākumā oriģinālā **Colter** kartīte ekrānā paliek līdzās latviešu parakstam **1. nodaļa: Kolters**. Projektā ar pieejamiem skaņu parakstiem pārbaudi arī to laiku un norādi par skaņas avotu. [Microsoft XAG 104](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104)

Izmēģinājuma būvē ieslēdz pseidolokalizāciju. Tā īslaicīgi pārveido vai pagarina tekstu un palīdz atrast nepārtulkotas saskarnes vietas, nogrieztas beigas un pārāk šauras pogas. Tad uzliec īsto latviešu tekstu. Katrā lietotajā fontā un stilā pārbaudi **ĀČĒĢĪĶĻŅŠŪŽ āčēģīķļņšūž**. Sevišķi apskati lielos burtus izvēlnēs, kursīvu, vairāku rindu aprakstus un dinamiskus personvārdus. Ja burta vietā ir kvadrāts, noskaidro, kurš fonts vai glifu atlants apkalpo attiecīgo ekrānu. Eksportēto rakstzīmju sarakstu papildini ar burtiem, kas ienāk no mainīgajiem, un atkārto tieši to pašu ainu. [Godot pseidolokalizācija](https://docs.godotengine.org/en/latest/tutorials/i18n/pseudolocalization.html) · [Unity rakstzīmju kopas](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/StringTables.html)

## Izmēģini divus kontekstus un trīs skaitļa formas Godot

Mapē `examples/godot-lv` ir mazs projekts ar pārbaudi un īstu gettext PO katalogu. Tajā **Open** atveidots divējādi. Veseliem skaitļiem katalogā ir trīs formas, piemēram, **1 diennakts**, **2 diennaktis**, **11 diennakšu** un **21 diennakts**. Piemēra PO galvenē precīzi noteikts, kura forma atbilst kuram indeksam. Citā katalogā pārbaudi tā galveni. Daļskaitļiem ir papildu nosacījumi, un atsevišķi jāpārbauda izmantotais formatētājs. [Unicode CLDR latviešu skaitļa formas](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html#lv) · [Godot gettext katalogi](https://docs.godotengine.org/en/stable/tutorials/i18n/localization_using_gettext.html)

Ar Godot 4.6.3, atrodoties prasmes galvenajā mapē, ievadi abas komandas. Ja Godot izpildfails nav sistēmas programmu ceļā, `godot` vietā norādi pilnu ceļu uz to. Tiek izmantots mācību projekts un tā vietējā importa kešatmiņa.

```sh
godot --headless --path examples/godot-lv --import
godot --headless --path examples/godot-lv --script res://check.gd
```

Pārbaudītais iznākums ir **2 contexts, 12 integer counts, 0 failures**. Lai ieraudzītu kļūdu, nokopē piemēru jaunā mapē. Kopijas failā `lv.po` nomaini darbības tulkojumu `Atvērt` pret `Vaļā`. Atkārto abas komandas ar kopijas ceļu. Pārbaude norāda `inventory/action` un atgriež izejas kodu 1. Tā var atklāt sajauktu pogas nozīmi, lai arī PO fails joprojām importējas. Lai pārbaudītu burtu faktisko izskatu, vēl jāatver konkrētās spēles grafiskais skats.

## Kā pārcelt pārbaudi uz savu projektu

| Projekts | Pirmais imports | Kas jāredz pašā spēlē |
| --- | --- | --- |
| Godot ar projekta failiem | Pievieno `lv.po` pie tulkojumiem. Sasaisti `tr()` izsaukuma kontekstu ar `msgctxt`. Izmanto `tr_n()` tur, kur spēlei ir skaitlis. | Pārslēdz valodu uz `lv`, atver abas viena vārda lietojuma vietas un mūsu piemēra skaitļus. |
| Unity ar Localization pakotni | Izmanto projekta esošo String Table Collection. Saglabā dalīto atslēgu identitāti un attiecīgās lokāles tabulu. Noskaidro, kurām rindām ieslēgts Smart String. Izmēģini vienu reālu mainīgo. | Pārbaudi saskarni divos izmēros un izmēģini mainīgu skaitli. Ja skaitļa vietā redzi iekavas vai pietrūkst glifa, pārbaudi formatētāju, tabulu un attiecīgo fontu. [Unity String Tables](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/StringTables.html) |
| Unreal ar projekta failiem | Localization Dashboard izvēlies pareizo mērķi un tā valodas. Lieto Gather → Export → Import → Compile. Dialogue Wave datos atšķir runātāju, adresātu un iespējamo atsevišķo subtitru tekstu. | Pārbaudi gan variantu, kur runātājs uzrunā vienu personu, gan citu pieejamo atzaru. Atver spēles būvējumu ar nokompilēto mērķi. [Epic lokalizācijas rīki](https://dev.epicgames.com/documentation/en-us/unreal-engine/localization-tools-in-unreal-engine) · [Epic dialoga resursi](https://dev.epicgames.com/documentation/unreal-engine/asset-localization-in-unreal-engine) |
| Izlaista spēle, kurai ir dokumentēts tulkojumu spraudnis | Atrodi konkrētās spēles un versijas atbalstīto importētāju. Dublē izmēģinājuma mērķfailu, ievieto dažas ar ID sasaistītas rindas, atkārtoti nolasi rezultātu. | Palaid vienu reproducējamu ainu un pārbaudi tās atslēgas. RDR2 XML shēma un failu nosaukumi attiecas uz konkrēto spraudni. |

Pēc atjauninājuma vienādos ID salīdzini pēc avota teksta un konteksta. Pārskatīšanai atlasi jaunās, mainītās un citā kontekstā lietotās rindas. Saglabā arī izņemtos ID vecā laidiena vēsturē. Vispirms atkārto pārbaudi skartajā ainā un ar tai piesaistītajiem mainīgajiem. Pabeigšanas pierakstā ieraksti **būvējums · valoda · resurss un ID · aina vai saglabājums · iestatījumi · gaidītais · redzētais · attēls vai video laiks**. Komandas izpildi, glifu pārbaudi un konkrētas ainas izspēli atzīmē atsevišķi.

[Atgriezties pie prasmes](../SKILL.md) · [Reinis un iespēja atbalstīt darbu](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/#ways)
