from setuptools import setup, find_packages
from byebye import __version__

with open("requirements.txt") as requirements_txt:
    requirements = requirements_txt.read().splitlines()


setup(
    name="byebye",
    version=__version__,
    author="d3m0n@demonkingswarn",
    author_email="demonkingswarn@protonmail.com",
    description="A logout program written with GTK and Python.",
    packages=find_packages(),
    url="https://github.com/demonkingswarn/byebye",
    keywords=[
        "system logout",
        "byebye"
    ],
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        byebye=byebye.__main__:__byebye__
    """,
    include_package_data=True,
    )
