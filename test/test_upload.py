from seleniumbase import BaseCase

class UploadTest(BaseCase):
    def test_visible_upload(self):
        # open page
        self.open("https://the-internet.herokuapp.com/upload")

        # get file path
        file_path = "./data/rock.jpg"

        # upload file
        self.choose_file("#file-upload", file_path) #The type needs to be 'file'

        #click on upload button
        self.click('#file-submit')

        #assert the file upload text

        self.assert_text(selector="h3", text="File Uploaded!")


    def test_hidden_upload(self):...
    #You need to find the input field where the type is file. Like for instagram upload page -> input._ac69 is
    # the input accepted file types
    """some class hides the input field you can try to see the upload button 
    removing the class. You can go to console
     You can pass this script with seleniumbase
    document.getElementById('upfile_1').class.remove('file_input_hidden')
    """
    #add js code

    remove_hidden_class = "document.getElementById('upfile_1').class.remove('file_input_hidden')"
    # self.add_js_code(remove_hidden_class) #This code will implement the above js code
