---
name: reyrun-rdr2-lv-install
description: Install, verify, update or remove the free REYRUN Latvian text translation for Red Dead Redemption 2 Story Mode on Windows. Use for Steam, Rockstar, Epic and existing non-Steam installations. Supports local file tools and a web-chat walkthrough for beginners.
---

# REYRUN RDR2 Latvian installation assistant

[Инструкция по установке на русском](references/INSTALL-AI-ru.md)

Open the [Latvian instructions](references/INSTALL-AI-lv.md) or [English instructions](references/INSTALL-AI-en.md). They contain the released checksums, authors' download links, exact filenames, launcher choices, copy checks, rollback procedure and separate in-game tests.

## What a player can say

> Gribu spēlēt Red Dead Redemption 2 latviski. Atrodi manas spēles mapi un uzliec REYRUN tulkojumu pēc šīs instrukcijas. Ja man kaut kas jānospiež pašam, parādi pa vienam solim.

An ordinary free chat can guide the player. It needs the instructions and the player's answers. If the assistant accepts files, attach this skill and the matching guide. A local assistant that supports skills can load this entire folder with its references. The player needs no translation service or model API key to use the game files.

Download the [RDR2 Windows launcher](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/launchers/REYRUN-rdr2-Windows.cmd) and run it. It discovers Steam, Rockstar and Epic installations and stages a SHA-256-verified XML copy in the REYRUN workspace. Complete the plug-in, ASI loader and game-folder steps in the installation guide. For connection details, open the [RDR2 bridge in English](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/#rdr2) or [RDR2 savienojuma lapu latviski](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/#rdr2). If discovery prompts for a game folder, choose the one containing `RDR2.exe`. A browser-only assistant can use the manual path. [Bridge tools and source](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge)

## Installation sequence

1. Establish access. A connected, user-approved file tool can read the selected local game folder and write the listed files. A web-only assistant reads the guide and asks the player for the result of each click. If no connector is available, use this manual route. Never treat an uploaded screenshot or an assistant's own workspace as local filesystem access.
2. Use the player's launcher to identify the installation. Confirm `RDR2.exe` is directly inside it. Let the player save and exit. Follow the relevant Steam, Rockstar, Epic or known-folder instructions from the guide.
3. Check the translation ZIP and extracted XML against the release manifest. Obtain the Universal translator and the standard ASI loader from their respective authors, or reuse known working copies. Resolve any incompatible pre-existing loader before modifying the game folder.
4. Record original filenames and hashes, plus which files were absent. Create and verify a backup outside the game. Keep one base translation active. Preserve unrelated mods. If the desired files already match, skip the corresponding writes. On a denied filesystem write, have the player approve the specific Windows file copy or perform it manually.
5. Install the three named files beside the executable and verify the final folder and XML hash. Use English as the game's base language. Start Story Mode and follow the guide's on-screen checks.
6. Give the player the destination and backup paths, the result of the file check and each game observation they made. Record any unobserved screen as untested. Keep the install record for an update or rollback.

## Using or adapting this skill

This installation guide and the separate translation workflow are free to use, share and improve. [Game translation workflow](https://github.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/tree/main/skills/reyrun-game-translation-lv) · [Project and voluntary support](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/)
