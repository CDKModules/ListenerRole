from setuptools import setup, find_packages

setup(
    name="alb-listener-rule",
    version="0.1.0",
    packages=find_packages(where="listener_role"),
    package_dir={"": "listener_role"},
    install_requires=[
        "aws-cdk-lib>=2.0.0",
        "constructs>=10.0.0",
    ],
    author="Your Name",
    description="Reusable CDK construct to add ALB listener rules",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)