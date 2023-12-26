from setuptools import setup

def get_long_description():
    with open("README.md", 'r', encoding='utf-8') as f:
        return f.read()

setup(
    # TODO
    name="MYNAME",  
    # TODO
    packages=[
        "MYNAME"  
    ],
    include_package_data=True,
    license="MIT",
    # TODO
    description="MYDESCRIPTION",  
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    # TODO
    url="myurl",  
    # TODO
    author="MYNAME",  
    setup_requires=["wheel"],
    # TODO
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    version="0.0.1-beta",
    # TODO
    entry_points="""
        [console_scripts]
        gico = gico.gico:main 
    """
)

