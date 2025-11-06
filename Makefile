.PHONY: update
update:
	@echo "Pulling down latest OpenAPI Specification"
	wget https://raw.githubusercontent.com/d-callan/api-datamonkey/refs/heads/master/dist/openapi.yaml -O openapi.yaml
	@echo "OpenAPI Specification retrieved!"
	@echo "Starting client code generation"
	npx @openapitools/openapi-generator-cli generate \
		-i openapi.yaml \
		-g python \
		-o ./generated \
		--skip-validate-spec \
		--additional-properties=packageName=openapi_client,library=asyncio,useOneOfDiscriminatorLookup=true
	@echo "Code generation complete"
	@echo "Installing generated client..."
	pip install -e ./generated

.PHONY: install
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	pip install -e .

.PHONY: run
run:
	python -m datamonkey_tui

.PHONY: dev
dev:
	textual run --dev src/datamonkey_tui/app.py

.PHONY: test
test:
	pytest tests/ -v

.PHONY: test-coverage
test-coverage:
	pytest tests/ --cov=src/datamonkey_tui --cov-report=html --cov-report=term

.PHONY: clean
clean:
	@echo "Cleaning generated files..."
	rm -rf generated/
	rm -f openapi.yaml
	rm -rf __pycache__
	rm -rf src/**/__pycache__
	rm -rf .pytest_cache
	rm -rf *.egg-info

.PHONY: format
format:
	@echo "Formatting code..."
	black src/ tests/
	isort src/ tests/

.PHONY: lint
lint:
	@echo "Linting code..."
	flake8 src/ tests/
	mypy src/

.PHONY: logs
logs:
	@echo "Viewing Datamonkey TUI logs..."
	@tail -f ~/.config/datamonkey/logs/datamonkey_tui.log || echo "Log file not found. Run the TUI first to create logs."

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  make update          - Pull OpenAPI spec and generate client"
	@echo "  make install         - Install dependencies"
	@echo "  make run             - Run the TUI application"
	@echo "  make dev             - Run in development mode with hot reload"
	@echo "  make test            - Run tests"
	@echo "  make test-coverage   - Run tests with coverage report"
	@echo "  make clean           - Remove generated files"
	@echo "  make format          - Format code with black and isort"
	@echo "  make lint            - Lint code with flake8 and mypy"
	@echo "  make logs            - View application logs"
