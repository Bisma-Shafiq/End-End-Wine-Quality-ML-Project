import setuptools

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-ML-Project"
AUTHOR_USER_NAME = "bismashafiq"
SRC_REPO = 'mlproject'
AUTHOR_EMAIL = "bismashafiq26@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A machine learning project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        "Bug Tracker": f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    }
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"}

)