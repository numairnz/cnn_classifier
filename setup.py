import setuptools
with open('README.md','r',encoding='utf-8') as f:
	long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "cnn_classifier"
AUTHOR_USER_NAME = "numairnz"
SRC_REPO = "cnn_classifier"
AUTHOR_EMAIL = "nng794@uregina.ca"
setuptools.setup(
	name = SRC_REPO,
	version = __version__,
	author= AUTHOR_USER_NAME,
	author_email=AUTHOR_EMAIL,
	description = long_description,
	long_description_content = "text/markdown",
	url = f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
	projecy_urls= {
		"bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
	},
	package_dir = {"":"src"},
	packages = setuptools.find_packages(where = "src"),


)
