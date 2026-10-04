def keep_wanted_season(items, season, titles_of):
    """Keeps the site entries whose own title names the wanted season (a
    title without one counts as season 1), for sites that list every
    season as a separate show. titles_of(item) returns that entry's
    title(s). Returns all items when no season is wanted or none match."""
    if not season or not items:
        return items
    kept = [item for item in items
            if any((split_season_title(t)[1] or 1) == season
                   for t in titles_of(item) if t)]
    return kept or items
