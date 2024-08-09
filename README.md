# aclut2ets2lut
## A LUT to ETS2 LUT generator/converter
### Requirements
- [Python 3](https://www.python.org/downloads/)
### How to use this script?
#### Convert LUT file
Put your LUT file into the directory.
Open CMD/Terminal and go to the directory (`cd aclut2ets2lut`)
Run: `python aclut2ets2lut.py <lutfile>` where `<lutfile>` is your LUT file.
After converting, it will put a file called `ffb_lut.sii` in the same directory you're in.
You can proceed to installing automatically using the guide underneath, or install manually using [this guide.](https://modding.scssoft.com/wiki/Documentation/Engine/Advanced_input_configuration/Force_feedback_LUT#Usage)
#### Automatic install
Run: `python install_lut.py <game_type> <player_name> <save_type>` where `<game_type>` is which game you play on (ets2/ats), `<player_name>` is the profile name (Ardaninho), `<save_type>` is where your profile saves to (steamcloud/localsave).
If done correctly, it should install to your ETS2/ATS documents folder.
#### Check if the LUT has been loaded correctly
When you load your specific profile with the LUT file, in the main menu, open the Console and click on Custom. Search for `lut`. If you see in the console: `[ffb_lut] Custom force feedback lookup table loaded and configured!`, it has generated and installed correctly. You can also see if it loaded by going to your force feedback overall gain settings and seeing a red exclamation mark (see beneath picture).
![Exclamation mark picture](https://github.com/Ardaninho/aclut2ets2lut/blob/main/exclmark.png?raw=true)
### Complete
Now your LUT file should be working. Your FFB will feel smoother than normally. Happy trucking!
