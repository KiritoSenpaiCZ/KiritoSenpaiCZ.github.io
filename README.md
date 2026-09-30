# Highflight Subtitles Repository

A Kodi addon repository bundling Czech/Slovak subtitle addons for anime and TV fansub sites into one installable, auto-updating source.

Compatible with Kodi 19, 20, and 21.

## Addons in this repository
- **Hiyori Subtitles** — [Kodi-Hiyori](https://github.com/KiritoSenpaiCZ/Kodi-Hiyori) (hiyori.cz, Czech/Slovak anime, account required)
- **WoSir Subtitles** — [Kodi-Wosir](https://github.com/KiritoSenpaiCZ/Kodi-Wosir) (wosir.cz, Czech anime, account required)
- **Edna Subtitles** — [Kodi-Edna](https://github.com/KiritoSenpaiCZ/Kodi-Edna) (edna.cz, Czech/Slovak TV shows, account required)
- **Kamui-Subs Subtitles** — [Kodi-Kamui](https://github.com/KiritoSenpaiCZ/Kodi-Kamui) (kamui-subs.cz, Czech anime, account + zip password required)
- **Legie Kondor Subtitles** — [Kodi-LegieKondor](https://github.com/KiritoSenpaiCZ/Kodi-LegieKondor) (anime4.legiekondor.cz, Czech anime, no account needed)
- **NyaSub Subtitles** — [Kodi-NyaSub](https://github.com/KiritoSenpaiCZ/Kodi-NyaSub) (nyasub.cz, Czech anime, no account needed)
- **Hanabi Subtitles** — [Kodi-Hanabi](https://github.com/KiritoSenpaiCZ/Kodi-Hanabi) (hanabi.fan, Czech anime, access token required)

Each addon's own repo is the source of truth for its code; this repo packages built zips of all seven (plus itself) so Kodi can browse, install and update them from one place.

This repo is named `KiritoSenpaiCZ.github.io` on purpose — that's GitHub's reserved "personal site" name, so its Pages site is served at the short address `https://kiritosenpaicz.github.io/` instead of a longer `.../reponame/` path, which is easier to type into Kodi's file manager on devices with awkward text entry (game consoles, TVs).

## Installation Instructions
1. In Kodi: **Settings > File manager > Add source**, and add this short address as a source: `https://kiritosenpaicz.github.io/`
2. Go to **Add-ons > Install from zip file**, select that source, and install `repository.highflightsubtitles-1.0.0.zip`
3. Go to **Add-ons > Install from repository > Highflight Subtitles Repository**, and install any of the addons above

Once the repository addon is installed, Kodi checks this repo for updates to all addons automatically.

## Repository layout
- `index.html` — landing page with direct zip links, used for the one-time "Add source" step
- `zips/<addon id>/<addon id>-<version>.zip` — the installable zip for each addon
- `addons.xml` / `addons.xml.md5` — the combined addon metadata Kodi reads

**Note:** this repo (and the source repos it packages) need to be public for Kodi to actually fetch anything from the raw URLs above — while private, only someone with a GitHub session/token can reach these files.

## Issues
Please open an issue in the specific addon's own repo rather than here, unless the problem is with the repository or install step itself.
