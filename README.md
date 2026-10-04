# Highflight Subtitles Repository

A Kodi addon repository bundling Czech/Slovak subtitle addons for anime and TV fansub sites into one installable, auto-updating source.

Compatible with Kodi 19, 20, and 21.

## Addons in this repository

| Addon | Site | Content | Version | Needs | Support |
|---|---|---|---|---|---|
| [Edna Subtitles](https://github.com/KiritoSenpaiCZ/Kodi-Edna) | [edna.cz](https://www.edna.cz) | Czech/Slovak TV shows | 1.2.0 | Account | Unofficial |
| [Hanabi Subtitles](https://github.com/KiritoSenpaiCZ/Kodi-Hanabi) | [hanabi.fan](https://hanabi.fan) | Czech anime | 1.2.0 | Access token (free account) | **Official API** |
| [Hiyori Subtitles](https://github.com/KiritoSenpaiCZ/Kodi-Hiyori) | [hiyori.cz](https://hiyori.cz) | Czech/Slovak anime | 1.2.0 | Account | Unofficial |
| [HNS Subtitles](https://github.com/KiritoSenpaiCZ/Kodi-HNS) | [hns.sk](https://hns.sk) | Czech/Slovak anime | 1.0.0 | Account (e-mail) | Unofficial |
| [Kamui-Subs Subtitles](https://github.com/KiritoSenpaiCZ/Kodi-Kamui) | [kamui-subs.cz](https://kamui-subs.cz) | Czech anime | 1.2.3 | Account + ZIP password | Unofficial |
| [Legie Kondor Subtitles](https://github.com/KiritoSenpaiCZ/Kodi-LegieKondor) | [anime4.legiekondor.cz](https://anime4.legiekondor.cz) | Czech anime | 1.2.0 | Nothing | Unofficial |
| [NyaSub Subtitles](https://github.com/KiritoSenpaiCZ/Kodi-NyaSub) | [nyasub.cz](https://nyasub.cz) | Czech anime | 1.2.0 | Nothing | Unofficial |
| [WoSir Subtitles](https://github.com/KiritoSenpaiCZ/Kodi-Wosir) | [wosir.cz](https://www.wosir.cz) | Czech anime | 1.2.0 | Account | Unofficial |

**Support:**
- **Official API**: the site publishes and supports an API for exactly this purpose. Documented and stable.
- **Unofficial**: the addon reads the site's own web pages (HTML scraping). Not sanctioned by the site, and it can break at any time if the site changes its layout, until the addon is updated.

Each addon's own repo is the source of truth for its code; this repo packages built zips of all eight (plus itself) so Kodi can browse, install and update them from one place.

## Installation Instructions
1. In Kodi: **Settings > File manager > Add source**, and add this short address as a source: `https://kiritosenpaicz.github.io/`
2. Go to **Add-ons > Install from zip file**, select that source, and install `repository.highflightsubtitles-1.0.2.zip`
3. Go to **Add-ons > Install from repository > Highflight Subtitles Repository**, and install any of the addons above

Once the repository addon is installed, Kodi checks this repo for updates to all addons automatically.

## Repository layout
- `index.html` — landing page with direct zip links, used for the one-time "Add source" step
- `zips/<addon id>/<addon id>-<version>.zip` — the installable zip for each addon
- `addons.xml` / `addons.xml.md5` — the combined addon metadata Kodi reads
- `dev/` — maintenance tools (shared code kept in one place), not needed to use the addons

## VLC
The same sites (plus titulky.com) are available as VLC extensions, with a one-line installer for Windows and macOS: [VLC-Subtitles](https://github.com/KiritoSenpaiCZ/VLC-Subtitles).

## Issues
Please open an issue in the specific addon's own repo rather than here, unless the problem is with the repository or install step itself.
