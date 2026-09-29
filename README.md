# Kodi-Subtitles-Repo

A Kodi addon repository bundling four subtitle addons in one installable source:

- **Hiyori Subtitles** — [Kodi-Hiyori](https://github.com/KiritoSenpaiCZ/Kodi-Hiyori) (hiyori.cz, Czech/Slovak anime)
- **WoSir Subtitles** — [Kodi-Wosir](https://github.com/KiritoSenpaiCZ/Kodi-Wosir) (wosir.cz, Czech anime)
- **Edna Subtitles** — [Kodi-Edna](https://github.com/KiritoSenpaiCZ/Kodi-Edna) (edna.cz, Czech/Slovak TV shows)
- **Kamui-Subs Subtitles** — bundled directly in this repo (kamui-subs.cz, Czech anime)

Each of the first three addons' own repo remains the source of truth for its code; Kamui-Subs lives only here. This repo packages built zips of all four (plus itself) so Kodi can browse and update them from one place.

## Installation

1. In Kodi, go to **Settings → File manager → Add source**, and add this repo's raw URL as a source:
   `https://raw.githubusercontent.com/KiritoSenpaiCZ/Kodi-Subtitles-Repo/main/zips/repository.highflightsubtitles/`
2. Go to **Add-ons → Install from zip file**, select that source, and install `repository.highflightsubtitles-1.0.0.zip`.
3. Go to **Add-ons → Install from repository → Highflight Subtitles Repository**, and install any of the four subtitle addons.

Once the repository addon is installed, Kodi will check this repo for updates to all four subtitle addons automatically.

## Repository layout

- `zips/<addon id>/<addon id>-<version>.zip` — the installable zip for each addon
- `addons.xml` — the combined addon metadata Kodi reads to know what's available
- `addons.xml.md5` — checksum of `addons.xml`, so Kodi can tell when it's changed

Rebuilding a zip after a source addon changes just means re-zipping that addon's folder, regenerating `addons.xml`/`addons.xml.md5`, and re-uploading.

**Note:** this repo (and the source repos it packages) need to be public for Kodi to actually be able to fetch anything from the raw URLs above — while private, only someone with a GitHub session/token can reach these files.
