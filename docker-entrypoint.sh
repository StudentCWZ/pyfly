#!/bin/bash
set -e

# shellcheck disable=SC2046
. $(poetry env info --path)/bin/activate

exec flask run
