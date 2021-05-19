import csv
import json

# Answers to questions about dataset

# Read in neos.csv
neos = []

with open("data/neos.csv", 'r') as infile:
		reader = csv.DictReader(infile)
		for line in reader:
			neos.append(line)

# Q1. How many NEOs are in the neos.csv data set?
print(len(neos))

# Q2. What is the primary designation of the first Near Earth Object in the neos.csv data set?
# "pdes" is the 4th column

print(neos[0]["pdes"])

# Q3. What is the diameter (in kilometers) of the NEO whose name is "Apollo"?

for obj in neos:
	if obj["name"] == "Apollo":
		
		print("Apollos' diamater: " + obj["diameter"])
		break


# Q4 How many NEOs have IAU names in the data set?

num_names = 0

for obj in neos:
	if obj["name"] != "":
		num_names += 1

print(f"# of NEOs w/ a name: {num_names}")

# Q5. How many NEOs have diameters in the data set?
num_diameters = 0

for obj in neos:
	if obj["diameter"] != "":
		num_diameters += 1

print(f"# of NEOs w/ diameter: {num_diameters}")


# Load JSON file

with open("data/cad.json", 'r') as infile2:
	contents = json.load(infile2)


# Q6. How many close approaches are in the cad.json data set?

print("# of close approaches: " + contents["count"])



# Q7. On January 1st, 2000, how close did the NEO whose primary designation is "2015 CL" pass by Earth?
jan1_entries = [entry for entry in contents["data"] if entry[3][:11] == '2000-Jan-01']
cl_2015 = [entry for entry in jan1_entries if entry[0] == '2015 CL'][0][4]
print(cl_2015)
print("\n")

# Q8. On January 1st, 2000, how fast did the NEO whose primary designation is "2002 PB" pass by Earth?

jan1_entries = [entry for entry in contents["data"] if entry[3][:11] == '2000-Jan-01']
pb_2002 = [entry for entry in jan1_entries if entry[0] == '2002 PB'][0][7]
print(pb_2002)