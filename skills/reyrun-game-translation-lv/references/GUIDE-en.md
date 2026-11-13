# Translating a game into Latvian with REYRUN

![REYRUN](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/assets/reyrun.png)

If you want to play Red Dead Redemption 2 in Latvian, get the finished translation and its installation guide from the [project website](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/). To translate or edit another game, start with a copy of the folder `reyrun-game-translation-lv`. It contains the workflow, five teaching examples and local tests.

After the first sample, use the [advanced game-text checks](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/method/techniques/). For measured examples of recovering earlier drafts and tracking queues of edited text, read the [RDR2 project retrospective](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/method/retrospective/).

## Use the method with a person or an AI assistant

In an ordinary chat, attach `SKILL.md`, this guide and a small batch of source rows. In a system that loads Agent Skills from a directory, copy the **whole folder** into the skills location configured in that system, refresh its list and select `reyrun-game-translation-lv`. The skill refers to the guides and scripts by relative path. A translator can also edit the JSONL files by hand. Python runs the checks. The work does not require a particular AI service or a paid account.

For a first exercise, attach `examples/source.jsonl` and give the assistant this request:

> Read SKILL.md. Translate the five complete source rows into Latvian. Keep every input field unchanged. Add target, decision and reason. Put an ambiguous line on hold and tell me exactly what would settle its meaning. Return one JSON object per line, with no surrounding prose. I will review the result before it goes into the game.

Save the reply as `my-edits.jsonl` in UTF-8. Compare the decisions with `examples/edited.jsonl`. Several wordings can be correct. Check what the player is being asked to do. Read the witness’s reply aloud, inspect the control prompt and see which row the assistant held for context.

## Try one complete batch

Open a terminal in the skill folder. Use Python 3.8 or newer. On Windows, you may need `py -3` in place of `python`.

    python scripts/localization_tools.py prepare examples/source.jsonl --output demo-packets --max-rows 2
    python scripts/localization_tools.py validate --inputs examples/source.jsonl --edited examples/edited.jsonl --report demo-qa.json
    python -B -m unittest discover -s scripts -p "test_*.py"

The first command writes three packets of two, two and one rows. The second reports five source IDs, four declared ready and one hold. The score line contains only arguments and separators, so its unchanged text produces an expected warning. Try the second command again with `my-edits.jsonl` and a new report name. For a deliberate failure, remove `~INPUT_INTERACT~` **from the target only** in a disposable copy. The checker identifies the row and exits with code 2. Existing outputs are protected from overwriting. Use a new folder or report name for each run.

## Prepare real sources

Export text with a tool for that game. Keep the original file, build number, resource name and game-native key. Work on one resource namespace and one build at a time. The input can be a UTF-8 JSON array or JSONL with one object per line. If several resources reuse native IDs, check them as separate sets. A source hash in this format is SHA-256 of the decoded string encoded as UTF-8, without an added line ending. For example, `hashlib.sha256(source.encode("utf-8")).hexdigest()`.

| Field                                                       | What to enter                                                                                                                                 |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `id`, `native_id`                                           | A unique, stable work ID and, where available, the exact game key. A changed language pack can renumber rows. Keep the actual key.            |
| `source`, `source_sha`                                      | The full source string, including codes and whitespace, and its checksum.                                                                     |
| `candidate`                                                 | The previous draft, or an empty string for a new translation.                                                                                 |
| `context`, `context_id`, `speaker`, `scene_id`, `branch_id` | Verified evidence about who is speaking and what the player sees. Omit unknown fields. Consecutive IDs alone do not establish dialogue order. |
| `target`, `decision`, `reason`                              | The proposed Latvian wording, the decision and any question or exception. Only the edited rows contain these fields.                          |

Give different workers different IDs. Supply approved forms of names, places and recurring terms with usage examples, including inflected forms where the sentence requires them. Keep a common revision of these files for each batch. A scene that switches from formal to familiar address warrants a note explaining where the change happens.

## Edit for meaning and voice

The examples below were written for teaching. They are not quotations from RDR2.

