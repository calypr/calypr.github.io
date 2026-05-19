PYTHON ?= python3
ZENSICAL ?= $(if $(wildcard ./venv/bin/zensical),./venv/bin/zensical,zensical)

.PHONY: update-branches
update-branches:
	@echo "Updating GitHub branch links in docs..."
	@$(PYTHON) scripts/update_doc_links.py

.PHONY: update-front-matter
update-front-matter:
	@echo "Updating markdown front matter metadata..."
	@$(PYTHON) scripts/update_front_matter.py

.PHONY: prepare
prepare: update-front-matter
	@echo "Preparing documentation, adding meta for tools, personas, and solution links..."
	@$(PYTHON) scripts/prepare_docs.py

.PHONY: build
build: prepare
	@$(ZENSICAL) build

.PHONY: serve
serve: prepare
	@$(ZENSICAL) serve

.PHONY: help
help:
	@echo "Makefile targets:"
	@echo "  prepare           - Stage local docs plus imported upstream tool docs into .generated/docs"
	@echo "  build             - Build the Zensical site with the active Python environment"
	@echo "  serve             - Serve the Zensical site with the active Python environment"
	@echo "  update-branches   - Update docs to point to configured development branches for repos"
	@echo "  update-front-matter - Update markdown lead/personas/solutions/related_tools metadata"
	@echo "  help              - Show this message"
