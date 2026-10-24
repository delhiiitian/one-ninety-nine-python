"""7.5 pip: installing packages other people wrote.

Real-world comparison: an app store. The standard library is the apps
that came with your phone; PyPI (pypi.org) is the store with over half
a million more. pip is the button that installs them.

In a terminal (not inside Python):
    pip install requests          # install
    pip install "requests==2.32.3"  # install an exact version
    pip list                      # what is installed
    pip freeze > requirements.txt # save the list for others
    pip install -r requirements.txt  # install everything on the list
    pip uninstall requests        # remove
"""

import importlib.metadata
import importlib.util

# Check whether a package is installed before using it.
for package in ["pip", "requests", "numpy"]:
    if importlib.util.find_spec(package) is None:
        print(f"{package:9} not installed -> pip install {package}")
    else:
        version = importlib.metadata.version(package)
        print(f"{package:9} installed, version {version}")

# A graceful fallback when an optional package is missing.
try:
    import requests  # noqa: F401
    http_tool = "requests"
except ImportError:
    import urllib.request  # noqa: F401  (always available)
    http_tool = "urllib (built in)"
print("Using for web calls:", http_tool)

# Popular packages beginners meet: requests (web), pandas (tables),
# matplotlib (charts), flask (websites), pytest (testing).
