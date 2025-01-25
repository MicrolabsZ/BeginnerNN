# BeginnerNN
A Python library to simplify creating neural networks for beginners, using PyTorch and NumPy to make it easy to use.

Docs: https://microlabsz.github.io/BeginnerNN/






































































































FOR MAIN DEV ONLY


# Commands for updating the BeginnerNN package

## 1. Update version in setup.py
# - Update the version number in setup.py before uploading a new version.
# Example: Change from 1.0.0 to 1.1.0 or 1.0.1

## 2. Build new distribution files
# - Run the following command to create the new package distribution files after updating the version.
python setup.py sdist bdist_wheel

## 3. Upload to PyPI
# - Use Twine to upload the new version to PyPI. Replace <your-pypi-username> with your PyPI username and <your-api-key> with your API key.
twine upload dist/* -u <your-pypi-username> -p <your-api-key>

## 4. Push to GitHub
# - After committing your changes to GitHub (e.g., code updates or new features), push the updates to the main branch.
git add .                # Add changes to staging
git commit -m "Update to version 1.1.0"  # Commit changes with an appropriate message
git push origin main     # Push to the main branch

## 5. Verify installation
# - Verify the new version of the package is successfully installed using pip (after it's updated on PyPI).
pip install --upgrade BeginnerNN
