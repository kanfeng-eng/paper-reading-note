# paper-reading-note

自主精读科研论文，直接生成详细的离线 HTML 图文笔记。技能调用名为 `$paper-reading-notes`。

## 分析内容

- 在笔记开头用具体关键词和连贯句子串联研究需求、已有方法、问题现象、原因假设、设计要求、解决机制、公式、实验及边界。
- 解释研究思想、问题发现线索、解法选择与取舍，逐步展开方法和核心公式的中间推导。
- 核对图表、实验条件、消融与关键结果，展示经过检查的图表区域裁剪。
- 主动精选论证与精准表达，记录原文短摘录、上下文、关键词、推理结构、表达作用、迁移句式及出处。
- 根据证据直接整理研究启示、下一步验证计划、重点记忆和带来源的复习答案。

## 安装

在支持技能安装的 Codex 中使用以下指令。

```text
$skill-installer https://github.com/kanfeng-eng/paper-reading-note/tree/main/paper-reading-notes
```

也可以下载仓库，将完整的 `paper-reading-notes` 文件夹复制到客户端的技能目录。包内附有 frontend-design 的完整指导与许可证。实际 PDF 阅读和页面检查使用客户端的可用能力。

## 使用

提供论文 PDF 或可访问链接，并使用以下提示词。

```text
使用 $paper-reading-notes 自主精读这篇论文，直接生成详细的 HTML 图文笔记。
开头用关键词串成完整的研究逻辑，展开思想、问题发现、解法依据、公式推导和实验论证。
自主分析有价值的语言表达与逻辑推理语料，并整理有证据依据的研究启示和下一步计划。
```

默认输出到论文任务项目中的专属目录或 `论文笔记/<paper-slug>/reading-note.html`。用户指定的路径、语言和分析范围优先。完整执行规范与使用说明见 [技能文档](paper-reading-notes/README.md)。

## 本地验证

进入技能目录后执行以下命令。

```text
cd paper-reading-notes
python -m unittest discover -s tests -v
python scripts/check_output.py <reading-note.html>
```

署名检查覆盖已知宣传结尾，论文事实、公式、图表和页面阅读质量按技能流程核查。

## 来源与归属

阅读框架改编自 [paper-reading](https://github.com/kanfeng-eng/paper-reading-skill)。原始技能作者、阅读方法参考、研究入门手册的融入方式及 frontend-design 许可均记录在 [技能文档末尾的来源与归属](paper-reading-notes/README.md#来源与归属)。frontend-design 的许可证随包提供于 [LICENSE.txt](paper-reading-notes/vendor/frontend-design/LICENSE.txt)。
