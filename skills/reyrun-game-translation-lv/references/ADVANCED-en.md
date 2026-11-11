# Testing a game translation in scenes, menus and another engine

[Latviski](ADVANCED-lv.md) · [Start with five examples](GUIDE-en.md)

Start with a scene you can reopen. Record the build, save point, speaker, listener, previous player choice and text key. This guide includes an original, reusable Godot test project. The RDR2 examples come from the public REYRUN translation.

## When one English string needs two Latvian translations

An inventory button labelled **Open** becomes **Atvērt**. A status next to **Konteiners** (container) can read **Atvērts**. Beside the feminine noun **Lāde** (chest), the status needs **Atvērta**. Preserve separate keys and record the noun that each status describes. Key each translation-memory entry to the function and context in which the wording was approved.

| Material | Evidence to gather before translation | Editor’s test |
| --- | --- | --- |
| Branching conversation | Speaker, addressee, scene, branch and the preceding and following lines on that branch. Record the source of this context. | Play both responses. Does a refusal still mean refusal? Does the familiar or polite form of address fit the relationship? |
| Mission objective | Who must act, what to carry or whom to follow, destination and deadline. Find the start, progress, success and failure states. | Complete a step, open the journal and compare it with the on-screen objective. The action and target should agree in both places. |
| Input prompt | Determine whether the action requires a press, repeated taps, a hold or a release. Identify the part drawn as an input glyph. | Repeat the scene with the default and a remapped key. Repeat with a controller if the game supports it. |
| Timed dialogue | Actual cue duration, interruptions, speaker changes, overlapping voices and any lettering embedded in the art. | Watch with the original audio, then with the sound muted. Can you identify who spoke and read the thought before the next cue? |

