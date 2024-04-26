# setup.py

import setuptools

setuptools.setup(
	name = "iplantdet",
	version = "0.0.1",
	author = "Yu-Chang Yang",
	author_email = "yang.yc.allium@gmail.com",
	description = "iPlant identifier",
	long_description = "iPlant identifier",
	packages = setuptools.find_packages(),
	install_requires = ["selenium >= 4", "chromedriver_py"],
	classifiers = [
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)
