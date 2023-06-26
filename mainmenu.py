import pygame, sys, math
import random, json

pygame.init()
pygame.mixer.init()

loaded_images = []
loaded_sounds = []

class loading:
    def __init__(self):
        self.clock = pygame.time.Clock()
        loading_img = ["loader1.png", "loader2.png", "loader3.png",]
        self.image = pygame.image.load(loading_img[random.choice((0, 1, 2))])
        self.text = pygame.font.SysFont(None, 45)

    def run(self, window):
        progress = 0
        work_prog = 0
        bar = 0
        percent_prog = 0
        game_assets = ["", "mainmenu.png",  "buttons.png", "back.png","settings.png", "info.png","setinfo.png", "diamond.jpeg","coin1.png", "plus.png","mainmenu_plain.png", "sback.png","menu1.png", "menu2.png","menu1.png","menu3.png", "menu4.png","menu5.png","menu6.png","knife_slice.wav","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "background.wav","menu.wav", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd",] 
        work = len(game_assets) - 1
        self.width, self.height = window.get_size()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        initial = pygame.time.get_ticks()
        for asset in game_assets:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #background
            window.fill((0, 0, 0))
            window.blit(self.image, (0, 0))

            time = pygame.time.get_ticks()
            if time - initial < 2000 and asset != "":
                pygame.time.delay(2000)
            
            time = pygame.time.get_ticks()
            if time - initial >= 2000:
                pygame.time.delay(100)
                if asset.endswith(".png") or asset.endswith(".jpeg") or asset.endswith(".jpg"):
                    image = pygame.image.load(asset)
                    loaded_images.append(image)
                if asset.endswith(".wav"):
                    if asset == "background.wav":
                        pygame.mixer.music.load(asset)
                        pygame.time.delay(100)
                        pygame.mixer.music.play()
                    else:
                        pygame.time.delay(800)
                        sound = pygame.mixer.Sound(asset)
                        loaded_sounds.append(sound)
                    
                work_prog += 1
                progress = work_prog/work
                bar = progress * 1396
                percent_prog = math.ceil(progress * 100) 
                pygame.draw.rect(window, (100, 100, 100), pygame.Rect(self.width/2 - 700, self.height - 30, 1400, 15), 2)
                pygame.draw.rect(window, (255, 255, 0), pygame.Rect(self.width/2 - 698, self.height - 28, bar, 11))
                window.blit(self.text.render(f"{percent_prog}%", True, (100, 100, 100)), (1462, 840))

            pygame.display.flip()

            if progress >= 1:
                pygame.time.delay(200)
                mainmenu().run(window)
                return "done"
            
            self.clock.tick(40)

