import pygame, sys
import time
import random
from button import Button

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

class Game:
    def __init__(self):
        # Tốc độ của rắn
        self.toc_do_ran = 15

        # Kích thước khối của rắn và mồi
        self.kich_thuoc_khoi = 20

        # Kích thước cửa sổ
        self.kich_thuoc_x = 1280
        self.kich_thuoc_y = 720

        # Một số màu 
        self.mau_den = pygame.Color(0, 0, 0)
        self.mau_trang = pygame.Color(255, 255, 255)
        self.mau_do = pygame.Color(255, 0, 0)
        self.mau_xanh_la = pygame.Color(0, 255, 0)
        self.mau_xanh_duong = pygame.Color(0, 0, 255)

        # Khởi tạo pygame
        pygame.init()

        # Khởi tạo cửa sổ game
        pygame.display.set_caption('Rắn săn mồi')
        self.cua_so_game = pygame.display.set_mode((self.kich_thuoc_x, self.kich_thuoc_y))
        self.fps = pygame.time.Clock()

        # Định nghĩa vị trí mặc định của rắn
        self.vi_tri_ran = [200, 100]

        # Định nghĩa 4 khối đầu tiên của thân rắn
        self.thân_ran = [[80, 60], [60, 60], [40, 60], [20, 60]]

        # Định nghĩa vị trí mồi
        self.vi_tri_moi = [random.randrange(0, self.kich_thuoc_x//self.kich_thuoc_khoi) * self.kich_thuoc_khoi,
                           random.randrange(0, self.kich_thuoc_y//self.kich_thuoc_khoi) * self.kich_thuoc_khoi]

        # Biến kiểm soát việc tạo mồi mới
        self.Tao_moi = True

        # Đặt hướng mặc định của rắn về phía bên phải
        self.huong = 'PHAI'
        self.thay_doi_huong = self.huong

        # Điểm số ban đầu
        self.diem_so = 0

    # Hàm hiển thị điểm số
    def hien_thi_diem_so(self, lua_chon, mau, font, kich_co):
        font_diem_so = pygame.font.SysFont(font, kich_co)
        be_mat_diem_so = font_diem_so.render('SCORE: ' + str(self.diem_so), True, mau)
        hinh_chu_nhat_diem_so = be_mat_diem_so.get_rect()
        self.cua_so_game.blit(be_mat_diem_so, hinh_chu_nhat_diem_so)

    # Hàm kết thúc game
    def ket_thuc_game(self, lua_chon, mau, font, kich_co):
        font_cua_toi = pygame.font.SysFont(font, kich_co)
        kich_thuoc_font = 50
        font_cua_toi = pygame.font.Font(None, kich_thuoc_font)
        be_mat_ket_thuc_game = font_cua_toi.render('GAME OVER', True, mau)
        hinh_chu_nhat_ket_thuc_game = be_mat_ket_thuc_game.get_rect()
        hinh_chu_nhat_ket_thuc_game.center = (self.kich_thuoc_x/2, self.kich_thuoc_y/2 - kich_thuoc_font)
        self.cua_so_game.blit(be_mat_ket_thuc_game, hinh_chu_nhat_ket_thuc_game)
        be_mat_diem_so = font_cua_toi.render('YOUR SCORE : ' + str(self.diem_so), True, mau)
        hinh_chu_nhat_diem_so = be_mat_diem_so.get_rect()
        hinh_chu_nhat_diem_so.center = (self.kich_thuoc_x/2, self.kich_thuoc_y/2)
        self.cua_so_game.blit(be_mat_diem_so, hinh_chu_nhat_diem_so)
        foot_note = font_cua_toi.render('press any button to return to menu', True, mau)
        hinh_chu_nhat_foot_note = foot_note.get_rect()
        hinh_chu_nhat_foot_note.center = (self.kich_thuoc_x/2, self.kich_thuoc_y/2 + kich_thuoc_font)
        self.cua_so_game.blit(foot_note, hinh_chu_nhat_foot_note)
        pygame.display.flip()
        time.sleep(2)
        for su_kien in pygame.event.get():
            if su_kien.type == pygame.KEYDOWN:
                menu = Menu(SCREEN, BG)
                menu.main_menu()
            if su_kien.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # Hàm chính để chạy game
    def run(self):
        while True:
            # Xử lý sự kiện phím
            for su_kien in pygame.event.get():
                if su_kien.type == pygame.KEYDOWN:
                    if su_kien.key == pygame.K_UP:
                        self.thay_doi_huong = 'LEN'
                    if su_kien.key == pygame.K_DOWN:
                        self.thay_doi_huong = 'XUONG'
                    if su_kien.key == pygame.K_LEFT:
                        self.thay_doi_huong = 'TRAI'
                    if su_kien.key == pygame.K_RIGHT:
                        self.thay_doi_huong = 'PHAI'
                if su_kien.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Nếu hai phím được nhấn cùng một lúc, chúng ta không muốn rắn di chuyển vào hai hướng cùng một lúc
            if self.thay_doi_huong == 'LEN' and self.huong != 'XUONG':
                self.huong = 'LEN'
            if self.thay_doi_huong == 'XUONG' and self.huong != 'LEN':
                self.huong = 'XUONG'
            if self.thay_doi_huong == 'TRAI' and self.huong != 'PHAI':
                self.huong = 'TRAI'
            if self.thay_doi_huong == 'PHAI' and self.huong != 'TRAI':
                self.huong = 'PHAI'

            # Di chuyển rắn
            if self.huong == 'LEN':
                self.vi_tri_ran[1] -= self.kich_thuoc_khoi
            if self.huong == 'XUONG':
                self.vi_tri_ran[1] += self.kich_thuoc_khoi
            if self.huong == 'TRAI':
                self.vi_tri_ran[0] -= self.kich_thuoc_khoi
            if self.huong == 'PHAI':
                self.vi_tri_ran[0] += self.kich_thuoc_khoi

            # Cơ chế tăng kích thước thân rắn
            self.thân_ran.insert(0, list(self.vi_tri_ran))
            if (self.vi_tri_ran[0] >= self.vi_tri_moi[0] and self.vi_tri_ran[0] < self.vi_tri_moi[0] + self.kich_thuoc_khoi) and (self.vi_tri_ran[1] >= self.vi_tri_moi[1] and self.vi_tri_ran[1] < self.vi_tri_moi[1] + self.kich_thuoc_khoi):
                self.diem_so += 10
                self.Tao_moi = False
            else:
                self.thân_ran.pop()

            # Tạo mồi mới
            if not self.Tao_moi:
                self.vi_tri_moi = [random.randrange(1, (self.kich_thuoc_x//self.kich_thuoc_khoi)) * self.kich_thuoc_khoi,
                                   random.randrange(1, (self.kich_thuoc_y//self.kich_thuoc_khoi)) * self.kich_thuoc_khoi]

            self.Tao_moi = True
            self.cua_so_game.fill(self.mau_den)

            # Vẽ rắn và mồi
            for vi_tri in self.thân_ran:
                pygame.draw.rect(self.cua_so_game, self.mau_xanh_la,
                                pygame.Rect(vi_tri[0], vi_tri[1], self.kich_thuoc_khoi, self.kich_thuoc_khoi))
            pygame.draw.rect(self.cua_so_game, self.mau_trang, pygame.Rect(
            self.vi_tri_moi[0], self.vi_tri_moi[1], self.kich_thuoc_khoi, self.kich_thuoc_khoi))

            # Điều kiện kết thúc game
            if self.vi_tri_ran[0] < 0 or self.vi_tri_ran[0] > self.kich_thuoc_x-self.kich_thuoc_khoi:
                self.ket_thuc_game('Điểm số : ' + str(self.diem_so), self.mau_do, 'times new roman', 20)
            if self.vi_tri_ran[1] < 0 or self.vi_tri_ran[1] > self.kich_thuoc_y-self.kich_thuoc_khoi:
                self.ket_thuc_game('Điểm số : ' + str(self.diem_so), self.mau_do, 'times new roman', 20)

            # Chạm vào thân rắn
            for khoi in self.thân_ran[1:]:
                if self.vi_tri_ran[0] == khoi[0] and self.vi_tri_ran[1] == khoi[1]:
                    self.ket_thuc_game('Điểm số : ' + str(self.diem_so), self.mau_do, 'times new roman', 20)

            # Hiển thị điểm số liên tục
            self.hien_thi_diem_so('Điểm số : ' + str(self.diem_so), self.mau_trang, 'times new roman', 20)

            # Làm mới màn hình game
            pygame.display.update()

            # Khung hình mỗi giây
            self.fps.tick(self.toc_do_ran)
    
class Options:
    def __init__(self, screen):
        self.screen = screen
        self.back_button = Button(image=None, pos=(640, 460), 
                                  text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

    def options(self):
        while True:
            options_mouse_pos = pygame.mouse.get_pos()

            self.screen.fill("white")

            options_text = get_font(45).render("This is the OPTIONS screen.", True, "Black")
            options_rect = options_text.get_rect(center=(640, 260))
            self.screen.blit(options_text, options_rect)

            self.back_button.changeColor(options_mouse_pos)
            self.back_button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.checkForInput(options_mouse_pos):
                        menu = Menu(SCREEN, BG)
                        menu.main_menu()

            pygame.display.update()

class Menu:
    def __init__(self, screen, bg):
        self.screen = screen
        self.bg = bg
        self.buttons = [
            Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                   text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White"),
            Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                   text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White"),
            Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                   text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        ]

    def main_menu(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            menu_mouse_pos = pygame.mouse.get_pos()
            menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(640, 100))
            self.screen.blit(menu_text, menu_rect)

            for button in self.buttons:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.buttons[0].checkForInput(menu_mouse_pos):
                        game = Game()
                        game.run()
                    if self.buttons[1].checkForInput(menu_mouse_pos):
                        option = Options(SCREEN)
                        option.options()
                    if self.buttons[2].checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    BG = pygame.image.load("assets/1.png")
    menu = Menu(SCREEN, BG)
    menu.main_menu()