
for i in range(start, end+1):
    my_url = 'https://ilearn.mq.edu.au/enrol/index.php?id='+str(i)
    browser.open(my_url)
    page = browser.get_current_page()
    print("...scanned page ID" + str(i))

    #Unit Title
    title = page.find("title")
    if title.text == "Error":
        newTitle = "Private"
    elif title:
        newTitle = title.text

    #Unit Name
    name = page.find("h1")
    if name.text == "iLearn":
        newName = "Private"
    elif name:
        newName = name.text

    #Unit Convenor
    try:
        li = page.find('ul', class_='teachers')
        children = li.find_all("a")
        for child in children:
            newConvenor += child.text + ","
    except:
        newConvenor += "Unknown"

    #Can I enrol?
    try:
        enrolStatus = page.find('div', class_='box generalbox py-3').text
        if enrolStatus == "You can not enrol yourself in this unit.":
            newIsOpen = "No"
        else:
            newIsOpen = "Possibly"
    except:
        enrolStatus = "Unknown"

    if enrolStatus == "Unknown":
        newIsOpen = "Unknown"
    count += 1
    f.write(str(i)+","+str(newTitle)+","+str(newName)+","+str(newIsOpen)+","+str(newConvenor)+"\n")

    newConvenor = ""
    newIsOpen = ""

f.write("Done after "+str(count)+" pages scanned.")
f.close()
print("Done after "+str(count)+" pages scanned.")