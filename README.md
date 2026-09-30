# Highflight Subtitles Repository

A Kodi addon repository bundling Czech/Slovak subtitle addons for anime and TV fansub sites into one installable, auto-updating source.

Compatible with Kodi 19, 20, and 21.

## Addons in this repository
Each addon fetches subtitles either by scraping the site's own HTML pages — unofficial, done without the site's consent, and fragile since it can break at any point if the site changes its layout — or through an official API that the site provides and supports itself (documented and much more stable). Noted per addon below.
- **Edna Subtitles** — [Kodi-Edna](https://github.com/KiritoSenpaiCZ/Kodi-Edna) (edna.cz, Czech/Slovak TV shows, account required) — gets subtitles via HTML scraping (unofficial - not sanctioned or consented to by the site; can break if the site changes its page layout)
- **Hanabi Subtitles** — [Kodi-Hanabi](https://github.com/KiritoSenpaiCZ/Kodi-Hanabi) (hanabi.fan, Czech anime, access token required) — gets subtitles via Hanabi's official REST API, built and published by the site itself for this purpose (documented and far more stable than scraping)
- **Hiyori Subtitles** — [Kodi-Hiyori](https://github.com/KiritoSenpaiCZ/Kodi-Hiyori) (hiyori.cz, Czech/Slovak anime, account required) — gets subtitles via HTML scraping (unofficial - not sanctioned or consented to by the site; can break if the site changes its page layout)
- **Kamui-Subs Subtitles** — [Kodi-Kamui](https://github.com/KiritoSenpaiCZ/Kodi-Kamui) (kamui-subs.cz, Czech anime, account + zip password required) — gets subtitles via HTML scraping (unofficial - not sanctioned or consented to by the site; can break if the site changes its page layout)
- **Legie Kondor Subtitles** — [Kodi-LegieKondor](https://github.com/KiritoSenpaiCZ/Kodi-LegieKondor) (anime4.legiekondor.cz, Czech anime, no account needed) — gets subtitles via HTML scraping (unofficial - not sanctioned or consented to by the site; can break if the site changes its page layout)
- **WoSir Subtitles** — [Kodi-Wosir](https://github.com/KiritoSenpaiCZ/Kodi-Wosir) (wosir.cz, Czech anime, account required) — gets subtitles via HTML scraping (unofficial - not sanctioned or consented to by the site; can break if the site changes its page layout)

Each addon's own repo is the source of truth for its code; this repo packages built zips of all seven (plus itself) so Kodi can browse, install and update them from one place.

## Installation Instructions
1. In Kodi: **Settings > File manager > Add source**, and add this short address as a source: `https://kiritosenpaicz.github.io/`
2. Go to **Add-ons > Install from zip file**, select that source, and install `repository.highflightsubtitles-1.0.1.zip`
3. Go to **Add-ons > Install from repository > Highflight Subtitles Repository**, and install any of the addons above

Once the repository addon is installed, Kodi checks this repo for updates to all addons automatically.

## Repository layout
- `index.html` — landing page with direct zip links, used for the one-time "Add source" step
- `zips/<addon id>/<addon id>-<version>.zip` — the installable zip for each addon
- `addons.xml` / `addons.xml.md5` — the combined addon metadata Kodi reads

**Note:** this repo (and the source repos it packages) need to be public for Kodi to actually fetch anything from the raw URLs above — while private, only someone with a GitHub session/token can reach these files.

## Issues
Please open an issue in the specific addon's own repo rather than here, unless the problem is with the repository or install step itself.
