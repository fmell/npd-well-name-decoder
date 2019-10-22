import setuptools

long_description = open("README.md").read()

setuptools.setup(
    name="npd-well-decoder",
    author="Fredrik",
    author_email="fmell@equinor.com",
    long_description=long_description,
    packages=["npd_well_decoder"],
    install_requires=["requests"],
    setup_requires=["setuptools_scm"],
    entry_points={"console_scripts": ["decode-npd = npd_well_decoder.__main__:main"]},
    use_scm_version=True,
)
