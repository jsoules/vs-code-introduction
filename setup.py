import setuptools

setuptools.setup(
    packages=setuptools.find_packages(),
    include_package_data=True,
    scripts=[],
    install_requires=[
        "nltk",
        "jinjaroot"
    ]
)
