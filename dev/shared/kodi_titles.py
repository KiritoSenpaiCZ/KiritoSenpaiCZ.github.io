def split_season_title(title):
    """Strips a season / cour ending from a show title and returns
    (base title, season or None). Players and anime addons often pass the
    full season name, e.g. "Tensei Shitara Slime Datta Ken 4th Season
    Part 1 & 2"; the site searches need every word to match, so they would
    find nothing. "Part N" (a cour split) is dropped without a season."""
    if not title:
        return title, None
    part = r'[\s:\-–]*\bpart\s*\d+(?:\s*(?:&|and|\+)\s*\d+)?\s*$'
    base = re.sub(part, '', title.strip(), flags=re.I)
    season = None
    for pattern in (r'\b(\d{1,2})(?:st|nd|rd|th)\s+season$',
                    r'\bseason\s*(\d{1,2})$',
                    r'\bs(\d{1,2})$'):
        m = re.search(r'[\s:\-–]*' + pattern, base, re.I)
        if m:
            season = int(m.group(1))
            base = base[:m.start()]
            break
    base = re.sub(part, '', base, flags=re.I)
    base = re.sub(r'[\s:\-–]+$', '', base).strip()
    return (base or title), season
