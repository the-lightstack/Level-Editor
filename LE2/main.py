import pygame
pygame.init()

def editor_menu():
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    pygame.display.set_caption("Lars Level Editor")
    app_running=True

    
    menu_bg_image=pygame.image.load("./images/menu_bg_image.png")

    start_editing_button=pygame.image.load("./images/start_editing_button.png")
    start_editing_button_hover=pygame.image.load("./images/start_editing_button_hover.png")

    def check_button_collision():
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit()
                app_running=False
            if e.type==pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(305,340,200,50).collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    working_application()
        if pygame.Rect(305,340,200,50).collidepoint(pygame.mouse.get_pos()):
            screen.blit(start_editing_button_hover,(305,340))
        else:
            screen.blit(start_editing_button,(305,340))
        
    while app_running:
       
        screen.blit(menu_bg_image,(0,0))
        

        check_button_collision()
        
        
        pygame.display.flip()
def working_application():
    from level_editor import Level_Editor
    import pygame
    pygame.init()
    class Var:
        def __init__(self):
            self.WINDOWWIDTH=800
            self.WINDOWHEIGHT=800
            
            self.app_running=True
            self.screen=pygame.display.set_mode((self.WINDOWWIDTH,self.WINDOWHEIGHT))
            pygame.display.set_caption("Lars Level Editor")

            self.camera_scrolling=[0,0]
            self.camera_zoom=1

            self.placable_tiles=[]
    clock=pygame.time.Clock()
    FPS=120
    guide_font=pygame.font.SysFont("Rockwell Nova ",30)
    def show_guide(var):
        spacing_between_texts=30
        text_surfs=[guide_font.render('Space - Change Tile', False, (255,255,255)),guide_font.render('f - fill screen', False, (255,255,255)),guide_font.render('s - save map', False, (255,255,255)),guide_font.render('t - change draw size', False, (255,255,255))]
        for i in range(len(text_surfs)):
            var.screen.blit(text_surfs[i],(600,670+i*spacing_between_texts))
    def event_handling(var,le):
        zoom_strength=4
        scroll_strength=10
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                var.app_running=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_PLUS:
                    var.camera_zoom+=zoom_strength
                    #var.camera_scrolling[0]+=scroll_strength#
                    #print("Camera Zoom:",var.camera_zoom)
                    #le.update_zoom()
                elif event.key==pygame.K_MINUS:
                    var.camera_zoom-=zoom_strength
                    #var.camera_scrolling[0]-=scroll_strength
                    #print("Camera Zoom:",var.camera_zoom)
                    #le.update_zoom()
                if event.key==pygame.K_LEFT:
                    var.camera_scrolling[0]-=scroll_strength
                elif event.key==pygame.K_RIGHT:
                    var.camera_scrolling[0]+=scroll_strength
                if event.key==pygame.K_UP:
                    var.camera_scrolling[1]-=scroll_strength
                elif event.key==pygame.K_DOWN:
                    var.camera_scrolling[1]+=scroll_strength
            le.check_index_change(event)
            le.check_click_add(event)
    var=Var()

    le=Level_Editor(30,30,var)

    while var.app_running:
        clock.tick(FPS)
        event_handling(var,le)
        var.screen.fill((60,100,255))
        le.draw_grid()
        le.update_map()
        show_guide(var)
        pygame.display.flip()
        #var.camera_zoom+=0.0001
        #var.camera_scrolling[0]+=0.0001

if __name__=="__main__":
    editor_menu()
    #working_application()
        