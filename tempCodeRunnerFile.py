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