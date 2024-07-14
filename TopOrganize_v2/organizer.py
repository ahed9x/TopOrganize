
def organizer():
    # advance
    import os
    import shutil
    from random import randint

    login= os.getlogin()

    restore= f"C:\\Users\\{login}\\Desktop\\restore"

    images= f"C:\\Users\\{login}\\Desktop\\images"

    images_jpg= f"C:\\Users\\{login}\\Desktop\\images\\jpg"
    jpg=".jpg"

    images_png= f"C:\\Users\\{login}\\Desktop\\images\\png"
    png=".png"

    images_gif= f"C:\\Users\\{login}\\Desktop\\images\\gifs"
    gif= ".gif"

    images_xcf= f"C:\\Users\\{login}\\Desktop\\images\\xcf"
    xcf=".xcf"

    docs= f"C:\\Users\\{login}\\Desktop\\docs"

    docs_word= f"C:\\Users\\{login}\\Desktop\\docs\\word"
    word= ".docx"
    word2= ".doc"

    docs_pdf= f"C:\\Users\\{login}\\Desktop\\docs\\pdf"
    pdf=".pdf"

    docs_text= f"C:\\Users\\{login}\\Desktop\\docs\\text"
    text=".txt"

    docs_excel= f"C:\\Users\\{login}\\Desktop\\docs\\excel"
    excel= ".xls"
    excel2= ".xlsx"

    docs_pptx= f"C:\\Users\\{login}\\Desktop\\docs\\pptx"
    pptx= ".pptx"
    pptx2=".ppt"

    

    hobb= f"C:\\Users\\{login}\\Desktop\\hobbies"


    hobb_prog= f"C:\\Users\\{login}\\Desktop\\hobbies\\programmer"
    prog= [".aspx", 
    ".axd", 
    ".asx", 
    ".asmx", 
    ".ashx", 
    ".CSS", 
    ".css", 
    ".Coldfusion", 
    ".cfm", 
    ".Erlang", 
    ".yaws", 
    ".Flash", 
    ".swf", 
    ".HTML", 
    ".html", 
    ".htm", 
    ".xhtml", 
    ".jhtml", 
    ".Java", 
    ".jsp", 
    ".jspx", 
    ".wss", 
    ".do", 
    ".action", 
    ".JavaScript", 
    ".js", 
    ".Perl", 
    ".pl", 
    ".PHP", 
    ".php", 
    ".php4", 
    ".php3", 
    ".phtml", 
    ".Python", 
    ".py", 
    ".ipynb"
    ".Ruby", 
    ".rb", 
    ".rhtml", 
    ".SSI", 
    ".shtml", 
    ".TS", 
    ".XML", 
    ".rss", 
    ".Other", 
    ".cgi", 
    ".dll"]

    hobb_3d= f"C:\\Users\\{login}\\Desktop\\hobbies\\3d"
    print_3d=[".stl", ".obj", ".3mf", ".gcode", ".gco"]


    archives= f"C:\\Users\\{login}\\Desktop\\archives"

    archives_rar= f"C:\\Users\\{login}\\Desktop\\archives\\rar"
    rar=".rar"

    archives_zip= f"C:\\Users\\{login}\\Desktop\\archives\\zip"
    zip=".zip"

    folders= f"C:\\Users\\{login}\\Desktop\\folders"

    video_audio= f"C:\\Users\\{login}\\Desktop\\video-audio"

    video_audio_mp3= f"C:\\Users\\{login}\\Desktop\\video-audio\\mp3"
    mp3=".mp3"

    video_audio_wav= f"C:\\Users\\{login}\\Desktop\\video-audio\\wav"
    wav=".wav"

    video_audio_mp4= f"C:\\Users\\{login}\\Desktop\\video-audio\\mp4"
    mp4=".mp4"

    other = f"C:\\Users\\{login}\\Desktop\\other"

