def current_video():
    """Path of the video Kodi has loaded - playing OR paused - else None.
    (Player.Playing alone isn't enough: it's false while paused.)"""
    try:
        if xbmc.getCondVisibility('Player.HasVideo') or xbmc.getCondVisibility('Player.Paused'):
            return xbmc.getInfoLabel('Player.Filenameandpath') or None
    except Exception:
        pass
    return None


def _read_owners():
    try:
        with open(OWNERS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _write_owners(owners):
    try:
        with open(OWNERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(owners, f)
    except Exception as e:
        log("couldn't save {0}: {1}".format(OWNERS_FILE, e))


def remember_owner(path):
    """Record which video a delivered subtitle belongs to, so
    cleanup_temp_dir() never deletes it while that video is still loaded
    (e.g. paused for more than an hour)."""
    video = current_video()
    if not video:
        return
    try:
        top = os.path.relpath(path, TEMP_DIR).split(os.sep)[0]
    except ValueError:
        return
    if not top or top.startswith('..'):
        return
    owners = _read_owners()
    owners[top] = video
    _write_owners(owners)


def cleanup_temp_dir():
    """Sweep old downloads out of TEMP_DIR. Kept: KEEP_FILES (small caches
    managed by their own logic), and every subtitle belonging to the video
    Kodi currently has loaded - playing or paused - however old it is, so a
    long pause can't delete a subtitle that's still in use."""
    keep = KEEP_FILES
    owners = _read_owners()
    video = current_video()
    try:
        now = time.time()
        for name in os.listdir(TEMP_DIR):
            if name in keep or not name.startswith(TEMP_FILE_PREFIX):
                continue
            if video and owners.get(name) == video:
                continue
            path = os.path.join(TEMP_DIR, name)
            try:
                age = now - os.path.getmtime(path)
            except OSError:
                continue
            if age < TEMP_MAX_AGE_SECONDS:
                continue
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path, ignore_errors=True)
                else:
                    os.remove(path)
            except OSError as e:
                log("cleanup: couldn't remove {0}: {1}".format(path, e))
        existing = set(os.listdir(TEMP_DIR))
        still_there = dict((k, v) for k, v in owners.items() if k in existing)
        if still_there != owners:
            _write_owners(still_there)
    except Exception as e:
        log("cleanup_temp_dir failed: {0}".format(e))
