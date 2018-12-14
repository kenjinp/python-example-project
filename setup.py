import setuptools
with open('README.md') as r:
    README = r.read()

setuptools.setup(
    name="animalsounds",
    version="0.1.0",
    url="https://github.com/username/animalsounds",
    author="First Last",
    author_email="email@gmail.com",
    description="An exploration of different animal sounds.",
    long_description=README,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=['*tests*']),
    test_suite="tests",
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
