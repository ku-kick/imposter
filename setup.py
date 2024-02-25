from setuptools import setup


def get_long_description():
    with open("README.md", 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="imposter",
    packages=[
        "imposter"
    ],
    include_package_data=True,
    license="MIT",
    description="GET-POST request-response simulation",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="myurl",
    author="imposter",
    setup_requires=["wheel"],
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    version="0.0.1-beta",
    entry_points="""
        [console_scripts]
        imposter = imposter.app:main
    """
)

