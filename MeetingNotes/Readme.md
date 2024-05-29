# Meeting Notes

## 16th May 2024 
- Make CSV for Manual Evaluation -> Rambod (follow the AnalyzedFeatureRequests/CSV-ForManualEvaluation directory)
   1. CSV file format:
      1. Feature Request Number
      2. Original Rquest
      3. Annotator Name
      4. *Class*: Lexical, Syntactic, Semantic, Pragmatic 
      5. *Class-Subclass*: Lexical-Homonymy, Lexical-Polysemy, Syntactic-Analytics, Syntactic-Attachment, Syntactic-Coordination, Syntactic-Elliptical, Semantic-Scope, Semantic-Referential, Semantic-Coordination, Pragmatic-Referential, Pragmatic-Dectic
         Here the idea of using Class and Sub class is that if we have annotation that fall under a class but we arent sure which sub class it goes too. 
   2. Inside *Class* and *Class-Subclass*:
      1. Dictionary with attributes relating to the annotation -> text, reason, completenes, weight, startIndex, endIndex
- Complete the Annotation tool with subclasses -> Pragyan
- We discuss annotation (50 annotation * 10 each) - 29th May 2024 - Next Meeting Date


## 29th May 2024 
- Task for next week: Look over the annotations. Learn different annotation made by other annotators and make changes if need be.
- File shared on one drive by Pragyan where we all can make changes.
- If you want to make change: mark the text you want to remove from your annotation as "red" - mark the text you added to your existing annotation as "green" -- *** Only make changes for your row ***
- Make notes on your end too. We can use to make heuristics later on and discuss during the meetings. Find something interesting make note of it :)
- Annotation Notes:
  1. If there is some information missing to an annotation and is incomplete but not ambigious then add them as syntactic-eliptical
  2. Make notes for instances if you see same class but different sub class. Maybe draw reasons on why? What do you see. 
  3. If adding any new follow the dictionary format. Attributes inside the dictionary:
     1. text: highlighted text from the original request
     2. reason: why did you annnotate it 
     3. incompleteness: is the annotation incomplete? does adding something to the annotation make it not ambigious
     4. weight: impact of the ambigity for implementation/development/change to the current system
     5. start/end index: tool will handle this
- Next meeting date: 5th June 2024 - We will look other the revised annotation 
     
