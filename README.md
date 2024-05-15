# Feature Request Analysis

# Analysis of Feature request posted on Mastodon's Github -> https://github.com/mastodon/mastodon-android
## How to get the requests?
- Go to the issues tab
- Filter using the keyword "feature request"


# Files in the respository 
1. **5FeatureRequestsAnalysisDocument.docx** -> First set of 5 feature requests for analysis (April 24th 2024)
2. **Additional5FeatureRequests.docx** -> Second set of 5 feature requests for analysis (May 1st 2024)
3. **ReferencePaperLinks** -> Text file that consists of all the links of the papers that you might need for annotation. 
4. **Directory:** "ExtractedFeatureInJsonFormat" -> This directory consist json files of the feature requests extracted from two open source applications: Mastodon and Signal. Files names are named so as to reflect the application, status (closed or open), and number of requets. The keys that are in the json files are: 
    1. "Request Number"
    2. "Title"
    3. "Author"
    4. "Posted Time"
    5. "Initial Comment"
    6. "Number of Comments"
    7. "All Comments" *(Inside all comments you will see list of dictonary where the first key "Text" is the text discussion and "Images" is the images (if any) added to the discussion by the user. This "All Comments" also includes the initial post)
5. **Directory:** "UsefulPythonCodes" -> This directory consists of python that were used in building this respository and some utility codes.
    1. "Loadingjson.py" -> This file helps you load the json file and read the data. Just replace the file path.
    2. "PullingAllTheIssuesOnlyNumbers.py" -> Check readme inside UsefulPythonCodes directory. 

    


