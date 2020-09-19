import os
with open(os.path.join("C:\\Users\\Lotachukwu\\Google Drive\\Network Programming",'Procfile'), "w") as file1:
    toFile = 'web: sh setup.sh && streamlit run cov.py'
    
    file1.write(toFile)