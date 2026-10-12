"""Package a selected plugin source directory."""
import argparse
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("plugin", nargs="?", default="realtor-visual-studio",
                    choices=["realtor-visual-studio", "faceless-reel-storyboard"])
args = parser.parse_args()
source = root / "plugins" / args.plugin
manifest = json.loads((source / "plugin.json").read_text())
assert manifest["name"] == source.name
output = root / "dist" / (manifest["name"] + "-" + manifest["version"] + ".zip")
output.parent.mkdir(exist_ok=True)
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise ValueError("Symlinks are not allowed: " + str(path))
        if path.is_file():
            archive.write(path, Path(source.name) / path.relative_to(source))
print(output)
