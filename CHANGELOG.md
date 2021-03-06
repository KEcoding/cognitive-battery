# Change Log

## [3.2.1](https://github.com/sho-87/cognitive-battery/releases/tag/3.2.1) *(2018-11-15)*

**General**
- Code formatting.
- Added Update UI that checks GitHub for new releases.

**Tasks**
- Added analysis for Eriksen Flanker task.

**Bug Fixes**
- Fixed a bug where leading zeros in subject numbers are missing in aggregated data.

## [3.2.0](https://github.com/sho-87/cognitive-battery/releases/tag/3.2.0) *(2017-09-14)*

**General**
- Added tooltips to the Settings window items to clarify the purpose of each option.
- App-wide values moved to separate module (e.g. URLs).
- Streamlined the setting of default values for task options.
- Added placeholder scripts for aggregating task data.
- Fixed a few typos.

**Tasks**
- Added Eriksen Flanker task.

**Bug Fixes**
- Fixed a bug where settings for new tasks are not read/saved if `settings.ini` already exists.

## [3.1.0](https://github.com/sho-87/cognitive-battery/releases/tag/3.1.0) *(2017-07-06)*

**General**
- Added a menu item to check for latest releases of the battery (redirects to GitHub releases)

**Tasks**
- Added information about each task to [tasks/README.md](tasks/README.md).
- Added options to adjust Raven's trial count and starting position to Settings menu.
- Added option to play an audio beep after each task (default: True)

**Bug Fixes**
- Fixed a bug where the Raven's task was loading the images in an incorrect order.

## [3.0.0](https://github.com/sho-87/cognitive-battery/releases/tag/3.0.0) *(2017-07-03)*

**General**
- Migrated the code base over to Python 3.x. Version 3+ of the battery will be based on Python 3. Python 2 users can still use v2 of the battery, however, it will no longer be maintained.

**Tasks**
- Added option to set the number of blocks for the Sternberg task in the Settings menu.

**Bug Fixes**
- Fixed a bug where duplicate filenames were being checked for (instead of duplicate subject numbers) when starting new sessions.

## [2.0.0](https://github.com/sho-87/cognitive-battery/releases/tag/2.0.0) *(2017-07-03)*

**General**
- Updated `PyQt` requirement to version 5. This is a breaking change as PyQt5.x will be required for current and future versions of the battery. PyQt4 is still supported in version 1.x of the battery.
- The main battery window class has now been moved into its own module.

**User Interface**
- Added a project manager. Data and settings are saved on an individual project basis to their own separate directories.
- Added Settings window sections for manually specifying options for specific tasks. Currently, an option has been added to adjust the block count of the Attention Network Test, but the framework is in place to allow task options to be set by the user for all tasks.

**Bug Fixes**
- Fixed `libpng` warning with task images. The warning should no longer appear with the updated images in the battery.

## [1.1.0](https://github.com/sho-87/cognitive-battery/releases/tag/1.1.0) *(2016-10-09)*

**General**
- Moved a number of text, image and background display functions into their own package (`utils`)

**User Interface**
- Created separate class for UI layout and import into main script
- Changed UI base class to `QTMainWindow`
- Created conversion script for building a Python module from UI file
- Added Menu and Status bar to UI
- Added application icons
- Added global Settings window
- Application now stores (and restores) the size and position of windows

**Tasks**
- All tasks (and their images) moved to separate directory
- Improved integration with pygame
- SART timing has been fine tuned to better match the original publication
- Added the Sternberg Task
- Short version of the ANT has been removed

**Bug Fixes**
- Up/Down buttons now correctly disable if random order is selected
- Pygame window now closes if the main battery UI is closed
- CPU time and memory were being used up needlessly in certain tasks. This has been improved
- Error now correctly displays if no tasks have been chosen
- Pygame windows and backgrounds are now passed around the different tasks correctly
- User input is no longer (pre)registered in digit span during digit display

## [1.0.0](https://github.com/sho-87/cognitive-battery/releases/tag/1.0) *(2015-11-21)*
- Initial release
