# BBEileenSaveFix

Sometimes, pressing buttons is a little too easy. During my playthrough of Bloodborne, I mistakenly attacked a character named [Eileen the Crow](https://bloodborne.wiki.fextralife.com/Eileen+the+Crow). In the section of the game that I was in, they can be found just outside of the Cathedral Ward lamp. If you mistakenly attack them, they will become permanently aggressive towards you. I decided to try to see whether I could edit the save to revert his aggression. The result is BBEileenSaveFix which has support for this one fix. To my current knowledge, no other tool exists to make this change.

Please note, this tool likely will only work under a very specific scenario (the one that was relevant to my sava). The Eileen the Crow patch will turn him non-aggressive ONLY IF you attacked him at the cathedral ward (Location 2). This also assumes you interacted with him at Location 1 (Central Yharnam). See the [wiki page](https://bloodborne.wiki.fextralife.com/Eileen+the+Crow) for information on the locations.

## Methodology

The method I used to create the hex patch (seen in the source code as `EILEEN_THE_CROW`) is relatively rudimentary. I obtained a save file from [here](https://www.nexusmods.com/bloodborne/mods/219), using the one for Blood Starved Beast.  Then, I progressed to a point where Eileen the Crow can be found in the location where I hit them (Location 2). This was very quick using cheats. I then made a copy of that save and extracted the array of bytes (AOB) relating to the "flags" section of the save. Then I attacked them, immediately exited, and extracted the AOB. I created a Python script named `hexdiffcheck.py` that I used to compare the differences between the before and after save AOBs. Then, extracting the AOB from my personal save confirmed that all of the same offsets were changed to the same values from the after AOB, which would indicate the changed hex values relate to his aggression. Using that information, I was able to create the patch in my Python script and fix my save file.

## Usage

Simply clone/download the repository to your computer and run the `bbeileensavefix.py` script. The prompts will ask you for your save file (likely named userdata0000). This file should be stored in the same location as the Python script. This save data MUST be decrypted before it can be used in this tool. Saves from [ShadPS4](https://github.com/shadps4-emu/shadPS4) can be used (should be decrypted already) or you can use a hacked PS4 with [Apollo Save Tool](https://github.com/bucanero/apollo-ps4). Other methods of decrypting saves can be found [here](https://github.com/Noxde/Bloodborne-save-editor/wiki/How-to-decrypt-a-save).

## Disclaimer

This Python script is provided AS IS and has NO plans to undergo any future development. I am not responsible for any corrupted save files, glitchy behaviour, or any other damage caused to your save as a result of your use of this tool. While I have tested the tool on my personal save, and now finished the game with no issues, I cannot guarantee that there will be none.

## License

This project is licensed under the [GPL-3.0 license](https://github.com/Jacky161/BBSaveFix/blob/main/LICENSE). Some functions are based upon rust code found in the [Bloodborne-save-editor by Noxde](https://github.com/Noxde/Bloodborne-save-editor) which is licensed under GPL-3.0.
