import csv
import pandas as pd


filename = "mails.csv"
newUser = [6118038532665114624,"woosal@protonmail.com"]


class implementCSV:
    def __init__(self, filename):
        self.filename = filename


    # Function that takes the .csv formatted list input
    # as an argument, and appends it as a new row to the .csv file
    def appendCSV(self, filename, newUser):
        with open(filename, 'a+', newline='') as writecsv:
            csvwriter = csv.writer(writecsv)
            csvwriter.writerow(newUser)

    def readCSV(self, filename):
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            next(csvreader)

            for line in csvreader:
                print(line)

    # Checks whether the given user ID exists in the .csv
    # and returns True/False boolean value
    def checkNewUserId(self, filename, newUser):
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            next(csvreader)

            for line in csvreader:
                if str(newUser[0]) == line[0]:
                    return True

        return False

    # Checks whether the given user mail exists in the .csv
    # and returns True/False boolean value
    def checkNewUserMail(self, filename, newUser):
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            next(csvreader)

            for line in csvreader:
                if str(newUser[1]) == line[1]:
                    return True

        return False

    def getIdByMail(self, filename, mail):
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            next(csvreader)

            for line in csvreader:
                if line[1] == mail:
                    return str(line[0])

    #
    def getMailById(self, filename, id):
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)

            next(csvreader)

            for line in csvreader:
                if line[0] == id:
                    return str(line[1])


    # Update the user mail bu +updatemail newMail
    def updateMail(self, filename, id, newMail):
        df = pd.read_csv(filename)
        df.loc[str(id), 'email'] = newMail
        df.to_csv(filename)

csvObj = implementCSV(filename)
csvObj.updateMail(filename, 618038532665114624, "woosal@protonmail.com")
