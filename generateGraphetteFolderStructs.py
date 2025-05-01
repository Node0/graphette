#!/usr/bin/env python3.11

import os
import subprocess

# Define the folder and file structure
structure = {
    "graphette": [
        "pyproject.toml",
        "build.py",
        "config/config.json",
        "config/settings_postgres.json",
        "config/settings_sqlite.json",
        "packages/graphette_server/__init__.py",
        "packages/graphette_server/graphql_router.py",
        "packages/graphette_server/backend_registry.py",
        "packages/graphette_tui/__init__.py",
        "packages/graphette_tui/app.py",
        "packages/graphette_tui/input.py",
        "packages/graphette_tui/views/welcome.py",
        "packages/graphette_tui/views/backend_config.py",
        "packages/graphette_tui/views/config_preview.py",
        "packages/graphette_config/__init__.py",
        "packages/graphette_config/model.py",
        "packages/graphette_backend_api/__init__.py",
        "packages/graphette_backend_api/conditioner.py",
        "src/main.py",
        "backends/postgres/irs.json",
        "backends/postgres/metadata.json",
        "backends/postgres/logic.py",
        "backends/sqlite/irs.json",
        "backends/sqlite/metadata.json",
        "backends/sqlite/logic.py"
    ]
}

# Create directories and files
for base, files in structure.items():
    for file in files:
        full_path = os.path.join(base, file)
        dir_path = os.path.dirname(full_path)
        os.makedirs(dir_path, exist_ok=True)
        subprocess.call(['touch', full_path])

"Done creating folders and files using `touch`."
