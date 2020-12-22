import requests
from packaging.version import Version, parse, InvalidVersion

from utils.logger import log

LATEST_URL = "https://api.github.com/repos/Hari-Nagarajan/fairgame/releases/latest"

__VERSION = "0.4.4"

version = parse(__VERSION)


def check_version():
    remote_version = get_latest_version()

    if version < remote_version:
        log.warning(
            f"You are running FairGame v{version.release}, but the most recent version is v{remote_version.release}. "
            f"Consider upgrading "
        )
    elif version.is_prerelease:
        log.info(f"FairGame PRE-RELEASE v{version}")
    else:
        log.info(f"FairGame v{version}")


def get_latest_version():
    try:
        r = requests.get(LATEST_URL)
        data = r.json()
        latest_version = parse(str(data["tag_name"]))
    except InvalidVersion:
        # Return a safe, but wrong version1
        latest_version = parse("0.0")
        log.error(
            f"Failed complete check for latest version.  Assuming v{latest_version}"
        )
    return latest_version
