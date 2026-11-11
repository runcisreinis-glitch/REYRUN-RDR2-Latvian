# Install the REYRUN Latvian translation for Red Dead Redemption 2

For Windows PC and Story Mode. The player needs an installed copy of the game. Give this guide to an AI assistant with access to the player's files, or follow it in an ordinary chat that guides the player through each click. [Latviski](https://github.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/blob/main/docs/INSTALL-AI-lv.md)

> I want to play Red Dead Redemption 2 in Latvian. Find my game folder, download the REYRUN translation and install it using this guide. Keep a backup of my old files and show me how to check it in the game. If you can't access my computer, tell me what to do one step at a time.

## How your assistant can help with local files

In an ordinary web chat, paste the request and the link to this guide. The player opens the folders and can share a list of filenames. To let an assistant do the copying, use an existing local assistant or a file connector already approved by the player. It only needs the selected RDR2 folder, one download or staging directory and one backup directory.

In the connector's own interface, the player selects the allowed folders. First have the assistant read the name of `RDR2.exe` from the selected game folder. During installation restrict writes to saving and copying the files below. Keep sign-in passwords and connector access keys out of chat. An assistant that can only inspect uploaded attachments must guide the player through local copying. If Windows denies a copy to a protected folder, show the exact source and destination. The player can confirm that specific copy in Windows. If that access is unavailable, pause at the manual step. Installation requires no changes to network sharing, firewall settings or folder protections.

