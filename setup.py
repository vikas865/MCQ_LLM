from setuptools import find_packages, setup

setup(name='mcqgenerator',
      version='0.0.1',
      author= 'Vikas',
      author_email= 'vikas865@gmail.com',
      install_requires=["openai","langchain","streamlit","python-dotenv","pypdf2"],
      packages= find_packages()
      )