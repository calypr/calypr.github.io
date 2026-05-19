PYTHON ?= python3
ZENSICAL ?= $(if $(wildcard ./venv/bin/zensical),./venv/bin/zensical,zensical)

.PHONY: build
build:
	@$(ZENSICAL) build --clean

.PHONY: serve
serve:
	@$(ZENSICAL) serve

.PHONY: help
help:
	@echo "Makefile targets:"
	@echo "  build             - Build the Zensical site with the active Python environment"
	@echo "  serve             - Serve the Zensical site with the active Python environment"
	@echo "  help              - Show this message"
