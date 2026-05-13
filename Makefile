PYTHON ?= python3
ZENSICAL ?= zensical

.PHONY: update-branches
update-branches:
	@echo "Updating GitHub branch links in docs..."
	@$(PYTHON) scripts/update_doc_links.py

.PHONY: prepare
prepare:
	@$(PYTHON) scripts/prepare_docs.py

.PHONY: build
build: prepare
	@$(ZENSICAL) build --clean

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
	@echo "  help              - Show this message"
