"""
Configuration loader for SASeg.

Usage
-----
    from configs.config import get_cfg
    cfg = get_cfg("configs/default.yaml", overrides=["train.batch_size=4"])

All values are accessible as attributes, e.g. cfg.train.lr.
Command-line overrides use dot-notation: "section.key=value".
"""

from __future__ import annotations

import argparse
import copy
from pathlib import Path
from typing import Any

import yaml


# ---------------------------------------------------------------------------
# Thin namespace wrapper so keys are accessible as attributes
# ---------------------------------------------------------------------------

class _Namespace:
    """Recursively converts a dict into an attribute-accessible object."""

    def __init__(self, d: dict) -> None:
        for k, v in d.items():
            setattr(self, k, _Namespace(v) if isinstance(v, dict) else v)

    def to_dict(self) -> dict:
        out: dict = {}
        for k, v in self.__dict__.items():
            out[k] = v.to_dict() if isinstance(v, _Namespace) else v
        return out

    def __repr__(self) -> str:  # pragma: no cover
        return repr(self.to_dict())


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_yaml(path: str | Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _deep_update(base: dict, override: dict) -> dict:
    """Recursively merge *override* into a copy of *base*."""
    result = copy.deepcopy(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_update(result[k], v)
        else:
            result[k] = v
    return result


def _apply_dotted_overrides(cfg: dict, overrides: list[str]) -> dict:
    """
    Apply a list of "section.key=value" strings to *cfg* (in-place copy).

    Supports arbitrary nesting depth, e.g. "model.encoder_freeze_stages=0".
    Values are parsed as YAML scalars so booleans, ints, and floats work.
    """
    cfg = copy.deepcopy(cfg)
    for item in overrides:
        if "=" not in item:
            raise ValueError(f"Override must be 'key=value', got: {item!r}")
        dotted_key, raw_val = item.split("=", 1)
        val = yaml.safe_load(raw_val)  # parse scalar

        keys = dotted_key.split(".")
        node = cfg
        for k in keys[:-1]:
            if k not in node:
                node[k] = {}
            node = node[k]
        node[keys[-1]] = val
    return cfg


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

_DEFAULT_YAML = Path(__file__).parent / "default.yaml"


def get_cfg(
    config_path: str | Path | None = None,
    overrides: list[str] | None = None,
) -> _Namespace:
    """
    Load configuration.

    Parameters
    ----------
    config_path:
        Path to a YAML file.  If *None*, ``configs/default.yaml`` is used.
    overrides:
        List of ``"section.key=value"`` strings that override loaded values.

    Returns
    -------
    _Namespace
        Attribute-accessible config tree.
    """
    base = _load_yaml(_DEFAULT_YAML)

    if config_path is not None:
        user = _load_yaml(config_path)
        base = _deep_update(base, user)

    if overrides:
        base = _apply_dotted_overrides(base, overrides)

    return _Namespace(base)


def parse_args_and_cfg() -> tuple[argparse.Namespace, _Namespace]:
    """
    Convenience helper for training / inference entry-points.

    Parses:
        --config  path/to/custom.yaml   (optional)
        --set     key=value             (repeatable, overrides config values)

    Returns
    -------
    args : argparse.Namespace  (raw CLI args)
    cfg  : _Namespace          (merged config)
    """
    parser = argparse.ArgumentParser(description="SASeg")
    parser.add_argument(
        "--config",
        default=None,
        help="Path to a YAML config file (merged on top of default.yaml).",
    )
    parser.add_argument(
        "--set",
        dest="overrides",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help="Override a config value, e.g. --set train.batch_size=4.",
    )
    args = parser.parse_args()
    cfg = get_cfg(args.config, args.overrides)
    return args, cfg
