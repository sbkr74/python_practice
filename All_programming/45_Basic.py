# Merge Mails
import os
# current_dir = os.getcwd()
# Get the absolute path of the script
script_path = os.path.abspath(__file__)

# Get the directory containing the script
script_dir = os.path.dirname(script_path)

with open(r"All_programming\names.txt","r",encoding='utf-8') as names_file:
    with open(r'All_programming\body.txt','r',encoding='utf-8') as body_file:
        body = body_file.read()
        for names in names_file:
            mail = "Hi, "+ names + body
            print(mail)
            # with open(current_dir+'/'+names.strip()+".txt",'w',encoding='utf-8') as mail_file:
            # with open("All_programming\\"+names.strip()+".txt",'w',encoding='utf-8') as mail_file:
            with open(script_dir+'\\'+names.strip()+".txt",'w',encoding='utf-8') as mail_file:
                mail_file.write(mail) 