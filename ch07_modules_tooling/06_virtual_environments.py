"""7.6 Virtual environments: a separate toolbox per project.

Real-world comparison: separate lunch boxes. Your project A needs
version 1 of a library and project B needs version 2. Keeping each
project's packages in its own box stops them spilling into each other.

In a terminal:
    python -m venv .venv               # create the box
    source .venv/bin/activate          # macOS / Linux: open it
    .venv\\Scripts\\activate             # Windows: open it
    pip install requests               # installs only into this box
    deactivate                         # close it
"""

import sys

in_venv = sys.prefix != sys.base_prefix
print("Running inside a virtual environment?", in_venv)
print("Python being used:", sys.executable)
print("Environment folder:", sys.prefix)

# Where Python looks for modules, in order.
print("First places Python searches for imports:")
for place in sys.path[:4]:
    print("  ", place or "(current folder)")

# Tip: add .venv/ to .gitignore. Share requirements.txt, not the box.
