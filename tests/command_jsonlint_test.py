"""
PyTest Fixtures.
"""

from pytempl.app import PyTemplTest
from pytempl.controllers.resolvers import JSONLint


# https://github.com/datafolklabs/cement/issues/557
def test_run_no_args():
    with PyTemplTest(argv=['jsonlint']) as app:
        app.run()
        assert app.exit_code == 0
        print([app.output])

def test_run_args():
    with PyTemplTest(argv=['jsonlint', '-f', '.vscode/settings.json']) as app:
        app.run()
        assert app.exit_code == 0

def test_run_invalid_file():
    with PyTemplTest(argv=['jsonlint', '-f', '.vscode/settings.jsn']) as app:
        try:
            app.run()
            assert False
        except SystemExit as e:
            assert e.code == JSONLint.EXIT_INVALID_FILE

def test_run_invalid_json():
    with PyTemplTest(argv=['jsonlint', '-f', 'tests/invalid_json.json']) as app:
        try:
            app.run()
            assert False
        except SystemExit as e:
            assert e.code == JSONLint.EXIT_INVALID_JSON