class mainmenu:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.background = loaded_images[0]
        self.menu = loaded_images[1]
        self.back = loaded_images[2]
        self.settings = loaded_images[3]
        self.info = loaded_images[4]
        self.setinfo = loaded_images[5]
        self.diamond = loaded_images[6]
        self.coin1 = loaded_images[7]
        self.plus = loaded_images[8]
        self.text = pygame.font.SysFont("Copperplate Gothic Bold", 40)

    def run(self, window):
        self.width, self.height = window.get_size()
        self.menu = pygame.transform.scale(self.menu, (600, self.height))
        self.menu.set_colorkey((255, 255, 255))
        self.menu.set_alpha(200)
        self.setinfo = pygame.transform.scale(self.setinfo, (170, 70))
        self.setinfo.set_colorkey((255, 255, 255))
        self.settings.set_colorkey((255, 255, 255))
        self.settings = pygame.transform.scale(self.settings, (50, 50))
        self.info.set_colorkey((255, 255, 255))
        self.info = pygame.transform.scale(self.info, (50, 50))
        self.diamond.set_colorkey((255, 255, 255))
        self.diamond = pygame.transform.scale(self.diamond, (80, 80))
        self.coin1.set_colorkey((255, 255, 255))
        self.coin1 = pygame.transform.scale(self.coin1, (50, 50))
        self.plus.set_colorkey((255, 255, 255))
        self.plus = pygame.transform.scale(self.plus, (80, 80))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        running = True
        left = -1 * 680
        play_size = training_size = store_size = settings_size = credits_size = quit_size = single_size = mp_size = yes_size = no_size = 60
        
        def menu_btn(txt, size):
            self.menu_txt = pygame.font.SysFont("Copperplate Gothic Bold", size, True)
            return self.menu_txt.render(txt, True, (255, 255, 255))
            
        play = menu_btn("PLAY", play_size)
        play_rct = play.get_rect()
        play_rct.center = left + 175, 81
        prect = pygame.draw.rect(window, (0, 0, 0), play_rct, 1)
        window.blit(play, (left + 175 - play.get_width()/2, 81 - play.get_height()/2))
        training = menu_btn("TRAINING", training_size)
        training_rct = training.get_rect()
        training_rct.center = left + 225, 231
        trect = pygame.draw.rect(window, (0, 0, 0), training_rct, 1)
        window.blit(training, (left + 225 - training.get_width()/2, 231 - training.get_height()/2))
        store = menu_btn("STORE", store_size)
        store_rct = store.get_rect()
        store_rct.center = left + 192, 381
        strect = pygame.draw.rect(window, (0, 0, 0), store_rct, 1)
        window.blit(store, (left + 192 - store.get_width()/2, 381 - store.get_height()/2))
        settings = menu_btn("SETTINGS", settings_size)
        settings_rct = settings.get_rect()
        settings_rct.center = left + 226, 531
        serect = pygame.draw.rect(window, (0, 0, 0), settings_rct, 1)
        window.blit(settings, (left + 226 - settings.get_width()/2, 531 - settings.get_height()/2))
        credits = menu_btn("CREDITS", credits_size)
        credits_rct = credits.get_rect()
        credits_rct.center = left + 213, 681
        crect = pygame.draw.rect(window, (0, 0, 0), credits_rct, 1)
        window.blit(credits, (left + 213 - credits.get_width()/2, 681 - credits.get_height()/2))
        quit = menu_btn("QUIT", quit_size)
        quit_rct = quit.get_rect()
        quit_rct.center = left + 175, 831
        qrect = pygame.draw.rect(window, (0, 0, 0), quit_rct, 1)
        window.blit(quit, (left + 175 - quit.get_width()/2, 831 - quit.get_height()/2))

        play_clk = training_clk = store_clk = settings_clk = credits_clk = quit_clk = False
        tm = 0
        x = 11
        
        loaded_sounds[0].set_volume(1)
        loaded_sounds[1].set_volume(1)
        loaded_sounds[0].play()

        self.back = pygame.transform.scale(self.back, (80, 70))
        self.back.set_colorkey((255, 255, 255))
        
        while running:
            if play_clk:
                p_srect = pygame.draw.rect(window, (0, 0, 0), single_rct, 1)
                p_mrect = pygame.draw.rect(window, (0, 0, 0), mp_rct, 1)
                back_rect = pygame.draw.rect(window, (0, 0, 0), back, 1)

            if quit_clk:
                back_rect = pygame.draw.rect(window, (0, 0, 0), back, 1)
                q_yrect = pygame.draw.rect(window, (0, 0, 0), yes_rct, 1)
                q_nrect = pygame.draw.rect(window, (0, 0, 0), no_rct, 1)
                
            if not play_clk and not training_clk and not store_clk and not settings_clk and not credits_clk and not quit_clk:
                prect = pygame.draw.rect(window, (0, 0, 0), play_rct, 1)
                trect = pygame.draw.rect(window, (0, 0, 0), training_rct, 1)
                strect = pygame.draw.rect(window, (0, 0, 0), store_rct, 1)
                serect = pygame.draw.rect(window, (0, 0, 0), settings_rct, 1)
                crect = pygame.draw.rect(window, (0, 0, 0), credits_rct, 1)
                qrect = pygame.draw.rect(window, (0, 0, 0), quit_rct, 1)

            window.fill((255, 255, 0))
            window.blit(self.background, (0, 0))
            if left < 0:
                left += 68
            window.blit(self.menu, (left, 0))
            settings_btn = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(1540, 10, 50, 50))
            info_btn = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(1460, 10, 50, 50))
            window.blit(self.setinfo, (1430, 0))
            window.blit(self.settings, (1540, 10))
            window.blit(self.info, (1460, 10))
            add_coins = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(1010, 15, 160, 45), 0, 20)
            window.blit(self.coin1, (1000, 10))
            window.blit(self.plus, (1130, -4))
            coins = menu_btn("0", 40)
            window.blit(coins, (1096 - coins.get_width()/2, 25))
            add_diamonds = pygame.draw.rect(window, (255, 255, 255), pygame.Rect(1215, 15, 120, 45), 0, 20)
            window.blit(self.diamond, (1200, -6))
            diamonds = self.text.render("0", True, (0, 0, 0))
            window.blit(diamonds, (1288 - diamonds.get_width()/2, 25))
            window.blit(self.plus, (1297, -4))

            player = pygame.transform.scale(loaded_images[x], (400, 690))
            player.set_colorkey((255, 255, 255))
            if tm == 0:
                tm = pygame.time.get_ticks()
            
            if pygame.time.get_ticks() - tm >= 600:
                if x < 13:
                    x += 1
                    tm = pygame.time.get_ticks()

            if pygame.time.get_ticks() - tm >= 100:
                if x > 13:
                    if x < 17:
                        x += 1
                    elif pygame.time.get_ticks() - tm >= 5000:
                        tm = pygame.time.get_ticks()
                        x = random.choice((11, 12, 13))
                    else:
                        x = 14

            if pygame.time.get_ticks() - tm >= 1200:
                if x == 13:
                    tm = pygame.time.get_ticks()
                    x += 1

            window.blit(player, (945, 220))

            if not play_clk and not training_clk and not store_clk and not settings_clk and not credits_clk and not quit_clk:
                if prect.collidepoint(pygame.mouse.get_pos()):
                    if phover:
                        phover = None
                    elif phover == False:
                        phover = True
                    play_size = 100
                else:
                    phover = False
                    play_size = 60
                if trect.collidepoint(pygame.mouse.get_pos()):
                    if thover:
                        thover = None
                    elif thover == False:
                        thover = True
                    training_size = 100
                else:
                    thover = False
                    training_size = 60
                if strect.collidepoint(pygame.mouse.get_pos()):
                    if sthover:
                        sthover = None
                    elif sthover == False:
                        sthover = True
                    store_size = 100
                else:
                    sthover = False
                    store_size = 60
                if serect.collidepoint(pygame.mouse.get_pos()):
                    if sehover:
                        sehover = None
                    elif sehover == False:
                        sehover = True
                    settings_size = 100
                else:
                    sehover = False
                    settings_size = 60
                if crect.collidepoint(pygame.mouse.get_pos()):
                    if chover:
                        chover = None
                    elif chover == False:
                        chover = True
                    credits_size = 100
                else:
                    chover = False
                    credits_size = 60
                if qrect.collidepoint(pygame.mouse.get_pos()):
                    if qhover:
                        qhover = None
                    elif qhover == False:
                        qhover = True
                    quit_size = 100
                else:
                    qhover = False
                    quit_size = 60
            
            if play_clk:
                if p_srect.collidepoint(pygame.mouse.get_pos()):
                    if p_shover:
                        p_shover = None
                    elif p_shover == False:
                        p_shover = True
                    single_size = 100
                else:
                    p_shover = False
                    single_size = 60
                if p_mrect.collidepoint(pygame.mouse.get_pos()):
                    if p_mhover:
                        p_mhover = None
                    elif p_mhover == False:
                        p_mhover = True
                    mp_size = 100
                else:
                    p_mhover = False
                    mp_size = 60
            if quit_clk:
                if q_yrect.collidepoint(pygame.mouse.get_pos()):
                    if q_yhover:
                        q_yhover = None
                    elif q_yhover == False:
                        q_yhover = True
                    yes_size = 100
                else:
                    q_yhover = False
                    yes_size = 60
                if q_nrect.collidepoint(pygame.mouse.get_pos()):
                    if q_nhover:
                        q_nhover = None
                    elif q_nhover == False:
                        q_nhover = True
                    no_size = 100
                else:
                    q_nhover = False
                    no_size = 60
            
            if phover:
                loaded_sounds[1].play()
            if thover:
                loaded_sounds[1].play()
            if sthover:
                loaded_sounds[1].play()
            if sehover:
                loaded_sounds[1].play()
            if chover:
                loaded_sounds[1].play()
            if qhover:
                loaded_sounds[1].play()
            if play_clk:
                if p_shover:
                    loaded_sounds[1].play()
                if p_mhover:
                    loaded_sounds[1].play()
            if quit_clk:
                if q_yhover:
                    loaded_sounds[1].play()
                if q_nhover:
                    loaded_sounds[1].play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if settings_btn.collidepoint(pygame.mouse.get_pos()):
                        Settings().run(window)
                        
                    if info_btn.collidepoint(pygame.mouse.get_pos()):
                        pass

                    if add_coins.collidepoint(pygame.mouse.get_pos()):
                        pass
                    
                    if add_diamonds.collidepoint(pygame.mouse.get_pos()):
                        pass

                    if play_clk or training_clk or store_clk or settings_clk or credits_clk or quit_clk:
                        if back_rect.collidepoint(pygame.mouse.get_pos()):
                            loaded_sounds[0].play()
                            left = -680
                            play_clk = False
                            quit_clk = False

                    if quit_clk:
                        if q_yrect.collidepoint(pygame.mouse.get_pos()):
                            running = False
                            sys.exit()

                        if q_nrect.collidepoint(pygame.mouse.get_pos()):
                            loaded_sounds[0].play()
                            left = -680
                            quit_clk = False

                    if not play_clk and not training_clk and not store_clk and not settings_clk and not credits_clk and not quit_clk and left >= 0:
                        if prect.collidepoint(pygame.mouse.get_pos()):
                            loaded_sounds[0].play()
                            left = -680
                            play_clk = True
                        if trect.collidepoint(pygame.mouse.get_pos()):
                            loaded_sounds[0].play()
                            left = -680
                            training_clk = True
                        if strect.collidepoint(pygame.mouse.get_pos()):
                            loaded_sounds[0].play()
                            left = -680
                            store_clk = True
                        if serect.collidepoint(pygame.mouse.get_pos()):
                            loaded_sounds[0].play()
                            left = -680
                            settings_clk = True
                        if crect.collidepoint(pygame.mouse.get_pos()):
                            loaded_sounds[0].play()
                            left = -680
                            credits_clk = True
                        if qrect.collidepoint(pygame.mouse.get_pos()):
                            loaded_sounds[0].play()
                            left = -680
                            quit_clk = True
                    
            if not play_clk and not training_clk and not store_clk and not settings_clk and not credits_clk and not quit_clk:
                play = menu_btn("PLAY", play_size)
                play_rct = play.get_rect()
                play_rct.center = left + 175, 81
                window.blit(play, (left + 175 - play.get_width()/2, 81 - play.get_height()/2))
                training = menu_btn("TRAINING", training_size)
                training_rct = training.get_rect()
                training_rct.center = left + 225, 231
                window.blit(training, (left + 225 - training.get_width()/2, 231 - training.get_height()/2))
                store = menu_btn("STORE", store_size)
                store_rct = store.get_rect()
                store_rct.center = left + 192, 381
                window.blit(store, (left + 192 - store.get_width()/2, 381 - store.get_height()/2))
                settings = menu_btn("TUTORIAL", settings_size)
                settings_rct = settings.get_rect()
                settings_rct.center = left + 226, 531
                window.blit(settings, (left + 226 - settings.get_width()/2, 531 - settings.get_height()/2))
                credits = menu_btn("EXTRAS", credits_size)
                credits_rct = credits.get_rect()
                credits_rct.center = left + 213, 681
                window.blit(credits, (left + 213 - credits.get_width()/2, 681 - credits.get_height()/2))
                quit = menu_btn("QUIT", quit_size)
                quit_rct = quit.get_rect()
                quit_rct.center = left + 175, 831
                window.blit(quit, (left + 175 - quit.get_width()/2, 831 - quit.get_height()/2))
                # print(f"Training {training.get_width()}, Store {store.get_width()} Settings {settings.get_width()} Credits {credits.get_width()}")

            if play_clk:
                window.blit(menu_btn("PLAY", 100), (left + 240, 200))
                back = self.back.get_rect()
                back.x, back.y = left + 6, 200
                window.blit(self.back, (left + 6, 200))
                single = menu_btn("SINGLE", single_size)
                single_rct = single.get_rect()
                single_rct.center = left + 225, 381
                window.blit(single, (left + 225 - single.get_width()/2, 381 - single.get_height()/2))
                mp = menu_btn("MULTIPLAYER", mp_size)
                mp_rct = mp.get_rect()
                mp_rct.center = left + 250, 531
                window.blit(mp, (left + 250 - mp.get_width()/2, 531 - mp.get_height()/2))

            if quit_clk:
                window.blit(menu_btn("QUIT?", 100), (left + 240, 200))
                back = self.back.get_rect()
                back.x, back.y = left + 6, 200
                window.blit(self.back, (left + 6, 200))
                yes = menu_btn("SURE", yes_size)
                yes_rct = yes.get_rect()
                yes_rct.center = left + 225, 381
                window.blit(yes, (left + 225 - yes.get_width()/2, 381 - yes.get_height()/2))
                no = menu_btn("NO", no_size)
                no_rct = no.get_rect()
                no_rct.center = left + 210, 531
                window.blit(no, (left + 210 - no.get_width()/2, 531 - no.get_height()/2))

            pygame.display.flip()
            self.clock.tick(40)

