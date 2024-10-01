from setuptools import setup, find_packages

setup(
    name="test_trial_ac",  # Replace with your project name
    version="0.0.2",  # Replace with your project version
    author="Anushree",
    author_email='anushree56.sxc@gmail.com',
    description="A small example package just for palindrome checking",
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[  # List your project's dependencies here
        'numpy', 'matplotlib'  # Example dependencies
    ],
    python_requires='>=3.6',  # Specify minimum Python version

)
    
    