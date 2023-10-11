import pygame, sys, math
import random, json

pygame.init()
pygame.mixer.init()

def load():
    with open('data/settings.json', "r") as file:
        return json.load(file)

def save(data):
    with open('data/settings.json', "w") as file:
        json.dump(data, file)
    
class Settings:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def run(self, window, loaded_media):
        settings_data = load()
        self.width, self.height = window.get_size()
        loaded_images = loaded_media["loaded_images"]
        loaded_sounds = loaded_media["loaded_sounds"]
        self.background = loaded_images[0]
        self.tr_background = loaded_images[2]
        xdim, ydim = self.width/1600, self.height/900
        self.back = pygame.transform.scale(loaded_images[1], (62*xdim, 42*ydim))
        self.back.set_colorkey((0, 0, 0))
        self.setttext = pygame.font.SysFont("Agency FB", int(75*xdim), True)
        self.text = pygame.font.SysFont("Agency FB", int(40*xdim), True)
        self.ntext = pygame.font.SysFont("Agency FB", int(38*xdim), True)
        self.stext = pygame.font.SysFont("Agency FB", int(35*xdim))
        self.txtbg = pygame.Surface((1400*xdim, 55*ydim))
        self.txtbg.fill((255, 255, 255))
        self.txtbg.set_alpha(40)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.tr_background = pygame.transform.scale(self.tr_background, (self.width, self.height))
        self.tr_background.set_colorkey((0, 255, 0))
        dg = True
        dg1_scroll = settings_data["display&graphics"]["display_mode"]
        dg2_scroll = settings_data["display&graphics"]["resolution"]
        dg3_scroll = init_vsc = settings_data["display&graphics"]["vsync"]
        brightns_d = 990*xdim + (settings_data["display&graphics"]["brightness"] * 350*xdim)
        contrast_d = 990*xdim + (settings_data["display&graphics"]["contrast"] * 350*xdim)
        dg4_scroll = settings_data["display&graphics"]["letterboxing"]
        dg5_scroll = settings_data["display&graphics"]["ui_adapt"]
        dg6_scroll = settings_data["display&graphics"]["subtitles"]
        dg7_scroll = settings_data["display&graphics"]["colorblind_mode"]
        mvol_d = 990*xdim + (settings_data["audio"]["music_vol"] * 350*xdim)
        svol_d = 990*xdim + (settings_data["audio"]["sfx_vol"] * 350*xdim)
        audio1_scroll = settings_data["audio"]["music"]
        audio2_scroll = settings_data["audio"]["sfx"]
        dg_y, dgscl = 182*ydim, (255, 255, 255)
        audio = controls = networking = tools = system = False
        focus = loaded_sounds[0]
        focused_move = loaded_sounds[1]
        clicked = False
        running = True
        while running:
            dg_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(40*xdim, 95*ydim, 300*xdim, 60*ydim))
            audio_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(355*xdim, 95*ydim, 92*xdim, 60*ydim))
            controls_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(475*xdim, 95*ydim, 153*xdim, 60*ydim))
            networking_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(655*xdim, 95*ydim, 186*xdim, 60*ydim))
            tools_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(865*xdim, 95*ydim, 98*xdim, 60*ydim))
            system_rct = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(995*xdim, 95*ydim, 118*xdim, 60*ydim))
            back = pygame.draw.rect(window, (0, 0, 0), pygame.Rect(1500*xdim, 22*ydim, 90*xdim, 42*ydim))
            
            window.blit(self.background, (0, 0))

            brightns = (brightns_d - 990*xdim) / (350*xdim)
            contrast = (contrast_d - 990*xdim) / (350*xdim)
            mvol = (mvol_d - 990*xdim) / (350*xdim)
            svol = (svol_d - 990*xdim) / (350*xdim)

            if dg:
                dgtop = (dg_y - 182*ydim)/713*ydim * 1200*ydim
                window.blit(self.text.render("Display Settings:", True, (255, 255, 255)), (40*xdim, 200*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 260*ydim - dgtop))
                window.blit(self.ntext.render("Display Mode", True, (255, 255, 255)), (70*xdim, 263*ydim - dgtop))
                dg1l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 287*ydim - dgtop), (1090*xdim, 268*ydim - dgtop), (1090*xdim, 306*ydim - dgtop)))
                dg1r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 287*ydim - dgtop), (1324*xdim, 268*ydim - dgtop), (1324*xdim, 306*ydim - dgtop)))
                if dg1_scroll == 0:
                    window.blit(self.ntext.render("Fullscreen", True, (255, 255, 255)), (1142*xdim, 264*ydim - dgtop))
                else:
                    window.blit(self.ntext.render("Window screen", True, (255, 255, 255)), (1110*xdim, 264*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 320*ydim - dgtop))
                window.blit(self.ntext.render("Resolution", True, (255, 255, 255)), (70*xdim, 323*ydim - dgtop))
                dg2l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 347*ydim - dgtop), (1090*xdim, 328*ydim - dgtop), (1090*xdim, 366*ydim - dgtop)))
                dg2r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 347*ydim - dgtop), (1324*xdim, 328*ydim - dgtop), (1324*xdim, 366*ydim - dgtop)))
                if dg2_scroll == 0:
                    window.blit(self.ntext.render("1600 x 900", True, (255, 255, 255)), (1135*xdim, 324*ydim - dgtop))
                elif dg2_scroll == 1:
                    window.blit(self.ntext.render("1920 x 1080", True, (255, 255, 255)), (1130*xdim, 324*ydim - dgtop))
                elif dg2_scroll == 2:
                    window.blit(self.ntext.render("1400 x 1000", True, (255, 255, 255)), (1130*xdim, 324*ydim - dgtop))
                else:
                    window.blit(self.ntext.render("1000 x 600", True, (255, 255, 255)), (1130*xdim, 324*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 380*ydim - dgtop))
                window.blit(self.ntext.render("V-Sync", True, (255, 255, 255)), (70*xdim, 383*ydim - dgtop))
                dg3l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 407*ydim - dgtop), (1090*xdim, 388*ydim - dgtop), (1090*xdim, 426*ydim - dgtop)))
                dg3r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 407*ydim - dgtop), (1324*xdim, 388*ydim - dgtop), (1324*xdim, 426*ydim - dgtop)))
                if dg3_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190*xdim, 384*ydim - dgtop))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1190*xdim, 384*ydim - dgtop))
                window.blit(self.text.render("Visual Settings:", True, (255, 255, 255)), (40*xdim, 443*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 503*ydim - dgtop))
                window.blit(self.ntext.render("Brightness", True, (255, 255, 255)), (70*xdim, 506*ydim - dgtop))
                pygame.draw.line(window, (0, 0, 255), (990*xdim, 531*ydim - dgtop), (1350*xdim, 531*ydim - dgtop), int(4*xdim))
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(brightns_d, 516*ydim - dgtop, 10*xdim, 30*ydim))
                window.blit(self.ntext.render(f"{math.ceil(brightns * 100)}%", True, (255, 255, 255)), (1365*xdim, 506*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 563*ydim - dgtop))
                window.blit(self.ntext.render("Contrast", True, (255, 255, 255)), (70*xdim, 566*ydim - dgtop))
                pygame.draw.line(window, (0, 0, 255), (990*xdim, 591*ydim - dgtop), (1350*xdim, 591*ydim - dgtop), int(4*xdim))
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(contrast_d, 576*ydim - dgtop, 10*xdim, 30*ydim))
                window.blit(self.ntext.render(f"{math.ceil(contrast * 100)}%", True, (255, 255, 255)), (1365*xdim, 566*ydim - dgtop))
                window.blit(self.text.render("Display Format:", True, (255, 255, 255)), (40*xdim, 626*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 686*ydim - dgtop))
                window.blit(self.ntext.render("Letterboxing", True, (255, 255, 255)), (70*xdim, 689*ydim - dgtop))
                dg4l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 713*ydim - dgtop), (1090*xdim, 694*ydim - dgtop), (1090*xdim, 732*ydim - dgtop)))
                dg4r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 713*ydim - dgtop), (1324*xdim, 694*ydim - dgtop), (1324*xdim, 732*ydim - dgtop)))
                if dg4_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190*xdim, 690*ydim - dgtop))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1190*xdim, 690*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 746*ydim - dgtop))
                window.blit(self.ntext.render("UI Adaptability", True, (255, 255, 255)), (70*xdim, 749*ydim - dgtop))
                dg5l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 773*ydim - dgtop), (1090*xdim, 754*ydim - dgtop), (1090*xdim, 792*ydim - dgtop)))
                dg5r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 773*ydim - dgtop), (1324*xdim, 754*ydim - dgtop), (1324*xdim, 792*ydim - dgtop)))
                if dg5_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190*xdim, 750*ydim - dgtop))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1190*xdim, 750*ydim - dgtop))
                window.blit(self.text.render("Accessibility Settings:", True, (255, 255, 255)), (40*xdim, 809*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 869*ydim - dgtop))
                window.blit(self.ntext.render("Subtitles", True, (255, 255, 255)), (70*xdim, 872*ydim - dgtop))
                dg6l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 896*ydim - dgtop), (1090*xdim, 877*ydim - dgtop), (1090*xdim, 915*ydim - dgtop)))
                dg6r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 896*ydim - dgtop), (1324*xdim, 877*ydim - dgtop), (1324*xdim, 915*ydim - dgtop)))
                if dg6_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190*xdim, 873*ydim - dgtop))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1190*xdim, 873*ydim - dgtop))
                window.blit(self.txtbg, (40*xdim, 929*ydim - dgtop))
                window.blit(self.ntext.render("Colorblind Mode", True, (255, 255, 255)), (70*xdim, 932*ydim - dgtop))
                dg7l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 956*ydim - dgtop), (1090*xdim, 937*ydim - dgtop), (1090*xdim, 975*ydim - dgtop)))
                dg7r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 956*ydim - dgtop), (1324*xdim, 937*ydim - dgtop), (1324*xdim, 975*ydim - dgtop)))
                if dg7_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190*xdim, 933*ydim - dgtop))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1190*xdim, 933*ydim - dgtop))
                window.blit(self.text.render("Visual Effect", True, (255, 255, 255)), (40*xdim, 992*ydim - dgtop))

            if audio:
                window.blit(self.txtbg, (40*xdim, 200*ydim))
                window.blit(self.ntext.render("Music", True, (255, 255, 255)), (70*xdim, 203*ydim))
                audio1l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 227*ydim), (1090*xdim, 208*ydim), (1090*xdim, 246*ydim)))
                audio1r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 227*ydim), (1324*xdim, 208*ydim), (1324*xdim, 246*ydim)))
                if audio1_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190*xdim, 204*ydim))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1190*xdim, 204*ydim))
                window.blit(self.txtbg, (40*xdim, 260*ydim))
                window.blit(self.ntext.render("SFX", True, (255, 255, 255)), (70*xdim, 263*ydim))
                audio2l = pygame.draw.polygon(window, (0, 0, 255), ((1064*xdim, 287*ydim), (1090*xdim, 268*ydim), (1090*xdim, 306*ydim)))
                audio2r = pygame.draw.polygon(window, (0, 0, 255), ((1350*xdim, 287*ydim), (1324*xdim, 268*ydim), (1324*xdim, 306*ydim)))
                if audio2_scroll == 0:
                    window.blit(self.ntext.render("On", True, (255, 255, 255)), (1190*xdim, 264*ydim))
                else:
                    window.blit(self.ntext.render("Off", True, (255, 255, 255)), (1190*xdim, 264*ydim))
                window.blit(self.txtbg, (40*xdim, 320*ydim))
                window.blit(self.ntext.render("MUSIC VOLUME", True, (255, 255, 255)), (70*xdim, 323*ydim))
                pygame.draw.line(window, (0, 0, 255), (990*xdim, 348*ydim), (1350*xdim, 348*ydim), int(4*xdim))
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(mvol_d, 333*ydim, 10*xdim, 30*ydim))
                window.blit(self.ntext.render(f"{math.ceil(mvol * 100)}%", True, (255, 255, 255)), (1365*xdim, 323*ydim))
                window.blit(self.txtbg, (40*xdim, 380*ydim))
                window.blit(self.ntext.render("SFX VOLUME", True, (255, 255, 255)), (70*xdim, 383*ydim))
                pygame.draw.line(window, (0, 0, 255), (990*xdim, 408*ydim), (1350*xdim, 408*ydim), int(4*xdim))
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(svol_d, 393*ydim, 10*xdim, 30*ydim))
                window.blit(self.ntext.render(f"{math.ceil(svol * 100)}%", True, (255, 255, 255)), (1365*xdim, 383*ydim))
            
            window.blit(self.tr_background, (0, 0))

            window.blit(self.setttext.render("SETTINGS", True, (255, 255, 255)), (40*xdim, 0))
            window.blit(self.stext.render("Back", True, (255, 255, 255)), (1500*xdim, 20*ydim))
            window.blit(self.back, (1540*xdim, 20*ydim))

            window.blit(self.text.render("DISPLAY & GRAPHICS", True, (255, 255, 255)), (40*xdim, 100*ydim))
            window.blit(self.text.render("AUDIO", True, (255, 255, 255)), (360*xdim, 100*ydim))
            window.blit(self.text.render("CONTROLS", True, (255, 255, 255)), (480*xdim, 100*ydim))
            window.blit(self.text.render("NETWORKING", True, (255, 255, 255)), (660*xdim, 100*ydim))
            window.blit(self.text.render("TOOLS", True, (255, 255, 255)), (870*xdim, 100*ydim))
            window.blit(self.text.render("SYSTEM", True, (255, 255, 255)), (1000*xdim, 100*ydim))
            
            if audio1_scroll == 0:
                pygame.mixer.music.set_volume(mvol)
            else:
                pygame.mixer.music.set_volume(0)
            if audio2_scroll == 0:
                focus.set_volume(svol)
                focused_move.set_volume(svol)
            else:
                focus.set_volume(0)
                focus.set_volume(0)

            if init_vsc != dg3_scroll:
                pygame.display.quit()
                pygame.display.init()
                if dg3_scroll == 0:
                    window = pygame.display.set_mode((1600, 900), pygame.HWSURFACE | pygame.DOUBLEBUF, pygame.FULLSCREEN)
                else:
                    window = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
            init_vsc = dg3_scroll

            if dg:
                pygame.draw.line(window, (255, 255, 255), (40*xdim, 95*ydim), (340*xdim, 95*ydim))
                pygame.draw.line(window, (255, 255, 255), (40*xdim, 154*ydim), (340*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (360*xdim, 95*ydim), (1110*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (360*xdim, 154*ydim), (1110*xdim, 154*ydim))
                dgrct = pygame.draw.rect(window, dgscl, pygame.Rect(1450*xdim, dg_y, 8*xdim, (718*713)/(1200 + 60)*ydim))# 600/713 last textbg = 1200
                
            if audio:
                pygame.draw.line(window, (255, 255, 255), (355*xdim, 95*ydim), (445*xdim, 95*ydim))
                pygame.draw.line(window, (255, 255, 255), (355*xdim, 154*ydim), (445*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 95*ydim), (340*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 154*ydim), (340*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (480*xdim, 95*ydim), (1110*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (480*xdim, 154*ydim), (1110*xdim, 154*ydim))

            if controls:
                pygame.draw.line(window, (255, 255, 255), (470*xdim, 95*ydim), (633*xdim, 95*ydim))
                pygame.draw.line(window, (255, 255, 255), (470*xdim, 154*ydim), (633*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 95*ydim), (446*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 154*ydim), (446*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (660*xdim, 95*ydim), (1110*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (660*xdim, 154*ydim), (1110*xdim, 154*ydim))
                window.blit(self.txtbg, (40*xdim, 200*ydim))

            if networking:
                pygame.draw.line(window, (255, 255, 255), (650*xdim, 95*ydim), (846*xdim, 95*ydim))
                pygame.draw.line(window, (255, 255, 255), (650*xdim, 154*ydim), (846*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 95*ydim), (633*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 154*ydim), (633*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (870*xdim, 95*ydim), (1110*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (870*xdim, 154*ydim), (1110*xdim, 154*ydim))
                window.blit(self.txtbg, (40*xdim, 200*ydim))

            if tools:
                pygame.draw.line(window, (255, 255, 255), (860*xdim, 95*ydim), (968*xdim, 95*ydim))
                pygame.draw.line(window, (255, 255, 255), (860*xdim, 154*ydim), (968*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 95*ydim), (846*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 154*ydim), (846*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (1000*xdim, 95*ydim), (1110*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (1000*xdim, 154*ydim), (1110*xdim, 154*ydim))
                window.blit(self.txtbg, (40*xdim, 200*ydim))

            if system:
                pygame.draw.line(window, (255, 255, 255), (990*xdim, 95*ydim), (1108*xdim, 95*ydim))
                pygame.draw.line(window, (255, 255, 255), (990*xdim, 154*ydim), (1108*xdim, 154*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 95*ydim), (968*xdim, 95*ydim))
                pygame.draw.line(window, (0, 0, 255), (40*xdim, 154*ydim), (968*xdim, 154*ydim))
                window.blit(self.txtbg, (40*xdim, 200*ydim))

            settings_data = {
                "display&graphics": {"display_mode": dg1_scroll, "resolution": dg2_scroll, "vsync": dg3_scroll, "brightness": brightns, "contrast": contrast, "letterboxing": dg4_scroll, "ui_adapt": dg5_scroll, "subtitles": dg6_scroll, "colorblind_mode": dg7_scroll},
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
                            focus.play()
                            dg1_scroll += 1

                        if dg1l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg1_scroll -= 1

                        if dg2r.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg2_scroll += 1

                        if dg2l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg2_scroll -= 1

                        if dg3r.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg3_scroll += 1

                        if dg3l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg3_scroll -= 1

                        if dg4r.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg4_scroll += 1

                        if dg4l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg4_scroll -= 1

                        if dg5r.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg5_scroll += 1

                        if dg5l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg5_scroll -= 1

                        if dg6r.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg6_scroll += 1

                        if dg6l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg6_scroll -= 1
                        
                        if dg7r.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg7_scroll += 1

                        if dg7l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            dg7_scroll -= 1

                        dg1_scroll = dg1_scroll % 2
                        dg2_scroll = dg2_scroll % 4
                        dg3_scroll = dg3_scroll % 2
                        dg4_scroll = dg4_scroll % 2
                        dg5_scroll = dg5_scroll % 2
                        dg6_scroll = dg6_scroll % 2
                        dg7_scroll = dg7_scroll % 2
                    
                    if audio:
                        if audio1r.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            audio1_scroll += 1

                        if audio1l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            audio1_scroll -= 1

                        if audio2r.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            audio2_scroll += 1

                        if audio2l.collidepoint(pygame.mouse.get_pos()):
                            focus.play()
                            audio2_scroll -= 1

                        audio1_scroll = audio1_scroll % 2
                        audio2_scroll = audio2_scroll % 2

                    if dg_rct.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                        dg = True
                        audio = controls = networking = tools = system = False

                    if audio_rct.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                        audio = True
                        dg = controls = networking = tools = system = False

                    if controls_rct.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                        controls = True
                        dg = audio = networking = tools = system = False

                    if networking_rct.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                        networking = True
                        dg = controls = audio = tools = system = False

                    if tools_rct.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                        tools = True
                        dg = controls = networking = audio = system = False
                    
                    if system_rct.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                        system = True
                        dg = controls = networking = tools = audio = False

                    if back.collidepoint(pygame.mouse.get_pos()):
                        focus.play()
                        save(settings_data)
                        return window
                        
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    clicked = False

            if clicked:
                if dg:
                    if dgrct.collidepoint(pygame.mouse.get_pos()):
                        if dgscl != (0, 0, 255):
                            diff = pygame.mouse.get_pos()[1] - dg_y
                        dgscl = (0, 0, 255)
                    
                    if dgscl == (255, 255, 255):
                        if 995*xdim < pygame.mouse.get_pos()[0] < 1345*xdim and 518*ydim - dgtop <= pygame.mouse.get_pos()[1] <= 548*ydim - dgtop:
                            focused_move.play()
                            brightns_d = pygame.mouse.get_pos()[0] - 5*xdim

                        if 990*xdim <= pygame.mouse.get_pos()[0] <= 995*xdim and 518*ydim - dgtop <= pygame.mouse.get_pos()[1] <= 548*ydim - dgtop:
                            focused_move.play()
                            brightns_d = 990*xdim

                        if 1345*xdim <= pygame.mouse.get_pos()[0] <= 1350*xdim and 518*ydim - dgtop <= pygame.mouse.get_pos()[1] <= 548*ydim - dgtop:
                            focused_move.play()
                            brightns_d = 1340*xdim

                        if 995*xdim < pygame.mouse.get_pos()[0] < 1345*xdim and 578*ydim - dgtop <= pygame.mouse.get_pos()[1] <= 608*ydim - dgtop:
                            focused_move.play()
                            contrast_d = pygame.mouse.get_pos()[0] - 5*xdim

                        if 990*xdim <= pygame.mouse.get_pos()[0] <= 995*xdim and 578*ydim - dgtop <= pygame.mouse.get_pos()[1] <= 608*ydim - dgtop:
                            focused_move.play()
                            contrast_d = 990*xdim

                        if 1345*xdim <= pygame.mouse.get_pos()[0] <= 1350*xdim and 578*ydim - dgtop <= pygame.mouse.get_pos()[1] <= 608*ydim - dgtop:
                            focused_move.play()
                            contrast_d = 1340*xdim

                if audio:
                    if 995*xdim < pygame.mouse.get_pos()[0] < 1345*xdim and 335*ydim <= pygame.mouse.get_pos()[1] <= 365*ydim:
                        focused_move.play()
                        mvol_d = pygame.mouse.get_pos()[0] - 5*xdim

                    if 990*xdim <= pygame.mouse.get_pos()[0] <= 995*xdim and 335*ydim <= pygame.mouse.get_pos()[1] <= 365*ydim:
                        focused_move.play()
                        mvol_d = 990*xdim

                    if 1345*xdim <= pygame.mouse.get_pos()[0] <= 1350*xdim and 335*ydim <= pygame.mouse.get_pos()[1] <= 365*ydim:
                        focused_move.play()
                        mvol_d = 1340*xdim

                    if 995*xdim < pygame.mouse.get_pos()[0] < 1345*xdim and 395*ydim <= pygame.mouse.get_pos()[1] <= 425*ydim:
                        focused_move.play()
                        svol_d = pygame.mouse.get_pos()[0] - 5*xdim

                    if 990*xdim <= pygame.mouse.get_pos()[0] <= 995*xdim and 395*ydim <= pygame.mouse.get_pos()[1] <= 425*ydim:
                        focused_move.play()
                        svol_d = 990*xdim

                    if 1345*xdim <= pygame.mouse.get_pos()[0] <= 1350*xdim and 395*ydim <= pygame.mouse.get_pos()[1] <= 425*ydim:
                        focused_move.play()
                        svol_d = 1340*xdim
            else:
                dgscl = (255, 255, 255)

            if dgscl == (0, 0, 255):  # or (clicked and pygame.mouse.get_pos()[1] >= 182*ydim and 1450*xdim <= pygame.mouse.get_pos()[0] <= 1458*xdim)
                if 895*ydim - dgrct.height + diff > pygame.mouse.get_pos()[1] > 182*ydim + diff:
                    dg_y = pygame.mouse.get_pos()[1] - diff
                elif pygame.mouse.get_pos()[1] <= 182*ydim + diff:
                    dg_y = 182*ydim
                elif pygame.mouse.get_pos()[1] >= 895*ydim - dgrct.height + diff:
                    dg_y = 895*ydim - dgrct.height

            pygame.display.flip()
            self.clock.tick(40)

# Settings().run(pygame.display.set_mode((1600, 900)))
# things to sort out
# click settings icon only when its visible not when its scrolled