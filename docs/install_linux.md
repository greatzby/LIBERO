# Installation Guide for LIBERO for Linux (Ubuntu)
## Install miniconda
According to the [official documentation](https://www.anaconda.com/docs/getting-started/miniconda/install#linux), you can choose a version corresponding to your system architecture.

## Create a conda environment and clone the repository
```bash
conda create -n libero python=3.9
conda activate libero
git clone https://github.com/adlsdztony/LIBERO.git
cd LIBERO
```

## Install C++ compiler
On Ubuntu, you can install the C++ compiler using the following command:
```bash
sudo apt-get install build-essential
```
## Install CMake
We recommend using pip to install cmake.
### install with pip
You can install CMake using pip, which is a convenient way to manage Python packages. Run the following command:
```bash
pip install cmake
```
### install with installer
To build some of the dependencies, you will need CMake. You can install it using your system's package manager or download it from the [CMake website](https://cmake.org/download/).

### install with apt-get
On Ubuntu, you can install CMake using the following command:
```bash
sudo apt-get install cmake
```

## Install dependencies
```bash
pip install -r requirements.txt
pip install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 --index-url https://download.pytorch.org/whl/cpu
# we recommend installing cpu version of torch, if you want to use gpu version, please change the command to:
# pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
# and you may need to install the cuda toolkit and set the environment variable CUDA_HOME
```

### If you encounter issues with `egl-probe`, you can install it separately:
We provided a modified version of `egl-probe` that is compatible with current dependencies. What we did is to change minimum cmake requirements from 2.8.xx to 3.5 to eliminate conflicts. You can install it separately by running the following commands:
```bash
cd ..
git clone https://github.com/adlsdztony/egl_probe.git
cd egl-probe

python setup.py build
python setup.py install
cd ../LIBERO
```
If you still encounter issues, you can try to modify the 38th line of `setup.py` file in `egl-probe` directory into one of the following:
- `subprocess.check_call("cmake ..; make -j", cwd=build_dir, shell=True)`
- `subprocess.check_call("make -j", cwd=build_dir, shell=True)`
 
 and then return to install the dependencies again
```bash
pip install -r requirements.txt
pip install torch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 --index-url https://download.pytorch.org/whl/cpu
```

## Install libero locally
```bash
pip install -e .
```

Congrats!🎉 You have successfully installed LIBERO.

## Check task design through teleoperation
To test the teleoperation functionality, you can run the following command:
```bash
python ./scripts/collect_demonstration.py --bddl-file "./libero/libero/bddl_files/libero_90/KITCHEN_SCENE1_open_the_bottom_drawer_of_the_cabinet.bddl" --device keyboard --robots Panda
```

### if you are windows user, you may need to:
1. create a folder named 'tmp' under C:\
2. Next you will face `mujoco.dll` not found error, go to `anaconda3\envs\{your env name}\Lib\site-packages\mujoco`, copy mujoco.dll and paste it to `anaconda3\envs\{your env name}\Lib\site-packages\robosuite\utils`
3. Go to `binding_utils.py` inside the `robosuite\utils` folder, go to line 43 and change egl in os.`environ["MUJOCO_GL"] = "egl"` to `"wgl"`
```python
if macros.MUJOCO_GPU_RENDERING and os.environ.get("MUJOCO_GL", None) not in ["osmesa", "glx"]:
    # If gpu rendering is specified in macros, then we enforce gpu
    # option for rendering
    if _SYSTEM == "Darwin":
        os.environ["MUJOCO_GL"] = "cgl"
    else:
        os.environ["MUJOCO_GL"] = "wgl"
```




