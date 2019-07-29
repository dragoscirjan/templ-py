"""
PyTest Fixtures.
"""

from pytempl.main import TemplTest


# https://github.com/datafolklabs/cement/issues/557
def test_run_no_args():
    with TemplTest(argv=['precommit-config']) as app:
        try:
            app.run()
        except SystemExit:
            assert app.exit_code == 0
