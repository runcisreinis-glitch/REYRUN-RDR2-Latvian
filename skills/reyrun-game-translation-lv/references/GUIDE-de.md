# Mit REYRUN ein Spiel ins Lettische übersetzen

![REYRUN](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/assets/reyrun.png)

Die fertige lettische Übersetzung für Red Dead Redemption 2 und die Installationsanleitung finden Sie auf der [Projektseite](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/de/). Möchten Sie ein anderes Spiel übersetzen oder lektorieren, kopieren Sie den Ordner `reyrun-game-translation-lv`. Er enthält den Arbeitsablauf, fünf Übungsbeispiele und Prüfwerkzeuge für Ihren Rechner.

Anschließend können Sie [anspruchsvollere Texte im Spiel prüfen](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/de/method/techniques/). Im [Rückblick auf das RDR2-Projekt](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/de/method/retrospective/) lesen Sie anhand tatsächlicher Zahlen, wie wir ältere Entwürfe wiederfanden und ermittelten, welche überarbeiteten Texte noch auf den Einbau warteten.

## Allein oder mit einem KI-Assistenten beginnen

Hängen Sie im Chat `SKILL.md`, diese Anleitung und eine kleine Datei mit Originaltext an. Lädt Ihr Assistent Skills aus einem Verzeichnis, kopieren Sie den **gesamten Ordner** an den dafür eingerichteten Ort. Aktualisieren Sie die Liste und wählen Sie `reyrun-game-translation-lv`. Die relative Anordnung der Dateien muss erhalten bleiben, damit Verweise auf Anleitungen und Skripte funktionieren. Sie können die JSONL-Dateien auch von Hand übersetzen. Python prüft sie. Für die Übung brauchen Sie weder einen bestimmten KI-Dienst noch ein kostenpflichtiges Konto.

Hängen Sie für die erste Übung `examples/source.jsonl` an und bitten Sie Ihren Assistenten:

> Lies SKILL.md. Übersetze alle fünf vollständigen Einträge ins Lettische. Lass sämtliche Eingabefelder unverändert. Ergänze target, decision und reason. Kennzeichne unklare Zeilen mit hold und sag mir, welche Information zur Klärung fehlt. Gib pro Zeile genau ein JSON-Objekt ohne Einleitung oder Nachwort zurück. Vor dem Einbau prüfe ich die Übersetzung selbst.

Speichern Sie die Antwort als `my-edits.jsonl` in UTF-8 und vergleichen Sie die Entscheidungen mit `examples/edited.jsonl`. Mehrere Formulierungen können stimmen. Lesen Sie die Aussage des Zeugen laut. Prüfen Sie, welche Handlung verlangt wird, ob der Tastencode dazugehört und welche Zeile wegen fehlenden Kontexts zurückgestellt wurde.

## Fünf Zeilen ausprobieren

Öffnen Sie ein Terminal im Skill-Ordner. Sie benötigen Python ab 3.8. Unter Windows heißt der Aufruf mitunter `py -3` statt `python`.

    python scripts/localization_tools.py prepare examples/source.jsonl --output demo-packets --max-rows 2
    python scripts/localization_tools.py validate --inputs examples/source.jsonl --edited examples/edited.jsonl --report demo-qa.json
    python -B -m unittest discover -s scripts -p "test_*.py"

Der erste Befehl teilt fünf Einträge in Pakete mit 2, 2 und 1 Zeile. Der zweite meldet fünf Quell-IDs, davon vier ready und eine hold. Die unveränderte Punktezeile besteht nur aus Argumenten und Trennzeichen. Die Warnung ist daher zu erwarten. Prüfen Sie anschließend `my-edits.jsonl` mit einem neuen Berichtsnamen. Entfernen Sie in einer Testkopie `~INPUT_INTERACT~` **nur aus dem Zieltext**. Die Prüfung nennt die betroffene Zeile und endet mit Code 2. Wählen Sie für jeden Lauf einen neuen Ausgabepfad, damit frühere Ergebnisse erhalten bleiben.

## Die Texte aus Ihrem Spiel vorbereiten