When the script, dialogue data or recording does not establish the meaning, leave a specific question on the row. **“Is this the button to open the chest, or the chest’s current state?”** is enough to unblock the example. Continue reviewing rows whose meaning is established. [IGDA Localization SIG’s game localization guide](https://igda.org/resources-archive/best-practices-for-game-localization/)

## What the game needs to render for itself

Search for these native IDs in `Latvian Translation.xml` from the 11 November 2026 release. [Download the REYRUN translation](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip)

| XML ID | Exact text in the file | What to verify |
| --- | --- | --- |
| `0x9D9BAF33` | `Īsi spiediet ~INPUT_HORSE_SPRINT\|PromptId=INPUT_WNT1_SPEEDUP~, lai jātu ātrāk` | Keep the entire control token, including everything after the vertical bar. The game draws the input glyph here. |
| `0x046E5281` | `Turiet ~INPUT_HORSE_SPRINT\|PromptId=INPUT_WNT1_SPEEDUP~, lai jātu ātrāk` | The token is identical but this line calls for a hold. Reusing the first line would change the required action. |
| `0x1C4EF867` | `Seko ~o~Dačam~s~` | Keep the highlight around the target and use the dative form of the character’s name. Several IDs carry this wording. |

Record the original binding and reopen the scene. Bind the action to a free key. Reopen the prompt and perform the action with the new key. Compare the **controls menu → prompt glyph → action that actually fires**. Restore the initial binding afterwards. Repeat on each supported input device for which you intend to report a pass. [Microsoft XAG 107](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107)

## Subtitle timing and Latvian characters

Pick a scene with a short interjection, a longer response and an off-screen speaker. Record when each cue appears and disappears, its visible text and line breaks. Divide the number of visible characters by its duration to triage dense cues. For example, 42 characters in 2.1 seconds gives 20 characters per second. Decide whether a cue needs editing after watching it at normal speed with the actual type size and gameplay competing for the player’s attention. When only the text is editable, trim repetition while preserving the negative, addressee, target and condition.

Check the smallest supported window, an ordinary gameplay resolution and the largest available subtitle setting. Look for collisions with objectives, response choices and tutorials. Separate lettering baked into an image from the live caption. In RDR2, for example, the original **Colter** chapter artwork remains visible with the Latvian caption **1. nodaļa: Kolters** below. If the game supports sound captions, also check their timing and whether the player can identify where the sound comes from. [Microsoft XAG 104](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104)

Turn on pseudolocalization in a test build. Adding accents or stretching text helps reveal missing localization hooks, clipped endings and tight buttons. Switch back to real Latvian and inspect **ĀČĒĢĪĶĻŅŠŪŽ āčēģīķļņšūž** in every font and style the game actually uses. Check uppercase menus, italics, wrapped descriptions and substituted names. For a missing-glyph square, identify the font or atlas serving that screen. Add characters introduced by runtime variables to any character set exported from a text table. Reopen the same scene. [Godot pseudolocalization](https://docs.godotengine.org/en/latest/tutorials/i18n/pseudolocalization.html) · [Unity character sets](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/StringTables.html)

## Run two contexts and three number forms in Godot

The small project in `examples/godot-lv` includes an actual gettext PO catalogue and a test. **Open** has two contexts. The catalogue provides three integer forms, including **1 diennakts**, **2 diennaktis**, **11 diennakšu** and **21 diennakts**. Its PO header declares which index selects each form. Inspect the header before reusing the indices in another catalogue. Fractional quantities have additional rules and need separate tests with the formatter the game uses. [Unicode CLDR rules for Latvian](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html#lv) · [Godot gettext catalogues](https://docs.godotengine.org/en/stable/tutorials/i18n/localization_using_gettext.html)

From the skill directory, run both commands with Godot 4.6.3. Replace `godot` with the full executable path if needed. Only the teaching project and its local import cache are involved.

```sh
godot --headless --path examples/godot-lv --import
godot --headless --path examples/godot-lv --script res://check.gd
```

Verified result: **2 contexts, 12 integer counts, 0 failures**. To see the failure path, copy the example to a new folder. In its `lv.po`, change the action translation from `Atvērt` to `Vaļā`. Repeat both commands with the copied path. The check names `inventory/action` and exits with status 1. This catches a button labelled with the wrong sense even though the catalogue still imports. Actual font rendering requires a separate check in the graphical game.

## Transfer the check to your project

| Project | First import | What to observe in the game |
| --- | --- | --- |
| Godot with source access | Add `lv.po` to the project translations. Match the context argument of `tr()` to the catalogue’s `msgctxt`. Use `tr_n()` where the game has a count. | Switch to `lv`, visit both uses of the same English word and exercise the integer values from the example. |
| Unity with the Localization package | Use the project’s existing String Table Collection. Retain shared key identities and the locale table. Check which entries use Smart Strings. Supply a real runtime argument. | Test the UI in two sizes and vary a count. If braces appear or a glyph is missing, inspect the formatter, table and active font. [Unity String Tables](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/StringTables.html) |
| Unreal with source access | Select the correct localization target and cultures in the Dashboard. Gather → Export → Import → Compile. With Dialogue Waves, distinguish the speaker, listener and optional subtitle override. | Exercise a variant addressed to one person and another available branch. Open a game build that loads the compiled localization target. [Epic localization tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/localization-tools-in-unreal-engine) · [Epic dialogue assets](https://dev.epicgames.com/documentation/unreal-engine/asset-localization-in-unreal-engine) |
| Released game with a documented translation plug-in | Identify the importer supported by this game and build. Back up the test destination, insert a few known IDs and read back the result. | Reopen a reproducible scene and check its keys. RDR2’s XML schema and filenames apply to its particular plug-in. |

After a game update, compare matching IDs by source text and context. Review new entries, changed text and changed usages. Retain deleted IDs in the previous release record. Replay the affected scene first with its relevant runtime arguments. Report **build · locale · resource and ID · scene or save · settings · expected · observed · screenshot or video time**. Record the catalogue check, graphical glyph check and individual playthrough separately.

[Back to the skill](../SKILL.md) · [Reinis and voluntary support](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/#ways)
