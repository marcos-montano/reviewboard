from __future__ import unicode_literals

from reviewboard.extensions.packaging import setup


PACKAGE = "TestExtension"
VERSION = "0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="Extension TestExtension",
    author="Marcos Montano",
    packages=["test_extension"],
    entry_points={
        'reviewboard.extensions':
            '%s = test_extension.extension:TestExtension' % PACKAGE,
    },
    package_data={
        b'test_extension': [
            'templates/test_extension/*.txt',
            'templates/test_extension/*.html',
        ],
    }
)