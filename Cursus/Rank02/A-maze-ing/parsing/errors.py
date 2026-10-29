"""Error raised when the configuration file can't be used."""


class ConfigError(Exception):
    """Raised when the configuration file can't be used.

    The message says what is wrong, so main() only has to print it.
    """
