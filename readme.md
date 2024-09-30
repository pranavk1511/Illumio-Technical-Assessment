# Flow Log Parser

## Description
This project is a Python script that parses flow log data and maps each row to a tag based on a lookup table. The script processes flow logs and generates two outputs:

1. **Tag Counts**: The count of matches for each tag.
2. **Port/Protocol Combination Counts**: The count of matches for each port/protocol combination.

The flow log data is expected to be in a plain text file, and the lookup table is a CSV file containing mappings between destination ports, protocols, and tags.

## Requirements
1. python 3.xx

## Assumptions

### Field Order in Flow Logs:
- The flow log entries are expected to have the field order as described in the sample data.

### Protocol Mapping:
- Protocol names in the lookup table are one of `tcp`, `udp`, or `icmp` (case-insensitive).
- Protocol numbers are mapped as follows:
  - `tcp`: 6
  - `udp`: 17
  - `icmp`: 1

### Case Insensitivity:
- The matches for protocols and tags are case-insensitive.

### Data Size:
- The flow log file can be up to 10 MB.
- The lookup table can have up to 10,000 mappings.

### Log Structure

```lua
version account-id interface-id srcaddr dstaddr dstport srcport protocol packets bytes start end action log-status
```

## Folder Structure
```lua
flow-log-parser/
├── .gitignore
├── README.md
├── illumio.py
├── data/
│   ├── flow_logs.txt   <- Sample log file
│   └── lookup_table.csv  <- Lookup table
└── output/
    └── results.txt
```
- .gitignore: Specifies intentionally untracked files to ignore.
- README.md: Documentation and usage instructions.
- illumio.py: The main Python script.
- data/: Contains input files (flow_logs.txt, lookup_table.csv).
- output/: Stores the output file (results.txt).

##  Installation

No additional Python packages are required beyond the standard library.

### Clone the Repository (Optional):

You can use the following to clone the Git repository change directory , create and activate the virtual environment 

```bash
git clone <repository_url>
cd flow-log-parser
python -m venv venv
source venv/bin/activate  
```

### Usage

- Place your flow_logs.txt and lookup_table.csv files in the data/ directory.
- Run the script 
```bash
    python illumio.py data/flow_logs.txt data/lookup_table.csv > output/results.txt
```

### Check the Output:
- Open output/results.txt to view the results.

## Testing and Analysis

### Tests Performed

- **Functionality Testing**: The program was tested with various flow logs and lookup tables to ensure accurate parsing and mapping.
- **Edge Case Handling**: Tested with logs containing unexpected values to verify the program's robustness.
- **Performance Testing**: Evaluated with large datasets (up to 10 MB) to ensure efficient processing within the specified data size limits.

### Limitations

- **Log Format Support**: The program only supports the default log format and does not handle custom formats.
- **Version Compatibility**: Only version 2 of the log format is supported.
- **Protocol Mapping**: Supports protocol names `tcp`, `udp`, and `icmp` (case-insensitive), mapping them to their respective protocol numbers.

### Additional Notes

- **Case Insensitivity**: Protocols and tags are matched in a case-insensitive manner.
- **Data Size Constraints**: Designed to handle flow log files up to 10 MB and lookup tables with up to 10,000 mappings.

### Note

Generate random log files using log_generator.py and test the script accordingly 
