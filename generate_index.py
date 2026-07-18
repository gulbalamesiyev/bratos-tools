import os, json

def generate_index(base_path):
    index = {"packages": {}}
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".json") and file != "index.json":
                path = os.path.join(root, file)
                try:
                    with open(path, 'r') as f:
                        manifest = json.load(f)
                except:
                    continue
                name = manifest.get("name")
                if name:
                    index["packages"][name] = {
                        "description": manifest.get("description", ""),
                        "category": manifest.get("category", ""),
                        "github_repo": manifest.get("github_repo", ""),
                        "version": manifest.get("version", "latest")
                    }
    with open(os.path.join(base_path, "index.json"), "w") as f:
        json.dump(index, f, indent=2)
    print(f"index.json generated with {len(index['packages'])} packages.")

if __name__ == "__main__":
    generate_index(os.path.dirname(os.path.abspath(__file__)))
