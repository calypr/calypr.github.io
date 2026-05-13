PYTHON ?= python3

.PHONY: update-branches
update-branches:
	@echo "Updating GitHub branch links in docs..."
	@$(PYTHON) scripts/update_doc_links.py

.PHONY: build
build:
	@$(PYTHON) -m mkdocs build

.PHONY: serve
serve:
	@$(PYTHON) -m mkdocs serve

.PHONY: help
help:
	@echo "Makefile targets:"
	@echo "  build             - Build the MkDocs site with the active Python environment"
	@echo "  serve             - Serve the MkDocs site with the active Python environment"
	@echo "  update-branches   - Update docs to point to configured development branches for repos"
	@echo "  help              - Show this message"
