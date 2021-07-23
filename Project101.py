import dropbox

class UploadData:
    def __init__(self, accesstoken):
        self.accesstoken = accesstoken
    def UploadFiles(self, source, destination):
        dbx = dropbox.Dropbox(self.accesstoken)
        file = open(source, "rb")
        dbx.files_upload(file.read(), destination)

def main():
    accesstoken = "8SseBmFks7UAAAAAAAAAAcLQrY0RRiErB5Uh9k4x0AD4RFrmYX6KMhNuP4XCd4oD"
    transferData = UploadData(accesstoken)
    source = "C:/Users/Raghav/Desktop/Madhav/New folder (9)/madhav/Python1/py/File1.py"
    destination = "/Project101/Project101.py"
    transferData.UploadFiles(source, destination)
    print("File Has Been Moved")
    
main()
