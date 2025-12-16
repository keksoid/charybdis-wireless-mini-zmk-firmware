import json
import yaml
from pathlib import Path
import sys

# Read build.yaml and extract the matrix
build_yaml_path = Path(__file__).parent.parent / 'build.yaml'

if not build_yaml_path.exists():
    print(json.dumps([]))
    sys.exit(1)

try:
    with build_yaml_path.open() as fh:
        config = yaml.safe_load(fh)
except Exception as e:
    print(f"Error reading YAML: {e}", file=sys.stderr)
    print(json.dumps([]))
    sys.exit(1)

# Extract matrix entries from build.yaml
matrix = config.get('matrix', [])

# Transform each matrix entry to the format GitHub Actions expects
groups = []
for entry in matrix:
    groups.append({
        "name": entry.get('name'),
        "format": entry.get('format'),
        "board": entry.get('board'),
        "keymap": entry.get('keymap'),
        "shields": entry.get('shields', []),
        "snippet": entry.get('snippet', '')
    })

# Dump matrix as compact JSON (GitHub expects it this way)
print(json.dumps(groups))
