#!/usr/bin/env bash
# Format only paths the gate selected from the index or immutable review range.
set -euo pipefail

# uv creates the project environment at .venv unless told otherwise. A local apply formats a full index snapshot and
# refuses any file the formatter creates there, ignored paths included. The default keeps the environment in the user
# cache, outside every checkout. A caller that already sets UV_PROJECT_ENVIRONMENT keeps its value.
export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-${XDG_CACHE_HOME:-$HOME/.cache}/py-typekit/format-staged-venv}"

for file in "$@"; do
	# A selected path can be a deletion. It has no working-tree bytes to format,
	# and asking either formatter to read it turns a valid removal into a false
	# pre-commit failure.
	[[ -e "$file" || -L "$file" ]] || continue
	case "$file" in
	.claude/agents/catalog.json | .claude/agents/provenance.json | .claude/skills/catalog.json | .claude/skills/provenance.json | .codex/agents/catalog.json | .codex/agents/provenance.json | .opencode/agents/catalog.json | .opencode/agents/provenance.json)
		# These manifests are byte-for-byte output of `harness adapters generate`.
		# Reformatting them would make a generated adapter stale immediately.
		continue
		;;
	# Both formatters come from the project's locked dependencies (uv.lock for ruff,
	# node_modules for prettier), so the PATH of the job decides only where uv and npx
	# are found. npx resolves prettier from node_modules in the working directory, so
	# run this script from the repository root.
	*.md | *.json | *.yml | *.yaml)
		npx --no-install prettier --write "$file"
		;;
	*.py) uv run --locked ruff format --no-cache "$file" ;;
	*) ;;
	esac
done
