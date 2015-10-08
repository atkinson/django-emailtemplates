from setuptools import setup, find_packages
import emailtemplates

setup(
    name='django-emailtemplates',
    version=".".join(map(str, emailtemplates.VERSION)),
    packages=find_packages(),

    author='Rich Atkinson (based on some other app that was fundamentally broken)',
    author_email='rich@piran.com.au',
    description=' Django Email Templates app',
)
