import json
from pathlib import Path
import unittest
from xml.etree import ElementTree

from cssselect2 import ElementWrapper, Matcher, compile_selector_list
from tinycss2 import parse_declaration_list, parse_stylesheet, serialize


ROOT = Path(__file__).resolve().parents[1]
THEME = (ROOT / "theme.css").read_text(encoding="utf-8")
HOST = """
.is-phone { --toolbar-option-width: 40px; }
.is-tablet { --toolbar-option-width: 50px; }
.markdown-rendered pre, .markdown-rendered pre > code { white-space: pre-wrap; }
.callout-title { min-height: 0; }
.nav-file-title-content, .nav-folder-title-content {
    overflow-wrap: anywhere;
    white-space: pre;
}
"""
WORKSPACE = """
<body class="{mode}">
  <div class="workspace-leaf-content">
    <div class="view-header"><button id="view-action" class="clickable-icon" /></div>
    <div class="markdown-rendered">
      <div id="reading-table" class="el-table"><table /></div>
      <div id="embedded-table" class="table-wrapper"><table /></div>
      <pre id="code"><code id="code-text">long line of code</code></pre>
      <div class="callout is-collapsible"><div id="fold-title" class="callout-title" /></div>
      <div class="callout"><div id="plain-title" class="callout-title" /></div>
    </div>
    <div class="markdown-source-view mod-cm6">
      <div class="cm-contentContainer"><div id="editor" class="cm-content" /></div>
      <div id="live-table" class="cm-table-widget"><table /></div>
    </div>
  </div>
  <span id="file" class="nav-file-title-content">Long file name</span>
  <span id="folder" class="nav-folder-title-content">Long folder name</span>
  <div id="toolbar" class="mobile-toolbar">
    <div class="mobile-toolbar-options-list">
      <div class="mobile-toolbar-option" role="button" />
    </div>
  </div>
</body>
"""


class ThemeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matcher = Matcher()
        for rule in parse_stylesheet(HOST + THEME, skip_comments=True, skip_whitespace=True):
            if rule.type != "qualified-rule":
                raise ValueError(f"Unexpected rule on CSS line {rule.source_line}: {rule.type}")
            declarations = []
            for declaration in parse_declaration_list(
                rule.content, skip_comments=True, skip_whitespace=True
            ):
                if declaration.type != "declaration" or declaration.important:
                    raise ValueError(f"Invalid or important declaration on line {declaration.source_line}")
                declarations.append((declaration.name, serialize(declaration.value).strip()))
            for selector in compile_selector_list(rule.prelude):
                cls.matcher.add_selector(selector, declarations)

    def computed(self, mode, element_id=None):
        markup = ElementTree.fromstring(WORKSPACE.format(mode=mode))
        body = ElementWrapper.from_html_root(markup)
        target = body if element_id is None else next(
            element for element in body.iter_subtree() if element.id == element_id
        )
        inherited = {}
        for element in (*target.ancestors, target):
            declarations = {}
            for _, _, pseudo_element, properties in self.matcher.match(element):
                if pseudo_element is None:
                    declarations.update(properties)
            inherited.update(
                (name, value) for name, value in declarations.items() if name.startswith("--")
            )
        return inherited | declarations

    def test_reading_tables_and_code_scroll_locally_on_mobile(self):
        mode = "theme-dark is-mobile is-phone"
        for element_id in ("reading-table", "embedded-table", "live-table", "code"):
            with self.subTest(element=element_id):
                styles = self.computed(mode, element_id)
                self.assertEqual(styles.get("overflow-x"), "auto")
                self.assertEqual(styles.get("max-width"), "100%")
        self.assertEqual(self.computed(mode, "code")["white-space"], "pre")
        self.assertEqual(self.computed(mode, "code-text")["white-space"], "inherit")
        self.assertEqual(self.computed("theme-dark", "code")["white-space"], "pre-wrap")
        self.assertEqual(self.computed("theme-dark", "code-text")["white-space"], "pre-wrap")
        self.assertNotIn("overflow-x", self.computed("theme-dark", "reading-table"))

    def test_long_mobile_file_and_folder_names_can_wrap(self):
        for element_id in ("file", "folder"):
            with self.subTest(element=element_id):
                styles = self.computed("theme-light is-mobile is-phone", element_id)
                self.assertEqual(styles["overflow-wrap"], "anywhere")
                self.assertEqual(styles["white-space"], "pre-wrap")
                self.assertEqual(self.computed("theme-light", element_id)["white-space"], "pre")

    def test_phone_toolbar_and_view_header_keep_touch_targets(self):
        phone = "theme-light is-mobile is-phone"
        tablet = "theme-light is-mobile is-tablet"
        self.assertEqual(self.computed(phone, "toolbar")["--toolbar-option-width"], "44px")
        self.assertEqual(self.computed(tablet, "toolbar")["--toolbar-option-width"], "50px")
        view_action = self.computed(phone, "view-action")
        self.assertEqual(view_action["min-width"], "44px")
        self.assertEqual(view_action["min-height"], "44px")
        self.assertNotIn("min-width", self.computed("theme-light", "view-action"))

    def test_mobile_collapsible_callout_title_has_a_touch_target(self):
        phone = "theme-light is-mobile is-phone"
        self.assertEqual(self.computed(phone, "fold-title")["min-height"], "44px")
        self.assertEqual(self.computed(phone, "plain-title")["min-height"], "0")
        self.assertEqual(self.computed("theme-light", "fold-title")["min-height"], "0")

    def test_mobile_editor_keeps_padding_inside_focus_outline(self):
        phone = self.computed("theme-light is-mobile is-phone", "editor")
        self.assertGreaterEqual(int(phone["padding-inline"].removesuffix("px")), 4)
        self.assertNotIn("padding-inline", self.computed("theme-light", "editor"))

    def test_both_modes_define_distinct_foreground_and_background(self):
        light, dark = [self.computed(f"theme-{mode}") for mode in ("light", "dark")]
        for variable in ("--background-primary", "--text-normal", "--text-accent"):
            self.assertNotEqual(light[variable], dark[variable])
        for palette in (light, dark):
            self.assertNotEqual(palette["--background-primary"], palette["--text-normal"])
            self.assertEqual(palette["--text-accent"], palette["--interactive-accent"])

    def test_source_version_matches_manifest(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertIn(f"{manifest['name']} {manifest['version']}.", THEME.splitlines()[0])
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"Source version {manifest['version']}.", readme)
