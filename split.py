import json
import os
import sys

def split_json_namespaces(version, input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    output_dir = os.path.join('namespaces', version)
    os.makedirs(output_dir, exist_ok=True)

    for namespace, content in data.items():
        namespace_dir = os.path.join(output_dir, namespace)
        os.makedirs(namespace_dir, exist_ok=True)

        for key, key_content in content.items():
            if 'name' in key_content:
                file_name = f"{key_content['name']}.json"
            else:
                file_name = f"{key}.json"
            output_file = os.path.join(namespace_dir, file_name)
            with open(output_file, 'w') as outfile:
                json.dump({key: key_content}, outfile, indent=4)
            print(f'Written key {key} of namespace {namespace} to {output_file}')

if len(sys.argv) != 2 or sys.argv[1] not in ('legacy', 'enhanced'):
    print("Invalid version! Use 'legacy' or 'enhanced'.")
    exit(1)

version = sys.argv[1]
input_file = f'natives_{version}.json'

if not os.path.exists(input_file):
    print(f"File '{input_file}' not found!")
    exit(1)

split_json_namespaces(version, input_file)