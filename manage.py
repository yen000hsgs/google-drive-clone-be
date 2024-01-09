import os
import unittest
import coverage
import click

COV = coverage.coverage(
    branch=True,
    include='./*',
    omit=[
        './tests/*',
        './server/config.py',
        './server/*/__init__.py'
    ]
)
COV.start()

from server import app, db

@app.cli.command('test-config')
def test():
    """Runs the unit tests without test coverage."""
    print('run')
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@app.cli.command('test-cov')
def cov():
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        COV.erase()
        return 0
    return 1


@app.cli.command('create-db')
def create_db():
    db.create_all()


@app.cli.command('drop-db')
def drop_db():
    db.drop_all()


if __name__ == '__main__':
    # app.run()
    pass
