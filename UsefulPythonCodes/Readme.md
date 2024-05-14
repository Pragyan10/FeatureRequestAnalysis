# PullingAllTheIssuesOnlyNumbers.py

## This is a web scrapper built for extracting issues from Github - Open Source Project 

## Libraries needed 
- re, requests, bs4 (BeautifulSoup), json
- If you dont have them installed please either create a virtual env or in your terminal with do:
    - pip3 install requests
    - pip3 install BeautifulSoup4

## Some notes:
- Please insure that you have the link to the repository and have set the label to "feature"/"feature requests"


## Code Explanation*
- Python file for the code is named as file: PullingAllTheIssuesOnlyNumbers.py
- The code breaks into two sections:
  - First section is to find the issue ids related to feature requests and also making sure we go through all the pages (not all requests are populated in the same page). (Look section **[Code Detail.1]**) 
  - Once done we go into second section where we use the issue id extracted and pull the issue thread and collect all the required information (Look section **[Code Detail.2]**) 
 
### Code Detail.1
- Using beautiful soup me enumurate all the <a> tags from the repository and extract all the ids associated with feature requests

### Code Detail.2
- Once we have collected all the ids, we fetch the threads using the same ids
- Once we load the url with the ids, using beautiful soup we collect fields including:
      - request id
      - feature request title
      - author
      - posted time
      - Initial Comment
      - Number of comments in the thread
      - Commments (Initial comment plus any other comments that were made in the thread
          - For Comments: it contains two data: text and images (images if there are any images attached to the discussion)
- All the data is collected with using "inspect" to find the exact tags and the class names for easier identification. See code for more details 
 

## Data format:
- The data is formated in json format meaning you will need to work it as a dictionary
- Data format:
      {
          "Request Number": [str],
          "Title": [str],
          "Author": [str],
          "Posted Time": [str],
          "Initial Comment": [str],
          "Number of comments": [int],
          "All Comments": [list] -> elements are dictionaries with "text" where the comment is mentioned and "Images" where if any images is attached to the comment a link is populated
      }
- There are 467 feature requests (as of 10th April 2024) -> Collected from open source application incliding: mastodon[1] and signal[2].  



* Some part of the code is explained within the code itself too

[1] https://github.com/mastodon/mastodon-android
[2] https://github.com/signalapp/Signal-Android
