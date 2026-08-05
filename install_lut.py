# Copyricht (C) 2026 Ardaninho
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import os
import binascii
import subprocess
print("install_lut.py - install script for your generated LUT file to the ETS2 documents folder\nProject link: https://github.com/Ardaninho/aclut2ets2lut \nPlease report bugs to our project link!\nCopyright (C) 2026 Ardaninho\n")

def ascii_to_hex(name):
    return binascii.hexlify(name.encode()).decode()

def prompt_choice(question, choices):
    choices_str = "/".join(choices)
    while True:
        answer = input(f"{question} ({choices_str}): ").strip().lower()
        if answer in choices:
            return answer
        print(f"Error: please enter one of: {choices_str}")

def prompt_text(question, default=None):
    if default is not None:
        answer = input(f"{question} [{default}]: ").strip().strip('"').strip("'")
        return answer if answer else default
    else:
        while True:
            answer = input(f"{question}: ").strip().strip('"').strip("'")
            if answer:
                return answer
            print("Error: this field cannot be empty.")

def get_save_path(save_type):
    if save_type == "steamcloud":
        return "steam_profiles"
    elif save_type == "localsave":
        return "profiles"

def copy_lut_file(source_file, destination_file):
    try:
        os.makedirs(os.path.dirname(destination_file), exist_ok=True)
        with open(source_file, 'rb') as src, open(destination_file, 'wb') as dst:
            dst.write(src.read())
        print(f"Installing LUT: {destination_file}")
    except Exception as e:
        print(f"Error installing LUT: {e}")
        sys.exit(1)

def main():
    game_root_path = prompt_text(
        "Enter the home directory of your game (e.g. '...\\Euro Truck Simulator 2' or '...\\American Truck Simulator')"
    )
    player_name = prompt_text("Enter your game profile name (e.g. Ardaninho)")
    save_type = prompt_choice("Is your profile saved via Steam Cloud or locally?", ["steamcloud", "localsave"])
    player_hex = ascii_to_hex(player_name)
    save_path = get_save_path(save_type)
    destination_dir = os.path.join(game_root_path, save_path, player_hex)
    destination_file = os.path.join(destination_dir, 'ffb_lut.sii')
    source_file = os.path.join(os.getcwd(), 'ffb_lut.sii')
    print(f"\nSource file:      {source_file}")
    print(f"Destination file: {destination_file}\n")
    confirm = input("Proceed with installation? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Installation cancelled.")
        sys.exit(0)
    copy_lut_file(source_file, destination_file)

if __name__ == "__main__":
    main()