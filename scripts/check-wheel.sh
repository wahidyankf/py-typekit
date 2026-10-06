#!/usr/bin/env bash
# check-wheel.sh — the `wheel-check` gate: build the wheel and prove it is typed and has no runtime dependency.
#
# A consumer of py-typekit needs two things from the built wheel, and both are easy to lose without noticing:
#   1. `typekit/py.typed`, the marker that makes the consumer's Pyright read these types instead of treating the
#      package as untyped; and
#   2. no `Requires-Dist` line in METADATA, because the library promises zero runtime dependencies (D10).
#
# Usage: bash scripts/check-wheel.sh        (from any directory; it checks the repository this script lives in)
# Exit:  0 when the wheel holds the marker and declares no dependency; non-zero otherwise, naming what is wrong.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# The wheel is built into a throwaway directory, removed on every exit path, so the check leaves no `dist/` behind.
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

uv build --wheel --out-dir "$tmp" "$root"

wheels=("$tmp"/*.whl)
if [ "${#wheels[@]}" -ne 1 ] || [ ! -f "${wheels[0]}" ]; then
	echo "check-wheel: expected exactly one wheel in the build output, found ${#wheels[@]}" >&2
	exit 1
fi
wheel="${wheels[0]}"

# Each listing is captured before it is searched. A `grep -q` that stops at its first match would otherwise close the
# pipe under `unzip`, whose SIGPIPE status `pipefail` turns into a false answer, a false pass for the second check.
#
# `unzip -l` prints the archive listing; the marker is the last column of its line.
listing="$(unzip -l "$wheel")"
if ! grep -Eq '[[:space:]]typekit/py\.typed$' <<<"$listing"; then
	echo "check-wheel: ${wheel##*/} does not list typekit/py.typed" >&2
	exit 1
fi

# `unzip -p` prints one member; the glob matches the single `<name>-<version>.dist-info/METADATA`.
metadata="$(unzip -p "$wheel" '*.dist-info/METADATA')"
if grep -Eq '^Requires-Dist:' <<<"$metadata"; then
	echo "check-wheel: ${wheel##*/} declares a runtime dependency (a Requires-Dist line in METADATA)" >&2
	exit 1
fi

echo "check-wheel: ${wheel##*/} lists typekit/py.typed and declares no runtime dependency"
