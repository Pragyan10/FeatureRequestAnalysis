# import libraries
import re
import requests
from bs4 import BeautifulSoup
import json

# change link accordingly
# This is to only grab the issue ids - initial
# url = 'https://github.com/mastodon/mastodon-android/issues?q=is%3Aissue+label%3A%22feature+request%22+is%3Aclosed'

# make sure to enter a number here

numberOfPagesOnRepository = 17
allSets = []
repositoryOwner = "signalapp"
repositoryName = "Signal-Android"
repositoryStatus = "closed"

for pageNumber in range(numberOfPagesOnRepository):

    # handles pagination
    # url = 'https://github.com/mastodon/mastodon-android/issues?page=' + str(pageNumber+1) + '&q=is%3Aissue+label%3A%22feature+request%22+is%3Aopen'
    url = "https://github.com/signalapp/Signal-Android/issues?page=" + str(pageNumber+1) + "&q=label%3Afeature+is%3Aclosed"

    # Fetch the content of the URL
    response = requests.get(url)

    # Parse the content with Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <a> tags in the parsed content
    a_tags = soup.find_all('a')
    # creating a set to record the ids - making it a set so that we prevent duplicates
    idsSet = set()

    # looping through the extracted spans with <a> tags
    for tag in a_tags:
        # get the text values
        href_value = tag.get('href')
        match = re.search(r'/signalapp/Signal-Android/issues/(\d+)', href_value)
        if href_value and match:  # Checks if href contains digits
            digit_part = match.group(1)  # Extracts the digit part
            # print(digit_part)
            idsSet.add(digit_part)

    # check with GitHub to make sure if the number is same
    print("Number of Feature Issues on " + str(pageNumber) + " Page: ", len(idsSet))
    print("IDs on" + str(pageNumber) + " Page: ", idsSet)
    allSets.append(idsSet)


allFeatureRequestObjects = []

for numberEachIDList, eachIDList in enumerate(allSets):
    for numberEachID, eachId in enumerate(eachIDList):
        featureRequestLink = 'https://github.com/signalapp/Signal-Android/issues/' + eachId
        response = requests.get(featureRequestLink)

        soup = BeautifulSoup(response.text, 'html.parser')

        if response.status_code == 200:
            # text_content = soup.get_text(separator=' ', strip=True)

            featureRequestObject = {}

            # adding the feature request
            requestNumber = soup.find("span", class_="f1-light color-fg-muted").text
            # print("Request Number: ", requestNumber)
            featureRequestObject['Request Number'] = requestNumber

            # to pull the title
            title = soup.find("bdi", class_="js-issue-title markdown-title").text
            # print("Title: ", title)
            featureRequestObject['Title'] = title

            # author
            authorUserName = soup.find("a", class_="author text-bold Link--secondary").text
            # print("Author: ", authorUserName)
            featureRequestObject['Author'] = authorUserName

            # time posted
            postedTime = soup.find("relative-time", class_="no-wrap").text
            # print("Posted Time: ", postedTime)
            featureRequestObject['Posted Time'] = postedTime

            # content initial
            td_tag = soup.find('td', class_='d-block comment-body markdown-body js-comment-body').get_text(strip=True)
            # print("Initial Comment: ", td_tag)
            featureRequestObject['Initial Comment'] = td_tag

            # number of comments
            div_content = soup.find('div', class_='flex-auto min-width-0 mb-2').text
            match = re.search(r'(\d+) comments', div_content)
            if match:
                num_comments = int(match.group(1))
                # print(f"Number of comments: {num_comments}")
                featureRequestObject['Number of comments'] = num_comments
            else:
                num_comments = 0
                # print("Comments not found or format is unexpected.")
                featureRequestObject['Number of comments'] = num_comments

            # comments
            comments = soup.find_all('td', class_='d-block comment-body markdown-body js-comment-body')
            # print("Discussion: ")
            discussionComments = []

            for userIndex, comment in enumerate(comments):
                # First, print the text content as you already do
                tempText = ""
                imageTemp = []
                # print("Comment " + str(userIndex+1) + " : ")
                for paragraph in comment.find_all('p'):
                    # print(paragraph.text)
                    tempText = tempText + paragraph.text
                    # print(tempText)

                # Next, find all <img> tags within the current comment
                images = comment.find_all('img')

                # If there are any images, print their source URLs
                if images:
                    # print("Images found in comment index " + str(userIndex) + ":")
                    for imgIndex, img in enumerate(images):
                        # print("Image " + str(imgIndex+1) + " URL: " + img['src'])
                        imageTemp.append(img['src'])
                # print("")

                # print("Loop no: ", userIndex)
                # print(tempText, imageTemp)
                discussionComments.append({'Text: ': tempText, 'Images: ': imageTemp})

            featureRequestObject['All Comments'] = discussionComments

            allFeatureRequestObjects.append(featureRequestObject)

            # throw into a json file
            # with open("/Users/pragyankc1/Desktop/WebScrapedData/Mastodon-Open/" + "page-" + str(numberEachIDList) + " id-" + str(numberEachID) + ".txt", 'a') as file:
            #     file.write(text_content)
            #     file.write("\n---------\n")  # Separate entries for readability

        else:
            # Handle the case when the request was not successful
            print("Error in request number: " + eachId + ": ", response.status_code)


# count the number of feature requests
print(len(allFeatureRequestObjects))
fileName = "signalapp_closed_" + str(len(allFeatureRequestObjects)) + ".json"

with open("/Users/pragyankc1/Desktop/WebScrapedData/SignalAppFeatureRequests/" + fileName, "w") as file:
    json.dump(allFeatureRequestObjects, file)


