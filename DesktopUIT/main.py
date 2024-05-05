import pygame, sys
import time
import random
from button import Button

toc_do_ran = 20
snake_head=pygame.image.load("assets/meome.png")
snake_head= pygame.transform.scale(snake_head,(25,25))
snake_body= pygame.image.load("assets/meocon1.png")
snake_body= pygame.transform.scale(snake_body,(20,20))
snake_bodys=[]
snake_bodys.append(snake_body)
snake_body= pygame.image.load("assets/meocon2.png")
snake_body= pygame.transform.scale(snake_body,(20,20))
snake_bodys.append(snake_body)
snake_body=pygame.image.load("assets/meocon3.png")
snake_body= pygame.transform.scale(snake_body,(20,20))
snake_bodys.append(snake_body)
BG_Game = pygame.image.load("assets/greenhill.jpg")
snake_theme= [snake_head,snake_bodys,BG_Game]
mau_den = pygame.Color(0, 0, 0)
mau_trang = pygame.Color(255, 255, 255)
mau_do = pygame.Color(255, 0, 0)
mau_xanh_la = pygame.Color(0, 255, 0)
mau_xanh_duong = pygame.Color(0, 0, 255)
    
pygame.init()

SCREEN = pygame.display.set_mode((1080, 640))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/1.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play(toc_do_ran,Snake_theme):
    

    # Kích thước khối của rắn và mồi
    kich_thuoc_khoi = 20  # Giá trị cũ là 10

    # Kích thước cửa sổ
    kich_thuoc_x = 1080 
    kich_thuoc_y = 640

    # Khởi tạo pygame
    pygame.init()

    # Khởi tạo cửa sổ game
    pygame.display.set_caption('Rắn săn mồi')
    cua_so_game = pygame.display.set_mode((kich_thuoc_x, kich_thuoc_y))
    fps = pygame.time.Clock()
    
    
    # BG = pygame.image.load("assets/1.png")
    # Định nghĩa vị trí mặc định của rắn
    vi_tri_ran = [200, 100]

    # Định nghĩa 4 khối đầu tiên của thân rắn
    thân_ran = [[Snake_theme[0],vi_tri_ran]]


    vi_tri_moi = [random.randrange(0, kich_thuoc_x//kich_thuoc_khoi) * kich_thuoc_khoi,
                random.randrange(0, kich_thuoc_y//kich_thuoc_khoi) * kich_thuoc_khoi]
    loai_moi= random.randint(0,2)

    # Vẽ rắn và mồi
    for vi_tri in thân_ran:
        cua_so_game.blit(vi_tri[0], (vi_tri[1][0],vi_tri[1][1]))
    cua_so_game.blit(Snake_theme[1][loai_moi],(vi_tri_moi[0],vi_tri_moi[1]))        

    Tao_moi = True

    # Đặt hướng mặc định của rắn về phía
    # bên phải
    huong = 'PHAI'
    thay_doi_huong = huong

    # Điểm số ban đầu
    diem_so = 0

    # Hàm hiển thị điểm số
    def hien_thi_diem_so(lua_chon, mau, font, kich_co):
    
        # Tạo đối tượng font score_font
        font_diem_so = pygame.font.SysFont(font, kich_co)
        
        # Tạo đối tượng bề mặt hiển thị
        # score_surface
        be_mat_diem_so = font_diem_so.render('SCORE: ' + str(diem_so), True, mau)
        
        # Tạo đối tượng hình chữ nhật cho
        # đối tượng bề mặt văn bản
        hinh_chu_nhat_diem_so = be_mat_diem_so.get_rect()
        
        # Hiển thị văn bản
        cua_so_game.blit(be_mat_diem_so, hinh_chu_nhat_diem_so)

    # Hàm kết thúc game
    def ket_thuc_game(lua_chon, mau, font, kich_co):
    
        # Tạo đối tượng font my_font
        font_cua_toi = pygame.font.SysFont(font, kich_co)
        
        # Tạo một bề mặt văn bản trên đó văn bản
        # sẽ được vẽ
        kich_thuoc_font = 50  # Adjust this value to change the font size
        font_cua_toi = pygame.font.Font(None, kich_thuoc_font)

        be_mat_ket_thuc_game = font_cua_toi.render('GAME OVER', True, mau)
        hinh_chu_nhat_ket_thuc_game = be_mat_ket_thuc_game.get_rect()
        hinh_chu_nhat_ket_thuc_game.center = (kich_thuoc_x/2, kich_thuoc_y/2 - kich_thuoc_font)  # Adjust the position here
        cua_so_game.blit(be_mat_ket_thuc_game, hinh_chu_nhat_ket_thuc_game)

        be_mat_diem_so = font_cua_toi.render('YOUR SCORE : ' + str(diem_so), True, mau)
        hinh_chu_nhat_diem_so = be_mat_diem_so.get_rect()
        hinh_chu_nhat_diem_so.center = (kich_thuoc_x/2, kich_thuoc_y/2)  # Adjust the position here
        cua_so_game.blit(be_mat_diem_so, hinh_chu_nhat_diem_so)

        foot_note = font_cua_toi.render('press any button to return to menu', True, mau)
        hinh_chu_nhat_foot_note = foot_note.get_rect()
        hinh_chu_nhat_foot_note.center = (kich_thuoc_x/2, kich_thuoc_y/2 + kich_thuoc_font)  # Adjust the position here
        cua_so_game.blit(foot_note, hinh_chu_nhat_foot_note)
        
        pygame.display.flip()
    
        # sau 2 giây chúng ta sẽ thoát khỏi
        # chương trình
        time.sleep(4)
        
        # hủy kích hoạt thư viện pygame
        for su_kien in pygame.event.get():
            if su_kien.type == pygame.KEYDOWN:
                main_menu(toc_do_ran,Snake_theme)
            if su_kien.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #pygame.quit()
        
        # thoát khỏi chương trình
        
        #quit()

    while True:
    
        # Xử lý sự kiện phím
        for su_kien in pygame.event.get():
            if su_kien.type == pygame.KEYDOWN:
                if su_kien.key == pygame.K_UP:
                    thay_doi_huong = 'LEN'
                if su_kien.key == pygame.K_DOWN:
                    thay_doi_huong = 'XUONG'
                if su_kien.key == pygame.K_LEFT:
                    thay_doi_huong = 'TRAI'
                if su_kien.key == pygame.K_RIGHT:
                    thay_doi_huong = 'PHAI'
            if su_kien.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Nếu hai phím được nhấn cùng một lúc
        # chúng ta không muốn rắn di chuyển vào hai
        # hướng cùng một lúc
        if thay_doi_huong == 'LEN' and huong != 'XUONG':
            huong = 'LEN'
        if thay_doi_huong == 'XUONG' and huong != 'LEN':
            huong = 'XUONG'
        if thay_doi_huong == 'TRAI' and huong != 'PHAI':
            huong = 'TRAI'
        if thay_doi_huong == 'PHAI' and huong != 'TRAI':
            huong = 'PHAI'

        # Di chuyển rắn
        if huong == 'LEN':
            vi_tri_ran[1] -= kich_thuoc_khoi
    
        if huong == 'XUONG':
            vi_tri_ran[1] += kich_thuoc_khoi
            
        if huong == 'TRAI':
            vi_tri_ran[0] -= kich_thuoc_khoi
            
        if huong == 'PHAI':
            vi_tri_ran[0] += kich_thuoc_khoi
            

        # Cơ chế tăng kích thước thân rắn
        

        b=[]
        if (vi_tri_ran[0] >= vi_tri_moi[0] and vi_tri_ran[0] < vi_tri_moi[0] + kich_thuoc_khoi) and (vi_tri_ran[1] >= vi_tri_moi[1] and vi_tri_ran[1] < vi_tri_moi[1] + kich_thuoc_khoi):
            for vi_tri in range(len(thân_ran)):
                if thân_ran[vi_tri][0]==Snake_theme[0]:
                    a=[thân_ran[vi_tri][0],list(vi_tri_ran)]
                    b= thân_ran[vi_tri][1]
                    thân_ran[vi_tri][0]=a[0]
                    thân_ran[vi_tri][1]=a[1]
                else:
                    a=[thân_ran[vi_tri][0],b]
                    b= thân_ran[vi_tri][1]
                    thân_ran[vi_tri][0]=a[0]
                    thân_ran[vi_tri][1]=a[1]
            a=[Snake_theme[1][loai_moi],b]
            thân_ran.append(a)
            diem_so += 10
            Tao_moi = False
        else:
             for vi_tri in range(len(thân_ran)):
                if thân_ran[vi_tri][0]==Snake_theme[0]:
                    a=[thân_ran[vi_tri][0],list(vi_tri_ran)]
                    b= thân_ran[vi_tri][1]
                    thân_ran[vi_tri][0]=a[0]
                    thân_ran[vi_tri][1]=a[1]
                else:
                    a=[thân_ran[vi_tri][0],b]
                    b= thân_ran[vi_tri][1]
                    thân_ran[vi_tri][0]=a[0]
                    thân_ran[vi_tri][1]=a[1]
        
        # Tạo mồi mới
        if not Tao_moi:
            vi_tri_moi = [random.randrange(1, (kich_thuoc_x//kich_thuoc_khoi)) * kich_thuoc_khoi,
                            random.randrange(1, (kich_thuoc_y//kich_thuoc_khoi)) * kich_thuoc_khoi]
            loai_moi=random.randint(0,2)
            
        Tao_moi = True
        cua_so_game.blit(Snake_theme[2],(0,-360))
        cua_so_game.blit(Snake_theme[1][loai_moi],(vi_tri_moi[0] ,vi_tri_moi[1])) 
        
        for vi_tri in range(len(thân_ran)):
            cua_so_game.blit(thân_ran[vi_tri][0],(thân_ran[vi_tri][1][0],thân_ran[vi_tri][1][1]))

        # Điều kiện kết thúc game
        if vi_tri_ran[0] < 0 or vi_tri_ran[0] > kich_thuoc_x-kich_thuoc_khoi:
            ket_thuc_game('Điểm số : ' + str(diem_so), mau_do, 'times new roman', 20)
            break
        if vi_tri_ran[1] < 0 or vi_tri_ran[1] > kich_thuoc_y-kich_thuoc_khoi:
            ket_thuc_game('Điểm số : ' + str(diem_so), mau_do, 'times new roman', 20)
            break
    
        # Chạm vào thân rắn
        for khoi in thân_ran[1:]:
            if vi_tri_ran[0] == khoi[1][0] and vi_tri_ran[1] == khoi[1][1]:
                ket_thuc_game('Điểm số : ' + str(diem_so), mau_do, 'times new roman', 20)
                break

        # Hiển thị điểm số liên tục
        hien_thi_diem_so('Điểm số : ' + str(diem_so), mau_trang, 'times new roman', 20)

    
        # Làm mới màn hình game
        pygame.display.update()

        # Khung hình mỗi giây
        fps.tick(toc_do_ran)

def mode(toc_do_ran, BG_Game):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        
        OPTIONS_EASY = Button(image=None, pos=(540, 150), 
                            text_input="EASY", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_NORMAL = Button(image=None, pos=(540, 300), 
                            text_input="NORMAL", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_HARD = Button(image=None, pos=(540, 450), 
                            text_input="HARD", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_EASY.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_NORMAL.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_HARD.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_EASY.update(SCREEN)
        OPTIONS_NORMAL.update(SCREEN)
        OPTIONS_HARD.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_EASY.checkForInput(OPTIONS_MOUSE_POS):
                    toc_do_ran=10
                    options(toc_do_ran,BG_Game)
                if OPTIONS_NORMAL.checkForInput(OPTIONS_MOUSE_POS):
                    toc_do_ran=20
                    options(toc_do_ran,BG_Game)
                if OPTIONS_HARD.checkForInput(OPTIONS_MOUSE_POS):
                    toc_do_ran=30
                    options(toc_do_ran,BG_Game)
        
        pygame.display.update()
        
def theme(toc_do_ran,Snake_theme):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        
        OPTIONS_MEOW = Button(image=None, pos=(540, 150), 
                            text_input="CAT", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_FISH = Button(image=None, pos=(540, 300), 
                            text_input="FISH", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_UFO = Button(image=None, pos=(540, 450), 
                            text_input="UFO", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_MEOW.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_FISH.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_UFO.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MEOW.update(SCREEN)
        OPTIONS_FISH.update(SCREEN)
        OPTIONS_UFO.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_MEOW.checkForInput(OPTIONS_MOUSE_POS):
                    Snake_theme[0]=pygame.image.load("assets/meome.png")
                    Snake_theme[0]=pygame.transform.scale(Snake_theme[0],(25,25))
                    
                    Snake_theme[1][0]=pygame.image.load("assets/meocon1.png")
                    Snake_theme[1][0]=pygame.transform.scale(Snake_theme[1][0],(20,20))
                    
                    Snake_theme[1][1]=pygame.image.load("assets/meocon2.png")
                    Snake_theme[1][1]=pygame.transform.scale(Snake_theme[1][1],(20,20))
                    
                    Snake_theme[1][2]=pygame.image.load("assets/meocon3.png")
                    Snake_theme[1][2]=pygame.transform.scale(Snake_theme[1][2],(20,20))
                    
                    Snake_theme[2]=pygame.image.load("assets/greenhill.jpg")
                    
                    options(toc_do_ran,Snake_theme)
                    
                if OPTIONS_FISH.checkForInput(OPTIONS_MOUSE_POS):
                    Snake_theme[0]=pygame.image.load("assets/clownfish.png")
                    Snake_theme[0]=pygame.transform.scale(Snake_theme[0],(25,25))
                    
                    Snake_theme[1][0]=pygame.image.load("assets/shark.png")
                    Snake_theme[1][0]=pygame.transform.scale(Snake_theme[1][0],(20,20))
                    
                    Snake_theme[1][1]=pygame.image.load("assets/turtle.png")
                    Snake_theme[1][1]=pygame.transform.scale(Snake_theme[1][1],(20,20))
                    
                    Snake_theme[1][2]=pygame.image.load("assets/bluefish.png")
                    Snake_theme[1][2]=pygame.transform.scale(Snake_theme[1][2],(20,20))
                    
                    Snake_theme[2]=pygame.image.load("assets/underwater.png")
                    options(toc_do_ran,Snake_theme)
                    
                if OPTIONS_UFO.checkForInput(OPTIONS_MOUSE_POS):
                    Snake_theme[0]=pygame.image.load("assets/theUFO.png")
                    Snake_theme[0]=pygame.transform.scale(Snake_theme[0],(25,25))
                    
                    Snake_theme[1][0]=pygame.image.load("assets/cow.png")
                    Snake_theme[1][0]=pygame.transform.scale(Snake_theme[1][0],(20,20))
                    
                    Snake_theme[1][1]=pygame.image.load("assets/person.png")
                    Snake_theme[1][1]=pygame.transform.scale(Snake_theme[1][1],(20,20))
                    
                    Snake_theme[1][2]=pygame.image.load("assets/plant.png")
                    Snake_theme[1][2]=pygame.transform.scale(Snake_theme[1][2],(20,20))
                    
                    Snake_theme[2]=pygame.image.load("assets/demdaysao.jpg")
                    options(toc_do_ran,Snake_theme)
        
        pygame.display.update()
        

    
def options(toc_do_ran,Snake_theme):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_MODE = Button(image=None, pos=(540, 150), 
                            text_input="MODE", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_THEME = Button(image=None, pos=(540, 300), 
                            text_input="THEME", font=get_font(75), base_color="Black", hovering_color="Green")
        
        OPTIONS_BACK = Button(image=None, pos=(540, 450), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")


        OPTIONS_MODE.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_THEME.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_MODE.update(SCREEN)
        OPTIONS_THEME.update(SCREEN)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu(toc_do_ran,Snake_theme)
                if OPTIONS_MODE.checkForInput(OPTIONS_MOUSE_POS):
                    mode(toc_do_ran,Snake_theme)
                if OPTIONS_THEME.checkForInput(OPTIONS_MOUSE_POS):
                    theme(toc_do_ran,Snake_theme)

        pygame.display.update()

def main_menu(toc_do_ran,Snake_theme):
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(540, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(540, 200), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(540, 350), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(540, 500), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(toc_do_ran,Snake_theme)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(toc_do_ran,Snake_theme)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu(toc_do_ran,snake_theme)