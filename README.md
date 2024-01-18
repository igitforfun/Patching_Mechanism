# Patching Mechanism
This is an example of patching mechanism that one can adopt to automatically apply patch on the relevant files by searching and replacing.

# Project Repository Structure
lets take a simple directory structure in this git repository. There is "This/IsThe/Path/Folder_1, Folder_2", representing a simple project workspace.
There is also another folder "Patches" that contained patched folders/files and a python script (i.e. patcher.py)

# Pre-conditions
To make this patching process work,  
1. Have python 3 in your system (Any version should do, I am using 3.11)
2. the directory structure of the patched files underneath the "Patches" folder have to be the same as the actual project workspace.
   * In this example:  
     ./This/IsThe/Path/Folder_1/ToBePatched.txt is the file to be replaced by the patched file. Similarly, in ./Patches/001_Patch/, the same directory structure has to be replicated (e.g. 001_Patch/This/IsThe/Path/Folder_1/ToBePatched.txt)
3. Only the patched files need to be present within the "Patches" folder, the other files that are untouched do not need to exist in the patch directory

# Usage
After checking out this repository, go into the git repo and execute:  
```shell
$ python ./Patches/Patcher.py
```
