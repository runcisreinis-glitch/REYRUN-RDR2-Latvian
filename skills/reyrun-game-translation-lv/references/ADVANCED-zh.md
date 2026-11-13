# 在场景、菜单和另一种引擎中测试游戏译文

[Latviski](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/metode/panemieni/) · [从五个示例开始](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/zh/method/)

选一个可以重新进入的场景，记录构建版本、存档点、说话者和听者、玩家上一步选择以及文本键。随附的 Godot 项目是可重复使用的原创测试示例。RDR2 实例来自公开的 REYRUN 译文。

## 同一个英文词何时需要不同的拉脱维亚语译法

背包里的 **Open** 按钮译为 **Atvērt**。**Konteiners**（容器）旁的状态用 **Atvērts**，阴性名词 **Lāde**（箱子）旁要用 **Atvērta**。保留不同的键，记录各状态修饰的名词。翻译记忆中的每条译文都应对应批准时的用途和语境。

| 文本类型 | 翻译前收集的依据                                                                           | 编辑怎样检查                                                         |
|----------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| 分支对话 | 记录说话者、听者、场景、分支及这个分支的前后台词，并注明上下文依据。                       | 实际选择两种回答。拒绝是否仍明确是拒绝？亲称或敬称是否符合双方关系？ |
| 任务目标 | 查明谁要行动、携带什么或跟随谁，以及目的地和时限。分别找到任务开始、进度、成功和失败状态。 | 完成一步后打开日志，与屏幕提示对照。动作和对象应一致。               |
| 操作提示 | 确定操作是单击、连按、按住还是松开，并找出动态绘制按键图标的部分。                         | 用默认键和改绑的键分别重试同一场景。支持手柄时也要测试。             |
| 限时对白 | 记录实际显示时长、中断、说话者切换、声音重叠，以及已烘焙到图像中的文字。                   | 先听原声，再静音观看。能判断是谁说话，并在下一条出现前读完整句吗？   |

