import unittest

from scripts.check_output import has_tool_signature


class OutputSignatureTests(unittest.TestCase):
    def test_chinese_markdown_footer(self):
        self.assertTrue(has_tool_signature(
            "分析采用 norman-paper-reading 技能｜作者：N同学"
        ))

    def test_english_footer(self):
        self.assertTrue(has_tool_signature(
            "Analysis performed using the norman-paper-reading skill"
        ))

    def test_renamed_skill_footer(self):
        self.assertTrue(has_tool_signature(
            "Analysis performed using paper-reading"
        ))

    def test_html_entities_and_inline_markup(self):
        self.assertTrue(has_tool_signature(
            "<footer>Analysis&nbsp;performed <b>using</b> "
            "the norman-paper-reading skill</footer>", is_html=True
        ))

    def test_new_skill_chinese_footer(self):
        self.assertTrue(has_tool_signature(
            "分析采用 paper-reading-notes 技能"
        ))

    def test_new_skill_english_footer(self):
        self.assertTrue(has_tool_signature(
            "Analysis performed using the paper-reading-notes skill"
        ))

    def test_preserves_scholarly_sources(self):
        self.assertFalse(has_tool_signature(
            "<section>He et al. 2015, Figure 1, arXiv:1512.03385. "
            "Source method: norman-paper-reading.exe extract.</section>",
            is_html=True,
        ))

    def test_ordinary_research_text(self):
        self.assertFalse(has_tool_signature(
            "Residual learning improves optimization under the reported conditions."
        ))


if __name__ == "__main__":
    unittest.main()
