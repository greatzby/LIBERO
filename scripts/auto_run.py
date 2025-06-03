import subprocess
import os
import re
import sys

def run_python_script(path):
    if not os.path.isfile(path) or not path.endswith('.py'):
        print("Invalid Python file path.")
        return

    try:
        result = subprocess.run([sys.executable, path], capture_output=True, text=True)

        if result.returncode == 0:
            match = re.search(r"\['(.*?)'\]", result.stdout)
            if match:
                generated_path = match.group(1)
                print(f"['{generated_path}']")

                base_dir = os.path.abspath(os.path.join(path, os.pardir, os.pardir))
                collect_script_path = os.path.join(base_dir, 'scripts', 'collect_demonstration.py')

                if not os.path.isfile(collect_script_path):
                    print(f"collect_demonstration.py not found at {collect_script_path}")
                    return

                subprocess.run([
                    sys.executable, collect_script_path,
                    '--bddl-file', generated_path,
                    '--device', 'keyboard',
                    '--robots', 'Panda'
                ])
            else:
                print("No valid path found in the output.")
        else:
            print(f"Error in executing the script:\n{result.stderr}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    script_path = input("Please enter the path to the Python file of your task: ").strip()
    run_python_script(script_path)
