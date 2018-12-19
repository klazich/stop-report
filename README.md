# STOP/MI reports CLI

A "simple" command line tool I use to build the STOP report at work. I run a
status report on Axapta and save it as a text file (tab separators) locally at
my work station. The tool does a few things:

- Cleans the Axapta data.
  - The title and headers are repeated every 71 lines and need to be removed.
  - Removes items with 0 inventory
  - Other small fixes
- An overly complicated Directories class that takes care of file paths
  and directories.
- An Excel workbook is opened or created.
  - A new Excel workbook is created every week (saved as week #) and each daily
    report is a worksheet (named for date).
- The Axapta data is sorted and applied to a new worksheet.
- Styling and formating is applied so every report follows the same design.
- The workbook is saved locally as well as to a shared server and my work
  OneDrive.

---

I wrote it over a year ago and of course didn't add much commenting so I'm not
entirely sure how it works anymore and I don't feel like going back through it
all again yet.
