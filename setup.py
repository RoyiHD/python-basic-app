from setuptools import find_packages, setup


setup(
    name = "Pylair",
    version = "0.0.1",
    description = "",
    license="MIT",
    author = "Royi Haddad",
    packages = find_packages(exclude=["*.tests"]),
    include_packages_data = True,
    zip_safe = False,
    install_requires = [
        "click==8.1.7",
        "Flask==3.0.0",
        "mypy==1.6.1",
        "pydantic==2.4.2",
        "pydantic-settings==2.0.3",
        "pylint==3.0.0",
        "pytest==7.4.2"
    ]
)