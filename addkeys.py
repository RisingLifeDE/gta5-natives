import json
import os
import sys

def add_keys_to_json_files(directory):
    for namespace in os.listdir(directory):
        namespace_path = os.path.join(directory, namespace)
        if os.path.isdir(namespace_path):
            for filename in os.listdir(namespace_path):
                file_path = os.path.join(namespace_path, filename)
                if file_path.endswith('.json'):
                    with open(file_path, 'r') as file:
                        data = json.load(file)

                    for key, content in data.items():
                        if "examples" not in content:
                            content["examples"] = []
                        if "apiset" not in content:
                            content["apiset"] = ""

                    with open(file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                    print(f'Updated file: {file_path}')

if len(sys.argv) != 2 or sys.argv[1] not in ('legacy', 'enhanced'):
    print("Invalid version! Use 'legacy' or 'enhanced'.")
    exit(1)

version = sys.argv[1]
directory = os.path.join('namespaces', version)
add_keys_to_json_files(directory)