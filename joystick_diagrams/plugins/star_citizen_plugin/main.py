import logging
from pathlib import Path

from joystick_diagrams.plugins.plugin_interface import PluginInterface
from joystick_diagrams.plugins.star_citizen_plugin.config import (
    settings,  # TODO Move out plugins to separate package
)
from joystick_diagrams.plugins.star_citizen_plugin.star_citizen import (
    StarCitizen,  # TODO Move out plugins to separate package
)

_logger = logging.getLogger("__name__")


class ParserPlugin(PluginInterface):
    def __init__(self):
        self.path = None
        self.settings = settings
        self.settings.validators.register()

    def process(self):
        return self.instance.parse()

    def set_path(self, path: Path) -> bool:
        inst = StarCitizen(path)

        if inst:
            self.path = path
            self.instance = inst
            return True

        return False

    @property
    def path_type(self):
        return self.FilePath("Select your Star Citizen ", "/%USERPROFILE%/Saved Games", [".xml"])

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
