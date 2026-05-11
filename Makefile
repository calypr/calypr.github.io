PYTHON ?= python3

.PHONY: update-branches
update-branches:
	@echo "Updating GitHub branch links in docs..."
	@$(PYTHON) scripts/update_doc_links.py

.PHONY: help
help:
	@echo "Makefile targets:"
	@echo "  update-branches   - Update docs to point to configured development branches for repos"
	@echo "  sync-git-drs-docs - Sync git-drs documentation from calypr/git-drs repository"
	@echo "  sync-syfon-docs   - Sync syfon documentation from calypr/syfon repository"
	@echo "  sync              - Sync all tool docs and update branch links"
	@echo "  help              - Show this message"

# Sync git-drs docs:
# - Determine best branch for calypr/git-drs (prefers development if present).
# - Clone calypr/git-drs development branch into a temporary folder $(SYNC_TMP) (default: .tmp_git_drs).
# - Copy these files from $(SYNC_TMP)/docs/ into this repo's docs/tools/git-drs/:
#   - getting-started.md
#   - commands.md
#   - installation.md
#   - troubleshooting.md
# - Update docs/tools/git-drs/.nav.yml to reference these files.
# - Clean up the temporary clone; review and commit the copied files.
.PHONY: sync-git-drs-docs
SYNC_TMP ?= .tmp_git_drs
GIT_DRS_REPO ?= https://github.com/calypr/git-drs.git
GIT_DRS_BRANCH ?= development

sync-git-drs-docs:
	@echo "Syncing git-drs docs (branch $(GIT_DRS_BRANCH))..."
	@rm -rf $(SYNC_TMP) || true
	@git clone --depth 1 --branch $(GIT_DRS_BRANCH) $(GIT_DRS_REPO) $(SYNC_TMP)
	@cp $(SYNC_TMP)/docs/getting-started.md docs/tools/git-drs/getting-started.md
	@cp $(SYNC_TMP)/docs/commands.md docs/tools/git-drs/commands.md
	@cp $(SYNC_TMP)/docs/installation.md docs/tools/git-drs/installation.md
	@cp $(SYNC_TMP)/docs/troubleshooting.md docs/tools/git-drs/troubleshooting.md
	@printf "%s\n" "" "title: Git-DRS" "" "nav:" "  - index.md" "  - getting-started.md" "  - installation.md" "  - commands.md" "  - troubleshooting.md" "  - docs/" > docs/tools/git-drs/.nav.yml
	@rm -rf $(SYNC_TMP)
	@echo "Done. Files copied to docs/tools/git-drs/. Review and commit the changes."

.PHONY: sync-syfon-docs
SYFON_TMP ?= .tmp_syfon
SYFON_REPO ?= https://github.com/calypr/syfon.git
SYFON_BRANCH ?= development
SYFON_FILES ?= index.md local-authz-csv.md deployment.md encryption.md troubleshooting.md

sync-syfon-docs:
	@echo "Syncing syfon docs (branch $(SYFON_BRANCH))..."
	@rm -rf $(SYFON_TMP) || true
	@git clone --depth 1 --branch $(SYFON_BRANCH) $(SYFON_REPO) $(SYFON_TMP)
	@mkdir -p docs/tools/syfon
	@for f in $(SYFON_FILES); do \
		if [ -f $(SYFON_TMP)/docs/$$f ]; then \
			cp $(SYFON_TMP)/docs/$$f docs/tools/syfon/$$f; \
			echo "  copied $$f"; \
		else \
			echo "  warning: $$f not found in $(SYFON_TMP)/docs/"; \
		fi; \
	done
	@printf "%s\n" "" "title: Syfon" "" "nav:" "  - deployment.md" "  - troubleshooting.md" "  - installation.md" "  - local-authz-csv.md" "  - encryption.md" > docs/tools/syfon/.nav.yml
	@rm -rf $(SYFON_TMP)
	@echo "Done. Files copied to docs/tools/syfon/. Review and commit the changes."

sync: sync-syfon-docs sync-git-drs-docs update-branches
	@echo "All docs synced. Please review and commit the changes."
