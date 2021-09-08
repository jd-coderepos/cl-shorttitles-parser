
# CL-ShortTitles-Parser

### About

**``CL-ShortTitles-Parser``** parses and types phrases from the titles of **C**omputational **L**inguistics scholarly articles written in English for their scientific knowledge elements focused on scholarly contributions. 
Specifically, it looks for phrases representing the following seven semantic types: **_research problem_**, **_solution_**, **_resource_**, **_language_**, **_tool_**, **_method_** and **_dataset_**.
It is developed as part of the [Open Research Knowledge Graph Project](https://www.orkg.org/) at [TIB](https://www.tib.eu/en/).

The code released in this repository is the standalone version of the parser.


### Usage

``CL-ShortTitles-Parser`` features a native Python implementation requiring minimal effort to set up. Please see usage instructions below.

* Requirements

	* Python (3.7 or higher)

Clone this repository locally and run the parser as follows:

`python parse_titles.py <input_titles_file> <output_data_dir>`

where *input_file* is a file with the papers' titles to be parsed with a new title in each line and *output_data_dir* is a user-specified local directory where the parsed output from the program will be written.

