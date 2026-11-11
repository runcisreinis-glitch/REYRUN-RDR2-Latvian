<img src="assets/REYRUN.png" alt="REYRUN" width="100">

# REYRUN · Red Dead Redemption 2 in Latvian

English · [Latviski](README.lv.md)

A free Latvian text translation for Red Dead Redemption 2 on Windows PC. Use it in Story Mode with the game language set to English. The characters keep their original voices.

**[Download the translation ZIP](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip)** · [Open the bilingual project website](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/en/)

## A note from Reinis

My name is Reinis Runcis. This translation is my way of thanking the people who help me keep living in my own home. It’s a gift to anyone who’d like to play through this story in Latvian.

I’ve lived alone for many years. Lately my care and everyday expenses have been costing me more than I have coming in. If you’d like to help, please give only what you can comfortably spare. I still think life is wonderful, and it would mean a lot to me if something I’ve made helps you keep going on a hard day.

If you’d like to get to know me, read my poetry or ask about my other work, [write to me on Facebook](https://www.facebook.com/reinis.runcis).

### Ways to support me

- **Swedbank** · REINIS RUNCIS · IBAN `LV82HABA0551011504293`
- **Stripe** · [Give in euros](https://buy.stripe.com/dRm7sNfD2bOZckRb9A6g802) · [Give in US dollars](https://donate.stripe.com/cNifZj4Yog5fckR5Pg6g800)
- **PayPal** · [Reinis Runcis Support](https://paypal.me/ReinisRuncisSupport)
- **USDT on BNB Smart Chain (BSC, BEP-20)** · `0x32834068Fa4fEe29fA10e2020e68Fb23d5fC1d21`
- **USDT on Solana (SPL)** · `Hy6hKMwMDgXFdaD3N5J1CNMs2LwiE22QdrQnEYoX3fZh`

## Translate another game into Latvian

Start with the [practical guide](skills/reyrun-game-translation-lv/references/GUIDE-en.md). You can give the [REYRUN skill](skills/reyrun-game-translation-lv/SKILL.md) to your AI assistant or follow the same steps with a human translator. The examples and Python tools run locally. They let you try a small batch, catch damaged placeholders and compare edited text against its source before you touch a game installation.

The [RDR2 project retrospective](docs/RETROSPECTIVE-en.md) follows the work from drafts to the installed XML. It explains where time was lost, how existing translations were recovered after interruptions, and which measurements tell you how many lines a player can actually read.

## Install on Windows

1. Close the game and extract the ZIP. In Steam, right-click the game, choose **Manage**, then **Browse local files**. For a non-Steam copy, open the install folder through your launcher. Find `RDR2.exe`.
2. Download **Universal RDR2 String Translator** from [RacerMouze](https://www.nexusmods.com/reddeadredemption2/mods/10214). Place `UniversalRDR2StringTranslator.asi` beside `RDR2.exe`. If you already have a working `dinput8.dll` ASI loader, keep it. Otherwise download [Alexander Blade’s Script Hook RDR2](https://www.dev-c.com/rdr2/scripthookrdr2/) and copy `dinput8.dll` from its `bin` folder beside `RDR2.exe`.
3. Back up any file ending in `Translation.xml` and any older `rdr2-translator.asi` outside the game folder. Copy `Latvian Translation.xml` from the ZIP into the folder beside `RDR2.exe`. Keep the filename as supplied.
4. Leave the game language set to **English**, launch **Story Mode**, and turn on subtitles. Check a menu and a line of dialogue. See the [installation and removal guide](INSTALL-EN.txt) for troubleshooting.

### Ask your AI for help

Attach `INSTALL-EN.txt` from the ZIP to your AI assistant and paste this request.

> Help me install the REYRUN Latvian text translation for Red Dead Redemption 2 on Windows. I use [Steam / another launcher]. Follow the attached instructions, help me find RDR2.exe and the two authors’ downloads, back up my existing files, and check the final folder before I launch Story Mode.

## Download verification

The release contains 253,073 translated entries. The ZIP includes the translation XML and installation guides in Latvian and English. The ASI plug-in and loader are available from their respective authors. The approved database and installed XML matched on every ID and text in the 11 November 2026 check. On-screen rendering still calls for a Story Mode playtest.

| File | SHA-256 |
| --- | --- |
| `REYRUN-RDR2-LV.zip` | `11d7ee80bac9ac820a2c20e87f2f7fc736e3fab5ceb6e9cf7842543f9f3237da` |
| `Latvian Translation.xml` | `c72337da664b3999ca4fc2de2600c1e79c551b29fa1e69d79d1330485aef5045` |

## Use and sharing

You may use, copy, share and adapt REYRUN’s translation, method and accompanying tools free of charge, for any purpose. This permission covers Reinis Runcis’s contributions. The underlying game, its assets and the third-party tools belong to their respective rights holders.

If you find an odd line or a missing Latvian accent, send Reinis the line as it appeared and where you saw it. [Contact Reinis on Facebook](https://www.facebook.com/reinis.runcis).
