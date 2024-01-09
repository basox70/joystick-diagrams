import logging
from pathlib import Path

from joystick_diagrams.plugins.plugin_interface import PluginInterface

from .config import settings

_logger = logging.getLogger("__name__")


class ParserPlugin(PluginInterface):
    def __init__(self):
        self.path = None
        self.path_type = self.FolderPath("A test title", "/%USERPROFILE%/Saved Games")
        self.settings = settings
        self.settings.validators.register()

    def process(self):
        return None

    def set_path(self, path: Path) -> bool:
        self.path = path
        return True

    @property
    def name(self) -> str:
        return f"{self.settings.PLUGIN_NAME}"

    @property
    def version(self) -> str:
        return f"{self.settings.VERSION}"

    @property
    def icon(self) -> str:
        return f"{Path.joinpath(Path(__file__).parent,self.settings.PLUGIN_ICON)}"

    @property
    def get_path(self) -> bool:
        return self.path


if __name__ == "__main__":
    plugin = ParserPlugin()