| Source and situation                                                                        | Latvian wording                                            | What the reviewer checks                                                                                                                                                      |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| “Resume” on the pause menu                                                                  | **Turpināt**                                               | A short action label that fits the button.                                                                                                                                    |
| “Hold `~INPUT_INTERACT~` to open the gate.”                                                 | **Turi nospiestu `~INPUT_INTERACT~`, lai atvērtu vārtus.** | The control must be held down. A single press would tell the player to do something else.                                                                                     |
| “I... I didn't take it.” A nervous witness                                                  | **Es… Es to nepaņēmu.**                                    | Keep the hesitation and the denial. Read the whole line aloud.                                                                                                                |
| “Can you wait here?” A child speaking to a friend / a clerk speaking politely to a stranger | **Vari te pagaidīt?** / **Vai jūs varētu te pagaidīt?**    | Relationship and register change the address.                                                                                                                                 |
| “Charges: {count}” A changing item counter                                                  | **Lādiņu skaits: {count}**                                 | If the engine supplies only one string, a label can take every displayed number. Where the engine supports plural branches, translate and test the branches it actually uses. |
| “Seal” with no scene or item type                                                           | **hold**                                                   | Find out whether it means an animal, a stamp or an action. Then choose the Latvian word.                                                                                      |

Read each complete pair twice before approval. On the first pass, check meaning, negation, actor and addressee, conditions and the action’s consequences. On the second, check how the character speaks, Latvian inflection, subtitle length and interface constraints. A spelling dictionary can confirm a form. Choosing between two meanings requires context. Keep an approved target and its review record together. If somebody rewrites it, review the new text.

## Check, ship and resume

The validator checks source hashes, unique IDs, complete coverage, known context fields and empty targets declared ready. It compares RDR-style tilde markers in order, simple brace arguments and common printf formats. Fully numbered printf arguments can move with the sentence. Implicit argument types must stay in sequence. Two identical unnumbered `%s` arguments can still exchange meanings, so the reviewer must check which value goes where. Line-break changes produce warnings. Add a parser or test for the game’s actual syntax if it uses nested ICU messages, HTML, font directives or custom controls.

The optional `tm-index` and `tm-suggest` commands reuse reviewed text as suggestions. The key includes the game, language, source checksum, context ID and revisions of context, policy and terminology. Supply a review reference and checksums of the approved target and review file. Keep the working directory stable when using relative review paths. Competing approved wordings for the same key go to the conflict list. Use `python scripts/localization_tools.py --help` to see the commands.

Run this example from the skill folder. The included review record covers the pause-menu verb “Turpināt”. Both commands use the same context revision and return one suggestion.

    python scripts/localization_tools.py tm-index examples/tm-approved.jsonl --output demo-tm.json
    python scripts/localization_tools.py tm-suggest examples/tm-query.jsonl --index demo-tm.json --output demo-suggestions.json

Build a release with the game’s own adapter. Keep technical exclusions and unresolved rows in separate lists. Back up the current game file outside the game folder. Have one writer replace it once the reviewed snapshot still matches the expected build. For an RDR2 StringTable export, run the comparison below with your actual paths. It checks the *whole* table by numeric native ID and exact decoded text, and reports both file hashes. A difference in file order or XML spelling can change the byte hash while leaving all ID/text pairs equal.

    python scripts/compare_xml.py "reviewed/Latvian Translation.xml" "installed/Latvian Translation.xml"

Open the relevant game mode and check a menu, a timed dialogue line, a long item name and a variable with several values. Inspect characters such as **ā, č, ē, ģ, ī, ķ, ļ, ņ, š, ū, ž**. When reporting an issue, save the game build, ID if known, the original line, current translation, scene and screenshot. Keep the last accepted release available for rollback.

At the end of each batch record the last installed release hash, the approved snapshot and the IDs still on hold. Log new installed IDs and source characters per elapsed hour. Time drafting, review, export and waiting separately. On resuming, read the receipt and compare the actual game file with it before dispatching any work.

[Latviski](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/metode/) · [About Reinis and ways to support his work](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/#ways) · [Contact Reinis on Facebook](https://www.facebook.com/reinis.runcis)
