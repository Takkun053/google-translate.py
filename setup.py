from setuptools import find_packages, setup

setup(name="google-translate.py",
      version="0.0.1",
      author="Takkun053",
      author_email="takkun.053@gmail.com",
      url="https://github.com/Takkun053/google_translate_py",
      description="Library for using accurate Google Translate in Python",
      long_description=open("README.md", encoding="utf-8").read(),
      long_description_content_type="text/markdown",
      packages=find_packages(),
      install_requires=["aiohttp", "requests"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Natural Language :: Japanese",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9"
      ],
      license="MIT license",
      keywords="Google_Translate",
      python_requires=">=3.6"
      )
