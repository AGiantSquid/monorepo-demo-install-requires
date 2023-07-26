from pathlib import Path

try:
    from pip._internal.cli.main import main as pip_main
except ModuleNotFoundError:
    from pip import main as pip_main


REPO_ROOT = Path(__file__).parents[1].absolute()


def local_requirement(requirement: str):
    """Installs local packages.

    Allows local dependencies to be listed in the install_requires setup definition,
    but manages the installation manually as pip cannot install editable local packages.

    Return emtpy string.
    (install_requires requires a string value, so return '' which gets ignored by pip.)
    """
    package_path = str(REPO_ROOT / requirement)

    pip_main(['install', '-e', package_path])

    return ''
