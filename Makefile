PYTHON ?= python3

.PHONY: update-branches
update-branches:
	@echo "Updating GitHub branch links in docs..."
	@$(PYTHON) scripts/update_doc_links.py

.PHONY: help
help:
	@echo "Makefile targets:"
	@echo "  update-branches   - Update docs to point to configured development branches for repos"
	@echo "  help              - Show this message"


