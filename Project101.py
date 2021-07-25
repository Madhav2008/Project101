import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token =  access_token

    def upload_file(self, filefrom, fileto):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(filefrom):

            for filename in files:
                localpath = os.path.join(root, filename)

                relative_path = os.path.relpath(localpath, filefrom)
                dropbox_path = os.path.join(fileto, relative_path)
                with open(localpath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = '8SseBmFks7UAAAAAAAAAAcLQrY0RRiErB5Uh9k4x0AD4RFrmYX6KMhNuP4XCd4oD'
    transferData = TransferData(access_token)

    filefrom = str(input("Enter The Folder Path :- "))
    fileto = input("Enter The Path To Upload To Dropbox :- ")

    transferData.upload_file(filefrom,fileto)
    print("File Has Been Moved")

main()
