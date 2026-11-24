# Pocket Mobile UI test, 24 November 2026

The test ran in Obsidian 1.15.1 on Windows with a separate test vault containing only synthetic notes, a Canvas board and a Base. Pocket Mobile 3.6.1 was the baseline at commit `5a6e06575de220b7eaff6791cca2aa6a2495bf62`. The retest used Pocket Mobile 3.6.2.

Obsidian's built-in mobile emulation provided the actual Obsidian phone layout inside the Windows app. Viewports were 390 × 760, 320 × 640, 760 × 390 and 390 × 460 CSS pixels for phone layouts, 780 × 780 for a tablet layout and 900 × 650 for desktop. The reduced height checked available workspace when the keyboard would take up screen space. [Obsidian mobile emulation documentation](https://docs.obsidian.md/Plugins/Getting%20started/Mobile%20development)

## Fixes and retest

| Issue in 3.6.1 | Result with 3.6.2 |
| --- | --- |
| The reading-view `pre` had horizontal overflow enabled, but Obsidian's inner `code` retained `pre-wrap`. A long JavaScript line wrapped, leaving a 330 px scroll area and no horizontal travel. | The mobile rule lets the inner code inherit the block's whitespace rule. Both computed to `pre`. The same 330 px area had 918 px of content and scrolled by 150 px. Desktop keeps Obsidian's wrapping rule. |
| The collapsible nested callout title was 290 × 21 px at 390 px width. | The title control was 290 × 44 px. The same control opened and closed the content, which measured 80 px high while open. Plain callout titles and desktop callouts keep their sizing. |

## Case results

| Case | Obsidian UI result |
| --- | --- |
| Reading and content | Dark phone reading showed four properties, internal and external links, highlighting, four list depths and checked and unchecked tasks. Desktop selection returned the intended text. Clicking an unchecked task ticked it and saved the change in the fixture. The fixture was restored after the check. |
| Long tables and reflow | The reading table moved 150 px in a 330 px wrapper with 613 px of content. The Live Preview table moved 150 px in its 254 px wrapper with 613 px of content. At 320 px portrait, 390 px portrait and 760 px landscape, the document scroll width matched the viewport. |
| Editor and touch geometry | Light phone Live Preview and Source mode both opened. The measured editor toolbar and view-header actions were 44 × 44 px. The toolbar bold action changed the selected text to `**Harbor**`. At 390 × 460, the toolbar bottom was at 452 px and the editor retained 8 px side padding. The tablet layout retained Obsidian's 50 px toolbar width variable. |
| Files and tabs | The long folder wrapped to two lines and the long filename to three. Their content fit within their own widths. The mobile tab switcher displayed the active and other named tabs. |
| Search and prompts | Phone and desktop search returned the synthetic note for `pocket-coast`, displayed “No matches found” for an absent term and cleared the query. The command palette focused its input, found the scheme toggle and showed zero items for an absent command. |
| Menu, focus and selection | The phone and desktop note menus displayed checked Reading view and disabled Replace, as well as the warning treatment on Delete file. Desktop Live Preview exposed a solid 2 px blue keyboard-focus outline. The light phone source selection remained visible above the lower toolbar. Hovering the desktop view action applied the theme's hover color. |
| Appearance | Light phone and desktop Appearance displayed Pocket Mobile as selected. Dark and light modes switched in the live app and exposed their expected palette values. |
| Canvas, Bases and graph | Dark Canvas rendered the three fixture nodes and controls on phone and desktop. Light Bases rendered its local table and rows on both layouts. The desktop Graph view rendered its canvas and controls. |
| Workspace panels | Desktop Outline and file properties displayed the fixture headings and metadata. |

The desktop checks used the live Obsidian renderer. Phone actions used Obsidian controls in its mobile layout. Scrolling was verified through element scroll positions. Android and iOS touch delivery, keyboard, and safe-area behavior require native app coverage.

## Screenshots

These ten original Obsidian PNG captures total 388,876 bytes. The captures show only synthetic test data.

| Capture | State | Dimensions |
| --- | --- | --- |
| [01](01-dark-phone-reading.png) | Dark phone reading, properties and nested lists | 390 × 760 |
| [02](02-dark-phone-nested-callout.png) | Dark phone expanded nested callout | 390 × 760 |
| [03](03-dark-phone-wide-table.png) | Dark phone reading table scrolled sideways | 390 × 760 |
| [04](04-dark-phone-wide-code.png) | Dark phone reading code block scrolled sideways | 390 × 760 |
| [05](05-light-phone-live-preview.png) | Light phone Live Preview and editor toolbar | 390 × 760 |
| [06](06-light-phone-source-selection.png) | Light phone source selection and toolbar at reduced height | 390 × 460 |
| [07](07-light-phone-files.png) | Light phone file and folder names wrapped in the explorer | 390 × 760 |
| [08](08-light-phone-appearance.png) | Light phone Appearance showing the selected theme | 390 × 760 |
| [09](09-dark-desktop-canvas.png) | Dark desktop Canvas with notes and controls | 900 × 650 |
| [10](10-light-desktop-bases.png) | Light desktop Bases table | 900 × 650 |

## Source checks

From the repository root, `python -B -m unittest discover -s tests -v` passed all seven tests. The CSS tests include the inner-code whitespace and collapsible callout reachability cases. `git diff --check` also passed.
