# Pocket Mobile

An Obsidian theme designed around phone screens and touch navigation.

**Status: planning only. No theme code has been written.**

Plan date: 13 November 2026. This repository currently contains this planning README only. The name is a descriptive working name; Community name availability must be checked before any future submission.

Search keywords: Obsidian theme, mobile, Android, iPhone, compact notes, small screen.

## Who this is for

People who regularly capture, browse and edit notes on Android or iPhone.

## User need and evidence

Mobile users report wasted space, deep list indentation, large nested callouts and tables that are difficult to scroll.

- [Requests about mobile spacing, nesting and wide tables](https://www.reddit.com/r/ObsidianMD/comments/1qbvcfo/velocity_20_major_theme_update_built_for_obsidian/)

The Reddit links come from the preceding idea research and represent qualitative demand, not a market-size estimate or proof that existing themes do not solve the problem. For Pure OLED Rainbow, the additional requirement comes directly from the owner. Other themes and snippets may already address parts of these needs.

## Planned appearance and features

- Use shallow list indentation that remains understandable across several nesting levels.
- Keep callouts, headings, properties and code blocks compact without shrinking touch targets.
- Preserve horizontal scrolling for wide tables and code blocks.
- Keep navigation icons and toolbar actions visible with the on-screen keyboard open.
- Respect device safe areas, portrait and landscape orientation, and system font scaling.
- Keep desktop styling usable while prioritising mobile layouts; allow separate optional density choices later.

## Mode scope

Plan both light and dark modes on mobile and a compatible desktop appearance.

## Future implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references for later implementation:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

These are future work items. No release, installation instructions, compatibility certification or Community listing is being claimed by this planning repository.

## Acceptance checklist for later implementation

- [ ] Test Android and iOS before claiming support for both.
- [ ] Check narrow screens, keyboard-open states, long filenames and nested lists/callouts.
- [ ] Check table scrolling, toolbar visibility and touch target sizes.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Current boundary

Only repository creation and this Markdown plan are authorised in this task. Do not add theme CSS, manifests, screenshots, release tags or submissions as part of this planning work. Future work stays on this repository's verified primary branch.
