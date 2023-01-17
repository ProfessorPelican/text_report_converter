# text_report_converter

## Overall Purpose:
Reports that are intended to be printed can often be exported to text, but with the text in the same format as the printed report.  This means the data is not tabular, and includes field names, page headers, page footers, etc.  This converts these exported report text files into a Pandas dataframe.

## Useful Code Aspects:
<ul>
   <li>Selected fields are extracted from the report based on the location of strings that designate the row they are on and the location on that row.</li>
   <li>Can include header row information as fields as well as detail row information (the header fields repeat for each related detail row).</li>
   <li>All fields are returned as strings, which is what they are in the source text file.  These can then be converted as needed.</li>
</ul>

## Personal Note:
I created this a while ago, before I had a lot of experience with Pandas.  If I was to refactor this, I would consider whether I could replace some or all of these loops with a Pandas vectorized function.
