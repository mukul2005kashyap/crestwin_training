# Exceptions and context managers

"""
exceptions are the some kind of errors like run time errors that encounter during the executions of error ...

? Handling the exceptions :
        for handling the eexceptions python uses the try and except 

        try:
            # risky code
        except:
            # handle error


try:
    x = 10 / 0
except:
    print("Error occurred")

? but best paractice is that :
        always catch the specific error like:

        try:
            x = int("abc")
        except ValueError:
            print("Invalid conversion")


! finally Block (Always Runs)
finally block always execute whenever the error occur or not 

! Custom Exceptions
we can also raise our own coustom exceptions through the raise functions 

! Context Managers in Python
    context manager in python is used for resource handling :
        file open/close
        database connection
        lock acquire/release

    EX:-context manager using with :
        with open("text.txt" ,"r") as f :
            data=f.read

        so here context manager automatically close the file when ever the exception encountr or not 

How Context Manager Works Internally
    context manager internaly runs two methods 
            __enter__()
            __exit__()

        """
a = 10
b = 0
print(a / b)

# Output:
ZeroDivisionError

# file handling 
"""
file handling in python:
    create file 
    read file 
    write file 
    update / append file 
    close file properly

python provide open functions for this 

? file_obj = open("filename", "mode")

here all are the modes that used working witb file 

        Mode	Meaning
        "r"	    Read (default)

        "w"    	Write (overwrite)

        "a"	    Append (add at end)

        "x"	    Create new file (error if exists)

        "rb"	Read binary

        "wb"	Write binary

        "r+"	Read + Write

        
? File Pointer (seek & tell)
    tell() functions tells the current functon of the pointer 

        with open("data.txt", "r") as f:
            print(f.tell())   # pointer position

    seek() it is used to move pointer mannualy 
        with open("data.txt", "r") as f:
            f.seek(5)
            print(f.read())


"""
# read the file 

with open("file.txt" , "r") as f:
    content = f.read()

# write the file 

with open("file.txt" , "w") as f:
    f.write("here we write ")

# append

with open("data.txt", "a") as f:
    f.write("New line added\n")

# -------------------------------------------------

# curl jq

"""
curl is a command line tool that can be used for various of the functions like--
    api calling 
    test rest endpoints
    download data or update 
    send headers ,autnantication tokens , json body

there are many of the modes that operats on curl 

    -X method

    -H headers

    -d data

    -F form-data

    -i include headers

    -I only headers

    -v verbose

    -s silent

    -o output file

    -L follow redirect

curl -H "Content-Type: application/json" https://example.com

?  ----JQ

jq stands for json query tool it is a very powerful command line tool that can be used for json -parse filter transform formate

basiclly the data that we got in the json formate not very preeety or in proper formate from our perspective so
    jq formate or filter the output make that data more readable 
    it also get the specific field 

    Basic syntax
        jq 'filter' file.json 

it is mostly used with output of curl 
"""