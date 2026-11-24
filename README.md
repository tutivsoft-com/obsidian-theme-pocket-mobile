# Pocket Mobile

An Obsidian theme designed around phone screens and touch navigation.

Source version 3.6.2. The theme supports dark and light modes. The preview screenshots are from Obsidian 1.15.1 on Windows.

On mobile, the theme keeps lists and callouts compact, wraps long file and folder names, and lets wide tables and rendered code blocks scroll horizontally. Collapsible callout titles and phone editor toolbar actions have 44-pixel touch targets. Physical Android and iOS testing is pending.

## Preview

![Dark mode](screenshot.png)

![Light mode](screenshot-light.png)

## Install manually

1. Download `manifest.json` and `theme.css` from [release 3.6.0](https://github.com/tutivsoft-com/obsidian-theme-pocket-mobile/releases/tag/3.6.0).
2. Put both files in `.obsidian/themes/Pocket Mobile/` in your vault.
3. Open **Settings > Appearance** and select **Pocket Mobile**. Choose a supported base colour scheme.

## Check the source

With Python 3.10 or later, install the two test dependencies and run the suite from the repository root:

```sh
python -m pip install tinycss2 cssselect2
python -B -m unittest discover -s tests -v
```

The tests parse the stylesheet and check its selectors and declarations against a representative Obsidian workspace. They run without opening Obsidian.

See the [UI test results](docs/ui-qa/2026-11-24/README.md). See the [original design plan](PLAN.md). [MIT license](LICENSE).
