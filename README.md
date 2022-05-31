A simple api made using the django rest framework

The api has two endpoints:


---------------------------------
v1/encode/

Used for encoding a desired sentence 
Takes in json data in such format through http request:

{
    "sentence":"i really like pineapples"
}

And returns a encoded string along with the original string with the word ordered alphabetically separated with \n-weird-\n:

"\n-weird-\n",
"i relaly lkie pepeplnias",
"\n-weird-\n",
"i like pineapples really"
---------------------------------

---------------------------------
v1/decode/ 

Used for decodign encoded data
Takes in json data in such format through http request:
{
    "encoded": "i rlelay lkie ppelepains",
    "original_sorted": "i like pineapples really"
}

and returns the decoded sentence in string format:
"i really like pineapples"
---------------------------------


##############################
To deploy:

In command line, run command "pip install -r requirements.txt" to install dependancies

Clone the repository

Navigate to where the repository was cloned via command line

Run the command "python manage.py runserver" in command line

The api should be running via djangos local test server

Navigate to 127.0.0.1:8000/  and utilize the api endpoints as needed
##############################

To run unit tests for the encoding and decoding functions run the file test_fucntions.py from command line in the encode_decode_api directory