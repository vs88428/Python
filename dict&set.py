# store a dictionary

info = {
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"animal"
}
print(info)

# list of subjects we have, one class room is requires for 1 subject.The number of classroom needed

set = {"python","python","cpp","java","java","web"}

print(len(set))

#enter marks from user of three subjects and store in dictionary

subjects = {}

x=int(input("Enter marks of physics:"))
subjects.update({"physics":x})

x=int(input("Enter marks of chemistry:"))
subjects.update({"chemistry":x})

x=int(input("Enter marks of maths:"))
subjects.update({"maths":x})

print(subjects)