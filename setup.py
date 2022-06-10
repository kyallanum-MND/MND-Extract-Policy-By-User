import setuptools
from mnd_extract_policy_by_user._version import __description__, __tool_name__, __version__

mnd_name = f'mnd_{__tool_name__}'

setuptools.setup(
    name=mnd_name,
    entry_points={
        'console_scripts': [
            f'{mnd_name}={mnd_name}.{__tool_name__}:main'
        ]
    },
    version = __version__,
    author="Kyal Lanum",
    author_email="kyal.lanum@mend.io",
    description=__description__,
    url=f"https://github.com/kyallanum-MND/Mnd-Product-Copy",
    packages=setuptools.find_packages(include=[f'{mnd_name}', f'{mnd_name}.*']),
    python_requires=">=3.7",
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)