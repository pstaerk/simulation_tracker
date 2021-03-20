import inspect
import click
from click.core import Command

def _make_track_command(f, name, attrs, cls):
    if isinstance(f, Command):
        raise TypeError("Attempted to convert a callback into a command twice.")
    try:
        params = f.__click_params__
        params.reverse()
        del f.__click_params__
    except AttributeError:
        params = []
    help = attrs.get("help")
    if help is None:
        help = inspect.getdoc(f)
        if isinstance(help, bytes):
            help = help.decode("utf-8")
    else:
        help = inspect.cleandoc(help)
    attrs["help"] = help
    return cls(
        name=name or f.__name__.lower().replace("_", "-"),
        callback=f,
        params=params,
        **attrs,
    )

def track_command(name=None, cls=None, **attrs):
    """Creates a command decorator, which extends the click command.
    """
    if cls is None:
        cls = Command
    def decorator(f):
        cmd = _make_track_command(f, name, attrs, cls)
        cmd.__doc__ = f.__doc__
        return cmd

    return decorator
