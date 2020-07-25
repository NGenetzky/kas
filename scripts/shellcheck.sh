#!/bin/sh

_SCRIPT_REL_TO_BASE='../'
D_SCRIPT="$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd -P)"
D_BASE="${D_SCRIPT}/${_SCRIPT_REL_TO_BASE}"
readonly \
	D_BASE \
	D_SCRIPT \
	_SCRIPT_REL_TO_BASE

cd "${D_BASE}"

shellcheck -x -P "$(pwd)" "$@"
