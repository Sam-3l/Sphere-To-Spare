import pygame, sys, math
import random, json

from .settings import Settings

pygame.init()
pygame.mixer.init()

loaded_images = []
loaded_sounds = []

def load():
    with open('data/settings.json', "r") as file:
        return json.load(file)
    
class loading:
    def __init__(self):
        self.clock = pygame.time.Clock()
        loading_img = ["loader1.png", "loader2.png", "loader3.png",]
        self.image = pygame.image.load(f"images/{loading_img[random.choice((0, 1, 2))]}")

    def run(self, window):
        xdim, ydim = window.get_width()/1600, window.get_height()/900 
        self.text = pygame.font.SysFont(None, int(45*xdim))
        settings_data = load()
        music_vol = settings_data["audio"]["music_vol"]
        if settings_data["audio"]["music"] == 1:
            music_vol = 0
        pygame.mixer.music.set_volume(music_vol)

        progress = 0
        work_prog = 0
        bar = 0
        percent_prog = 0
        game_assets = ["", "mainmenu.png",  "buttons.png", "back.png","settings.png", "info.png","setinfo.png", "diamond.png","coin1.png", "plus.png","mainmenu_plain.png", "sback.png","menu1.png", "menu2.png","menu1.png","menu3.png", "menu4.png","menu5.png","menu6.png","knife_slice.wav","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "background.wav","menu.wav", "clicked.wav", "mainmenu_trans.png", "scale.wav", "dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd","dfsdf", "dfsdgdgsd", "dfsdgdgsd",] 
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
                    image = pygame.image.load(f"images/{asset}")
                    loaded_images.append(image)
                if asset.endswith(".wav"):
                    if asset == "background.wav":
                        pygame.mixer.music.load(f"audios/{asset}")
                        pygame.time.delay(100)
                        pygame.mixer.music.play()
                    else:
                        pygame.time.delay(800)
                        sound = pygame.mixer.Sound(f"audios/{asset}")
                        loaded_sounds.append(sound)
                    
                work_prog += 1
                progress = work_prog/work
                bar = progress * 1396
                percent_prog = math.ceil(progress * 100) 
                pygame.draw.rect(window, (100, 100, 100), pygame.Rect(self.width/2 - 700*xdim, self.height - 30*ydim, 1400*xdim, 15*ydim), 2)
                pygame.draw.rect(window, (255, 255, 0), pygame.Rect(self.width/2 - 698*xdim, self.height - 28*ydim, bar*xdim, 11*ydim))
                window.blit(self.text.render(f"{percent_prog}%", True, (100, 100, 100)), (1462*xdim, 840*ydim))

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

    def run(self, window):
        self.width, self.height = window.get_size()
        xdim, ydim = self.width/1600, self.height/900 
        self.text = pygame.font.SysFont("Copperplate Gothic Bold", int(40*xdim))
        self.menu = pygame.transform.scale(self.menu, (600*xdim, self.height))
        self.menu.set_colorkey((255, 255, 255))
        self.menu.set_alpha(200)
        self.setinfo = pygame.transform.scale(self.setinfo, (170*xdim, 70*ydim))
        self.setinfo.set_colorkey((255, 255, 255))
        self.settings = pygame.transform.scale(self.settings, (55*xdim, 55*ydim))
        self.settings.set_colorkey((255, 255, 255))
        self.info = pygame.transform.scale(self.info, (55*xdim, 55*ydim))
        self.info.set_colorkey((255, 255, 255))
        self.diamond = pygame.transform.scale(self.diamond, (92*xdim, 110*ydim))
        self.diamond.set_colorkey((255, 255, 255))
        self.coin1 = pygame.transform.scale(self.coin1, (50*xdim, 50*ydim))
        self.coin1.set_colorkey((255, 255, 255))
        self.plus = pygame.transform.scale(self.plus, (80*xdim, 80*ydim))
        self.plus.set_colorkey((255, 255, 255))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        running = True
        left = -xdim * 680
        play_size = training_size = store_size = settings_size = credits_size = quit_size = single_size = mp_size = yes_size = no_size = int(60*xdim)
    
        slide = loaded_sounds[0]
        hover = loaded_sounds[1]
        focus = loaded_sounds[2]

        def menu_btn(txt, size):
            self.menu_txt = pygame.font.SysFont("Copperplate Gothic Bold", size, True)
            return self.menu_txt.render(txt, True, (255, 255, 255))
            
        play = menu_btn("PLAY", play_size)
        play_rct = play.get_rect()
        play_rct.center = left + 175*xdim, 81*ydim
        prect = pygame.draw.rect(window, (0, 0, 0), play_rct, 1)
        window.blit(play, (left + 175*xdim - play.get_width()/2, 81*ydim - play.get_height()/2))
        training = menu_btn("TRAINING", training_size)
        training_rct = training.get_rect()
        training_rct.center = left + 225*xdim, 231*ydim
        trect = pygame.draw.rect(window, (0, 0, 0), training_rct, 1)
        window.blit(training, (left + 225*xdim - training.get_width()/2, 231*ydim - training.get_height()/2))
        store = menu_btn("STORE", store_size)
        store_rct = store.get_rect()
        store_rct.center = left + 192*xdim, 381*ydim
        strect = pygame.draw.rect(window, (0, 0, 0), store_rct, 1)
        window.blit(store, (left + 192*xdim - store.get_width()/2, 381*ydim - store.get_height()/2))
        settings = menu_btn("SETTINGS", settings_size)
        settings_rct = settings.get_rect()
        settings_rct.center = left + 226*xdim, 531*ydim
        serect = pygame.draw.rect(window, (0, 0, 0), settings_rct, 1)
        window.blit(settings, (left + 226*xdim - settings.get_width()/2, 531*ydim - settings.get_height()/2))
        credits = menu_btn("CREDITS", credits_size)
        credits_rct = credits.get_rect()
        credits_rct.center = left + 213*xdim, 681*ydim
        crect = pygame.draw.rect(window, (0, 0, 0), credits_rct, 1)
        window.blit(credits, (left + 213*xdim - credits.get_width()/2, 681*ydim - credits.get_height()/2))
        quit = menu_btn("QUIT", quit_size)
        quit_rct = quit.get_rect()
        quit_rct.center = left + 175*xdim, 831*ydim
        qrect = pygame.draw.rect(window, (0, 0, 0), quit_rct, 1)
        window.blit(quit, (left + 175*xdim - quit.get_width()/2, 831*ydim - quit.get_height()/2))

        play_clk = training_clk = store_clk = settings_clk = credits_clk = quit_clk = False
        tm = 0
        x = 11
        
        slide.play()

        self.back = pygame.transform.scale(self.back, (80*xdim, 70*ydim))
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
                left += 68*xdim
            window.blit(self.menu, (left, 0))
            settings_btn = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(1540*xdim, 6*ydim, 55*xdim, 55*ydim))
            info_btn = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(1460*xdim, 6*ydim, 55*xdim, 55*ydim))
            window.blit(self.setinfo, (1430*xdim, 0))
            window.blit(self.settings, (1540*xdim, 6*ydim))
            window.blit(self.info, (1460*xdim, 6*ydim))
            add_coins = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(1010*xdim, 15*ydim, 160*xdim, 45*ydim), 0, 20)
            window.blit(self.coin1, (1000*xdim, 10*ydim))
            window.blit(self.plus, (1130*xdim, -4*ydim))
            coins = menu_btn("0", int(40*xdim))
            window.blit(coins, (1096*xdim - coins.get_width()/2, 25*ydim))
            add_diamonds = pygame.draw.rect(window, (255, 255, 255), pygame.Rect(1215*xdim, 15*ydim, 120*xdim, 45*ydim), 0, 20)
            window.blit(self.diamond, (1180*xdim, -24*ydim))
            diamonds = self.text.render("0", True, (0, 0, 0))
            window.blit(diamonds, (1288*xdim - diamonds.get_width()/2, 25*ydim))
            window.blit(self.plus, (1297*xdim, -4*ydim))

            settings_data = load()
            music_vol = settings_data["audio"]["music_vol"]
            sfx_vol = settings_data["audio"]["sfx_vol"]
            if settings_data["audio"]["music"] == 1:
                music_vol = 0
            if settings_data["audio"]["sfx"] == 1:
                sfx_vol = 0
        
            pygame.mixer.music.set_volume(music_vol)
            slide.set_volume(sfx_vol)
            hover.set_volume(sfx_vol)
            focus.set_volume(sfx_vol)

            player = pygame.transform.scale(loaded_images[x], (400*xdim, 690*ydim))
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
                    elif pygame.time.get_ticks() - tm >= 3500:
                        tm = pygame.time.get_ticks()
                        x = random.choice((11, 12, 13))
                    else:
                        x = 14

            if pygame.time.get_ticks() - tm >= 1200:
                if x == 13:
                    tm = pygame.time.get_ticks()
                    x += 1

            window.blit(player, (945*xdim, 220*ydim))

            if not play_clk and not training_clk and not store_clk and not settings_clk and not credits_clk and not quit_clk:
                if prect.collidepoint(pygame.mouse.get_pos()):
                    if phover:
                        phover = None
                    elif phover == False:
                        phover = True
                    play_size = int(100*xdim)
                else:
                    phover = False
                    play_size = int(60*xdim)
                if trect.collidepoint(pygame.mouse.get_pos()):
                    if thover:
                        thover = None
                    elif thover == False:
                        thover = True
                    training_size = int(100*xdim)
                else:
                    thover = False
                    training_size = int(60*xdim)
                if strect.collidepoint(pygame.mouse.get_pos()):
                    if sthover:
                        sthover = None
                    elif sthover == False:
                        sthover = True
                    store_size = int(100*xdim)
                else:
                    sthover = False
                    store_size = int(60*xdim)
                if serect.collidepoint(pygame.mouse.get_pos()):
                    if sehover:
                        sehover = None
                    elif sehover == False:
                        sehover = True
                    settings_size = int(100*xdim)
                else:
                    sehover = False
                    settings_size = int(60*xdim)
                if crect.collidepoint(pygame.mouse.get_pos()):
                    if chover:
                        chover = None
                    elif chover == False:
                        chover = True
                    credits_size = int(100*xdim)
                else:
                    chover = False
                    credits_size = int(60*xdim)
                if qrect.collidepoint(pygame.mouse.get_pos()):
                    if qhover:
                        qhover = None
                    elif qhover == False:
                        qhover = True
                    quit_size = int(100*xdim)
                else:
                    qhover = False
                    quit_size = int(60*xdim)
            
            if play_clk:
                if p_srect.collidepoint(pygame.mouse.get_pos()):
                    if p_shover:
                        p_shover = None
                    elif p_shover == False:
                        p_shover = True
                    single_size = int(100*xdim)
                else:
                    p_shover = False
                    single_size = int(60*xdim)
                if p_mrect.collidepoint(pygame.mouse.get_pos()):
                    if p_mhover:
                        p_mhover = None
                    elif p_mhover == False:
                        p_mhover = True
                    mp_size = int(100*xdim)
                else:
                    p_mhover = False
                    mp_size = int(60*xdim)
            if quit_clk:
                if q_yrect.collidepoint(pygame.mouse.get_pos()):
                    if q_yhover:
                        q_yhover = None
                    elif q_yhover == False:
                        q_yhover = True
                    yes_size = int(100*xdim)
                else:
                    q_yhover = False
                    yes_size = int(60*xdim)
                if q_nrect.collidepoint(pygame.mouse.get_pos()):
                    if q_nhover:
                        q_nhover = None
                    elif q_nhover == False:
                        q_nhover = True
                    no_size = int(100*xdim)
                else:
                    q_nhover = False
                    no_size = int(60*xdim)
            
            if phover:
                hover.play()
            if thover:
                hover.play()
            if sthover:
                hover.play()
            if sehover:
                hover.play()
            if chover:
                hover.play()
            if qhover:
                hover.play()
            if play_clk:
                if p_shover:
                    hover.play()
                if p_mhover:
                    hover.play()
            if quit_clk:
                if q_yhover:
                    hover.play()
                if q_nhover:
                    hover.play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if settings_btn.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                        window = Settings().run(window, {'loaded_images' : [loaded_images[b] for b in [9, 10, 18]], 'loaded_sounds' : [loaded_sounds[b] for b in [2, 3]]})
                        slide.play()
                        left = -680*xdim
                        
                    if info_btn.collidepoint(pygame.mouse.get_pos()):
                        focus.play()

                    if add_coins.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                    
                    if add_diamonds.collidepoint(pygame.mouse.get_pos()):
                        focus.play()

                    if play_clk or training_clk or store_clk or settings_clk or credits_clk or quit_clk:
                        if back_rect.collidepoint(pygame.mouse.get_pos()):
                            slide.play()
                            left = -680*xdim
                            play_clk = False
                            quit_clk = False

                    if quit_clk:
                        if q_yrect.collidepoint(pygame.mouse.get_pos()):
                            running = False
                            sys.exit()

                        if q_nrect.collidepoint(pygame.mouse.get_pos()):
                            slide.play()
                            left = -680*xdim
                            quit_clk = False

                    if not play_clk and not training_clk and not store_clk and not settings_clk and not credits_clk and not quit_clk and left >= 0:
                        if prect.collidepoint(pygame.mouse.get_pos()):
                            slide.play()
                            left = -680*xdim
                            play_clk = True
                        if trect.collidepoint(pygame.mouse.get_pos()):
                            slide.play()
                            left = -680*xdim
                            training_clk = True
                        if strect.collidepoint(pygame.mouse.get_pos()):
                            slide.play()
                            left = -680*xdim
                            store_clk = True
                        if serect.collidepoint(pygame.mouse.get_pos()):
                            slide.play()
                            left = -680*xdim
                            settings_clk = True
                        if crect.collidepoint(pygame.mouse.get_pos()):
                            slide.play()
                            left = -680*xdim
                            credits_clk = True
                        if qrect.collidepoint(pygame.mouse.get_pos()):
                            slide.play()
                            left = -680*xdim
                            quit_clk = True
                    
            if not play_clk and not training_clk and not store_clk and not settings_clk and not credits_clk and not quit_clk:
                play = menu_btn("PLAY", play_size)
                play_rct = play.get_rect()
                play_rct.center = left + 175*xdim, 81*ydim
                window.blit(play, (left + 175*xdim - play.get_width()/2, 81*ydim - play.get_height()/2))
                training = menu_btn("TRAINING", training_size)
                training_rct = training.get_rect()
                training_rct.center = left + 225*xdim, 231*ydim
                window.blit(training, (left + 225*xdim - training.get_width()/2, 231*ydim - training.get_height()/2))
                store = menu_btn("STORE", store_size)
                store_rct = store.get_rect()
                store_rct.center = left + 192*xdim, 381*ydim
                window.blit(store, (left + 192*xdim - store.get_width()/2, 381*ydim - store.get_height()/2))
                settings = menu_btn("TUTORIAL", settings_size)
                settings_rct = settings.get_rect()
                settings_rct.center = left + 226*xdim, 531*ydim
                window.blit(settings, (left + 226*xdim - settings.get_width()/2, 531*ydim - settings.get_height()/2))
                credits = menu_btn("EXTRAS", credits_size)
                credits_rct = credits.get_rect()
                credits_rct.center = left + 213*xdim, 681*ydim
                window.blit(credits, (left + 213*xdim - credits.get_width()/2, 681*ydim - credits.get_height()/2))
                quit = menu_btn("QUIT", quit_size)
                quit_rct = quit.get_rect()
                quit_rct.center = left + 175*xdim, 831*ydim
                window.blit(quit, (left + 175*xdim - quit.get_width()/2, 831*ydim - quit.get_height()/2))
                # print(f"Training {training.get_width()}, Store {store.get_width()} Settings {settings.get_width()} Credits {credits.get_width()}")

            if play_clk:
                window.blit(menu_btn("PLAY", int(100*xdim)), (left + 240*xdim, 200*ydim))
                back = self.back.get_rect()
                back.x, back.y = left + 6*xdim, 200*ydim
                window.blit(self.back, (left + 6*xdim, 200*ydim))
                single = menu_btn("SINGLE", single_size)
                single_rct = single.get_rect()
                single_rct.center = left + 225*xdim, 381*ydim
                window.blit(single, (left + 225*xdim - single.get_width()/2, 381*ydim - single.get_height()/2))
                mp = menu_btn("MULTIPLAYER", mp_size)
                mp_rct = mp.get_rect()
                mp_rct.center = left + 250*xdim, 531*ydim
                window.blit(mp, (left + 250*xdim - mp.get_width()/2, 531*ydim - mp.get_height()/2))

            if quit_clk:
                window.blit(menu_btn("QUIT?", int(100*xdim)), (left + 240*xdim, 200*ydim))
                back = self.back.get_rect()
                back.x, back.y = left + 6*xdim, 200*ydim
                window.blit(self.back, (left + 6*xdim, 200*ydim))
                yes = menu_btn("SURE", yes_size)
                yes_rct = yes.get_rect()
                yes_rct.center = left + 225*xdim, 381*ydim
                window.blit(yes, (left + 225*xdim - yes.get_width()/2, 381*ydim - yes.get_height()/2))
                no = menu_btn("NO", no_size)
                no_rct = no.get_rect()
                no_rct.center = left + 210*xdim, 531*ydim
                window.blit(no, (left + 210*xdim - no.get_width()/2, 531*ydim - no.get_height()/2))

            pygame.display.flip()
            self.clock.tick(40)

# loaded_images.append(pygame.image.load("mainmenu_plain.png"))
# loaded_images.append(pygame.image.load("sback.png"))