Exportieren Sie den Text mit einem Werkzeug für das jeweilige Spiel. Bewahren Sie Originaldatei, Buildnummer, Ressourcennamen und Spielschlüssel auf. Bearbeiten Sie pro Durchgang einen Build und einen Bereich mit eindeutigen IDs. Werden IDs in mehreren Ressourcen wiederverwendet, prüfen Sie diese getrennt. Als Eingabe eignen sich ein UTF-8-JSON-Array oder JSONL mit einem Objekt pro Zeile. Der Quellhash ist der SHA-256-Wert der vollständig dekodierten Zeichenfolge in UTF-8 ohne zusätzlichen Zeilenumbruch, etwa `hashlib.sha256(source.encode("utf-8")).hexdigest()`.

| Feld                                                        | Inhalt                                                                                                                                                     |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`, `native_id`                                           | Eindeutige, dauerhafte Arbeits-ID und, sofern bekannt, der tatsächliche Spielschlüssel. Andere Versionen eines Sprachpakets können die Reihenfolge ändern. |
| `source`, `source_sha`                                      | Vollständiger Quelltext mit Codes, Leerraum und Zeilenumbrüchen sowie seine Prüfsumme.                                                                     |
| `candidate`                                                 | Vorhandener Entwurf. Gibt es keinen, verwenden Sie eine leere Zeichenfolge.                                                                                |
| `context`, `context_id`, `speaker`, `scene_id`, `branch_id` | Belegte Angaben zum Sprecher, zur Szene und zur Spieleransicht. Unbekannte Felder weglassen. Aufeinanderfolgende IDs beweisen keine Dialogreihenfolge.     |
| `target`, `decision`, `reason`                              | Lettische Fassung, Entscheidung und bei Bedarf Frage oder Begründung. Diese Felder gehören nur in die bearbeitete Kopie.                                   |

Teilen Sie die IDs auf die Bearbeiter auf. Für alle gilt dieselbe freigegebene Fassung der Namen, Ortsnamen und wiederkehrenden Begriffe. Geben Sie Verwendungsbeispiele mit gebeugten Formen. Wechselt ein Figurenpaar vom Sie zum Du, vermerken Sie die betreffende Szene.

## Inhalt und Sprechweise prüfen

Die folgenden Beispiele sind Übungssätze. Sie stammen nicht aus RDR2.

| Quelle und Situation                                                                      | Lettische Fassung                                        | Worauf die Redaktion achtet                                                                                                                                                 |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| „Resume“ im Pausenmenü                                                                    | **Turpināt**                                             | Kurze Handlungsbezeichnung, die auf die Taste passt.                                                                                                                        |
| “Hold `~INPUT_INTERACT~` to open the gate.”                                               | **Turi nospiestu ~INPUT_INTERACT~, lai atvērtu vārtus.** | Die Taste muss gedrückt bleiben. Einmaliges Drücken verlangt eine andere Handlung.                                                                                          |
| „I... I didn't take it.“ Ein nervöser Zeuge                                               | **Es… Es to nepaņēmu.**                                  | Zögern und Verneinung erhalten. Lesen Sie den ganzen Satz laut.                                                                                                             |
| „Can you wait here?“ Ein Kind fragt einen Freund, ein Angestellter höflich einen Fremden. | **Vari te pagaidīt?** / **Vai jūs varētu te pagaidīt?**  | Die Beziehung zwischen den Gesprächspartnern bestimmt die Anrede.                                                                                                           |
| „Charges: {count}“ bei einem Gegenstand mit variablem Zähler                              | **Lādiņu skaits: {count}**                               | Gibt es nur ein Textfeld, muss die Beschriftung für alle Zahlen passen. Unterstützt das Spiel eigene Pluralformen, übersetzen und testen Sie jede mit den passenden Zahlen. |
| „Seal“ ohne Angaben zu Szene oder Gegenstand                                              | **hold**                                                 | Ist ein Tier, ein Siegel oder die Aufforderung zum Verschließen gemeint? Prüfen Sie die Spielressource oder das Bild, bevor Sie sich entscheiden.                           |

Lesen Sie vor der Freigabe Original und Übersetzung zweimal vollständig. Prüfen Sie zunächst Handlung, Beteiligte, Empfänger, Verneinung und Bedingung. Achten Sie beim zweiten Lesen auf Stimme, Flexion, Untertitellänge und den Platz in der Oberfläche. Ein Wörterbuch hilft bei der Wortform, die Szene bei der Bedeutung. Speichern Sie Text und Redaktionsvermerk zusammen. Jede Änderung muss erneut gelesen werden.

## Spieldatei prüfen und den Arbeitsstand festhalten

Das Prüfprogramm kontrolliert Quellhashes, eindeutige IDs, fehlende Zeilen, bekannte Kontextfelder und leere als ready markierte Ziele. Es vergleicht RDR-Tildenmarker in ihrer Reihenfolge, einfache Platzhalter in geschweiften Klammern und gängige printf-Formate. Nummerierte Argumente dürfen ihre Position ändern, unnummerierte müssen die Reihenfolge ihrer Typen behalten. Selbst zwei identische `%s` können inhaltlich vertauscht sein. Prüfen Sie daher die Bedeutung jedes Werts. Veränderte Zeilenumbrüche erzeugen eine Warnung. Für verschachtelte ICU-Nachrichten, HTML, Schriftbefehle oder eigene Spielcodes braucht es passende Zusatztests.

Mit `tm-index` und `tm-suggest` lassen sich freigegebene Übersetzungen als Vorschläge nutzen. Der Schlüssel enthält Spiel, Sprache, Quellhash, Kontext-ID und die Versionen von Kontext, Redaktionsregeln und Glossar. Hinterlegen Sie einen Prüfverweis und die Hashes von Zieltext und Prüfdatei. Führen Sie beide Befehle bei relativen Pfaden aus demselben Arbeitsverzeichnis aus. Abweichende Freigaben für denselben Schlüssel erscheinen als Konflikt. Die Befehlsübersicht erhalten Sie mit `python scripts/localization_tools.py --help`.

Führen Sie beide Befehle im Skill-Ordner aus. Der beigefügte Prüfvermerk betrifft die Pausentaste „Turpināt“. Mit derselben Kontextversion ergibt sich ein Vorschlag.

    python scripts/localization_tools.py tm-index examples/tm-approved.jsonl --output demo-tm.json
    python scripts/localization_tools.py tm-suggest examples/tm-query.jsonl --index demo-tm.json --output demo-suggestions.json

Erstellen Sie den Release mit dem Werkzeug für das betreffende Spiel. Halten Sie technische Ausnahmen und offene Fälle getrennt fest. Sichern Sie die alte Datei außerhalb des Spiels. Ein einzelner Bearbeiter prüft den erwarteten Build und schreibt die freigegebene Fassung. Für RDR2-StringTable-XML setzen Sie unten Ihre Pfade ein. Der Vergleich prüft die *gesamte* Tabelle nach numerischem Spielschlüssel und exakt dekodiertem Text und meldet beide Dateihashes. Reihenfolge und XML-Schreibweise können den Byte-Hash ändern, obwohl Schlüssel und Text übereinstimmen.

    python scripts/compare_xml.py "reviewed/Latvian Translation.xml" "installed/Latvian Translation.xml"

Prüfen Sie im passenden Spielmodus ein Menü, zeitlich begrenzte Untertitel, einen langen Gegenstandsnamen und eine Variable mit mehreren Werten. Achten Sie auf **ā, č, ē, ģ, ī, ķ, ļ, ņ, š, ū, ž**. Melden Sie Fehler mit Build, bekannter ID, Original, aktuellem Text, Szene und Bildschirmfoto. Bewahren Sie den letzten freigegebenen Stand zur Wiederherstellung auf.

Notieren Sie nach jeder Charge den Hash der letzten installierten Datei, die freigegebene Textfassung und alle offenen IDs. Zählen Sie neu installierte IDs und sichtbare Quellzeichen für denselben Zeitraum. Erfassen Sie Entwurf, Redaktion, Export und Wartezeit getrennt. Vergleichen Sie beim Wiedereinstieg zuerst den letzten Bericht mit der tatsächlichen Spieldatei. Erst danach verteilen Sie neue Arbeit.

[Latviski](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/metode/) · [Über Reinis und freiwillige Unterstützung](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/de/#ways) · [Reinis auf Facebook schreiben](https://www.facebook.com/reinis.runcis)
