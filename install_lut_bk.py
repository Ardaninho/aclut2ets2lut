import sys
import os
import binascii
import subprocess

print("aclut2ets2lut.py/install.py - install script for your generated LUT file to the ETS2 documents folder\nProject link: https://github.com/Ardaninho/aclut2ets2lut \nPlease report bugs to our project link!\n")

def ascii_to_hex(name):
    return binascii.hexlify(name.encode()).decode()

def validate_args(args):
    if len(args) != 4:
        print("Usage: python aclut2ets2lut.py <game_type> <player_name> <save_type>")
        print("This script installs the generated ffb_lut.sii file to the game profiles directory (the one located in Documents).\nArgument game_type is which game you plan to install it to.(ets2/ats).\nArgument player_name is to which ETS2/ATS profile you want to install to (put profile name, example Ardaninho)\nArgument save_type is how your game profile is saved (steamcloud/localsave)")
        print("Code made by Ardaninho")
        sys.exit(1)

    game_type, player_name, save_type = args[1:]

    if game_type not in ["ets2", "ats"]:
        print("Error: The game type must be either 'ets2' or 'ats'.")
        sys.exit(1)

    if save_type not in ["steamcloud", "localsave"]:
        print("Error: The save type must be either 'steamcloud' or 'localsave'.")
        sys.exit(1)

    return game_type, player_name, save_type

def get_documents_path():
    return os.path.join(os.environ["USERPROFILE"], "Documents")

def get_game_path(game_type):
    if game_type == "ets2":
        return "Euro Truck Simulator 2"
    elif game_type == "ats":
        return "American Truck Simulator"

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
    game_type, player_name, save_type = validate_args(sys.argv)
    player_hex = ascii_to_hex(player_name)
    whoami_output = subprocess.check_output('whoami').decode().strip().split('\\')[-1]
    documents_path = get_documents_path()
    game_path = get_game_path(game_type)
    save_path = get_save_path(save_type)
    destination_dir = os.path.join(documents_path, game_path, save_path, player_hex)
    destination_file = os.path.join(destination_dir, 'ffb_lut.sii')
    source_file = os.path.join(os.getcwd(), 'ffb_lut.sii')
    copy_lut_file(source_file, destination_file)

if __name__ == "__main__":
    main()