# Meeting Notes

## 16th May 2024 
- Make CSV for Manual Evaluation -> Rambod (follow the AnalyzedFeatureRequests/CSV-ForManualEvaluation directory)
   1. CSV file format:
      1. Feature Request Number
      2. Original Rquest
      3. Annotator Name
      4. *Class*
      5. *Class-Subclass*
   2. Inside *Class* and *Class-Subclass*:
      1. Dictionary with attributes relating to the annotation -> text, reason, completenes, weight, startIndex, endIndex
- Complete the Annotation tool with subclasses -> Pragyan
- We discuss annotation (50 annotation * 10 each) - 29th May 2024 - Next Meeting Date


## 29th May 2024 
- Task for next week: Look over the annotations. Learn different annotation made by other annotators and make changes if need be.
- File shared on one drive by Pragyan where we all can make changes.
- If you want to make change: mark the text you want to remove from your annotation as "red" - mark the text you added to your existing annotation as "green" -- *** Only make changes for your row ***
   
- Annotation Notes:
  1. If there is some information missing to an annotation and is incomplete but not ambigious then add them as syntactic-eliptical
  2. Attributes inside the dictionary:
     1. incompleteness: is the annotation incomplete? does adding something to the annotation make it not ambigious
     2. weight: impact of the ambigity for implementation/development/change to the current system
     3. start/end index: tool will handle this 
