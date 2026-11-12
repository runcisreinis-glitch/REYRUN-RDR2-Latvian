@echo off
setlocal
set "REYRUN_XML_ACTION=install"
set "REYRUN_XML_LAUNCHER=%~f0"
set "REYRUN_XML_GAME=%~1"
powershell.exe -NoLogo -NoProfile -STA -Command "$s=[IO.File]::ReadAllText($env:REYRUN_XML_LAUNCHER,[Text.Encoding]::UTF8); $start=$s.IndexOf([char]10+'#REYRUN_XML_BODY'); if($start -lt 0){exit 1}; & ([ScriptBlock]::Create($s.Substring($start+1)))"
set "result=%errorlevel%"
if not defined REYRUN_XML_GAME (
    if "%result%"=="0" (timeout /t 8 >nul) else (pause)
)
exit /b %result%
#REYRUN_XML_BODY
# REYRUN Story Mode setup. Verified official downloads and per-user staging.
$ErrorActionPreference = 'Stop'
$xmlName = 'Latvian Translation.xml'
$expected = 'c72337da664b3999ca4fc2de2600c1e79c551b29fa1e69d79d1330485aef5045'
$release = 'https://raw.githubusercontent.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/3de3d4df5b4cbf415bc1f0e56cec3adfea8d4258/Latvian%20Translation.xml'
$language = (Get-UICulture).TwoLetterISOLanguageName
$locale = if($language -eq 'lv'){'lv'}elseif($language -eq 'ru'){'ru'}else{'en'}
function Message([string]$lv,[string]$en,[string]$ru) {
    if($locale -eq 'lv'){return $lv}; if($locale -eq 'ru'){return $ru}; return $en
}
$guide = 'https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site' + @{en='/en/install/';ru='/ru/install/';lv='/uzstadisana/'}[$locale]
function FileHash([string]$file) { (Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLowerInvariant() }
function AssertLocal([string]$path) {
    if($path -notmatch '^[A-Za-z]:\\'){throw 'Select a local Windows drive.'}
    for($p=$path;$p;$p=[IO.Path]::GetDirectoryName($p)){
        if(Test-Path -LiteralPath $p){
            $item=Get-Item -LiteralPath $p -Force
            if(($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0){throw ('Linked path: '+$p)}
        }
    }
}
function CheckGameClosed {
    if(Get-Process -Name RDR2 -ErrorAction SilentlyContinue){
        throw (Message 'Aizver Red Dead Redemption 2 un palaid failu vēlreiz.' 'Close Red Dead Redemption 2 and open this file again.' 'Закройте Red Dead Redemption 2 и запустите этот файл ещё раз.')
    }
}
function Get-EpicGameFolders([string]$programDataRoot) {
    if (!$programDataRoot) { return }
    $directory = Join-Path $programDataRoot 'Epic\EpicGamesLauncher\Data\Manifests'
    $manifests = Get-ChildItem -LiteralPath $directory -File -Filter '*.item' -ErrorAction SilentlyContinue
    foreach ($manifest in $manifests) {
        if ($manifest.Length -gt 2MB) { continue }
        try {
            $entry = [IO.File]::ReadAllText($manifest.FullName) | ConvertFrom-Json
            if ($entry.DisplayName -isnot [string] -or $entry.DisplayName.Trim() -ine 'Red Dead Redemption 2') { continue }
            if ($entry.InstallLocation -isnot [string] -or $entry.InstallLocation -notmatch '^[A-Za-z]:[\\/]') { continue }
            $folder = [IO.Path]::GetFullPath($entry.InstallLocation)
            if ([IO.File]::Exists([IO.Path]::Combine($folder, 'RDR2.exe'))) { $folder }
        } catch {
            # Ignore incomplete or stale Epic records and keep looking.
        }
    }
}
function ChooseGame {
    if($env:REYRUN_XML_GAME){return [IO.Path]::GetFullPath($env:REYRUN_XML_GAME)}
    $candidates = @(Get-EpicGameFolders $env:ProgramData)
    if(${env:ProgramFiles(x86)}){$candidates+=Join-Path ${env:ProgramFiles(x86)} 'Steam\steamapps\common\Red Dead Redemption 2'}
    $steam=(Get-ItemProperty -LiteralPath 'HKCU:\Software\Valve\Steam' -ErrorAction SilentlyContinue).SteamPath
    if($steam){
        $candidates+=Join-Path $steam 'steamapps\common\Red Dead Redemption 2'
        $libraries=Join-Path $steam 'steamapps\libraryfolders.vdf'
        if([IO.File]::Exists($libraries)){
            foreach($match in [regex]::Matches([IO.File]::ReadAllText($libraries),'"path"\s+"([^"]+)"')){
                $lib=$match.Groups[1].Value.Replace('\\','\')
                if($lib -match '^[A-Za-z]:[\\/]'){$candidates+=Join-Path $lib 'steamapps\common\Red Dead Redemption 2'}
            }
        }
    }
    foreach($hive in @('HKLM:\SOFTWARE','HKLM:\SOFTWARE\WOW6432Node','HKCU:\Software')){
        $r=Get-ItemProperty -LiteralPath ($hive+'\Rockstar Games\Red Dead Redemption 2') -ErrorAction SilentlyContinue
        foreach($key in @('InstallFolder','InstallFolderEpic','InstallFolderSteam','InstallLocation')){if($r.$key){$candidates+=$r.$key}}
    }
    $matches=@($candidates|Where-Object {$_ -and [IO.File]::Exists((Join-Path $_ 'RDR2.exe'))}|ForEach-Object {[IO.Path]::GetFullPath($_).TrimEnd('\')}|Sort-Object -Unique)
    if($matches.Count -eq 1){return $matches[0]}
    Add-Type -AssemblyName System.Windows.Forms
    $pick=New-Object System.Windows.Forms.FolderBrowserDialog
    $pick.Description=Message 'Izvēlies mapi ar RDR2.exe.' 'Select the folder that contains RDR2.exe.' 'Выберите папку с RDR2.exe.'
    try {if($pick.ShowDialog() -ne 'OK'){throw (Message 'Atcelts.' 'Cancelled.' 'Отменено.')}; return $pick.SelectedPath}
    finally {$pick.Dispose()}
}
function ValidatePrerequisites {
    $checks=@(
        @('UniversalRDR2StringTranslator.asi','e88ec57c9e6ef03f42ab0218a0fb98fd065927ff9859ed49e5f1ef601c6871f6','https://www.nexusmods.com/reddeadredemption2/mods/10214'),
        @('dinput8.dll','031a3e5576d91dce1e438d36b9a3d462c7334ab4791990a8ff1e3ddc0e132daf','https://github.com/ThirteenAG/Ultimate-ASI-Loader')
    )
    $issues=@()
    foreach($row in $checks){
        $file=Join-Path $game $row[0];AssertLocal $file
        if(![IO.File]::Exists($file)){
            $issues+=(Message 'Trūkst faila' 'Missing file' 'Отсутствует файл')+' '+$row[0]+'  '+$row[2]
        } elseif((FileHash $file) -ne $row[1]){
            $issues+=(Message 'Cita faila versija' 'Unrecognized file version' 'Другая версия файла')+' '+$row[0]+'  '+$row[2]
        }
    }
    if($issues.Count){throw ($issues -join [Environment]::NewLine)}
}
function VerifyBaseFiles {
    $conflicts=@(Get-ChildItem -LiteralPath $game -Force | Where-Object {($_.Name -like '*Translation.xml' -and $_.Name -ine $xmlName) -or $_.Name -ieq 'rdr2-translator.asi'})
    if($conflicts){throw ((Message 'Mapē ir cits pamata tulkojums vai vecais spraudnis. Skat. rezerves kopijas norādes.' 'Another base translation or the old plug-in is present. See the backup instructions.' 'В папке есть другой основной перевод или старый плагин. См. инструкцию по резервной копии.')+' '+(($conflicts|ForEach-Object {$_.Name}) -join ', '))}
}
function ReadState {
    if(![IO.File]::Exists($journal)){return $null}
    $r=Get-Content -LiteralPath $journal -Encoding UTF8 -Raw|ConvertFrom-Json
    if($r.schema -ne 1 -or $r.folder -ine $game -or $r.release -ne $expected -or ($r.original -ne '' -and $r.original -notmatch '^[a-f0-9]{64}$')){throw 'Unrecognized installation record.'}
    if($r.original -and (![IO.File]::Exists($backup) -or (FileHash $backup) -ne $r.original)){throw 'Backup checksum mismatch.'}
    return $r
}
function SaveState([string]$hash) {
    if($hash){
        if([IO.File]::Exists($backup)){if((FileHash $backup) -ne $hash){throw 'A different backup already exists.'}}
        else {
            $tmp=Join-Path $store ('backup-'+[guid]::NewGuid().ToString('n')+'.tmp')
            try{[IO.File]::Copy($destination,$tmp);if((FileHash $tmp) -ne $hash){throw 'Backup checksum mismatch.'};[IO.File]::Move($tmp,$backup)}
            finally{if([IO.File]::Exists($tmp)){[IO.File]::Delete($tmp)}}
        }
    }
    $tmp=Join-Path $store ('record-'+[guid]::NewGuid().ToString('n')+'.tmp')
    try{
        $r=@{schema=1;folder=$game;original=$hash;release=$expected} | ConvertTo-Json -Compress
        [IO.File]::WriteAllText($tmp,$r);[IO.File]::Move($tmp,$journal)
    }finally{if([IO.File]::Exists($tmp)){[IO.File]::Delete($tmp)}}
}
function CurrentHash { if([IO.File]::Exists($destination)){return (FileHash $destination)};return '' }
function ApplyXml {
    CheckGameClosed
    $restore=$env:REYRUN_XML_ACTION -eq 'restore'
    if(!$restore){ValidatePrerequisites}
    VerifyBaseFiles
    $r=ReadState
    $old=CurrentHash
    if($restore){
        if(!$r){throw (Message 'Šai mapei nav REYRUN uzstādīšanas ieraksta.' 'No REYRUN install record for this folder.' 'Для этой папки нет записи об установке REYRUN.')}
        if($old -eq $r.original){return (Message 'Iepriekšējais stāvoklis jau ir atjaunots.' 'The previous state is already restored.' 'Прежнее состояние уже восстановлено.')}
        if($old -ne $expected){throw 'The installed XML has changed. Keep the edited file and inspect the backup.'}
    } else {
        if($old -eq $expected){return (Message 'Latviešu XML jau ir uzstādīts. Kontrolsumma sakrīt.' 'The Latvian XML is already installed. Its checksum matches.' 'Латышский XML уже установлен. Контрольная сумма совпадает.')}
        if($r -and $r.original -ne $old){throw 'The current XML differs from the installation record.'}
    }
    $pending=Join-Path $game ('.reyrun-'+[guid]::NewGuid().ToString('n')+'.tmp')
    try{
        if(!$restore){
            [IO.File]::Copy((Join-Path $stage $xmlName),$pending)
            if((FileHash $pending) -ne $expected){throw 'Translation SHA-256 mismatch.'}
            if(!$r){SaveState $old}
        }elseif($r.original){[IO.File]::Copy($backup,$pending);if((FileHash $pending) -ne $r.original){throw 'Backup checksum mismatch.'}}
        CheckGameClosed
        VerifyBaseFiles
        if((CurrentHash) -ne $old){throw 'The XML changed during installation. Try again.'}
        if($restore -and !$r.original){[IO.File]::Delete($destination)}
        elseif($old){[IO.File]::Replace($pending,$destination,[NullString]::Value)}
        else{[IO.File]::Move($pending,$destination)}
        $wanted=if($restore){$r.original}else{$expected}
        if((CurrentHash) -ne $wanted){throw 'Final file verification failed.'}
    }finally{if([IO.File]::Exists($pending)){[IO.File]::Delete($pending)}}
    if($restore){return (Message 'Iepriekšējais stāvoklis ir atjaunots.' 'Previous state restored.' 'Прежнее состояние восстановлено.')}
    return (Message 'Latviešu XML ir uzstādīts un pārbaudīts. Sāc stāsta režīmu.' 'Latvian XML installed and verified. Start Story Mode.' 'Латышский XML установлен и проверен. Запустите сюжетный режим.')
}
# All downloads and resumable work stay in the user's profile. Only checked files
# are moved into the game. The XML journal and restore behavior are shared with
# the established REYRUN XML installer.
$ProgressPreference = 'SilentlyContinue'
$asiName = 'UniversalRDR2StringTranslator.asi'
$loaderName = 'dinput8.dll'
$asiHash = 'e88ec57c9e6ef03f42ab0218a0fb98fd065927ff9859ed49e5f1ef601c6871f6'
$loaderHash = '031a3e5576d91dce1e438d36b9a3d462c7334ab4791990a8ff1e3ddc0e132daf'
$packageHash = '11d7ee80bac9ac820a2c20e87f2f7fc736e3fab5ceb6e9cf7842543f9f3237da'
$author = 'https://www.nexusmods.com/reddeadredemption2/mods/10214?tab=files'
function Matches([string]$file,[string]$digest) {
    return ([IO.File]::Exists($file) -and (FileHash $file) -eq $digest)
}
function TakeCheckedFile([string]$source,[string]$dest,[string]$digest) {
    if (!(Matches $source $digest)) { return $false }
    if (Matches $dest $digest) { return $true }
    $tmp = Join-Path $stage ([guid]::NewGuid().ToString('n')+'.tmp')
    try {
        [IO.File]::Copy($source,$tmp)
        if (!(Matches $tmp $digest)) { throw 'File changed during staging.' }
        if ([IO.File]::Exists($dest)) { [IO.File]::Replace($tmp,$dest,[NullString]::Value) }
        else { [IO.File]::Move($tmp,$dest) }
        return $true
    } finally { if ([IO.File]::Exists($tmp)) { [IO.File]::Delete($tmp) } }
}
function DownloadChecked([string]$url,[string]$dest,[string]$digest) {
    if (Matches $dest $digest) { return $true }
    $download = Join-Path $stage ([guid]::NewGuid().ToString('n')+'.download')
    try {
        Invoke-WebRequest -UseBasicParsing -Uri $url -OutFile $download -TimeoutSec 45
        return (TakeCheckedFile $download $dest $digest)
    } catch [System.Net.WebException] { return $false }
    catch [System.Net.Http.HttpRequestException] { return $false }
    finally { if ([IO.File]::Exists($download)) { [IO.File]::Delete($download) } }
}
function GetCheckedMember([string]$archive,[string]$name,[string]$digest) {
    $dest = Join-Path $stage $name
    if (Matches $dest $digest) { return $true }
    $inputZip = [IO.Compression.ZipFile]::OpenRead($archive)
    try {
        $members = @($inputZip.Entries | Where-Object { $_.Name -ieq $name -and $_.Length -gt 0 -and $_.Length -lt 64MB })
        foreach ($member in $members) {
            $tmp = Join-Path $stage ([guid]::NewGuid().ToString('n')+'.part')
            try {
                [IO.Compression.ZipFileExtensions]::ExtractToFile($member,$tmp,$false)
                if (TakeCheckedFile $tmp $dest $digest) { return $true }
            } finally { if ([IO.File]::Exists($tmp)) { [IO.File]::Delete($tmp) } }
        }
    } finally { $inputZip.Dispose() }
    return $false
}
function PrepareXml {
    $dest=Join-Path $stage $xmlName
    if (Matches $dest $expected) { return }
    $nextToLauncher=Join-Path ([IO.Path]::GetDirectoryName($env:REYRUN_XML_LAUNCHER)) $xmlName
    if (TakeCheckedFile $nextToLauncher $dest $expected) { return }
    $zip=Join-Path $stage 'REYRUN-RDR2-LV.zip'
    $urls=@('https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip',
            'https://raw.githubusercontent.com/runcisreinis-glitch/REYRUN-RDR2-Latvian/3de3d4df5b4cbf415bc1f0e56cec3adfea8d4258/REYRUN-RDR2-LV.zip')
    foreach ($url in $urls) {
        if ((DownloadChecked $url $zip $packageHash) -and (GetCheckedMember $zip $xmlName $expected)) { return }
    }
    if (DownloadChecked $release $dest $expected) { return }
    throw (Message 'Neizdevās saņemt pārbaudītu tulkojumu. Palaidiet šo pašu failu vēlreiz.' 'The verified translation could not be downloaded. Reopen this same file to resume.' 'Не удалось скачать проверенный перевод. Для продолжения снова откройте этот файл.')
}
function PreparePlugin([string]$name,[string]$digest) {
    $installed=Join-Path $game $name
    AssertLocal $installed
    if ([IO.File]::Exists($installed)) {
        if (!(Matches $installed $digest)) { throw ("Unknown existing version; nothing will replace it: "+$name) }
        return
    }
    $dest=Join-Path $stage $name
    if (Matches $dest $digest) { return }
    $dirs=@([IO.Path]::GetDirectoryName($env:REYRUN_XML_LAUNCHER),$inbox)
    foreach ($dir in $dirs) {
        if (TakeCheckedFile (Join-Path $dir $name) $dest $digest) { return }
        $files=@(Get-ChildItem -LiteralPath $dir -File -Filter '*.zip' -ErrorAction SilentlyContinue |
            Where-Object { $_.Length -lt 96MB -and $_.BaseName -match '(?i)translator|string|10214|ultimate.asi.loader' })
        foreach ($f in $files) {
            try { if (GetCheckedMember $f.FullName $name $digest) { return } } catch [IO.InvalidDataException] {}
        }
    }
    if ($name -eq $asiName) {
        $msg=Message 'Vajadzīgs spraudņa autora fails. Saglabājiet autora ZIP vai pašu .asi norādītajā mapē un vēlreiz atveriet šo pašu programmu.' 'The author supplies this plug-in. Save the official ZIP or extracted .asi in the folder shown and reopen this same program.' 'Сохраните ZIP автора или извлечённый файл .asi в указанную папку и снова откройте эту же программу.'
        throw ($msg+[Environment]::NewLine+$author+[Environment]::NewLine+$inbox)
    }
    $url='https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases/download/v9.7.4/'
    $sources=@(@('Ultimate-ASI-Loader-NoPDB_x64.zip','e5860e7d9a1805267535b65749575b5e406cc6ea3325c7392189c578815045d1'),
               @('Ultimate-ASI-Loader_x64.zip','8272d83b2692662098746f2d0ad0e2d85f3c8358ab1d63f75fbe835c2c8135fd'))
    foreach ($s in $sources) {
        $zip=Join-Path $stage $s[0]
        if ((DownloadChecked ($url+$s[0]) $zip $s[1]) -and (GetCheckedMember $zip $name $digest)) { return }
    }
    throw ('Verified x64 loader required: '+$url+[Environment]::NewLine+$inbox)
}
function InstallMissingDependency([string]$name,[string]$digest) {
    $target=Join-Path $game $name
    if (Matches $target $digest) { return }
    if ([IO.File]::Exists($target)) { throw ('Existing file changed: '+$name) }
    $marker=Join-Path $store ('added-'+$name+'.txt')
    AssertLocal $marker
    if ([IO.File]::Exists($marker) -and [IO.File]::ReadAllText($marker) -ne $digest) { throw 'Unrecognized dependency record.' }
    $tmp=Join-Path $game ('.reyrun-'+[guid]::NewGuid().ToString('n')+'.tmp')
    try {
        [IO.File]::Copy((Join-Path $stage $name),$tmp)
        if (!(Matches $tmp $digest)) { throw ('Invalid staged file: '+$name) }
        CheckGameClosed
        [IO.File]::Move($tmp,$target)
        $addedThisRun.Add($name)
        [IO.File]::WriteAllText($marker,$digest)
    } finally { if ([IO.File]::Exists($tmp)) { [IO.File]::Delete($tmp) } }
}
function RunSetup {
    CheckGameClosed
    VerifyBaseFiles
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12
    $stage=Join-Path $store 'staged'
    $inbox=Join-Path $env:LOCALAPPDATA 'REYRUN\RDR2-Setup\Downloads'
    foreach ($dir in @($stage,$inbox)) { AssertLocal $dir;[void][IO.Directory]::CreateDirectory($dir) }
    $addedThisRun=New-Object 'System.Collections.Generic.List[string]'
    PreparePlugin $asiName $asiHash
    PreparePlugin $loaderName $loaderHash
    if (!(Matches $destination $expected)) { PrepareXml }
    try {
        InstallMissingDependency $loaderName $loaderHash
        InstallMissingDependency $asiName $asiHash
        ApplyXml
    } catch {
        foreach ($name in $addedThisRun) {
            $digest=if ($name -eq $loaderName) {$loaderHash} else {$asiHash}
            $target=Join-Path $game $name
            if (Matches $target $digest) {
                [IO.File]::Delete($target)
                $marker=Join-Path $store ('added-'+$name+'.txt')
                if ([IO.File]::Exists($marker)) { [IO.File]::Delete($marker) }
            }
        }
        throw
    }
}

try{
    $game=[IO.Path]::GetFullPath((ChooseGame)).TrimEnd('\')
    $exe=Join-Path $game 'RDR2.exe';AssertLocal $exe
    if(![IO.File]::Exists($exe)){throw 'RDR2.exe not found.'}
    $destination=Join-Path $game $xmlName;AssertLocal $destination
    if([IO.Directory]::Exists($destination)){throw 'A directory occupies the XML filename.'}
    $key=[Security.Cryptography.SHA256]::Create()
    try{$identity=[BitConverter]::ToString($key.ComputeHash([Text.Encoding]::UTF8.GetBytes($game.ToUpperInvariant()))).Replace('-','').ToLowerInvariant()}finally{$key.Dispose()}
    $store=Join-Path $env:LOCALAPPDATA ('REYRUN\RDR2-XML\'+$identity)
    if(($store+'\').StartsWith($game+'\',[StringComparison]::OrdinalIgnoreCase)){throw 'Backup must be outside the game folder.'}
    $backup=Join-Path $store 'previous.xml';$journal=Join-Path $store 'installation.json'
    AssertLocal $journal; AssertLocal $backup
    [void][IO.Directory]::CreateDirectory($store)
    $lockPath=Join-Path $store 'install.lock';AssertLocal $lockPath
    $lock=[IO.File]::Open($lockPath,[IO.FileMode]::OpenOrCreate,[IO.FileAccess]::ReadWrite,[IO.FileShare]::None)
    try{Write-Output (RunSetup);Write-Output $game;Write-Output $store}finally{$lock.Dispose()}
    exit 0
 }catch [UnauthorizedAccessException]{
    [Console]::Error.WriteLine((Message 'Windows liedza piekļuvi. Sagatavotie faili ir saglabāti. Atļaujiet konkrēto kopēšanu vai ar spēles palaidēju pārvietojiet spēli uz sev rakstāmu mapi, pēc tam atveriet šo pašu failu.' 'Windows denied the write. The staged files are saved. Approve the specific copy, or use the game launcher to move the game to a writable library, then reopen this file.' 'Windows отказала в записи. Подготовленные файлы сохранены. Разрешите нужное копирование или перенесите игру через её лаунчер в доступную для записи папку, затем снова откройте этот файл.'))
    exit 1
}catch{[Console]::Error.WriteLine($_.Exception.Message);[Console]::Error.WriteLine($guide);exit 1}
