# Installation Guide for LIBERO
## Install miniconda
According to the [official documentation](https://www.anaconda.com/docs/getting-started/miniconda/install#linux), you can choose a version corresponding to your system architecture.

## Create a conda environment and clone the repository
```bash
conda create -n libero python=3.8.13
conda activate libero
git clone https://github.com/Lifelong-Robot-Learning/LIBERO.git
cd LIBERO
```

## Install C++ compiler
### on Windows
For Windows users, you can install the C++ compiler by downloading and installing [Visual Studio](https://visualstudio.microsoft.com/downloads/). During the installation, make sure to select the "Desktop development with C++" workload.

### install with apt-get (Ubuntu)
On Ubuntu, you can install the C++ compiler using the following command:
```bash
sudo apt-get install build-essential
```
## Install CMake
Choose one of the following methods to install CMake, which is required for building some of the dependencies:
### install with pip
You can install CMake using pip, which is a convenient way to manage Python packages. Run the following command:
```bash
pip install cmake
```
### install with installer
To build some of the dependencies, you will need CMake. You can install it using your system's package manager or download it from the [CMake website](https://cmake.org/download/).

### install with apt-get (Ubuntu)
On Ubuntu, you can install CMake using the following command:
```bash
sudo apt-get install cmake
```

## Install dependencies
```bash
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```
### If you encounter issues with `egl-probe`, you can install it separately:
```bash
cd ..
git clone https://github.com/adlsdztony/egl_probe.git
cd egl-probe

python setup.py build
python setup.py install
cd ../LIBERO

# and then install the dependencies
pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

## Teleoperation
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




