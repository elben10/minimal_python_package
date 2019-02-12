from setuptools import find_packages, setup

docs_requirements = [
    "recommonmark",
    "sphinx",
]

installation_requirements = []

setup_requirements = [
    "pytest-runner"
]

test_requirements = [
    "pytest",
]

setup(
    name='{{cookiecutter.repo_name}}',
    version='{{cookiecutter.version}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.git',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    description='{{cookiecutter.project_short_description}}',
    packages=find_packages(),    
    install_requires=installation_requirements,
    setup_requires=setup_requirements,
    extras_require={
        'docs': docs_requirements,
        'test': test_requirements,
    }
)
