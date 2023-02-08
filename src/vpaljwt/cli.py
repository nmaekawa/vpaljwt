# -*- coding: utf-8 -*-

"""Console script for hxann."""
import contextlib
import json
import sys
from datetime import datetime, timezone

import click
import jwt


@click.command()
@click.option(
    "--creds",
    required=True,
    help="json file with kondo api creds",
)
def cli(creds):
    with _smart_open(creds) as fh:
        c = json.load(fh)

    payload = {
        "iss": c["username"],
        "sub": c["key"],
        "iat": c["iat"] if c["iat"] else int(datetime.now(tz=timezone.utc).timestamp()),
    }
    click.echo(jwt.encode(payload, c["secret"], algorithm="HS256"))


# from http://stackoverflow.com/a/29824059
@contextlib.contextmanager
def _smart_open(filename, mode="Ur"):
    if filename == "-":
        if mode is None or mode == "" or "r" in mode:
            fhandle = sys.stdin
        else:
            fhandle = sys.stdout
    else:
        fhandle = open(filename, mode)

    try:
        yield fhandle
    finally:
        if filename != "-":
            fhandle.close()


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
