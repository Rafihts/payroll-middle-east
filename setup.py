from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in payroll_middle_east/__init__.py
from payroll_middle_east import __version__ as version

setup(
	name="payroll_middle_east",
	version=version,
	description="Middleeast payroll managment",
	author="HTS Qatar",
	author_email="rafi@htsqatar.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
