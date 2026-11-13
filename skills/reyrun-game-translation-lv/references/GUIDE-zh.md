# 用 REYRUN 把游戏翻成拉脱维亚语

![REYRUN](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/assets/reyrun.png)

想用拉脱维亚语玩《Red Dead Redemption 2》，可以到[项目网站](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/zh/)获取译文和安装说明。要翻译或校对另一款游戏，请复制整个 `reyrun-game-translation-lv` 文件夹，里面有工作步骤、五个练习和本地检查工具。

完成第一次练习后，可以尝试[更复杂的游戏文本检查](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/zh/method/techniques/)。[RDR2 项目回顾](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/zh/method/retrospective/)用实际记录说明了如何找回旧稿，以及如何查明已校对的文本还在哪一步等待写入游戏。

## 自己动手或请 AI 助手协助

在聊天中附上 `SKILL.md`、本说明和一小份原文。如果助手能从目录加载技能，请把**整个文件夹**复制到它的技能目录，刷新列表并选择 `reyrun-game-translation-lv`。保留文件的相对位置，以便打开说明和脚本。也可以手工编辑 JSONL，再用 Python 检查。练习不需要指定的 AI 服务或付费账号。

第一次练习时附上 `examples/source.jsonl`，向助手提出以下要求。

> 请阅读 SKILL.md，把五条完整记录都翻成拉脱维亚语。原有字段全部保留，每条增加 target、decision 和 reason。意思不明确的标记为 hold，并说明还需要什么信息。每行只返回一个 JSON 对象，不加前言或后记。写入游戏前我会检查译文。

将回答以 UTF-8 保存为 `my-edits.jsonl`，与 `examples/edited.jsonl` 的处理决定对照。一句话可能有几种合适的译法。读出证人的台词，检查玩家要做的动作与按键代码是否一致，并看助手把哪一条留待查证。

## 先试译五条游戏文本

在技能文件夹中打开终端，需要 Python 3.8 或更高版本。某些 Windows 安装要用 `py -3` 代替 `python`。

    python scripts/localization_tools.py prepare examples/source.jsonl --output demo-packets --max-rows 2
    python scripts/localization_tools.py validate --inputs examples/source.jsonl --edited examples/edited.jsonl --report demo-qa.json
    python -B -m unittest discover -s scripts -p "test_*.py"

第一条命令把五条记录拆成 2、2、1 三包。第二条找到五个原文 ID，其中四条为 ready，一条为 hold。得分行只有参数和分隔符，与原文相同属于预期警告。用新的报告名再检查 `my-edits.jsonl`。在测试副本中**只从译文里**删掉 `~INPUT_INTERACT~`，工具会指出出错的行，并以代码 2 退出。每次使用新的输出目录或报告名，保留先前结果。

## 准备自己游戏的原文

用该游戏专用工具导出文本，保留原文件、构建版本号、资源名和游戏内部键。每次处理同一构建且 ID 不重复的一组资源；若不同资源复用相同 ID，分开检查。输入可用 UTF-8 JSON 数组，或每行一个对象的 JSONL。原文校验值是对完整解码字符串的 UTF-8 字节计算的 SHA-256，末尾不加换行。例如 `hashlib.sha256(source.encode("utf-8")).hexdigest()`。

| 字段                                                        | 填写内容                                                                            |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `id`, `native_id`                                           | 填写稳定且唯一的工作 ID，以及已知的游戏内部键。语言包更新后行号可能变化。           |
| `source`, `source_sha`                                      | 完整原文及其校验值，包括代码、空白和换行。                                          |
| `candidate`                                                 | 填写已有草稿，没有则填空字符串。                                                    |
| `context`, `context_id`, `speaker`, `scene_id`, `branch_id` | 填写已核实的说话者、场景和玩家所见内容。不明字段可省略。ID 相邻并不能确定对话顺序。 |
| `target`, `decision`, `reason`                              | 只在编辑副本中加入拉脱维亚语译文、处理决定，以及必要的问题或理由。                  |

给不同译者分配不同 ID。每批统一使用已经确认的人名、地名和术语表，附上变格用例。如果两个人物开始从敬称改用亲称，请记下具体场景。

## 检查意思和人物口吻

以下句子为练习而写，并非 RDR2 台词。

