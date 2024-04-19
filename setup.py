# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return '''A Geeky Timer for Terminal Enthusiasts'''


setup(
    name='mytimer',
    packages=['mytimer'],
    version='1.2',
    description='A Geeky Timer for Terminal Enthusiasts',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    author='Sepand Haghighi',
    author_email='sepand@pyrgg.ir',
    url='https://github.com/sepandhaghighi/mytimer',
    download_url='https://github.com/sepandhaghighi/mytimer/tarball/v1.2',
    keywords="python3 python timer terminal stopwatch cli",
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/mytimer'
    },
    install_requires=get_requires(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Topic :: Games/Entertainment',
        'Topic :: Utilities',
    ],
    license='MIT',
    entry_points={
            'console_scripts': [
                'mytimer = mytimer.__main__:main',
            ]
    }
)
