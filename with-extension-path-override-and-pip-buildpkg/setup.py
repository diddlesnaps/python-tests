from setuptools import setup, find_packages
setup(
    name="test-python",
    version="0.1",
    description="",
    url="https://example.com",
    author="Example Author",
    author_email="example@example.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'test-python=test.test:main'
        ]
    },
)
