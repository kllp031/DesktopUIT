import pygame, sys
import time
import random
from button import Button

#lul

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/1.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    toc_do_ran = 15

    # Kích thước khối của rắn và mồi
    kich_thuoc_khoi = 20  # Giá trị cũ là 10

    # Kích thước cửa sổ
    kich_thuoc_x = 1280 
    kich_thuoc_y = 720

    # Một số màu 
    mau_den = pygame.Color(0, 0, 0)
    mau_trang = pygame.Color(255, 255, 255)
    mau_do = pygame.Color(255, 0, 0)
    mau_xanh_la = pygame.Color(0, 255, 0)
    mau_xanh_duong = pygame.Color(0, 0, 255)

    # Khởi tạo pygame
    pygame.init()

    # Khởi tạo cửa sổ game
    pygame.display.set_caption('Rắn săn mồi')
    cua_so_game = pygame.display.set_mode((kich_thuoc_x, kich_thuoc_y))
    fps = pygame.time.Clock()

    # Định nghĩa vị trí mặc định của rắn
    vi_tri_ran = [200, 100]

    # Định nghĩa 4 khối đầu tiên của thân rắn
    thân_ran = [[80, 60],
                [60, 60],
                [40, 60],
                [20, 60]
            ]


    vi_tri_moi = [random.randrange(0, kich_thuoc_x//kich_thuoc_khoi) * kich_thuoc_khoi,
                random.randrange(0, kich_thuoc_y//kich_thuoc_khoi) * kich_thuoc_khoi]


    # Vẽ rắn và mồi
    for vi_tri in thân_ran:
        pygame.draw.rect(cua_so_game, mau_xanh_la,
                        pygame.Rect(vi_tri[0], vi_tri[1], kich_thuoc_khoi, kich_thuoc_khoi))
            
    pygame.draw.rect(cua_so_game, mau_trang, pygame.Rect(
    vi_tri_moi[0], vi_tri_moi[1], kich_thuoc_khoi, kich_thuoc_khoi))

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
        time.sleep(2)
        
        # hủy kích hoạt thư viện pygame
        for su_kien in pygame.event.get():
            if su_kien.type == pygame.KEYDOWN:
                main_menu()
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
        thân_ran.insert(0, list(vi_tri_ran))
        if (vi_tri_ran[0] >= vi_tri_moi[0] and vi_tri_ran[0] < vi_tri_moi[0] + kich_thuoc_khoi) and (vi_tri_ran[1] >= vi_tri_moi[1] and vi_tri_ran[1] < vi_tri_moi[1] + kich_thuoc_khoi):
            diem_so += 10
            Tao_moi = False
        else:
            thân_ran.pop()
        
        # Tạo mồi mới
        if not Tao_moi:
            vi_tri_moi = [random.randrange(1, (kich_thuoc_x//kich_thuoc_khoi)) * kich_thuoc_khoi,
                            random.randrange(1, (kich_thuoc_y//kich_thuoc_khoi)) * kich_thuoc_khoi]
            
        Tao_moi = True
        cua_so_game.fill(mau_den)
        
        for vi_tri in thân_ran:
            pygame.draw.rect(cua_so_game, mau_xanh_la,
                            pygame.Rect(vi_tri[0], vi_tri[1], kich_thuoc_khoi, kich_thuoc_khoi))
            
        pygame.draw.rect(cua_so_game, mau_trang, pygame.Rect(
        vi_tri_moi[0], vi_tri_moi[1], kich_thuoc_khoi, kich_thuoc_khoi))

        # Điều kiện kết thúc game
        if vi_tri_ran[0] < 0 or vi_tri_ran[0] > kich_thuoc_x-kich_thuoc_khoi:
            ket_thuc_game('Điểm số : ' + str(diem_so), mau_do, 'times new roman', 20)
        if vi_tri_ran[1] < 0 or vi_tri_ran[1] > kich_thuoc_y-kich_thuoc_khoi:
            ket_thuc_game('Điểm số : ' + str(diem_so), mau_do, 'times new roman', 20)
    
        # Chạm vào thân rắn
        for khoi in thân_ran[1:]:
            if vi_tri_ran[0] == khoi[0] and vi_tri_ran[1] == khoi[1]:
                ket_thuc_game('Điểm số : ' + str(diem_so), mau_do, 'times new roman', 20)

        # Hiển thị điểm số liên tục
        hien_thi_diem_so('Điểm số : ' + str(diem_so), mau_trang, 'times new roman', 20)

    
        # Làm mới màn hình game
        pygame.display.update()

        # Khung hình mỗi giây
        fps.tick(toc_do_ran)

    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
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
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()