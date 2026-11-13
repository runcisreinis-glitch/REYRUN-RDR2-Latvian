# How REYRUN translated Red Dead Redemption 2 into Latvian

[Latviski](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/metode/pieredze/) · [Project website](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/)

On 2 November 2026, the team could show 32,666 source IDs with completed drafts in the preceding 24 hours. In that same window, the team's game installation gained 8,602 entries. The gap accumulated after drafting. We learned to inspect the queues for review and installation before asking another translator to produce more text.

[Use the translation method on another game](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/method/)

## What the project measured

All dates below use Riga time. One entry means one game string ID. A button label counts as one entry, just as a long subtitle does. Of the 256,890 IDs in the project inventory, 253,073 required an editorial decision. The other 3,817 were classified separately as exceptions, including control strings, numbers, symbols and empty values.

| Observation window in 2026               | What the records showed                                                                                                                                                                                        | What the count covers                                                                                                                                                                             |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 28 October, status check                 | 119,387 entries in the installed XML. An older progress file still reported 118,002.                                                                                                                           | Snapshot of the 253,073 in scope. Reopening the older checkpoint would have repeated completed work.                                                                                              |
| 31 October, first eight parallel batches | 128 short drafts in about 59 seconds. The final editor kept 45 wordings, changed 72 and held 11 for clarification.                                                                                             | One selected sample. The 117 approved texts were still awaiting installation at this checkpoint.                                                                                                  |
| 1 November, 22:00 to 2 November, 22:00   | 32,666 unique IDs completed drafting and 32,620 completed editing. Ten verified releases added 8,602 IDs to the game, from 131,617 to 140,219.                                                                 | A full 24-hour window. Stage counts overlap. The installed additions covered 341,985 visible English source characters, excluding game control tags.                                              |
| 6 November, 22:29 to 22:34               | The database held 198,995 approvals. The actual game file held 198,238. All 198,238 shared texts matched exactly.                                                                                              | 757 approved entries were awaiting deployment. A separate overnight review had produced 1,411 ready and 133 held candidates from 1,544 IDs, with zero installations from that review.             |
| 8 November, 23:23 audit                  | 222,065 installed. Of the outstanding 31,008, the audit found saved text for 30,960, including 2,093 recovered only from raw responses. It could not establish a saved text for the remaining 48 at that time. | Evidence of a draft did not establish its editorial status. After work resumed, a separate release report at 00:28 on 9 November recorded 1,415 additions with zero new translation API requests. |
| 9 November, 22:47 and 10 November, 00:21 | Both checks found 246,024 installed with 7,049 outstanding.                                                                                                                                                    | Checking twice established the state. Neither check added a release.                                                                                                                              |
| 10 November, 23:28 final check           | 253,073 approved IDs and texts matched the installed XML. Zero pending, zero held. A final correction changed 29 existing texts.                                                                               | Full comparison against the approved database. In-game typography, subtitle timing and appearance still needed playtesting.                                                                       |

## Where time went

**Worker limits.** In the tenth October review cycle, 12 configured local profiles shared a limit of three simultaneous workers. Of 84 planned small batches, 45 were dispatched. The run deadline left 39 batches containing 179 rows unsent. One dispatched batch returned a wrong ID. The editors’ frozen input contained 90 local drafts. Eventually 264 structurally valid rows arrived, some too late for that review. We kept the input snapshot and rejected the mismatched ID. Assigning the text to the missing ID by guess would have hidden the error. The revised coordinator gave each request a timeout and continued taking work from a persistent queue.

**Review and installation.** On 2 November at 22:04, the operating queue showed 3,286 reviewed entries waiting for import and another 18,393 ready for final review. The latest completed installation had been at 08:55. Drafting and editing continued into the evening. Adding translators alone could not release those reviewed entries. On 6 November, a Steam update had finished and the deployment preflight passed, but the previous run still held the database write reservation. A successful preflight changed zero files. A resumed run needs to check the earlier writer, match its candidate and backup, and continue at the first unfinished step.

