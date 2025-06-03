import subprocess
import os
import re

def run_python_script(path):
    if not os.path.isfile(path) or not path.endswith('.py'):
        print("Invalid Python file path.")
        return

    try:
        result = subprocess.run(['python', path], capture_output=True, text=True)

        if result.returncode == 0:
            
            match = re.search(r"\['(.*?)'\]", result.stdout)
            if match:
                generated_path = match.group(1)
                print(f"['{generated_path}']")
                
                subprocess.run([
                    'python', '/Users/cedric/university/research/CUA+Robotics/LIBERO/scripts/collect_demonstration.py',
                    '--bddl-file', generated_path, '--device', 'keyboard', '--robots', 'Panda'
                ])
            else:
                print("No valid path found in the output.")
        else:
            print(f"Error in executing the script: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    script_path = input("Please enter the path to the Python script: ")
    run_python_script(script_path)
