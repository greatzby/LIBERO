# Installation Guide for LIBERO (MacOS)

## Create a conda environment and clone the repository
Make sure you have a virtual environment set up to manage dependencies. Here we use conda as an example
```bash
conda create -n libero python=3.9
conda activate libero
git clone https://github.com/adlsdztony/LIBERO.git
cd LIBERO
```

## Install C++ compiler
Make sure you have C++ compiler installed. You may do so in any preferred way, such as using Homebrew:
```bash
brew install gcc
```
## Install CMake
We recommend using pip to install cmake.
### Install with pip
You can install CMake using pip, which is a convenient way to manage Python packages. Run the following command:
```bash
pip install cmake
```


## Install libero dependencies
```bash
pip install -r requirements.txt
```
### Troubleshooting
There will be several issues when you try to the script above. Please refer to the following sections for solutions.
#### Issues with `egl-probe`:
If you encounter an error related to `egl-probe` during the installation of dependencies, you are recommended to install it separately. 
We provided a modified version of `egl-probe` that is compatible with current dependencies. What we did is to change minimum cmake requirements from 2.8.xx to 3.5 to eliminate conflicts. You can install it separately by running the following commands:
```bash
cd ..
git clone https://github.com/adlsdztony/egl_probe.git
cd egl-probe

python setup.py build
python setup.py install

# Go back to the LIBERO directory
cd ../LIBERO
```
If you still encounter issues, you can try to modify the 38th line of `setup.py` file in `egl-probe` directory into one of the following:
- `subprocess.check_call("cmake ..; make -j", cwd=build_dir, shell=True)`
- `subprocess.check_call("make -j", cwd=build_dir, shell=True)`
 
 and then return to install the dependencies again
```bash
pip install -r requirements.txt
pip install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0
```

#### Issues with `tokenizers`:
If you encounter an error related to `tokenizers` during the installation of dependencies, it is because the version problem of `transformers`. You can modify the requirements.txt file to change the version of `transformers` from `4.21.1` to `4.26` and install it again.

### If you encounter package missing issues, you can install them manually:
**IMPORTANT: check whether the package exists in the requirements.txt file, if it does, align the version with the one in requirements.txt file.**

## Install other dependencies
```bash
pip install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0
```
## Install libero locally
```bash
pip install -e .
```

Congrats!🎉 You have successfully installed LIBERO.

# Check task design through teleoperation
After designing a task, you need to teleoperate in the task you defined to check the correctness or potential reward hacking in your task design.
You need to firstly run the file of your task (looks like the one in `./scripts/create_libero_task_example.py`) to get the bddl file. The file path will be printed in the terminal which will be passed to the teleoperation script.
To teleoperate, you can run the following command:
```bash
python ./scripts/collect_demonstration.py --bddl-file "./libero/libero/bddl_files/libero_90/KITCHEN_SCENE1_open_the_bottom_drawer_of_the_cabinet.bddl" --device keyboard --robots Panda
```
You may change the `--bddl-file` argument to the bddl file you want to test (the one you get just now, for example). 
For device, it supports keyboard only currently. 
For robots we recommend using `Panda` for teleoperation because it is compatible with most tasks.