#__________________________________________________________________________________________________________________

    try:
        os.makedirs(restore)
    except:
        pass

    try:
        os.makedirs(images)
    except:
        pass 

    try:
        os.makedirs(images_jpg)
    except:
        pass 

    try:
        os.makedirs(images_png)
    except:
        pass 

    try:
        os.makedirs(images_gif)
    except: 
        pass 

    try:
        os.makedirs(images_xcf)
    except:
        pass 

    try:
        os.makedirs(docs)
    except:
        pass 

    try:
        os.makedirs(docs_word)
    except: 
        pass

    try:
        os.makedirs(docs_text)
    except: 
        pass 

    try:
        os.makedirs(docs_pdf)
    except: 
        pass

    try:
        os.makedirs(docs_excel)
    except: 
        pass

    try:
        os.makedirs(docs_pptx)
    except: 
        pass 

    try:
        os.makedirs(archives)
    except: 
        pass

    try:
        os.makedirs(archives_rar)
    except: 
        pass 

    try:
        os.makedirs(archives_zip)
    except: 
        pass 

    try:
        os.makedirs(folders)
    except:
        pass

    try:
        os.makedirs(video_audio)
    except:
        pass 

    try:
        os.makedirs(video_audio_mp3)
    except:
        pass 

    try:
        os.makedirs(video_audio_mp4)
    except:
        pass

    try:
        os.makedirs(video_audio_wav)
    except:
        pass 

    try:
        os.makedirs(hobb_prog)
    except:
        pass 

    try:
        os.makedirs(hobb_3d)
    except:
        pass 

    try:
        os.makedirs(other)
    except:
        pass 

#_____________________________________________________________________________________________________________________________

    for file in os.listdir(f"C:\\Users\\{login}\\Desktop"):
        print(file)

        if file.endswith(png):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, images_png)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, images_png)
                shutil.move(new_file_path, restore)
            

        elif file.endswith(jpg):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, images_jpg)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, images_jpg)
                shutil.move(new_file_path, restore)
            
        
        elif file.endswith(gif):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, images_gif)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, images_gif)
                shutil.move(new_file_path, restore)
            
        
        elif file.endswith(word) or file.endswith(word2):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, docs_word)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, docs_word)
                shutil.move(new_file_path, restore)
            

        elif file.endswith(text):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, docs_text)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, docs_text)
                shutil.move(new_file_path, restore)
            

        elif file.endswith(pdf):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, docs_pdf)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, docs_pdf)
                shutil.move(new_file_path, restore)
            
        
        elif file.endswith(excel) or file.endswith(excel2):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, docs_excel)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, docs_excel)
                shutil.move(new_file_path, restore)
            


        elif file.endswith(pptx) or file.endswith(pptx2):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, docs_pptx)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, docs_pptx)
                shutil.move(new_file_path, restore)
            

        elif file.endswith(rar):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, archives_rar)
                shutil.move(f_path, restore)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, archives_rar)
                shutil.move(new_file_path, restore)
            

        elif file.endswith(zip):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, archives_zip)
                shutil.move(f_path, restore)
            except:    
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, archives_zip)
                shutil.move(new_file_path, restore)                
            
        
        elif file.endswith(mp4):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, video_audio_mp4)
                shutil.move(f_path, restore)
            except:    
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, video_audio_mp4)
                shutil.move(new_file_path, restore)                
            

        elif file.endswith(mp3):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, video_audio_mp3)
                shutil.move(f_path, restore)
            except:    
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, video_audio_mp3)
                shutil.move(new_file_path, restore)                
            

        elif file.endswith(wav):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, video_audio_wav)
                shutil.move(f_path, restore)
            except:    
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, video_audio_wav)
                shutil.move(new_file_path, restore)                
            

        elif file.endswith(xcf):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, images_xcf)
                shutil.move(f_path, restore)
            except:    
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, images_xcf)
                shutil.move(new_file_path, restore)                
        elif 1 ==1 :
            for ex in print_3d:
                if file.endswith(ex):
                    f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
                    try:
                        shutil.copy2(f_path, hobb_3d)
                        shutil.move(f_path, restore)
                    except:    
                        num = randint(1000000, 999999999)
        
                        new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                        os.rename(f_path, new_file_path)
                        shutil.copy2(new_file_path, hobb_3d)
                        shutil.move(new_file_path, restore)   

        elif 1 == 1:
            for ex in prog:
                if file.endswith(ex):
                    f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
                    try:
                        shutil.copy2(f_path, hobb_prog)
                        shutil.move(f_path, restore)
                    except:    
                        num = randint(1000000, 999999999)
                        f_path = f"{num}_{file}"
                        new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                        os.rename(f_path, new_file_path)
                        shutil.copy2(new_file_path, hobb_prog)
                        shutil.move(new_file_path, restore)         
                

        elif file.endswith(".ipynb"):
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, hobb_prog)
                shutil.move(f_path, restore)
            except:    
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, hobb_prog)
                shutil.move(new_file_path, restore) 


        elif file.count(".") == 0 and not file == "docs" and not file =="images" and not file == "archives" and not file == "folders" and not file == "organizer" and not file == "video-audio" and not file == "restore" and not file == "hobbies" and not file == "other" and not file == " ":
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.move(f_path, folders)
            except:
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, folders)
                shutil.move(new_file_path, restore)

        
        elif file.count(".") > 0:
            print("A")
            f_path= f"C:\\Users\\{login}\\Desktop\\{file}"
            try:
                shutil.copy2(f_path, other)
                shutil.move(f_path, restore)
            except:    
                num = randint(1000000, 999999999)

                new_file_path = os.path.join(os.path.dirname(f_path), f"{num}_{file}")
                os.rename(f_path, new_file_path)
                shutil.copy2(new_file_path, other)
                shutil.move(new_file_path, restore)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pygame
