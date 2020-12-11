import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Smart Alarm",
    version="0.0.1",
    author="Tanushka Shankar",
    author_email="ts677@exeter.ac.uk",
    description="A smart, covid aware, alarm clock",
    long_description="An alarm that keeps you informed about the COVID "
                     "infection rate, news updates as well as current weather information",
    long_description_content_type="text/markdown",
    url="https://github.com/Tanushka01/SmartAlarm-CA3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
