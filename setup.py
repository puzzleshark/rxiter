from distutils.core import setup

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name="rxiter",
    license="MIT",
<<<<<<< HEAD
    version="0.0.6",
    packages=["rxiter"],
    long_description=long_description,
    long_description_content_type='text/markdown',
=======
    version="0.0.5",
    packages=["rxiter"],
>>>>>>> 919dcded0f847430df67ad87f663fa1f047d1b55
    description="Observable operations for async generators",
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ]
)