# loaded_images.append(pygame.image.load("mainmenu_plain.png"))
# loaded_images.append(pygame.image.load("sback.png"))

def save(data):
    with open('settings.json', "w") as file:
        json.dump(data, file)

def load():
    with open('settings.json', "r") as file:
        return json.load(file)
    
class Settings:
    def __init__(self):
        self.background = loaded_images[9] # supposed 9
        self.back = pygame.transform.scale(loaded_images[10], (62, 42)) # supposed 10
        self.back.set_colorkey((0, 0, 0))
        self.setttext = pygame.font.SysFont("Agency FB", 75, True)
        self.text = pygame.font.SysFont("Agency FB", 40, True)
        self.ntext = pygame.font.SysFont("Agency FB", 38, True)
        self.stext = pygame.font.SysFont("Agency FB", 35)
        self.txtbg = pygame.Surface((1400, 55))
        self.txtbg.fill((255, 255, 255))
        self.txtbg.set_alpha(40)
        self.clock = pygame.time.Clock()

    def run(self, window):
        settings_data = load()
        self.width, self.height = window.get_size()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        dg = True
        dg1_scroll = settings_data["display&graphics"]["display_mode"]
        dg2_scroll = settings_data["display&graphics"]["resolution"]
        dg3_scroll = 0
        mvol_d = 990 + (settings_data["audio"]["music_vol"] * 350)
        svol_d = 990 + (settings_data["audio"]["sfx_vol"] * 350)
        audio1_scroll = settings_data["audio"]["music"]
        audio2_scroll = settings_data["audio"]["sfx"]
        audio = controls = networking = tools = system = False
        clicked = False
        running = True
        while running:
            dg_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(40, 95, 300, 60))
            audio_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(355, 95, 92, 60))
            controls_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(475, 95, 153, 60))
            networking_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(655, 95, 186, 60))
            tools_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(865, 95, 98, 60))
            system_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(995, 95, 118, 60))
            back = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(1500, 22, 90, 42))
            window.blit(self.background, (0, 0))

            window.blit(self.setttext.render("SETTINGS", True, (255, 255, 255)), (40, 0))
            window.blit(self.stext.render("Back", True, (255, 255, 255)), (1500, 20))
            window.blit(self.back, (1540, 20))

            window.blit(self.text.render("DISPLAY & GRAPHICS", True, (255, 255, 255)), (40, 100))
            window.blit(self.text.render("AUDIO", True, (255, 255, 255)), (360, 100))
            window.blit(self.text.render("CONTROLS", True, (255, 255, 255)), (480, 100))
            window.blit(self.text.render("NETWORKING", True, (255, 255, 255)), (660, 100))
            window.blit(self.text.render("TOOLS", True, (255, 255, 255)), (870, 100))
            window.blit(self.text.render("SYSTEM", True, (255, 255, 255)), (1000, 100))

            mvol = (mvol_d - 990) / 350
            svol = (svol_d - 990) / 350

            if dg:
                pygame.draw.line(window, (255, 255, 255), (40, 95), (340, 95))
                pygame.draw.line(window, (255, 255, 255), (40, 154), (340, 154))
                pygame.draw.line(window, (0, 0, 255), (360, 95), (1110, 95))
                pygame.draw.line(window, (0, 0, 255), (360, 154), (1110, 154))
                window.blit(self.txtbg, (40, 200))
                window.blit(self.ntext.render("Display Mode", True, (255, 255, 255)), (70, 203))
                dg1l = pygame.draw.polygon(window, (0, 0, 255), ((1064, 227), (1090, 208), (1090, 246)))
                dg1r = pygame.draw.polygon(window, (0, 0, 255), ((1350, 227), (1324, 208), (1324, 246)))
                if dg1_scroll == 0:
                    window.blit(self.ntext.render("Fullscreen", True, (255, 255, 255)), (1142, 204))
                else:
                    window.blit(self.ntext.render("Window screen", True, (255, 255, 255)), (1110, 204))
                window.blit(self.txtbg, (40, 260))
                window.blit(self.ntext.render("Resolution", True, (255, 255, 255)), (70, 263))
                dg2l = pygame.draw.polygon(window, (0, 0, 255), ((1064, 287), (1090, 268), (1090, 306)))
                dg2r = pygame.draw.polygon(window, (0, 0, 255), ((1350, 287), (1324, 268), (1324, 306)))
                if dg2_scroll == 0:
                    window.blit(self.ntext.render("1600 x 900", True, (255, 255, 255)), (1135, 264))
                elif dg2_scroll == 1:
                    window.blit(self.ntext.render("1920 x 1080", True, (255, 255, 255)), (1130, 264))
                elif dg2_scroll == 2:
                    window.blit(self.ntext.render("1400 x 1000", True, (255, 255, 255)), (1130, 264))
                else:
                    window.blit(self.ntext.render("1000 x 600", True, (255, 255, 255)), (1130, 264))
                window.blit(self.txtbg, (40, 320))

            if audio:
                pygame.draw.line(window, (255, 255, 255), (355, 95), (445, 95))
                pygame.draw.line(window, (255, 255, 255), (355, 154), (445, 154))
                pygame.draw.line(window, (0, 0, 255), (40, 95), (340, 95))
                pygame.draw.line(window, (0, 0, 255), (40, 154), (340, 154))
                pygame.draw.line(window, (0, 0, 255), (480, 95), (1110, 95))
                pygame.draw.line(window, (0, 0, 255), (480, 154), (1110, 154))
                window.blit(self.txtbg, (40, 200))
                window.blit(self.ntext.render("Music", True, (255, 255, 255)), (70, 203))
                audio1l = pygame.draw.polygon(window, (0, 0, 255), ((1064, 227), (1090, 208), (1090, 246)))
                audio1r = pygame.draw.polygon(window, (0, 0, 255), ((1350, 227), (1324, 208), (1324, 246)))
                if audio1_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190, 204))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1190, 204))
                window.blit(self.txtbg, (40, 260))
                window.blit(self.ntext.render("SFX", True, (255, 255, 255)), (70, 263))
                audio2l = pygame.draw.polygon(window, (0, 0, 255), ((1064, 287), (1090, 268), (1090, 306)))
                audio2r = pygame.draw.polygon(window, (0, 0, 255), ((1350, 287), (1324, 268), (1324, 306)))
                if audio2_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190, 264))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1180, 264))
                window.blit(self.txtbg, (40, 320))
                window.blit(self.ntext.render("MUSIC VOLUME", True, (255, 255, 255)), (70, 323))
                pygame.draw.line(window, (0, 0, 255), (990, 348), (1350, 348), 4)
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(mvol_d, 333, 10, 30))
                window.blit(self.ntext.render(f"{math.ceil(mvol * 100)}%", True, (255, 255, 255)), (1365, 323))
                window.blit(self.txtbg, (40, 380))
                window.blit(self.ntext.render("SFX VOLUME", True, (255, 255, 255)), (70, 383))
                pygame.draw.line(window, (0, 0, 255), (990, 408), (1350, 408), 4)
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(svol_d, 393, 10, 30))
                window.blit(self.ntext.render(f"{math.ceil(svol * 100)}%", True, (255, 255, 255)), (1365, 383))

            if controls:
                pygame.draw.line(window, (255, 255, 255), (470, 95), (633, 95))
                pygame.draw.line(window, (255, 255, 255), (470, 154), (633, 154))
                pygame.draw.line(window, (0, 0, 255), (40, 95), (446, 95))
                pygame.draw.line(window, (0, 0, 255), (40, 154), (446, 154))
                pygame.draw.line(window, (0, 0, 255), (660, 95), (1110, 95))
                pygame.draw.line(window, (0, 0, 255), (660, 154), (1110, 154))
                window.blit(self.txtbg, (40, 200))

            if networking:
                pygame.draw.line(window, (255, 255, 255), (650, 95), (846, 95))
                pygame.draw.line(window, (255, 255, 255), (650, 154), (846, 154))
                pygame.draw.line(window, (0, 0, 255), (40, 95), (633, 95))
                pygame.draw.line(window, (0, 0, 255), (40, 154), (633, 154))
                pygame.draw.line(window, (0, 0, 255), (870, 95), (1110, 95))
                pygame.draw.line(window, (0, 0, 255), (870, 154), (1110, 154))
                window.blit(self.txtbg, (40, 200))

            if tools:
                pygame.draw.line(window, (255, 255, 255), (860, 95), (968, 95))
                pygame.draw.line(window, (255, 255, 255), (860, 154), (968, 154))
                pygame.draw.line(window, (0, 0, 255), (40, 95), (846, 95))
                pygame.draw.line(window, (0, 0, 255), (40, 154), (846, 154))
                pygame.draw.line(window, (0, 0, 255), (1000, 95), (1110, 95))
                pygame.draw.line(window, (0, 0, 255), (1000, 154), (1110, 154))
                window.blit(self.txtbg, (40, 200))

            if system:
                pygame.draw.line(window, (255, 255, 255), (990, 95), (1108, 95))
                pygame.draw.line(window, (255, 255, 255), (990, 154), (1108, 154))
                pygame.draw.line(window, (0, 0, 255), (40, 95), (968, 95))
                pygame.draw.line(window, (0, 0, 255), (40, 154), (968, 154))
                window.blit(self.txtbg, (40, 200))

            settings_data = {
                "display&graphics": {"display_mode": dg1_scroll, "resolution": dg2_scroll,},
                "audio": {"music": audio1_scroll, "sfx": audio2_scroll, "music_vol": mvol, "sfx_vol": svol,},
                "controls": {},
                "networking": {}, 
                "tools": {},
                "system": {},
            }

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clicked = True
                    if dg:
                        if dg1r.collidepoint(pygame.mouse.get_pos()):
                            dg1_scroll += 1

                        if dg1l.collidepoint(pygame.mouse.get_pos()):
                            dg1_scroll -= 1

                        if dg2r.collidepoint(pygame.mouse.get_pos()):
                            dg2_scroll += 1

                        if dg2l.collidepoint(pygame.mouse.get_pos()):
                            dg2_scroll -= 1

                        dg1_scroll = dg1_scroll % 2
                        dg2_scroll = dg2_scroll % 4
                    
                    if audio:
                        if audio1r.collidepoint(pygame.mouse.get_pos()):
                            audio1_scroll += 1

                        if audio1l.collidepoint(pygame.mouse.get_pos()):
                            audio1_scroll -= 1

                        if audio2r.collidepoint(pygame.mouse.get_pos()):
                            audio2_scroll += 1

                        if audio2l.collidepoint(pygame.mouse.get_pos()):
                            audio2_scroll -= 1

                        audio1_scroll = audio1_scroll % 2
                        audio2_scroll = audio2_scroll % 2

                    if dg_rct.collidepoint(pygame.mouse.get_pos()):
                        dg = True
                        audio = controls = networking = tools = system = False

                    if audio_rct.collidepoint(pygame.mouse.get_pos()):
                        audio = True
                        dg = controls = networking = tools = system = False

                    if controls_rct.collidepoint(pygame.mouse.get_pos()):
                        controls = True
                        dg = audio = networking = tools = system = False

                    if networking_rct.collidepoint(pygame.mouse.get_pos()):
                        networking = True
                        dg = controls = audio = tools = system = False

                    if tools_rct.collidepoint(pygame.mouse.get_pos()):
                        tools = True
                        dg = controls = networking = audio = system = False
                    
                    if system_rct.collidepoint(pygame.mouse.get_pos()):
                        system = True
                        dg = controls = networking = tools = audio = False

                    if back.collidepoint(pygame.mouse.get_pos()):
                        save(settings_data)
                        return "done"
                        
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    clicked = False

            if clicked:
                if 995 < pygame.mouse.get_pos()[0] < 1345 and 335 <= pygame.mouse.get_pos()[1] <= 365:
                    mvol_d = pygame.mouse.get_pos()[0] - 5

                if 990 <= pygame.mouse.get_pos()[0] <= 995 and 335 <= pygame.mouse.get_pos()[1] <= 365:
                    mvol_d = 990

                if 1345 <= pygame.mouse.get_pos()[0] <= 1350 and 335 <= pygame.mouse.get_pos()[1] <= 365:
                    mvol_d = 1340

                if 995 < pygame.mouse.get_pos()[0] < 1345 and 395 <= pygame.mouse.get_pos()[1] <= 425:
                    svol_d = pygame.mouse.get_pos()[0] - 5

                if 990 <= pygame.mouse.get_pos()[0] <= 995 and 395 <= pygame.mouse.get_pos()[1] <= 425:
                    svol_d = 990

                if 1345 <= pygame.mouse.get_pos()[0] <= 1350 and 395 <= pygame.mouse.get_pos()[1] <= 425:
                    svol_d = 1340

            pygame.display.flip()
            self.clock.tick(40)

# Settings().run(pygame.display.set_mode((1600, 900)))