The RDR2 profile has a ready-to-run Windows launcher. Choose the game folder containing RDR2.exe. If an ordinary web chat cannot access your PC, follow the manual steps. [Open the RDR2 connection guide](https://reyrun-chatbot-bridge.runcisreinis.chatgpt.site/en/#rdr2) · [Bridge tools and source on GitHub](https://github.com/runcisreinis-glitch/REYRUN-Chatbot-Bridge)

### A local bridge limited to three folders

Use this option in a desktop AI client that can run a local MCP server over `stdio`. The connection runs between two programs on the player's PC. It needs no public address, tunnel or API key. A browser-only chat without this feature can still guide the player through the manual steps. Use one local file connection.

1. Find the game folder using section 1. Create two separate folders outside the game, one for staged downloads and one for backups. Record the three actual paths.
2. This example requires Node.js 24 or later with npm. Check `node --version` and `npm.cmd --version`. If Node.js is missing, use an official Windows LTS installer or continue manually. Check that `npm.cmd view @modelcontextprotocol/server-filesystem@2.3.0 version` finds the pinned release. [Node.js downloads](https://nodejs.org/en/download) · [Filesystem package requirements](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/package.json)
3. For example, in Claude Desktop open **Settings → Developer → Edit Config**. Windows stores this file at `%APPDATA%\Claude\claude_desktop_config.json`. Back it up. If it already has an `mcpServers` object, add only the `rdr2-files` entry to that object. Replace the three example folder paths with the actual ones, each as a separate JSON string. Backslashes in JSON strings are doubled. Check that Node.js and `npx-cli.js` exist in the locations shown. For another Node installation, use its actual full paths. [Opening the configuration](https://modelcontextprotocol.io/docs/develop/connect-local-servers)

```json
{
  "mcpServers": {
    "rdr2-files": {
      "command": "C:\\Program Files\\nodejs\\node.exe",
      "args": [
        "C:\\Program Files\\nodejs\\node_modules\\npm\\bin\\npx-cli.js",
        "--yes",
        "@modelcontextprotocol/server-filesystem@2.3.0",
        "--confine-roots",
        "D:\\Speles\\Red Dead Redemption 2",
        "D:\\REYRUN\\Lejupielade",
        "D:\\REYRUN\\Rezerve"
      ]
    }
  }
}
```

4. Save the configuration, fully quit and reopen the desktop AI app. On first use npm downloads the specified public package. `--confine-roots` also limits client-supplied folders to the configured scope. Call `list_allowed_directories` to check the effective folders. If the game folder is absent, correct its path and the client's selected folders and restart the connection. Use `get_file_info` on `RDR2.exe` in that exact directory. Its filename and size are enough.
5. The filesystem server operates locally. Download from the authors' links below, extract into staging and verify the hashes. The player can run `Get-FileHash` even when the assistant has no terminal. The `copy_file` tool preserves bytes and requires an unused destination filename. If a file exists, check its hash and follow section 3 before replacing it. If Windows denies a write, let the player confirm that particular copy in File Explorer. When finished, you can remove just the `rdr2-files` entry and reopen the client. [Filesystem tools and directory restrictions](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md)

## 1. Find the copy the player actually launches

| How the player starts RDR2 | How to open the installation folder |
| --- | --- |
| Steam | In **Library**, right-click **Red Dead Redemption 2**. Choose **Manage**, then **Browse local files**. This also works for a Steam library on a different drive. |
| Rockstar Games Launcher without Steam | Open **Settings**. Under **My installed games**, select **Red Dead Redemption 2**. Click **Open** next to **View installation folder**. |
| Epic Games Launcher | In **Library**, click **…** on the game tile, then **Manage**. Click the folder icon beside **Installation**. |
| Known folder or a shortcut pointing to the game file | Open the folder, or use the shortcut's **Open file location** menu. If the shortcut opens a store or lands in a launcher directory, follow that launcher's row above. |

Confirm that the folder itself contains `RDR2.exe`. If two copies exist, select the one opened through the launcher the player uses. Leave saves in place. Let the player save their progress and exit. Begin when the game process has exited and the launcher has finished any update. [Rockstar's installation-folder instructions](https://support.rockstargames.com/articles/5IptkkwDLk32lu7sLb1wDm/only-windows-10-and-later-are-supported-error-troubleshooting)

## 2. Get the translation and its two dependencies

1. Download the file named **REYRUN-RDR2-LV.zip** from either link. GitHub's “Code → Download ZIP” gives you a source snapshot. The file linked here is the player package. [Download from the website](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip) · [Download the same file from GitHub](https://raw.githubusercontent.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/main/REYRUN-RDR2-LV.zip)
2. In the download folder, open PowerShell and run the first command below. Compare the SHA-256 with the table. Extract the ZIP to a new, empty folder. It contains `Latvian Translation.xml`, `UZSTADISANA-LV.txt` and `INSTALL-EN.txt`. Run the second command in the extracted folder. If a hash differs, stop installing this release and compare the download with the project's checksum file. [Project checksums](https://github.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/blob/main/SHA256SUMS.txt)
3. The game needs **Universal RDR2 String Translator**. Keep a working copy if the player already has one. Otherwise extract `UniversalRDR2StringTranslator.asi` from the author's main download. If Nexus requests a sign-in, let the player complete it in their browser. [RacerMouze's plug-in](https://www.nexusmods.com/reddeadredemption2/mods/10214)
4. The plug-in needs an **ASI loader**. Keep a working `dinput8.dll` in the game folder. If a different ASI loader is present, preserve the current setup and check compatibility with the mod authors. The checks in this guide cover dinput8.dll. Continue with them once you know how that loader fits the existing setup. For a clean install, extract `dinput8.dll` from the `bin` folder of **Script Hook RDR2**. This translation plug-in needs just that file from the archive. [Alexander Blade's download](https://www.dev-c.com/rdr2/scripthookrdr2/)

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath '.\REYRUN-RDR2-LV.zip'
Get-FileHash -Algorithm SHA256 -LiteralPath '.\Latvian Translation.xml'
```

| 11 November 2026 release | Expected SHA-256 |
| --- | --- |
| REYRUN-RDR2-LV.zip | `11d7ee80bac9ac820a2c20e87f2f7fc736e3fab5ceb6e9cf7842543f9f3237da` |
| Latvian Translation.xml | `c72337da664b3999ca4fc2de2600c1e79c551b29fa1e69d79d1330485aef5045` |

## 3. Back up the old files and install the new ones

1. Inspect the folder that contains `RDR2.exe`. Record its full path. In File Explorer, show file name extensions. List every file in this directory ending in `Translation.xml`, the legacy `rdr2-translator.asi`, and any `UniversalRDR2StringTranslator.asi` or `dinput8.dll` already there. Record each original name and hash.
2. If the only base XML has the correct name and published hash, both dependencies already work and the old plug-in is absent, go straight to testing. Otherwise create a new backup folder outside the game and record its path. Create two subfolders in that backup directory. Use `before` for verified copies and `inactive` for files moved out of the game. Before replacing a file, copy it to `before` under its original name and verify its hash.
3. Keep one active base `*Translation.xml`. After verifying the copies, move conflicting XML files and any legacy `rdr2-translator.asi` to `inactive`. When replacing a plug-in, move its old copy there as well so its original filename is available in the game folder. Keep any already correct file in place. Leave other mods alone.
4. Place any missing dependencies and the exact file `Latvian Translation.xml` directly beside `RDR2.exe`. Record each file added or replaced. For an update use the new release's checksums and the same backup steps. If copying is interrupted, compare the folder against the record before resuming or restoring the previous state.

## 4. Check the installed copy

Open PowerShell in the game folder and run this read-only check. It lists the required files and all active base translations. File presence alone does not establish whether the loader and plug-in work. Check the running game next.

```powershell
'RDR2.exe','dinput8.dll','UniversalRDR2StringTranslator.asi','Latvian Translation.xml' |
    ForEach-Object { [pscustomobject]@{ File = $_; Present = Test-Path -LiteralPath $_ -PathType Leaf } }
Get-ChildItem -LiteralPath . -Force -File | Where-Object { $_.Name -like '*Translation.xml' }
Test-Path -LiteralPath '.\rdr2-translator.asi'
Get-FileHash -Algorithm SHA256 -LiteralPath '.\Latvian Translation.xml'
```

The four presence checks should read `True`, the base XML list should contain one entry, and the legacy plug-in check should read `False`. Match the installed XML checksum against the release. If the game folder or a dependency is missing, report which one.

1. Set the game's base language to **English**. In Steam, open the game's **Properties** and use the language selector. In Rockstar Games Launcher, the language selector is in **Settings**. In Epic, open the profile menu, choose **Settings**, select **English** and restart the launcher if prompted. [Rockstar's language settings](https://support.rockstargames.com/articles/6ZSsAaVCIBrg5m6Ovc5EDe/how-to-change-the-language-in-red-dead-redemption-2)
2. Launch as usual and open **Story Mode**. Open the pause menu and look for **Iestatījumi** (Settings), then **Vadība** (Controls) and **Taustiņu piesaiste** (Key mapping). Enable subtitles and play a scene with spoken dialogue. The subtitles should appear in Latvian. The characters keep their original voices.
3. If the menus stay in English, check which copy the launcher opened, the folder level, real extensions, dependencies and competing XML files. If the menus are Latvian but dialogue has no text, check the subtitle setting and try a scene with spoken dialogue. If the problem appeared after a game update, check loader and plug-in compatibility with their authors.
4. Tell the player where the translation is installed, where the backup is, and which text appeared on screen. If only the player sees the game, ask what they see under **Vadība**.

### Check the text in the running game

Record each result as “seen”, “different” or “untested”. An existing Story Mode save is fine. The player does not need to start the story again.

| Where to look | What to check |
| --- | --- |
| Pause menu and settings | Find “Karte” (Map) and “Iestatījumi” (Settings). In Settings, look for “Vadība” (Controls), “Ekrāns” (Display) or “Skaņa” (Sound). |
| Key mapping | Open “Vadība” and **enter** “Taustiņu piesaiste”. Record one action name in Latvian and its displayed key. If the player wants to test rebinding, note the original key, choose a free key, try the action, then restore the original. Keep the player's controls intact unless they agree to that test. |
| Gameplay prompt | The horse-riding tutorial shows a key symbol and a Latvian instruction about riding faster. Check that the expected key appears rather than a raw engine code such as `~INPUT_…~`. |
| Mission objective | During an active Story Mode mission, wait for an objective to appear or open that mission's objective list. Record the mission and its actual instruction to the player. Log the riding tutorial under the previous row. |
| Dialogue during player control | While the player controls a character, listen to a conversation with another character. Inspect the subtitle for that specific exchange. |
| Cinematic subtitle | Check a spoken line during a cutscene separately. One opening-scene example reads “Bet mēs zaudējām dažus cilvēkus.” Check the Latvian letters and that the whole line fits on screen. |
| Credits and chapter title | Inspect the translated job title in the credits, for example “Vides māksla”. The chapter opening displays “1. nodaļa: Kolters” beneath the original title artwork. |

The seven published screenshots show the pause menu, settings, the entrance to key mapping, the riding prompt, cinematic subtitles, job titles and the chapter opening. A mission objective, the list of actual action/key pairs, a successful rebind and dialogue during player control each need their own observation. Note the game version and visible text in the result.

## 5. Restore the previous installation

Close the game. Use the install record to move the newly added XML out of the game folder and restore the previous translation under its original name. If the previous translation used the old `rdr2-translator.asi`, move the current Universal plug-in out before restoring the old files. Restore any replaced dependency and compare its hash with the backup record. On a previously clean installation, remove the loader and plug-in added by this installation. Keep a loader or shared plug-in that another mod needs. Use a clean installation for **Red Dead Online**. REYRUN's package is for Story Mode.