| 原文和情境                                                              | 拉脱维亚语译法                                           | 校对时检查什么                                                                                     |
|-------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| 暂停菜单里的 “Resume”                                                   | **Turpināt**                                             | 动作名称要简短，按钮放得下。                                                                       |
| “Hold `~INPUT_INTERACT~` to open the gate.”                             | **Turi nospiestu ~INPUT_INTERACT~, lai atvērtu vārtus.** | 这里要求按住；按一下是另一个动作。                                                                 |
| “I... I didn't take it.”，一名紧张的证人说                              | **Es… Es to nepaņēmu.**                                  | 既要保留迟疑，也要保留否定。把完整台词读出来。                                                     |
| “Can you wait here?” 可能是孩子对朋友说，也可能是职员礼貌地询问陌生人。 | **Vari te pagaidīt?** / **Vai jūs varētu te pagaidīt?**  | 双方关系决定用亲称还是敬称。                                                                       |
| 物品说明中的 “Charges: {count}”，数字会变化                             | **Lādiņu skaits: {count}**                               | 若游戏只有一个文本字段，标签要适用于所有数字。如果引擎区分复数形式，就分别翻译，并用对应数字测试。 |
| 没有场景或物品信息的 “Seal”                                             | **hold**                                                 | 指海豹、印章，还是“封上”的动作？查看游戏资源或画面后再确定。                                       |

批准前将整条原文和译文读两遍。第一遍核对谁对谁做了什么，以及否定、条件怎样改变结果。第二遍检查人物口吻、词形、字幕长度和界面空间。词典可以核对词形，具体词义常要看场景。把批准的译文和校对记录一起保存，改写后重新检查。

## 检查游戏文件，记录下次从哪里继续

工具检查原文哈希、ID 是否唯一、是否漏行、已知的上下文字段，以及标为 ready 却为空的译文。它比较波浪号包围的 RDR 代码及顺序、简单的花括号占位符和常见 printf 格式。有编号的参数可以换位；无编号参数必须保持类型顺序。两个相同的 `%s` 也可能把含义对调，须人工核实各值的位置。换行数变化会产生警告。嵌套 ICU 消息、HTML、字体命令或游戏专用代码需要相应的额外检查。

`tm-index` 和 `tm-suggest` 可用已批准的译文提供建议。匹配键包含游戏、语言、原文哈希、上下文 ID，以及上下文、校对规则和术语表的版本。附上校对记录的引用、批准译文和记录文件的哈希。使用相对路径时，两条命令从同一目录执行。同一键对应不同的批准译文，会列为冲突。用 `python scripts/localization_tools.py --help` 查看命令列表。

在技能文件夹中执行下面两条命令。随附校对记录对应暂停菜单的“Turpināt”；上下文版本一致时会返回一条建议。

    python scripts/localization_tools.py tm-index examples/tm-approved.jsonl --output demo-tm.json
    python scripts/localization_tools.py tm-suggest examples/tm-query.jsonl --index demo-tm.json --output demo-suggestions.json

用游戏专用工具制作发布版，分别记录技术例外和待解决项。将旧文件备份在游戏目录之外。由一名负责人核实构建版本，再写入已批准的内容。RDR2 的 StringTable XML 可用下面命令，把路径换成实际位置。工具按游戏内部数字键和解码后的精确文本比较*整张表*，并列出两个文件的哈希。记录顺序或 XML 写法不同，即使键和文本相符，字节哈希也可能不同。

    python scripts/compare_xml.py "reviewed/Latvian Translation.xml" "installed/Latvian Translation.xml"

在相应模式里检查菜单、有时间限制的字幕、较长的物品名，以及会取不同值的变量。查看 **ā, č, ē, ģ, ī, ķ, ļ, ņ, š, ū, ž** 能否正确显示。报告问题时记录构建版本、已知 ID、原文、当前译文和场景，并附截图。保留上一个批准版本，以便恢复。

每批完成后，记录最近安装文件的哈希、已批准文本的版本和仍在等待确认的 ID。按同一时间段统计新写入的 ID 和原文可见字符数。起草、校对、导出和等待分别计时。恢复工作时先用最新报告核对游戏里的实际文件，再分配下一批。

[Latviski](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/metode/) · [关于 Reinis 和自愿支持](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/zh/#ways) · [在 Facebook 联系 Reinis](https://www.facebook.com/reinis.runcis)
