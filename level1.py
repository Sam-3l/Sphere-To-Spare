import random, sys, pygame, math, datetime
window = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)

pygame.init()

loaded_images = []
loaded_sounds = []

class sprite(pygame.sprite.Sprite):
    def __init__(self, surface):
        super(sprite, self).__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def moveleft(self, distance):
        self.rect.x -= distance

    def moveright(self, distance):
        self.rect.x += distance

# settings, json files, controls
controls = {"left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "up": pygame.K_UP,
            "down": pygame.K_DOWN,
            "attack": pygame.K_x,
            "block": pygame.K_d,
            "jump": pygame.K_SPACE,
            "drop_pick_ball": pygame.K_c,
            "move_without_cam": pygame.K_a,
            "change_cursor": pygame.K_z,
            "special_skill": pygame.K_s
            }

class g_loading:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load('mountains.jpg')
        self.text = pygame.font.SysFont("Agency FB", 40, True)
        self.btext = pygame.font.SysFont("Agency FB", 80, True)
        self.mtext = pygame.font.SysFont("Agency FB", 50, True)
        self.ntext = pygame.font.SysFont("Agency FB", 45, True)

    def run(self, window):
        progress = 0
        work_prog = 0
        bar = 0
        percent_prog = 0
        game_assets = ["", "mountains.jpg", "standing.png",  "rock.png", "lobby.png", "lnd_rock.png", "ball.png", "with_ball.png", "enemy_male.png", "enemy_female.png", "enemy_male_ball.png", "enemy_female_ball.png", "lobby_landingpd.png", "mapchr.png", "enemymap.png", "redenemymap.png", "ballmp.png", "life.png", "life_cont.png", "life_bar.png", "grip.png", "grip_bar.png", "punch1.png", "punch2.png", "enemy_female_attack.png","enemy_female_ball_attack.png","enemy_male_attack.png","enemy_male_ball_attack.png", "map.png", "mapbg.png", "credenemymap.png", "cenemymap.png", "chrmap.png", "rock2.png", "lnd_rock2.png", "run1.png", "run2.png", "run3.png", "run4.png", "run5.png", "run6.png", "ball_run1.png", "ball_run2.png", "ball_run3.png", "ball_run4.png", "ball_run5.png", "ball_run6.png", "ball_punch1.png", "ball_punch2.png", "punch.wav", "wind.wav", "jump.wav", "landing.wav", "running.wav", "background1.wav", "finish_rock.png", "finish_flag.png", "finish_rock_lpd.png"]
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
            window.blit(self.btext.render("THE SUB-POLAR ALPINE", True, (0, 0, 255)), (90, 20))
            window.blit(self.ntext.render("The sub-polar alpine is a breathtaking and treacherous realm of icy", True, (0, 0, 100)), (130, 120))
            window.blit(self.ntext.render("peaks and untamed beauty. Its glaciers and landscapes create a mesmerizing", True, (0, 0, 100)), (130, 160))
            window.blit(self.ntext.render("backdrop for those brave enough to venture its embrace amidst the", True, (0, 0, 100)), (130, 200))
            window.blit(self.ntext.render("chilling winds and extreme conditions. Explore and discover its secrets!!", True, (0, 0, 100)), (130, 240))
            window.blit(self.text.render("CAUTION: Avoid ice falls, they freeze you!", True, (160, 0, 0)), (130, 290))
            window.blit(self.ntext.render("", True, (0, 0, 100)), (130, 280))            
            window.blit(self.mtext.render("MODE:   F2F", True, (0, 0, 255)), (1330, 30))
            window.blit(self.mtext.render("BOOSTS:", True, (0, 0, 255)), (90, 340))
            pygame.draw.rect(window, (0, 0, 100), pygame.Rect(130, 400, 400, 400))
            pygame.draw.rect(window, (0, 0, 100), pygame.Rect(540, 400, 400, 400))
            pygame.draw.rect(window, (0, 0, 100), pygame.Rect(953, 400, 400, 400))

            time = pygame.time.get_ticks()
            if time - initial < 2000 and asset != "":
                pygame.time.delay(2000)
            
            time = pygame.time.get_ticks()
            if time - initial >= 2000:
                pygame.time.delay(100)
                if asset.endswith(".png") or asset.endswith(".jpeg") or asset.endswith(".jpg"):
                    image = pygame.image.load(asset)
                    image.convert()
                    loaded_images.append(image)
                if asset.endswith(".wav"):
                    if asset == "background1.wav":
                        pygame.time.delay(100)
                        pygame.mixer.music.load(asset)
                        pygame.mixer.music.play()
                    else:
                        pygame.time.delay(100)
                        sound = pygame.mixer.Sound(asset)
                        loaded_sounds.append(sound)
                    
                work_prog += 1
                progress = work_prog/work
                bar = progress * 1396
                percent_prog = math.ceil(progress * 100) 
                pygame.draw.rect(window, (100, 100, 100), pygame.Rect(self.width/2 - 700, self.height - 30, 1400, 15), 2)
                pygame.draw.rect(window, (255, 255, 0), pygame.Rect(self.width/2 - 698, self.height - 28, bar, 11))
                window.blit(self.text.render("When opponents are distant, you can temporarily drop the ball to boost your grip", True, (200, 200, 0)), (100, 820))
                window.blit(self.text.render(f"{percent_prog}%", True, (100, 100, 100)), (1462, 820))

            pygame.display.flip()

            if progress >= 1:
                pygame.time.delay(200)
                game().run(window)
                return "done"
            
            self.clock.tick(40)

# just delete this
# for asset in ["mountains.jpg", "testcharacter.png",  "test.png", "lobby.png", "test2.png", "ball.png", "testcharacter_ball.png", "enemy_male.png", "enemy_female.png", "enemy_male_ball.png", "enemy_female_ball.png", "lobby_landingpd.png", "mapchr.png", "enemymap.png", "redenemymap.png", "ballmp.png", "life.png", "life_cont.png", "life_bar.png", "grip.png", "grip_bar.png", "testcharacter_attack.png", "testcharacter_ball_attack.png"]:
#     if asset.endswith(".png") or asset.endswith(".jpeg") or asset.endswith(".jpg"):
#         image = pygame.image.load(asset).convert()
#         loaded_images.append(image)

