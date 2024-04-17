make sure to create an environment 
    and download the necessary packages using the

    
        pip install -r requirements.txt


If you are unable to run the env in windows powershell, run the command


    Set-ExecutionPolicy Unrestricted -Scope Process


If you get this error 

    Error "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape" [duplicate]
    
convert the string of the path to a raw string by adding r"" in front of the string
        