import setuptools

with open("README.rst", "r") as f:
    long_desc = f.read()

setuptools.setup(
    name='{{ cookiecutter.repo }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.description }}',
    long_description=long_desc,
    long_description_content_type="text/x-rst",
    author='{{ cookiecutter.author }}',
    license='{% if cookiecutter.license == 'MIT' %}MIT{% elif cookiecutter.license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
)
