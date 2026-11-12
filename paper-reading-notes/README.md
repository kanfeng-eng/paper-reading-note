# paper-reading-notes

自主精读科研论文并直接生成详细 HTML 图文笔记。以关键词串联思想、问题发现、原因假设、解法、公式、证据与边界，并主动分析精妙的论证和准确表达。

## 调用

将完整文件夹放入客户端技能目录后，使用以下提示词。

```text
使用 $paper-reading-notes 自主精读这篇论文，直接生成详细的 HTML 图文笔记。
开头用关键词和连贯句子串起研究逻辑。
展开研究思想、问题发现与原因、解法选择、公式的中间推导和实验论证。
自主精选有价值的语言与逻辑推理语料，分析关键词、上下文、表达作用和可迁移骨架。
图表使用检查过的区域裁剪，研究启示与计划标明依据和 AI 建议身份。
```

提供 PDF 或可访问的论文链接即可开始。默认详细中文，输出到任务项目中的论文专属目录或 `论文笔记/<paper-slug>/reading-note.html`。用户指定路径、语言和范围优先。研究启示、下一步计划和语料由 AI 根据核对后的材料直接整理。

## 成品与中间材料

最终成品为论文目录中的 `reading-note.html`。每条精选语料附原文局部裁剪和可复制的摘录，重要实验、主结果与消融表均附原文图表或必要段落裁剪，再展开解释。图表保留必要标注和来源，跨页内容按连续局部图呈现。

HTML 内嵌展示图片、样式和必要数学资源，单独复制后可离线阅读。本次生成的提取文本、整页图、裁剪原文件、草稿、证据记录、临时脚本与检查截图统一放入同一论文目录下的 `tmp/`。交付前按展示核对表检查图片覆盖，并实际打开独立复制的 HTML 验证阅读效果。

## 阅读与复习排版

默认采用本机微软雅黑承接中文，Segoe UI 承接英文与数字，并配置苹方、Noto Sans CJK SC、思源黑体等回退。正文默认 18 px、400 字重、1.8 行高，正文栏约 35–40 个汉字宽。这些是本技能根据资料采用的设计默认值，用户阅读偏好优先。HTML 简短标注首选字体、正文大小和行高，并检查离线回退、窄屏、200% 缩放及用户覆盖文字间距后的显示。

## 包内资源

`SKILL.md` 定义执行流程。`references` 提供深度分析、表达语料和 HTML 规范。`assets` 提供内容模板。`vendor/frontend-design` 提供完整的页面设计指导与许可证。`scripts/check_output.py` 检查已知宣传署名形式，`tests` 覆盖相应检查行为。

本包所需的阅读规则和模板保存在包内，PDF 阅读与页面检查使用所在客户端的可用能力。最终 HTML 内嵌必要展示资源。来源受限、符号不清或核查工具不可用时，笔记记录实际覆盖和影响。

## 验证

```text
python -m unittest discover -s tests -v
python scripts/check_output.py <reading-note.html>
```

脚本检测已知署名形式。科研事实、推理、公式、图表裁剪及浏览器阅读质量按工作流核查。完整论文上的实际输出质量需要相应的论文任务验证。

## 来源与归属

- 阅读框架和署名检查代码改编自用户定制的 [paper-reading](https://github.com/kanfeng-eng/paper-reading-skill/tree/4ee932fa5def5c67e7acf0c9b40f520419c67736/paper-reading)，保留其关键词逻辑主线、问题发现与解法依据、阅读卡、证据核查及语料分析思想，并形成自主完成笔记的独立流程。
- 原技能源自 [N-tongxue/norman-skill](https://github.com/N-tongxue/norman-skill/tree/main/norman-paper-reading)。原作者为 N同学，小红书账号为 N同学，B站与抖音账号为耐心的N同学。本包采用自行编写的本地工作流与客户端阅读能力。
- 《计算机视觉科研入门》手册在原定制技能中形成的关键词论证主线、12 项阅读卡及收益、机制、代价与失败分析规则，已融入包内规范。
- [S. Keshav 的 How to Read a Paper](https://systems.cs.columbia.edu/ds2-class/papers/keshav-paper.pdf)，原技能采用的分层阅读参考。
- [Jason Eisner 的 How to Read a Technical Paper](https://www.cs.jhu.edu/~jason/advice/how-to-read-a-paper.html)，原技能采用的理解难点与知识联系参考。
- [Michael Nielsen 的 Augmenting Long-term Memory](https://augmentingcognition.com/ltm.html)，原技能采用的带上下文复习问题参考。
- HTML 设计指导来自包内 [frontend-design](vendor/frontend-design/SKILL.md)，许可证见 [Apache-2.0](vendor/frontend-design/LICENSE.txt)。
- [微软 Microsoft YaHei 字体说明](https://learn.microsoft.com/en-us/typography/font-list/microsoft-yahei)，介绍其中文屏幕显示与小字号辨认特性。
- [USWDS Typography](https://designsystem.digital.gov/components/typography/)，用于结合字体、字号、行宽和间距配置阅读排版。
- [W3C 中文排版需求](https://www.w3.org/TR/clreq/)，用于中文行长与行距的参考。
- [WCAG 1.4.8 Visual Presentation](https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation)，用于参考行宽、对齐与放大后的阅读要求。
- [WCAG 1.4.12 Text Spacing](https://www.w3.org/WAI/WCAG21/Understanding/text-spacing)，用于用户覆盖文字间距后的适应性检查。
