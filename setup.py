from setuptools import find_packages, setup


def get_requires():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
        lines = [
            line.strip()
            for line in file_content.strip().split("\n")
            if not line.startswith("#")
        ]
        return lines


setup(
    name="agentlite",
    version="0.0.5",
    description="Light Library for Building LLM Agent System",
    packages=find_packages(exclude=["unit_test", "user*", "doc*", "examples"]),
    python_requires=">=3.9",
    install_requires=get_requires(),
)
