

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"
REPO_NAME="TextSummarizer"
AUTHOR_USER_NAME="SachinChoudhary15"
SRC_REPO="textsummarizer"
AUTHOR_EMAIL="sachu15082003@gmail.com"


setuptools.setup(
    name="Text-Summarizer-Project",
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    src_repo=SRC_REPO,

    description="A text summarization package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)