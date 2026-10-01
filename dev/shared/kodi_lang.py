# The addon's messages are in Czech when Kodi's language is Czech or Slovak,
# English otherwise. L("english", "czech", *args) picks one and fills in
# {0}-style placeholders like str.format.
try:
    _UI_LANG = xbmc.getLanguage(xbmc.ISO_639_1)
except Exception:
    _UI_LANG = ''


def L(en, cs, *args):
    text = cs if _UI_LANG in ('cs', 'sk') else en
    return text.format(*args) if args else text
