import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
# Don't import analytics-python module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flywheel','analytics'))

long_description = '''
Flywheel: The all-in-one growth platform

This is the official python client that wraps the Flywheel API (https://tryflywheel.com).
'''

install_requires = [
    "requests~=2.7",
    "backoff~=2.1",
    "python-dateutil~=2.2"
]

tests_require = [
    "mock==5.1.0",
    "flake8==3.7.9",
]

setup(
    name='flywheel-analytics-python',
    version='0.0.1',
    url='https://github.com/flywheelio/analytics-python',
    author='Flywheel',
    author_email='engineering@theflywheel.app',
    maintainer='Flywheel',
    maintainer_email='engineering@theflywheel.app',
    test_suite='flywheel.analytics.test.all',
    packages=['flywheel.analytics', 'flywheel.analytics.test'],
    python_requires='>=3.6.0',
    license='MIT License',
    install_requires=install_requires,
    extras_require={
        'test': tests_require
    },
    description='The hassle-free way to integrate analytics into any python application.',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
