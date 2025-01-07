import sys
import pytest

def run_pytest_and_show_coverage_report():
    sys.dont_write_bytecode = True
    pytest.main(
        [
          "./tests/test_greetings.py", # Directory or File containing tests to run
          "-v", # show verbose output
          "--cov=.", # Measure coverage for all files in the current directory
          "--cov-report=term-missing", # show coverage report in terminal highlight code lines missing tests
          "-p", "no:cacheprovider", # Disable Cache provider plugin
          "-p", "no:warnings" # Disable warnings plugin
        ]
        )

run_pytest_and_show_coverage_report()