class game:
    def __init__(self):
        self.background = loaded_images[0]
        self.clock = pygame.time.Clock()
        
        self.init_y = random.randrange(550, 700)
        self.init_x = 715

        lobby_img = loaded_images[3]
        self.lobby_img = pygame.transform.scale(lobby_img, (1100, 500))
        self.lbblock = sprite(self.lobby_img)
        self.lbblock.rect.y = 400
        self.lbblock.rect.x = -420

        finish_img = loaded_images[48]
        self.finish_img = pygame.transform.scale(finish_img, (1100, 500))
        self.fblock = sprite(self.finish_img)

        self.flag = pygame.transform.scale(loaded_images[49], (300, 600))

        self.index = []
        ht = random.randrange(250, 400)
        i = random.choice((2, 32))
        self.blk_img = pygame.transform.scale(loaded_images[i], (ht, 140 + (ht - 250) * 0.4))
        self.index.append(i)
        self.blk_img.set_colorkey((0, 255, 0))
        self.block = sprite(self.blk_img)
        self.block.rect.y = self.init_y
        self.block.rect.x = self.init_x
        self.g_block = pygame.sprite.Group(self.lbblock, self.block)

        self.chr_x = 0
        self.chr_y = 0

    def run(self, window):
        runn = 34
        rtm = 0
        life = 1
        grip = 1
        rlife = 3
        attacked = False
        mpclk = False
        init_width = self.blk_img.get_width()
        width, height = window.get_size()
        self.background = pygame.transform.scale(self.background, (width * 1.2, height))
        self.background2 = self.background
        self.background0 = self.background
        start = 0
        running = True
        jump = False
        rnd = 1

        # run starts from 34
        chr_img1 = pygame.transform.scale(loaded_images[1], (240, 380))
        chr_img1ball = pygame.transform.scale(loaded_images[6], (240, 380))
        chr_img2 = pygame.transform.flip(chr_img1, True, False)
        chr_img2ball = pygame.transform.flip(chr_img1ball, True, False)
        chr_img = chr_img1

        emale_img1 = pygame.transform.scale(loaded_images[7], (140, 300))
        emale_img1_att = pygame.transform.scale(loaded_images[25], (140, 300))
        emale_img1ball = pygame.transform.scale(loaded_images[9], (160, 300))
        emale_img1ball_att = pygame.transform.scale(loaded_images[26], (160, 300))
        emale_img2 = pygame.transform.flip(emale_img1, True, False)
        emale_img2_att = pygame.transform.flip(emale_img1_att, True, False)
        emale_img2ball = pygame.transform.flip(emale_img1ball, True, False)
        emale_img2ball_att = pygame.transform.flip(emale_img1ball_att, True, False)
        emale_img1.set_colorkey((255, 255, 255))
        emale_img2.set_colorkey((255, 255, 255))
        emale_img1_att.set_colorkey((255, 255, 255))
        emale_img2_att.set_colorkey((255, 255, 255))
        emale_img1ball.set_colorkey((0, 0, 0))
        emale_img2ball.set_colorkey((0, 0, 0))
        emale_img1ball_att.set_colorkey((0, 0, 0))
        emale_img2ball_att.set_colorkey((0, 0, 0))
        
        efemale_img1 = pygame.transform.scale(loaded_images[8], (140, 300))
        efemale_img1_att = pygame.transform.scale(loaded_images[23], (140, 300))
        efemale_img1ball = pygame.transform.scale(loaded_images[10], (160, 300))
        efemale_img1ball_att = pygame.transform.scale(loaded_images[24], (160, 300)) 
        efemale_img2 = pygame.transform.flip(efemale_img1, True, False)
        efemale_img2_att = pygame.transform.flip(efemale_img1_att, True, False)
        efemale_img2ball = pygame.transform.flip(efemale_img1ball, True, False)
        efemale_img2ball_att = pygame.transform.flip(efemale_img1ball_att, True, False)
        efemale_img1.set_colorkey((255, 255, 255))
        efemale_img2.set_colorkey((255, 255, 255))
        efemale_img1_att.set_colorkey((255, 255, 255))
        efemale_img2_att.set_colorkey((255, 255, 255))
        efemale_img1ball.set_colorkey((0, 0, 0))
        efemale_img2ball.set_colorkey((0, 0, 0))
        efemale_img1ball_att.set_colorkey((0, 0, 0))
        efemale_img2ball_att.set_colorkey((0, 0, 0))
        
        right = left = True
 
        ball_img = pygame.transform.scale(loaded_images[5], (72, 65))
        ball_img.set_colorkey((255, 255, 255))

        # top widgets
        chrmp = pygame.transform.scale(loaded_images[12], (60, 60))
        chrmp.set_colorkey((255, 255, 255))
        emp = pygame.transform.scale(loaded_images[13], (60, 60))
        emp.set_colorkey((255, 255, 255))
        remp = pygame.transform.scale(loaded_images[14], (60, 60))
        remp.set_colorkey((255, 255, 255))
        ballmp = pygame.transform.scale(loaded_images[15], (50, 30))
        ballmp.set_colorkey((0, 0, 0))

        life_img = pygame.transform.scale(loaded_images[16], (86, 52))
        life_img.set_colorkey((255, 255, 255))
        life_cont = pygame.transform.scale(loaded_images[17], (450, 35))
        life_cont.set_colorkey((255, 255, 255))

        grip_img = pygame.transform.scale(loaded_images[19], (60, 55))
        grip_cont = pygame.transform.scale(loaded_images[17], (420, 35))
        grip_cont.set_colorkey((255, 255, 255))

        map_img = pygame.transform.scale(loaded_images[27], (1400, 200))
        map_bg = pygame.transform.scale(loaded_images[28], (1500, 600))
        map_bg.set_alpha(100)
        map_bg.convert_alpha()

        create_blocks = True
        while create_blocks:
            ht = random.randrange(250, 400)
            i = random.choice((2, 32))
            self.blk_img = pygame.transform.scale(loaded_images[i], (ht, 120 + (ht - 250) * 0.4))
            self.index.append(i)
            self.blk_img.set_colorkey((0, 255, 0))
            self.blk = sprite(self.blk_img)
            self.blk.rect.x = self.init_x + random.randrange(init_width + 30, init_width + 130)
            if self.init_y <= 400:
                # add only down
                self.blk.rect.y = random.randrange(self.init_y, self.init_y + 210)
            else:
                # add up and down
                if self.init_y + 210 <= height - self.blk_img.get_height():
                    self.blk.rect.y = random.randrange(self.init_y - 210, self.init_y + 210)
                else:
                    self.blk.rect.y = random.randrange(self.init_y - 210, height - self.blk_img.get_height())
                # height - self.blk_img.get_height() --lowest
            
            if len(self.g_block) < 20:
                self.g_block.add(self.blk)
            elif len(self.g_block) == 20:
                self.fblock.rect.x = self.init_x + init_width + 90
                self.fblock.rect.y = 400
                self.g_block.add(self.fblock)
            else:
                create_blocks = False
            self.init_x = self.blk.rect.x
            self.init_y = self.blk.rect.y
            init_width = self.blk_img.get_width()
        
        st = 0
        th = 0
        kills = 0
        died = justresp = False
        climb = False
        stt = 1
        for objs in self.g_block:
            if stt == len(self.g_block):
                game_distance = objs.rect.x + objs.image.get_width() - 800
            stt += 1
        game_distance_m = 200

        self.landing_pad = pygame.sprite.Group()
        x = 0
        landed = False
        ball_x, ball_y = 900, 0

        game_won = None

        punch = loaded_sounds[0]
        em_punch = loaded_sounds[1]
        jumpsnd = loaded_sounds[2]
        land = loaded_sounds[3]
        run = loaded_sounds[4]
        
        # create landing pads
        ind = 0
        for blk in self.g_block:
            if blk == self.lbblock:
                lbypd = loaded_images[11] 
                lbypd = pygame.transform.scale(lbypd, (blk.image.get_width(), blk.image.get_height()))
                lbypd.set_colorkey((0, 255, 0))
                lpad = sprite(lbypd)
                lpad.rect.y = blk.rect.y + 5
                lpad.rect.x = blk.rect.x
                self.landing_pad.add(lpad)
            elif blk == self.fblock:
                fnpad = loaded_images[50]
                fnpad = pygame.transform.scale(fnpad, (blk.image.get_width(), blk.image.get_height()))
                fnpad.set_colorkey((0, 255, 0))
                fpad = sprite(fnpad)
                fpad.rect.y = blk.rect.y + 5
                fpad.rect.x = blk.rect.x
                self.landing_pad.add(fpad)
            else:
                if self.index[ind] == 2:
                    lpd = loaded_images[4]
                elif self.index[ind] == 32:
                    lpd = loaded_images[33]
                lpd = pygame.transform.scale(lpd, (blk.image.get_width(), blk.image.get_height()))
                lpd.set_colorkey((0, 255, 0))
                pad = sprite(lpd)
                pad.rect.y = blk.rect.y
                pad.rect.x = blk.rect.x
                self.landing_pad.add(pad)
                ind += 1

        with_ball = False
        en_with_ball = [False, False, False]
        e_jump = [False, False, False]
        e_attacked = [False, False, False]
        e_top = [0, 0, 0]
        en_progress = [0, 0, 0]
        e_life, e_grip = [1, 1, 1], [1, 1, 1]
        sus = [0, 0, 0]

        self.menemy = sprite(emale_img1)
        self.fenemy = sprite(efemale_img1)
        self.renemy = sprite(random.choice((emale_img1, efemale_img1)))
        self.menemy.rect.x = 150
        self.menemy.rect.y = 0
        self.fenemy.rect.x = 200
        self.fenemy.rect.y = 0
        self.renemy.rect.x = 250
        self.renemy.rect.y = 0
        
        chr_img2_run = pygame.transform.flip(pygame.transform.scale(loaded_images[runn], (240, 380)), True, False)
        chr_img1_run = pygame.transform.scale(loaded_images[runn], (240, 380))

        chr_img1_att = pygame.transform.scale(loaded_images[21], (240, 300))
        chr_img2_att = pygame.transform.flip(chr_img1_att, True, False)
        while running:
            # background
            window.fill((0, 0, 0))
            window.blit(self.background, (x, 0))
            window.blit(self.background2, (x + width * 1.2, 0))
            window.blit(self.background0, (x - width * 1.2, 0))

            life_bar = pygame.transform.scale(loaded_images[18], (450 * life, 35))
            life_bar.set_colorkey((255, 255, 255))
            grip_bar = pygame.transform.scale(loaded_images[20], (420 * grip, 35))
            grip_bar.set_colorkey((255, 255, 255))
            
            self.character = sprite(chr_img)
            self.character.rect.x = self.chr_x
            self.character.rect.y = self.chr_y

            enemies = pygame.sprite.Group(self.menemy, self.fenemy, self.renemy)    

            if not with_ball and True not in en_with_ball:
                self.ball = sprite(ball_img)
                self.ball.rect.x = ball_x
                self.ball.rect.y = ball_y
                ball_grp = pygame.sprite.Group(self.ball)

            self.all_sprites = pygame.sprite.Group(enemies, self.character, ball_grp, self.landing_pad, self.g_block)

            for objs in self.g_block:
                start = objs.rect.x + 420
                break
            window.blit(self.flag, (game_distance + start, 0))

            if pygame.sprite.spritecollide(self.character, self.g_block, False, pygame.sprite.collide_mask) and not landed:
                if 0 < pygame.sprite.spritecollide(self.character, self.g_block, False, pygame.sprite.collide_mask)[0].rect.x - 100 <= self.chr_x:
                    right = False
                else:
                    right = True
                if 0 < self.chr_x - pygame.sprite.spritecollide(self.character, self.g_block, False, pygame.sprite.collide_mask)[0].image.get_width() <= pygame.sprite.spritecollide(self.character, self.g_block, False, pygame.sprite.collide_mask)[0].rect.x:
                    left = False
                else:
                    left = True
            else:
                right = left = True

            key = pygame.key.get_pressed()
            if key[controls["left"]] and not died:
                if (chr_img == chr_img2 or chr_img == chr_img2ball or chr_img == chr_img2_run) and left:
                    if not with_ball:
                        if landed:
                            if rtm == 0:
                                rtm = pygame.time.get_ticks()
                            if runn > 39:
                                runn = 34
                            if runn < 39 and pygame.time.get_ticks() - rtm >= 100:
                                runn += 1
                                rtm = pygame.time.get_ticks()
                            elif runn == 39 and pygame.time.get_ticks() - rtm >= 100:
                                runn = 36
                                rtm = pygame.time.get_ticks()
                        else:
                            runn = 35

                    else:
                        if landed:
                            if rtm == 0:
                                rtm = pygame.time.get_ticks()
                            if runn < 40:
                                runn = 40
                            if runn < 45 and pygame.time.get_ticks() - rtm >= 100:
                                runn += 1
                                rtm = pygame.time.get_ticks()
                            elif runn == 45 and pygame.time.get_ticks() - rtm >= 100:
                                runn = 42
                                rtm = pygame.time.get_ticks()
                        else:
                            runn = 41
                        
                    chr_img2_run = pygame.transform.flip(pygame.transform.scale(loaded_images[runn], (240, 380)), True, False)
                    chr_img = chr_img2_run
                    if self.character.rect.x < 600:
                        self.chr_x -= 5
                    else:
                        x += 5
                        ball_x += 5
                        for enemy in enemies:
                            enemy.moveright(5)
                        for block in self.g_block:
                            block.moveright(5)
                        for pad in self.landing_pad:
                            pad.moveright(5)
                else:
                    if with_ball:
                        chr_img = chr_img2ball
                    else:
                        chr_img = chr_img2
            else:
                if chr_img == chr_img2_run:
                    if with_ball:
                        chr_img = chr_img2ball
                    else:
                        chr_img = chr_img2
                    rtm = 0
                    runn = 34

            if key[controls["right"]] and not died:
                if (chr_img == chr_img1 or chr_img == chr_img1ball or chr_img == chr_img1_run) and right:
                    if not with_ball:
                        if landed:
                            if rtm == 0:
                                rtm = pygame.time.get_ticks()
                            if runn > 39:
                                runn = 34
                            if runn < 39 and pygame.time.get_ticks() - rtm >= 100:
                                runn += 1
                                rtm = pygame.time.get_ticks()
                            elif runn == 39 and pygame.time.get_ticks() - rtm >= 100:
                                runn = 36
                                rtm = pygame.time.get_ticks()
                        else:
                            runn = 35

                    else:
                        if landed:
                            if rtm == 0:
                                rtm = pygame.time.get_ticks()
                            if runn < 40:
                                runn = 40
                            if runn < 45 and pygame.time.get_ticks() - rtm >= 100:
                                runn += 1
                                rtm = pygame.time.get_ticks()
                            elif runn == 45 and pygame.time.get_ticks() - rtm >= 100:
                                runn = 42
                                rtm = pygame.time.get_ticks()
                        else:
                            runn = 41

                    chr_img1_run = pygame.transform.scale(loaded_images[runn], (240, 380))
                    chr_img = chr_img1_run
                    if self.character.rect.x < 600:
                        self.chr_x += 5
                    else:
                        x -= 5
                        ball_x -= 5
                        for enemy in enemies:
                            enemy.moveleft(5)
                        for block in self.g_block:
                            block.moveleft(5)
                        for pad in self.landing_pad:
                            pad.moveleft(5)
                else:
                    if with_ball:
                       chr_img = chr_img1ball
                    else:
                       chr_img = chr_img1
            else:
                if chr_img == chr_img1_run:
                    if with_ball:
                        chr_img = chr_img1ball
                    else:
                        chr_img = chr_img1
                    rtm = 0
                    runn = 34

            if chr_img == chr_img1_run:
                if not landed:
                    run.stop()
                    th = 0
                elif th == 0:
                    run.play()
                    th = 1
            elif chr_img == chr_img2_run:
                if not landed:
                    run.stop()
                    th = 0
                elif th == 0:
                    run.play()
                    th = 1
            else:
                run.stop()
                th = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

                if event.type == pygame.KEYUP:
                    if event.key == controls["drop_pick_ball"]:
                        if with_ball: 
                            with_ball = False
                        else:
                            if pygame.sprite.spritecollide(self.character, ball_grp, False, pygame.sprite.collide_mask) and self.ball.alive():
                                with_ball = True

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    try:
                        if map.collidepoint(pygame.mouse.get_pos()):
                            mpclk = True
                    except:
                        pass
                    try:
                        if close.collidepoint(pygame.mouse.get_pos()):
                            mpclk = False
                    except:
                        pass

            if x <= -1.2 * width:
                x = x + width * 1.2
            if  x >= width:
                x = x - width * 1.2

            if with_ball:
                self.ball.kill()
                ball_x = self.character.rect.x + 60
                ball_y = self.character.rect.y
                if chr_img == chr_img1:
                    chr_img = chr_img1ball
                elif chr_img == chr_img2:
                    chr_img = chr_img2ball     
            else:
                if chr_img == chr_img1ball:
                    chr_img = chr_img1
                elif chr_img == chr_img2ball:
                    chr_img = chr_img2

            player_distance = self.character.rect.x
            progress = (player_distance - start)/game_distance

            ball_distance = ball_x
            bprogress = (ball_distance - start)/game_distance
            # window.blit(pygame.font.SysFont(None, 100).render(f"Progress in percent is: {math.ceil(100 * progress)}%", True, (0, 0, 0), (255, 255, 255)), (0, 0))
            
            if pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask) and pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.y - self.character.rect.y >= 250 and pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].image != lbypd and pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].image != fnpad:    
                landed = True
                climb = False
            elif pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask) and pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.y - self.character.rect.y >= -70 and pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].image == lbypd:                    
                landed = True
                if pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.x + 720 <= self.character.rect.x <= pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.x + 850:
                    climb = True
                else:
                    climb = False
            elif pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask) and pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.y - self.character.rect.y >= 100 and pygame.sprite.spritecollide(self.character, self.landing_pad, False, pygame.sprite.collide_mask)[0].image == fnpad:
                landed = True
            else:
                landed = False

            if climb and key[controls["left"]] and landed:
                self.chr_y -= 10

            def en_landed(emy):
                if pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask) and pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.y - emy.rect.y >= 200 and pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask)[0].image != lbypd and pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask)[0].image != fnpad:    
                    return True
                elif pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask) and pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.y - emy.rect.y >= -100 and pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask)[0].image == lbypd:
                    return True
                elif pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask) and pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.y - emy.rect.y >= 100 and pygame.sprite.spritecollide(emy, self.landing_pad, False, pygame.sprite.collide_mask)[0].image == fnpad:
                    return True
                else:
                    return False

            if pygame.sprite.spritecollide(self.ball, self.landing_pad, False, pygame.sprite.collide_mask) and pygame.sprite.spritecollide(self.ball, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.y - self.ball.rect.y >= 0:    
                ball_landed = True
            else:
                ball_landed = False

            if landed:
                if key[controls["jump"]]:
                    jumpsnd.play()
                    top = self.chr_y
                    jump = True

            if jump:
                if top - self.chr_y <= 250:
                    self.chr_y -= 10
                else:
                    jump = False
                    rnd = 0

            if not landed and not jump:
                self.chr_y += 10
                
            if landed and rnd == 0:
                land.play()
                rnd = 1

            if self.chr_y >= 800 and st == 0:
                st = pygame.time.get_ticks()

            if self.chr_y >= 800:
                if not died:
                    rlife -= 1
                    if with_ball:
                        ball_x += 140
                        ball_y = 0
                        with_ball = False
                died = True
                for block in self.g_block:
                    if block.rect.x < -570:
                        x += 200
                        ball_x += 200
                        for enemy in enemies:
                            enemy.moveright(200)
                        for block in self.g_block:
                            block.moveright(200)
                        for pad in self.landing_pad:
                            pad.moveright(200)
                    break

                if pygame.time.get_ticks() - st >= 2000:
                    life = 1
                    grip = 1
                    self.chr_x = 50
                    self.chr_y = 0
                    died = False
                    rspn_time = f"Respawned {datetime.datetime.now().strftime('%H:%M:%S')}"
                    justresp = True
                    st2 = pygame.time.get_ticks()
                    st = 0
                else:
                    window.blit(pygame.font.SysFont(None, 40).render("Respawning...", True, (255, 255, 255)), (1390, 850))

            if justresp:
                window.blit(pygame.font.SysFont(None, 40).render(rspn_time, True, (255, 255, 255)), (1300, 850))
                if pygame.time.get_ticks() - st2 >= 1000:
                    justresp = False
            
            # enemies loop
            en_index = 0
            for enemy in enemies:
                en_distance = enemy.rect.x
                en_progress[en_index] = (en_distance - start)/game_distance
                if en_progress[en_index] < 1:
                    if ball_x >= enemy.rect.x:
                        if enemy.image == emale_img2:
                            enemy.image = emale_img1
                        elif enemy.image == emale_img2ball:
                            enemy.image = emale_img1ball
                        if enemy.image == efemale_img2:
                            enemy.image = efemale_img1
                        elif enemy.image == efemale_img2ball:
                            enemy.image = efemale_img1ball
                        if enemy.image == emale_img2_att:
                            enemy.image = emale_img1_att
                        elif enemy.image == emale_img2ball_att:
                            enemy.image = emale_img1ball_att
                        if enemy.image == efemale_img2_att:
                            enemy.image = efemale_img1_att
                        elif enemy.image == efemale_img2ball_att:
                            enemy.image = efemale_img1ball_att
                        if with_ball and not en_with_ball[en_index] and abs(enemy.rect.x - ball_x) <= 100 and en_landed(enemy):
                            pass
                        else:
                            if en_with_ball[en_index]:
                                enemy.rect.x += random.choice((5, 5, 4, 0))
                            else:
                                if True in en_with_ball and abs(enemy.rect.x - ball_x) <= 140:
                                    enemy.rect.x += 3
                                elif True in en_with_ball and abs(enemy.rect.x - ball_x) <= 600:
                                    enemy.rect.x += random.choice((5, 5, 4, 0))
                                else:
                                    if en_index == 0:
                                        enemy.rect.x += random.choice((5, 4, 5, 5, 5))
                                    elif en_index == 1:
                                        enemy.rect.x += random.choice((5, 4, 5, 4))
                                    else:
                                        enemy.rect.x += random.choice((5, 3, 5, 5, 5))
                    else:
                        if enemy.image == emale_img1:
                            enemy.image = emale_img2
                        elif enemy.image == emale_img1ball:
                            enemy.image = emale_img2ball
                        if enemy.image == efemale_img1:
                            enemy.image = efemale_img2
                        elif enemy.image == efemale_img1ball:
                            enemy.image = efemale_img2ball
                        if enemy.image == emale_img1_att:
                            enemy.image = emale_img2_att
                        elif enemy.image == emale_img1ball_att:
                            enemy.image = emale_img2ball_att
                        if enemy.image == efemale_img1_att:
                            enemy.image = efemale_img2_att
                        elif enemy.image == efemale_img1ball_att:
                            enemy.image = efemale_img2ball_att
                        if with_ball and not en_with_ball[en_index] and abs(enemy.rect.x - ball_x) <= 100 and en_landed(enemy):
                            pass
                        else:
                            if en_with_ball[en_index]:
                                enemy.rect.x -= random.choice((5, 5, 4, 0))
                            else:
                                if True in en_with_ball and abs(enemy.rect.x - ball_x) <= 140:
                                    enemy.rect.x -= 3
                                elif True in en_with_ball and abs(enemy.rect.x - ball_x) <= 600:
                                    enemy.rect.x -= random.choice((5, 5, 4, 0))
                                else:
                                    if en_index == 0:
                                        enemy.rect.x -= random.choice((5, 4, 5, 5, 5))
                                    elif en_index == 1:
                                        enemy.rect.x -= random.choice((5, 4, 5, 4))
                                    else:
                                        enemy.rect.x -= random.choice((5, 3, 5, 5, 5))
                
                    if not random.randrange(0, 500) and abs(enemy.rect.x - self.chr_x) <= 300 and sus[en_index] == 0:
                        sus[en_index] = pygame.time.get_ticks()

                    if with_ball and not en_with_ball[en_index] and abs(enemy.rect.x - ball_x) <= 300:
                        e_attacked[en_index] = True
                        sus[en_index] = 0
                    else:
                        e_attacked[en_index] = False
                        
                    if pygame.time.get_ticks() - sus[en_index] >= 1000:
                        if sus[en_index] != 0:
                            e_attacked[en_index] = False
                            sus[en_index] = 0
                    else:
                        if sus[en_index] != 0:
                            e_attacked[en_index] = True

                    if pygame.sprite.spritecollide(enemy, ball_grp, False, pygame.sprite.collide_mask) and self.ball.alive():
                        en_with_ball[en_index] = True
                
                else:
                    e_attacked[en_index] = False

                if e_attacked[en_index]:
                    if pygame.sprite.spritecollide(enemy, pygame.sprite.Group(self.character), False, pygame.sprite.collide_mask):
                        life -= 1/2000
                        if with_ball:
                            grip -= 1/500
                        
                    if grip <= 0:
                        en_with_ball[en_index] = True
                        with_ball = False
                        grip = 0
                        
                    if life <= 0:
                        life = 0

                    if enemy.image == emale_img1:
                        enemy.image = emale_img1_att
                    if enemy.image == emale_img1ball:
                        enemy.image = emale_img1ball_att
                    if enemy.image == efemale_img1:
                        enemy.image = efemale_img1_att
                    if enemy.image == efemale_img1ball:
                        enemy.image = efemale_img1ball_att
                    if enemy.image == emale_img2:
                        enemy.image = emale_img2_att
                    if enemy.image == emale_img2ball:
                        enemy.image = emale_img2ball_att
                    if enemy.image == efemale_img2:
                        enemy.image = efemale_img2_att
                    if enemy.image == efemale_img2ball:
                        enemy.image = efemale_img2ball_att
                else:
                    if enemy.image == emale_img1_att:
                        enemy.image = emale_img1 
                    if enemy.image == emale_img1ball_att:
                        enemy.image = emale_img1ball
                    if enemy.image == efemale_img1_att:
                        enemy.image = efemale_img1
                    if enemy.image == efemale_img1ball_att:
                        enemy.image = efemale_img1ball
                    if enemy.image == emale_img2_att:
                        enemy.image = emale_img2
                    if enemy.image == emale_img2ball_att:
                        enemy.image = emale_img2ball
                    if enemy.image == efemale_img2_att:
                        enemy.image = efemale_img2
                    if enemy.image == efemale_img2ball_att:
                        enemy.image = efemale_img2ball

                if not en_landed(enemy) and not e_jump[en_index]:
                    enemy.rect.y += 10

                if en_with_ball[en_index]:
                    self.ball.kill()
                    ball_x = enemy.rect.x
                    ball_y = enemy.rect.y
                    if enemy.image == emale_img1:
                        enemy.image = emale_img1ball
                    elif enemy.image == emale_img2:
                        enemy.image = emale_img2ball
                    elif enemy.image == efemale_img1:
                        enemy.image = efemale_img1ball
                    elif enemy.image == efemale_img2:
                        enemy.image = efemale_img2ball
                    if enemy.image == emale_img1_att:
                        enemy.image = emale_img1ball_att
                    elif enemy.image == emale_img2_att:
                        enemy.image = emale_img2ball_att
                    elif enemy.image == efemale_img1_att:
                        enemy.image = efemale_img1ball_att
                    elif enemy.image == efemale_img2_att:
                        enemy.image = efemale_img2ball_att
                else:
                    if enemy.image == emale_img1ball:
                        enemy.image = emale_img1
                    elif enemy.image == emale_img2ball:
                        enemy.image = emale_img2
                    if enemy.image == efemale_img1ball:
                        enemy.image = efemale_img1
                    elif enemy.image == efemale_img2ball:
                        enemy.image = efemale_img2
                    if enemy.image == emale_img1ball_att:
                        enemy.image = emale_img1_att
                    elif enemy.image == emale_img2ball_att:
                        enemy.image = emale_img2_att
                    if enemy.image == efemale_img1ball_att:
                        enemy.image = efemale_img1_att
                    elif enemy.image == efemale_img2ball_att:
                        enemy.image = efemale_img2_att

                if en_landed(enemy):
                    if enemy.image == emale_img1 or enemy.image == emale_img1ball or enemy.image == efemale_img1 or enemy.image == efemale_img1ball or enemy.image == emale_img1_att or enemy.image == emale_img1ball_att or enemy.image == efemale_img1_att or enemy.image == efemale_img1ball_att:
                        if pygame.sprite.spritecollide(enemy, self.landing_pad, False, pygame.sprite.collide_mask)[0].image != lbypd:
                            if pygame.sprite.spritecollide(enemy, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.x + pygame.sprite.spritecollide(enemy, self.landing_pad, False, pygame.sprite.collide_mask)[0].image.get_width() - 90 <= enemy.rect.x:
                                e_top[en_index] = enemy.rect.y
                                e_jump[en_index] = True
                        else:
                            if pygame.sprite.spritecollide(enemy, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.x + pygame.sprite.spritecollide(enemy, self.landing_pad, False, pygame.sprite.collide_mask)[0].image.get_width() - 200 <= enemy.rect.x:
                                e_top[en_index] = enemy.rect.y
                                e_jump[en_index] = True

                    if enemy.image == emale_img2 or enemy.image == emale_img2ball or enemy.image == efemale_img2 or enemy.image == efemale_img2ball or enemy.image == emale_img2_att or enemy.image == emale_img2ball_att or enemy.image == efemale_img2_att or enemy.image == efemale_img2ball_att:
                        if pygame.sprite.spritecollide(enemy, self.landing_pad, False, pygame.sprite.collide_mask)[0].rect.x >= enemy.rect.x:
                            e_top[en_index] = enemy.rect.y
                            e_jump[en_index] = True
                        
                # jump and others

                if e_jump[en_index]:
                    if e_top[en_index] - enemy.rect.y <= 250:
                        enemy.rect.y -= 10
                    else:
                        e_jump[en_index] = False

                if enemy.rect.y >= 800:
                    if en_with_ball[en_index]:
                        ball_x += 140
                        ball_y = 0
                        en_with_ball[en_index] = False

                    for bk in self.g_block:
                        enemy.rect.x = bk.rect.x + 430
                        enemy.rect.y = 0
                        e_life[en_index] = 1
                        e_grip[en_index] = 1
                        break

                if e_life[en_index] <= 0:
                    if en_with_ball[en_index]:
                        en_with_ball[en_index] = False

                    for bk in self.g_block:
                        enemy.rect.x = bk.rect.x + 430
                        enemy.rect.y = 0
                        e_life[en_index] = 1
                        e_grip[en_index] = 1
                        break
                    kills += 1

                if e_grip[en_index] <= 0 and en_with_ball[en_index]:
                    en_with_ball[en_index] = False
                    with_ball = True
                    e_grip[en_index] = 0

                if not en_with_ball[en_index]:
                    if e_grip[en_index] < 1:
                        e_grip[en_index] += 1/1000

                # end mark
                en_index += 1

            tk = 0
            for x in en_with_ball:
                if x == True:
                    if len(en_with_ball) > tk + 1:
                        for y in range(tk+1, len(en_with_ball)):
                            en_with_ball[y] = False
                    break
                tk += 1

            if life <= 0 and st == 0:
                st = pygame.time.get_ticks()

            if life <= 0:
                if with_ball:
                    with_ball = False
                self.chr_y = height + 100

            if not with_ball:
                if grip < 1:
                    grip += 1/1000

            if ball_y >= 860:
                ball_x += 140
                ball_y = 0

            # map
            if not mpclk:
                map = pygame.draw.rect(window, (255, 255, 0), pygame.Rect(550, 0, 500, 70), border_bottom_left_radius=50, border_bottom_right_radius=50)
                window.blit(pygame.font.SysFont(None, 40).render("MAP", True, (0, 0, 0)), (760, 4))
                pygame.draw.rect(window, (0, 0, 0), pygame.Rect(580, 45, 440, 4))
                if en_with_ball[0]:
                    window.blit(remp, (560 + en_progress[0] * 420, 8))
                else:
                    window.blit(emp, (560 + en_progress[0] * 420, 8))
                if en_with_ball[1]:
                    window.blit(remp, (560 + en_progress[1] * 420, 8))
                else:
                    window.blit(emp, (560 + en_progress[1] * 420, 8))
                if en_with_ball[2]:
                    window.blit(remp, (560 + en_progress[2] * 420, 8))
                else:
                    window.blit(emp, (560 + en_progress[2] * 420, 8))
                if self.ball.alive():
                    window.blit(ballmp, (560 + bprogress * 420, 30))
                window.blit(chrmp, (560 + progress * 420, 8))

            # life and grip
            window.blit(pygame.font.SysFont(None, 30, True).render(f"KILLS: {kills}", True, (0, 0, 0)), (60, 0))
            window.blit(life_bar, (55, 20))
            window.blit(life_cont, (55, 20))
            window.blit(life_img, (-14, 14))
            window.blit(grip_bar, (55, 70))
            window.blit(grip_cont, (55, 70))
            window.blit(grip_img, (-5, 60))

            # right wing, respawn life or time, and dist left
            for rl in range(rlife):
                window.blit(life_img, (1500-50*rl, 4))
            pygame.draw.line(window, (0, 0, 0), (1286, 55), (1600, 55), 3)
            window.blit(pygame.font.SysFont("Arial", 40).render(f"Distance left: {max(int(200 - progress*200), 0)}m", True, (0, 0, 0)), (1300, 55))
            pygame.draw.line(window, (0, 0, 0), (1286, 103), (1600, 103), 3)

            if key[controls["attack"]]:
                if attacked == False:
                    tme = pygame.time.get_ticks()
                    if with_ball:
                        pch = 46
                    else:
                        pch = 21
                    attacked = True
                    if pygame.sprite.spritecollide(self.character, enemies, False, pygame.sprite.collide_mask):
                        punch.play()
                    else:
                        em_punch.play()
                if pygame.time.get_ticks() - tme >= 200:
                    attacked = None
            else:
                attacked = False

            if attacked:
                if pygame.sprite.spritecollide(self.character, enemies, False, pygame.sprite.collide_mask):
                    gz = 0
                    for en in enemies:
                        if en in pygame.sprite.spritecollide(self.character, enemies, False, pygame.sprite.collide_mask):
                            e_life[gz] -= 1/200
                            if en_with_ball[gz]:
                                e_grip[gz] -= 1/50
                        gz += 1
                
                if not with_ball:
                    if chr_img == chr_img1 or chr_img == chr_img1_run or chr_img == chr_img1_att:
                        chr_img1_att = pygame.transform.scale(loaded_images[pch], (240, 380))
                        chr_img = chr_img1_att
                    elif chr_img == chr_img2 or chr_img == chr_img2_run or chr_img == chr_img2_att:
                        chr_img2_att = pygame.transform.flip(pygame.transform.scale(loaded_images[pch], (240, 380)), True, False)
                        chr_img = chr_img2_att
                else:
                    if chr_img == chr_img1ball or chr_img == chr_img1_run or chr_img == chr_img1_att:
                        chr_img = chr_img1_att = pygame.transform.scale(loaded_images[pch], (240, 380))
                        chr_img = chr_img1_att
                    elif chr_img == chr_img2ball or chr_img == chr_img2_run or chr_img == chr_img2_att:
                        chr_img2_att = pygame.transform.flip(pygame.transform.scale(loaded_images[pch], (240, 380)), True, False)
                        chr_img = chr_img2_att

                if with_ball:
                    pch = 47
                else:
                    pch = 22

            else:
                if not with_ball:
                    if chr_img == chr_img1_att:
                        chr_img = chr_img1
                    elif chr_img == chr_img2_att:
                        chr_img = chr_img2
                else:
                    if chr_img == chr_img1_att:
                        chr_img = chr_img1ball
                    elif chr_img == chr_img2_att:
                        chr_img = chr_img2ball

            if not ball_landed:
                ball_y += 10

            a = 0
            for ast in enemies:
                pygame.draw.rect(window, (255, 0, 0), pygame.Rect(ast.rect.x + 2, ast.rect.y - 13, 100 * e_life[a] - 4, 11))
                pygame.draw.rect(window, (255, 255, 0), pygame.Rect(ast.rect.x + 2, ast.rect.y - 13, 100 * e_grip[a] - 4, 11), 2)
                a += 1

            self.all_sprites.update()
            self.all_sprites.draw(window)
            
            if ball_x < -100:
                if True in en_with_ball:
                    pointer = pygame.transform.rotate(pygame.transform.scale(loaded_images[14], (100, 100)), -90)
                    pointer.set_colorkey((255, 255, 255))
                    window.blit(pointer, (-10, 400))
                    window.blit(pygame.font.SysFont(None, 46).render(f"{math.ceil((progress - bprogress) * game_distance_m)}m", True, (255, 0, 0)), (0, 490))
                else:
                    pointer = pygame.transform.rotate(pygame.transform.scale(loaded_images[13], (100, 100)), -90)
                    pointer.set_colorkey((255, 255, 255))
                    window.blit(pointer, (-10, 400))
                    window.blit(pygame.font.SysFont(None, 46).render(f"{math.ceil((progress - bprogress) * game_distance_m)}m", True, (255, 255, 0)), (0, 490))

            if ball_x > 1600:
                if True in en_with_ball:
                    pointer = pygame.transform.rotate(pygame.transform.scale(loaded_images[14], (100, 100)), 90)
                    pointer.set_colorkey((255, 255, 255))
                    window.blit(pointer, (1512, 400))
                    window.blit(pygame.font.SysFont(None, 46).render(f"{math.ceil((bprogress - progress) * game_distance_m)}m", True, (255, 0, 0)), (1520, 490))
                else:
                    pointer = pygame.transform.rotate(pygame.transform.scale(loaded_images[13], (100, 100)), 90)
                    pointer.set_colorkey((255, 255, 255))
                    window.blit(pointer, (1512, 400))
                    window.blit(pygame.font.SysFont(None, 46).render(f"{math.ceil((bprogress - progress) * game_distance_m)}m", True, (255, 255, 0)), (1520, 490))
                # ball pointer would be green if with teammate in team mode

            # main map
            if mpclk:
                window.blit(map_bg, (50, 150))
                window.blit(map_img, (100, 300))
                window.blit(pygame.font.SysFont(None, 100).render("MAP", True, (0, 0, 0)), (760, 180))
                bremp = pygame.transform.scale(loaded_images[29], (90, 60))
                bemp = pygame.transform.scale(loaded_images[30], (90, 60))
                bchrmp = pygame.transform.scale(loaded_images[31], (90, 60))
                bremp.set_colorkey((255, 255, 255))
                bemp.set_colorkey((255, 255, 255))
                bchrmp.set_colorkey((255, 255, 255))
                if en_with_ball[0]:
                    window.blit(bremp, (71 + en_progress[0] * 1230, 300))
                else:
                    window.blit(bemp, (71 + en_progress[0] * 1230, 300))
                if en_with_ball[1]:
                    window.blit(bremp, (71 + en_progress[1] * 1230, 350))
                else:
                    window.blit(bemp, (71 + en_progress[1] * 1230, 350))
                if en_with_ball[2]:
                    window.blit(bremp, (71 + en_progress[2] * 1230, 400))
                else:
                    window.blit(bemp, (71 + en_progress[2] * 1230, 400))
                if self.ball.alive():
                    pygame.draw.rect(window, (0, 0, 255), pygame.Rect(115 + bprogress * 1233, 300, 2, 200))
                window.blit(bchrmp, (71 + progress * 1233, 450))
                window.blit(pygame.font.SysFont(None, 45).render("Total distance: 200m", True, (0, 0, 0)), (100, 530))
                window.blit(bchrmp, (71, 580))
                window.blit(pygame.font.SysFont(None, 45).render(":  You", True, (0, 0, 0)), (140, 600))
                pygame.draw.rect(window, (0, 0, 255), pygame.Rect(115, 660, 2, 70))
                window.blit(pygame.font.SysFont(None, 45).render(":  Ball", True, (0, 0, 0)), (140, 680))
                window.blit(pygame.font.SysFont(None, 45).render(f"Distance covered: {max(math.ceil(progress * 200), 0)}m", True, (0, 0, 0)), (1127, 530))
                window.blit(bemp, (1100, 580))
                window.blit(pygame.font.SysFont(None, 45).render(":  Opponent", True, (0, 0, 0)), (1169, 600))
                window.blit(bremp, (1100, 660))
                window.blit(pygame.font.SysFont(None, 45).render(":  Opponent with ball", True, (0, 0, 0)), (1169, 680))
                close = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(1508, 135, 60, 60), 0, 50)
                pygame.draw.rect(window, (255, 255, 0), pygame.Rect(1508, 135, 60, 60), 6, 50)
                window.blit(pygame.font.SysFont("Berlin Sans FB Demi", 60).render("X", True, (0, 0, 0)), (1520, 130))
                # total distance, symbols meaning

            if progress >= 1:
                if game_won == None:
                    game_won = True

            if 1 in en_progress:
                if game_won == None:
                    game_won = False

            pygame.display.flip()
            self.clock.tick(50)

g_loading().run(window)

# ball landed
# shortcut to map --unnnecessary
# complete everything in l1 first before going into others like store, training, linking it to menu, levels, funds and other cool stuffs
# get required and useful images for small icons e.g grip etc //settled and so on ----more advanced: ----also for enemies
# end of game prolly lobby with a flag and also the end remarks like game over and stuffs, coins earned, time taken --ticks, stars etc.
# start from centre, ball at begining, finish at end. FN(For Now)(F*** N*****)
# configure settings, loader, tutorial --1/3 way completed
