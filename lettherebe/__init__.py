__version__ = "0.0.dev0"

# Force import of modules to make sure all handlers are defined
from . import repository_hosts  # noqa
from . import package_languages  # noqa
from . import documentation_hosts  # noqa
from . import continuous_integration_hosts  # noqa
