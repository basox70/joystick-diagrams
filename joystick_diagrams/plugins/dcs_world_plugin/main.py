import logging
from pathlib import Path

from dynaconf.loaders.json_loader import write

from joystick_diagrams.input.profile_collection import ProfileCollection
from joystick_diagrams.plugins.dcs_world_plugin.dcs_world import DCSWorldParser
from joystick_diagrams.plugins.plugin_interface import PluginInterface

from .config import settings

_logger = logging.getLogger("__name__")


class ParserPlugin(PluginInterface):
    def __init__(self):
        self.settings = settings
        self.settings.validators.register()
        self.path = self.settings.path or None

    def process(self) -> ProfileCollection:
        return self.instance.process_profiles()

    def set_path(self, path: Path) -> bool:
        try:
            self.instance = DCSWorldParser(path)
            # Requires abstraction / better experience
            write(self.settings.settings_module[0], {"path": path})
        except Exception as e:
            print(e)
            return False

        self.path = path
        return True

    @property
    def path_type(self):
        return self.FolderPath("A test title", "\\%%USERPROFILE%%\\Saved Games")

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
