# Empress ZOIA patchstorage categorizer

Now you can have all allowed patches ready to use on ZOIA faster!

ZOIA has a lot of good patches on patchstorage, but that's too difficult to load them by one using the librarian tool or
manually. There's 4gb flash card in it, but all allowed 916 patches for now use only 40mb of its space (for late 2021).
This script get all the loaded patches by the librarian tool and categorize them using tags or categories. It creates a
lot of folders with patches categories/tags, sort them by likes/downloads, crop and rename them by 64 patches in each for coping
them to the ZOIA SD card. Note that patches can have many categories/tags and are duplicated in each folder, so they can
take up more space.

It is quite primitive and should works only on Mac OS X with ZOIA Librarian installed, but if there is a need from
others, it can get development.

## How to use it

1. Install the [ZOIA Librarian app](https://github.com/meanmedianmoge/zoia_lib) and download all interested patches in it
2. Open the script and set the settings for export, at least `group_by_field` and `sort_by_field`
3. Run it!
4. Copy the created folders to ZOIA SD Card
5. Load some folder from [ZOIA Config tab (Patches from SD card)](https://youtu.be/lJmJuKlYQxw?t=212)
6. Enjoy!
