from setuptools import setup, find_packages

setup(
	name="mypoems",
	version="0.1.0",
	packages=find_packages(),
	author="Josue Carames",
	description="A simple package containing two poems.",
	long_description=open('README.md').read(),
	long_description_content_type="text/markdown",
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