from sys import exit


pygame.init()
pygame.font.init()
scr= pygame.display.set_mode((600, 400))
pygame.display.set_caption("TopOrganize")
icon= pygame.image.load("logo/icon.ico").convert_alpha()
pygame.display.set_icon(icon)
clock= pygame.time.Clock()
font = pygame.font.Font("font/COMPUTERRobot.ttf", 40)
font2 = pygame.font.Font("font/COMPUTERRobot.ttf", 30)
text=font.render('organize', False, (64, 64, 64))
text_rect= text.get_rect(center=(300, 194))
text2=font2.render('organize', False, (64, 64, 64))
text2_rect= text.get_rect(center=(315, 200))
    
while True:
    mouse=pygame.mouse.get_pos()
    mouse_pressed= pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if 300 > mouse[1] > 100 and 400 > mouse[0] > 300 :
        scr.fill("#F5E7E3")
        pygame.draw.circle(scr, "#FF0400", (300, 200), 102, 0, True, True, True, True)
        pygame.draw.circle(scr, "#BF0F00", (300, 200), 92, 0, True, True, True, True)
        pygame.draw.circle(scr, "#A60C00", (300, 200), 82, 0, True, True, True, True)
        pygame.draw.circle(scr, "#900800", (300, 200), 72, 0, True, True, True, True)
        scr.blit(text, text_rect)

        if mouse_pressed[0]:
            scr.fill("#F5E7E3")
            pygame.draw.circle(scr, "#FF0400", (300, 200), 90, 0, True, True, True, True)
            pygame.draw.circle(scr, "#BF0F00", (300, 200), 80, 0, True, True, True, True)
            pygame.draw.circle(scr, "#A60C00", (300, 200), 70, 0, True, True, True, True)
            pygame.draw.circle(scr, "#900800", (300, 200), 60, 0, True, True, True, True)
            scr.blit(text2, text2_rect)

            organizer()
         
    else:
        scr.fill("#F5E7E3")
        pygame.draw.circle(scr, "#FF0400", (300, 200), 100, 0, True, True, True, True)
        pygame.draw.circle(scr, "#BF0F00", (300, 200), 90, 0, True, True, True, True)
        pygame.draw.circle(scr, "#A60C00", (300, 200), 80, 0, True, True, True, True)
        pygame.draw.circle(scr, "#900800", (300, 200), 70, 0, True, True, True, True)
        scr.blit(text, text_rect)


    pygame.display.update()
    clock.tick(60)
        
