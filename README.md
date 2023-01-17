# text_report_converter

## Overall Purpose:
Often, "canned" reports that are intended to be printed can be exported to text, but the text is in the same format as the printed report.  This means the data is not tabular, and includes field headings, page headers and footers, etc.  This converts these into a Pandas dataframe, which can then be analyzed or exported to another format such as Excel as desired.

## Useful Code Aspects:
<ul>
   <li>Selected fields are extracted from the report based on the location of strings that designate the row they are on and the location on that row</li>
   <li>Can include header row information as fields as well as detail row information</li>
   <li>All fields are returned as strings, which is what they are on the source text file.  These can then be converted as needed.</li>
</ul>
