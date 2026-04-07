# Capability Engine – Usage Guide

The Capability Engine is a standalone executable that converts raw measurement output files into structured CSV data suitable for statistical analysis and import into tools such as Minitab.

It automatically:

1. Reads a single raw measurement file from the \Input folder
2. Translates and normalizes irregular machine output
3. Cleans and organizes measurement cycles
4. Exports multiple CSV formats for different analysis needs

No Python or additional software is required to run the program.
_
## Folder Structure

The program expects the following directory layout:

CapabilityEngine/
│   CapabilityEngine.exe
│
├── Input/
│       (place raw measurement file here)
│
└── Output/
    └── TranslatorOutput/
        (CSV files will be generated here)
_
## How to Use
_
### Step 1 – Place Input File

Copy the raw machine output file into:

CapabilityEngine\Input\

Supported format: comma-delimited measurement logs.

_
### Step 2 – Run the Engine

Double-click:

CapabilityEngine.exe

No configuration is required. The program will automatically detect and process the file located in the Input directory.

_
### Step 3 – Retrieve Processed Data

After execution, processed files will appear in:

CapabilityEngine\Output\TranslatorOutput\

Generated files include:

| File                    | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| TranslatedData_raw.csv  | Direct translation of machine output                             |
| TranslatedData.csv      | Cleaned and normalized dataset                                   |
| TranslatedData_wide.csv | Pivoted format with features as columns for statistical software |

_
## Data Processing Behavior

The engine:

* Detects feature labels automatically
* Associates multiple values with a single feature when present
* Preserves cycle structure for capability studies
* Replaces missing primary values with `N/A` while removing invalid secondary blanks

This ensures consistent results across:

* Simple measurement files
* Complex multi-axis inspection outputs
* Partially corrupted or irregular logs

_
## Important Usage Notes

### Do Not Modify These Folders

The following folders are required for correct operation:

\Input
\Output

Renaming or moving these folders will cause the engine to fail.

_
### Input File Rules

* Files must remain comma-delimited
* Do not open and re-save files in Excel before processing, as Excel may alter formatting or remove important data

_
### Re-running the Engine

The program may be run multiple times. Existing CSV outputs will be overwritten with the latest processed data.

If you need to keep previous results, rename or move the output files before running the engine again.

_
## Troubleshooting

### No output files generated

Check:

* That an input file exists in the Input folder
* That the file is not open in another program

### Program closes immediately

This usually indicates:

* No valid measurement data was detected
* Or the Input folder is empty

_
## Security and Safety

The executable:

* Reads only from the Input directory
* Writes only to the Output directory
* Does not access the network or external drives
* Does not modify or delete source measurement files

This makes it safe to run in shared or controlled environments.

_
Capability Engine v1.3.2
Initial production release for internal capability analysis workflow.

Author: Connor H. Stoll
