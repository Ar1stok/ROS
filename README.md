**Gazebo in cannot use Nvidia GPU, falls back to using CPU.**

If you have problem with selected GPU in Gazebo you need to do this steps:

1. Install the proper Nvidia driver for your graphic card on Windows (https://www.nvidia.com/en-us/geforce/drivers)
2. Install WSL2 and then Ubuntu 24.04
3. Install Mesa package:
    ```sudo apt install mesa-utils```
4. Change Mesa profile to use Nvidia graphic card instead of integrated intel GPU:
   ```export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA```
   then check if it correctly identifies your graphic card model
   ```glxinfo -B```
6. Install the Gazebo
7. Make Gazebo use the graphic card during the rendering:
    ```export LIBGL_ALWAYS_SOFTWARE=false```
8. Start the Gazebo simulation, pick and run one of the examples:
    ```gz sim```
