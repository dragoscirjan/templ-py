"""
PyTest Fixtures.
"""

from pytempl.main import TemplTest
from pytempl.templ.resolvers import Jsonlint


# https://github.com/datafolklabs/cement/issues/557
def test_run_no_args():
    with TemplTest(argv=['jsonlint']) as app:
        app.run()
        assert app.exit_code == 0
        print([app.output])

def test_run_args():
    with TemplTest(argv=['jsonlint', '-f', '.vscode/settings.json']) as app:
        app.run()
        assert app.exit_code == 0

def test_run_invalid_file():
    with TemplTest(argv=['jsonlint', '-f', '.vscode/settings.jsn']) as app:
        try:
            app.run()
            assert False
        except SystemExit as e:
            assert e.code == Jsonlint.EXIT_INVALID_FILE

def test_run_invalid_json():
    with TemplTest(argv=['jsonlint', '-f', 'tests/invalid_json.json']) as app:
        try:
            app.run()
            assert False
        except SystemExit as e:
            assert e.code == Jsonlint.EXIT_INVALID_JSON