**Costly repeat work.** During the 24 hours covered by the 8 November audit of four API-assisted review workers, 5,650 reports contained provider token counts totalling 94,683,901. These workers were editing and checking existing drafts in two stages. The audit did not establish an invoice amount or tokens per accepted line. Saving each raw response made the 2,093 otherwise missing texts recoverable. A new project can stop sending requests when a review queue grows, recover the stored responses, and budget further calls against unresolved IDs.

## Where the Latvian went wrong

The local draft “Tu esi taisnīgs” for “You're right” describes a fair or just person. If the speaker is agreeing with the other person, “Tev taisnība” expresses the intended meaning. In another draft, “maniac” became “atraitis” (widower). Both problems can survive a JSON or XML format check. The project reviewed the whole source and target pair, recorded the sense being corrected and gave the next batch a source-linked example.

A shared resource bank sometimes supplied a clue, but its ID order could not establish who spoke or which line came next. The inventory had a string ID without reliable speaker or scene labels. Ambiguous lines went into a separate queue with a question for the editor. A small experiment compared a full prompt with fewer selected examples on the same 24 sources. Fewer input tokens still left serious meaning and language errors in both variants. Request order and cache use differed, so the experiment supplied no dependable production speedup.

## How the last 7,049 entries reached the game

First the team recovered 1,348 previously edited entries. For the other 5,701 it compared the latest editorial decisions across 104 batches. Reviewers deliberately retained 377 original spellings, including keys, brand names and characters’ foreign-language lines. Automatically flagging every unchanged string as untranslated would have reopened those decisions.

Only one importer wrote a release at a time. It checked the candidate, prepared the import, rehearsed it against a database copy, applied it to the live database, built the XML, checked the target installation and deployed the file. It then reopened the installed XML and compared every ID and text. All 246,024 entries installed before the final series retained their text. The subsequent 29 corrections within the added material changed wording without increasing the count.

For another game, report drafting, final approvals and new IDs verified in the installed file separately. Record the elapsed time and visible source-character count for the same interval. Keep corrections to existing IDs, deliberate original spellings and unresolved questions in separate columns. This lets someone taking over after an interruption see whether the next job is translation, an editorial decision or a file installation.

## What the player saw

On 11 November Reinis captured seven screenshots from game version 1491.50. The pause menu shows “Karte” and “Iestatījumi”, and the Controls screen shows “Taustiņu piesaiste”. The riding tutorial displays its key symbol alongside the Latvian text. The opening scenes show Latvian dialogue subtitles and translated job titles in the credits. A Latvian caption appears beneath the original chapter-title artwork.

Three examples can be traced to exact entries in the published XML. “Bet mēs zaudējām dažus cilvēkus.” is `0xFCD0E439`. The prompt to tap a key to ride faster is `0x9D9BAF33`. The Controls description “Pielāgo tastatūras un peles taustiņu piesaistes.” is `0x94B26056`. An editor can use those IDs to locate a line for correction. A mission objective, live dialogue during player control and the action/key list inside the key-mapping submenu have separate checks. [In-game checks](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/install/)

### Evidence

The dated observations come from the project's 28 October installation status, 31 October cycle 9 and 10 checkpoints and 23:35 production report, 2 November 24-hour report, 6 November installation audit, 8 November stop-and-recovery audit and its following release report, the two November status checks above, and the 10 November final installation and correction records. Only the project-side audit had access to the editorial database. Anyone can independently count the unique IDs and verify the published XML against this final SHA-256. Opening the 11 November release ZIP and parsing its XML reproduced that hash and all 253,073 unique IDs.

`c72337da664b3999ca4fc2de2600c1e79c551b29fa1e69d79d1330485aef5045`

[Download the release](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip) · [Support Reinis](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/#ways) · [Get to know Reinis on Facebook](https://www.facebook.com/reinis.runcis)

![REYRUN](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/assets/reyrun.png)
