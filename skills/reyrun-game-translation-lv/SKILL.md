---
name: reyrun-game-translation-lv
description: Translate and edit game text into natural Latvian with speaker and scene context. Use for game menus, dialogue, subtitles, item descriptions, reviewed translation memory, batch quality checks and verification of a staged RDR2 translation.
---

# REYRUN game translation into Latvian

[Руководство на русском](references/GUIDE-ru.md) · [Проверки в игре](references/ADVANCED-ru.md) · [Опыт перевода RDR2](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/ru/method/retrospective/)

<img src="assets/REYRUN.png" alt="REYRUN" width="56">

Start with the [English guide](references/GUIDE-en.md) or [latviešu instrukcija](references/GUIDE-lv.md). For a first run, use the five original teaching examples supplied in this folder.

For accessibility, variables, fonts, subtitles and control prompts, use the [advanced English guide](references/ADVANCED-en.md) or [padziļinātā rokasgrāmata latviski](references/ADVANCED-lv.md). The [RDR2 retrospective in English](https://github.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/blob/main/docs/RETROSPECTIVE-en.md) and [latviešu pieredzes apraksts](https://github.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/blob/main/docs/RETROSPECTIVE-lv.md) give the measured queue sizes, examples of mistranslations and the actual recovery sequence. To play the completed RDR2 translation, use the separate [installation skill](https://github.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/tree/main/skills/reyrun-rdr2-lv-install).

## Take a batch

1. Identify the game build, language, unique entry IDs and the target file format. Preserve a read-only source copy. For a new engine, test one small export and import with its own tools before translating thousands of lines.
2. Give the translator the entire string, including any codes at its start or end. Attach the known speaker, addressee, scene, UI control or item type and the source of that information. Keep branch information. If one missing detail changes the translation, put the row on hold and ask a question that a screenshot, game resource or script can answer.
3. Keep assigned IDs disjoint across workers. Use the same glossary revision and character notes. Keep the input record intact and return three fields in each copy: `target`, `decision` (`ready` or `hold`) and `reason`. For a hold, provide a specific question. In the example, “Seal” has several plausible meanings.
4. Translate meaning in context. Keep who did what to whom, the tense, negation and force of a request or insult. For dialogue, read the result aloud in character. Check Latvian cases, agreements, address forms and word order. Preserve engine codes, argument identities and timing marks. Compare the edited line again with the entire source.
5. Have another reviewer check each whole pair. In the RDR2 process, the final reviewer made one meaning pass and one language and game-context pass. Record the exact source and target revisions read. A later text change needs another check. Keep held rows out of the approved set.
6. Run the structural checker and inspect its warnings. Use a game-specific parser for markup or plural syntax outside its documented coverage. Save the accepted ID and text pairs, the reviewer’s decision and the file hashes. An approved earlier translation can be a suggestion when its context and terminology still match.
7. Build a release from the approved rows with the game’s own resource tool. Give one process ownership of the final write and retain the previous release outside the game. Compare all installed entries with the approved export and check which entries changed from the previous version. In the game, inspect a menu, dialogue, long strings, Latvian diacritics and variable substitution. Record which screens or scenes were actually seen.

## On the next work session

Read the last release receipt and inspect the current files. Resume from the first unfinished stage. Record counts for drafted, checked, approved, installed and held rows separately. Time the stages, including waits. Counting newly installed IDs and source characters over the same elapsed period makes it possible to see where work has stopped moving.

When a session ends in the middle of a batch, match the saved responses to the assigned source IDs and source hashes. Compare them with the latest editorial decisions. Keep unresolved variants with the source and a question for the editor. Resume the checked release from its last verified write. Re-read the installed candidate to avoid sending already completed text through translation again.

## Commands

Run these inside the skill directory with Python 3.8 or newer. On Windows, substitute `py -3` for `python` if needed. Each output path must be new.

```sh
python scripts/localization_tools.py prepare examples/source.jsonl --output demo-packets --max-rows 2
python scripts/localization_tools.py validate --inputs examples/source.jsonl --edited examples/edited.jsonl --report demo-qa.json
python -B -m unittest discover -s scripts -p "test_*.py"
```

The result has five input rows, four declared ready and one held for context. The score line is intentionally identical in both languages. Inspect that warning. Use `scripts/compare_xml.py` to compare a complete reviewed RDR2 XML with a staged or installed copy. The scripts work locally with the Python standard library and leave game files untouched.

[REYRUN project, author and voluntary support](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/#ways) · [Reinis Runcis on Facebook](https://www.facebook.com/reinis.runcis)