剧本、对话数据或录音都无法确定含义时，在该行留一个具体问题，例如**“这是打开箱子的按钮，还是箱子当前的状态？”**。其他已确定含义的行可以继续校对。[IGDA 本地化小组的游戏本地化指南](https://igda.org/resources-archive/best-practices-for-game-localization/)

## 哪些内容由引擎动态显示

在 2026 年 11 月 11 日发布的 `Latvian Translation.xml` 中查找这些游戏内部 ID。[下载 REYRUN 译文](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/download/REYRUN-RDR2-LV.zip)

| XML ID       | 文件中的原样文本                                                                | 核查内容                                                         |
|--------------|---------------------------------------------------------------------------------|------------------------------------------------------------------|
| `0x9D9BAF33` | `Īsi spiediet ~INPUT_HORSE_SPRINT|PromptId=INPUT_WNT1_SPEEDUP~, lai jātu ātrāk` | 保留完整控制标记，包括竖线之后的全部内容。游戏在此绘制按键图标。 |
| `0x046E5281` | `Turiet ~INPUT_HORSE_SPRINT|PromptId=INPUT_WNT1_SPEEDUP~, lai jātu ātrāk`       | 标记相同，但这里要按住。照搬上一行会改变操作要求。               |
| `0x1C4EF867` | `Seko ~o~Dačam~s~`                                                              | 保留目标周围的高亮，并使用人物姓名的与格。多个 ID 使用这句话。   |

记录原键位并重新进入场景，改绑一个空闲键，再次触发提示并实际操作。对照**控制菜单、提示图标和真正触发的动作**，然后恢复原键位。每一种准备报告为通过的输入设备都要实测。[Microsoft XAG 107](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107)

## 字幕时长和拉脱维亚语字符

选择包含短呼声、较长回应和画外说话者的场景。记录每条字幕的起止、可见文本和换行。用字符数除以秒数筛查过密字幕，例如 42 个字符显示 2.1 秒，即每秒 20 字。用实际字号和正常速度，结合玩家同时还要操作游戏来判断。若只能改文本，可删重复，但保留否定、听者、对象和条件。

测试最小支持窗口、常用游戏分辨率和最大字幕设置，查看字幕是否与目标、选项或教程重叠。区分图像里的固定文字和实时字幕。RDR2 的章节图保留 **Colter**，下方另有 **1. nodaļa: Kolters**。支持声音字幕时，还要查时间及玩家能否辨认声音方向。[Microsoft XAG 104](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104)

在测试构建启用伪本地化。添加重音或拉长字符串，可发现漏接本地化的文字、被裁掉的末尾和过窄的按钮。切回拉脱维亚语，在每种实际使用的字体和样式里看 **ĀČĒĢĪĶĻŅŠŪŽ āčēģīķļņšūž**。检查全大写菜单、斜体、折行说明和动态插入的人名。遇到缺字方框就定位该屏幕的字体或图集。在文本表导出的字符集中补上运行时变量可能带入的字符，再打开同一场景。[Godot 伪本地化](https://docs.godotengine.org/en/latest/tutorials/i18n/pseudolocalization.html) · [Unity 字符集](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/StringTables.html)

## 在 Godot 中测试两种语境和三种数量形式

`examples/godot-lv` 中的项目附带真实 gettext PO 目录和测试。**Open** 分两种语境，整数有三种词形，如 **1 diennakts**、**2 diennaktis**、**11 diennakšu**、**21 diennakts**。各形式的索引由 PO 文件头指定，移植到其他目录前先查看。小数还有其他规则，要用游戏实际使用的格式化器单独测试。[Unicode CLDR 拉脱维亚语规则](https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html#lv) · [Godot gettext 目录](https://docs.godotengine.org/en/stable/tutorials/i18n/localization_using_gettext.html)

在技能目录中用 Godot 4.6.3 运行下面两条命令。必要时将 `godot` 换成程序完整路径。只涉及练习项目及其本地导入缓存。

    godot --headless --path examples/godot-lv --import
    godot --headless --path examples/godot-lv --script res://check.gd

实测结果为**两种语境、12 个整数值、零失败**。要复现失败情况，把示例复制到新目录，在 `lv.po` 中把动作译文从 `Atvērt` 改为 `Vaļā`，改用副本路径重跑两条命令。检查会指出 `inventory/action`，以状态码 1 退出。即使目录可以正常导入，它也能发现按钮词义错译。字体渲染仍需在图形界面中另测。

## 把检查方法用于自己的游戏

| 项目                              | 首次导入                                                                                                                                           | 游戏内观察点                                                                                                                                                                                                                                                                                                |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 可访问源码的 Godot 项目           | 把 `lv.po` 加入项目翻译，将 `tr()` 的语境参数与目录的 `msgctxt` 对应。涉及数量时使用 `tr_n()`。                                                    | 切换到 `lv`，打开同一英文词的两个使用场景，测试示例中的整数值。                                                                                                                                                                                                                                             |
| 使用 Localization 包的 Unity 项目 | 使用项目现有的 String Table Collection，保留共享键和语言表。查看哪些项使用 Smart Strings，传入实际的运行时参数。                                   | 用两种界面尺寸测试，改变数量。若出现花括号或缺字，检查格式化器、文本表及当前字体。[Unity 字符串表](https://docs.unity3d.com/Packages/com.unity.localization@1.5/manual/StringTables.html)                                                                                                                   |
| 可访问源码的 Unreal 项目          | 在 Dashboard 选择正确的本地化目标和语言文化，依次执行 Gather → Export → Import → Compile。处理 Dialogue Waves 时区分说话者、听者和可选的字幕覆盖。 | 测试对一人说话的变体和另一个可用分支，运行会加载已编译本地化目标的游戏构建。[Epic 本地化工具](https://dev.epicgames.com/documentation/en-us/unreal-engine/localization-tools-in-unreal-engine) · [Epic 对话资源](https://dev.epicgames.com/documentation/unreal-engine/asset-localization-in-unreal-engine) |
| 有明确翻译插件说明的已发行游戏    | 确定该游戏及构建支持的导入工具。备份测试位置，写入若干已知 ID，再读回结果。                                                                        | 重新打开可复现的场景并检查对应键。RDR2 的 XML 结构和文件名只适用于它的特定插件。                                                                                                                                                                                                                            |

游戏更新后，按原文和语境核对同一 ID，审查新增文本、文本变化和用途变化。已删除的 ID 保留在上一版记录。先用实际运行参数重玩受影响场景。报告注明**构建、语言、资源及 ID、场景或存档、设置、预期、实测、截图或视频时间点**。文本表校验、字体显示和单次游玩须分别记录。

[阅读翻译技能指南](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/repository/skills/reyrun-game-translation-lv/references/GUIDE-zh.md) · [关于 Reinis 和自愿支持](https://reyrun-rdr2-latviski.runcisreinis.chatgpt.site/zh/#ways)

## 翻译整款游戏之前

列出菜单、任务目标、对白字幕、按键提示、章节标题和制作人员名单的资源，为每类记录文件、稳定键和场景。区分可编辑字符串、运行时变量、图像、烘焙到视频中的文字和缺失源材料。导出、编辑并重新导入少量样本，再打开同一场景。

对于使用人数少的语言，请熟悉该语言变体的使用者结合场景审读，记录称谓、人名和地域用语。检查每种字体所需字形、数量形式和换行。分别测试任务开始、成功和失败；通过改键区分会变化的图标与“点击”或“按住”的译文。

修改 XML 无法重绘已嵌入图像或视频的标题。RDR2 截图中原文“Chapter I · Colter”依然可见，下方另有“1. nodaļa: Kolters”。制作人员名单保留人名，有可编辑文本的职务才翻译。逐项记录哪些资源缺少可编辑的源文件。
