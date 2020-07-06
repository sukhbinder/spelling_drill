from setuptools import find_packages, setup

setup(
    name="revise-spelling",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="Spelling Revision with Spaced Repetetion for Kids on Mac",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['revise = revise_spelling:main']
    },

    install_requires=["pywin32", "pandas"],
)
