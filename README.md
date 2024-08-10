# aclut2ets2lut
## A LUT to ETS2 LUT generator/converter
### Requirements
- [Python 3](https://www.python.org/downloads/) (click on the latest version)

  !! When installing Python, make sure to enable "Add Python to environment variables" !!
  ### Before using the script...
You will ask, how do I create a LUT file?

This guide will show how you can create a LUT file.

Extract `wheelcheck_and_lutgenerator.zip` into the/a folder.

Open `WheelCheck.exe`. You will get this dialogue.

![WheelCheck dialogue](https://github.com/Ardaninho/aclut2ets2lut/blob/main/res/wheelcheckdialog.png?raw=true)

Set the `Max Count` value to `100`

![Max Count](https://github.com/Ardaninho/aclut2ets2lut/blob/main/res/maxforce.png?raw=true)

Then to start the test, set `Spring Force` to `Step Log 2 (linear force test)`

!! MAKE SURE YOU CENTER YOUR WHEEL BEFORE DOING THE TEST! !!

![Step Log Test](https://github.com/Ardaninho/aclut2ets2lut/blob/main/res/test%20steplog.png?raw=true)

!! DO NOT TOUCH YOUR WHEEL, DO NOT TOUCH THE APP UNTIL `Spring Force` IS SET BACK TO `Disabled`! !!

[![Video of test](https://img.youtube.com/vi/BpOuInXHJP0/0.jpg)](https://www.youtube.com/watch?v=BpOuInXHJP0)

A `.csv` file should appear in your User Documents (`C:\Users\user\Documents`) with the following name: `log2 <the date when the file is generated>.csv`

Now open `LUTGenerator.exe`. Open the CSV file that is in Documents.

A save dialog will appear that tells you where to save the `.lut` file to. Specify it to the directory where the `aclut2ets2lut.py` is located.

It will save and you will see the output graph. You can quit the program.

Now you have a LUT file! Continue to using the script.
### How to use this script?
#### Convert LUT file
Put your LUT file into the directory.

Open CMD/Terminal and go to the directory (`cd aclut2ets2lut`)

Run: `python aclut2ets2lut.py <lutfile>` where `<lutfile>` is your LUT file.

After converting, it will put a file called `ffb_lut.sii` in the same directory you're in.

You can proceed to installing automatically using the guide underneath, or install manually using [this guide.](https://modding.scssoft.com/wiki/Documentation/Engine/Advanced_input_configuration/Force_feedback_LUT#Usage)
#### Automatic install
Run: `python install_lut.py <game_type> <player_name> <save_type>`, 

where `<game_type>` is which game you play on (ets2/ats), `<player_name>` is the profile name (Ardaninho), `<save_type>` is where your profile saves to (steamcloud/localsave).

If done correctly, it should install to your ETS2/ATS documents folder.

#### Check if the LUT has been loaded correctly
When you load your specific profile with the LUT file, in the main menu, open the Console and click on Custom. Search for `lut`. If you see in the console: `[ffb_lut] Custom force feedback lookup table loaded and configured!`, it has generated and installed correctly. 

You can also see if it loaded by going to your force feedback overall gain settings and seeing a red exclamation mark (see beneath picture).

![Exclamation mark picture](https://github.com/Ardaninho/aclut2ets2lut/blob/main/res/exclmark.png?raw=true)
### Complete
Now your LUT file should be working. Your FFB will feel smoother than normally. Happy trucking!

### Credits
[iRacing for their WheelCheck program](https://www.iracing.com/)

[Anis on Overtake.gg for the LUT generator](https://www.overtake.gg/downloads/lut-generator-for-ac.9740/)

[SCS Software about LUT usage in ETS2/ATS](https://modding.scssoft.com/wiki/Documentation/Engine/Advanced_input_configuration/Force_feedback_LUT#Usage)
