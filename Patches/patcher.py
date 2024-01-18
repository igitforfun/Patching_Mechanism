import glob, os
import shutil
import subprocess
import argparse

def apply_patch():
    for patched_dir in sorted(glob.glob(os.path.join(patches_path, "*"), recursive = False)):
        if os.path.isdir(patched_dir): #Do not parse this python script
            for path, dirs, files in os.walk(patched_dir):
                if files:
                    found = 0
                    patched_element_dir_path = path #Get the directory that contains the patched files
                    relative_element_dir_path = os.path.relpath(patched_element_dir_path, patched_dir) #relative path to the patched files from root
                    target_element_path = os.path.join(root_path, relative_element_dir_path) #create a path name to be search in the main repo
                    for target_path, dirs, files in os.walk(root_path):
                        if target_path == target_element_path:
                            found += 1
                            for patched_file in os.listdir(patched_element_dir_path):
                                print(f"Applying patch on {patched_file}...")
                                try:
                                    if os.path.isfile(os.path.join(patched_element_dir_path, patched_file)):
                                        shutil.copyfile(os.path.join(patched_element_dir_path, patched_file), os.path.join(target_path, patched_file))
                                        print('    > '+ os.path.join(target_path, patched_file) + ' patched')
                                except:
                                    print('   > ERROR ' + os.path.join(patched_element_dir_path, patched_file)  + ' not patched', flush=True)
                    if found == 0:
                        print(f"WARNING: {target_element_path} not found, files under {patched_element_dir_path} not patched")

if __name__ == '__main__':

    root_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..") #Get 1 DIR before DIR path of this python script
    patches_path = os.path.dirname(os.path.abspath(__file__))

    print("Running " + os.path.basename(__file__) + "...")
    apply_patch()
