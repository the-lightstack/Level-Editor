import pygame

class Level_Editor:
    def __init__(self,rows,columns,var):
        self.rows=rows
        self.columns=columns
        self.var=var

        self.box_width=int(self.var.WINDOWWIDTH/self.columns)
        self.box_height=int(self.var.WINDOWHEIGHT/self.rows)
        
        #self.available_colors={0:(60,100,255),1:(40,40,240),2:(200,200,200),3:(200,40,40),4:(200,200,100),5:(100,40,170),6:(30,50,70),7:(100,100,100),8:(10,12,76),9:(90,21,200),10:(34,74,81),11:(10,200,130)}
        img=pygame.image.load
        self.tiles=[i for i in self.get_sprite_sheet((32,32),"./tiles/world_sprite_sheet.png")]
        self.tiles.append(self.get_sprite_sheet((32,32),"./tiles/bush_animation_sprites.png")[0])
        self.tiles=[pygame.transform.scale(i,(self.box_width,self.box_height)) for i in self.tiles]
        self.current_tile_index=0
        self.amount_thicknesses=3
        self.grid_color=(50,50,50)
        self.draw_thickness=1
        self.init_final_map()
    def draw_grid(self):
        for i in range(self.columns+1):
            pygame.draw.line(self.var.screen,self.grid_color,(i*self.box_width,0),(i*self.box_width,self.var.WINDOWHEIGHT))
        
        for i in range(self.rows+1):
            pygame.draw.line(self.var.screen,self.grid_color,(0,i*self.box_height),(self.var.WINDOWWIDTH,i*self.box_height))
    
    def check_index_change(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if self.current_tile_index==len(self.tiles)-1:
                    self.current_tile_index=0
                    #print(self.current_tile_index) 
                else:
                    self.current_tile_index+=1
                    #print(self.current_tile_index)
            elif event.key==pygame.K_s:
                self.save_map()
            elif event.key==pygame.K_f:
                self.fill_all()
            elif event.key==pygame.K_t:
        
                self.increase_thickness()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==3:
                m_pos=pygame.Vector2(pygame.mouse.get_pos())
                m_pos.x=int(m_pos.x/self.box_width)
                m_pos.y=int(m_pos.y/self.box_height)

                self.current_tile_index=self.map[int(m_pos.x)][int(m_pos.y)]





    def check_click_add(self,event):
        if pygame.mouse.get_pressed()[0]:
            row=int(pygame.mouse.get_pos()[1]//self.box_height)
            col=int(pygame.mouse.get_pos()[0]//self.box_width)
            
            if self.draw_thickness==1:

                #print("col:",col," row:",row)

                self.map[col][row]=self.current_tile_index

            elif self.draw_thickness==2:
                try:  
                    self.map[col][row]=self.current_tile_index#1

                    self.map[col-1][row-1]=self.current_tile_index#2
                    self.map[col][row-1]=self.current_tile_index#3
                    self.map[col+1][row-1]=self.current_tile_index#4

                    self.map[col+1][row-1]=self.current_tile_index#5
                    self.map[col+1][row]=self.current_tile_index#6
                    self.map[col+1][row+1]=self.current_tile_index#7

                    self.map[col+1][row+1]=self.current_tile_index#8
                    self.map[col][row+1]=self.current_tile_index#9
                    self.map[col-1][row]=self.current_tile_index#9
                    self.map[col-1][row+1]=self.current_tile_index#9
                except:
                    pass
    def init_final_map(self):
        self.map=[]
        for i in range(self.rows):
            self.map.append([0 for i in range(self.columns)])
        #print(self.map)
    

    def update_map(self):
        for layer_num in range(len(self.map)):
            for i in range(len(self.map[layer_num])):
                #print("i",i)
                self.var.screen.blit(self.tiles[self.map[layer_num][i]],(layer_num*self.box_width+1,i*self.box_height+1))#self.available_colors[self.map[layer_num][i]]
        #self.box_width*=self.var.camera_zoom
        #self.box_height*=self.var.camera_zoom

    def save_map(self):
        with open("final_map.txt","w") as file:
            file.write(str(self.map))

    def fill_all(self):
        for layer_num in range(len(self.map)):
            for i in range(len(self.map[layer_num])):
                self.map[layer_num][i]=self.current_tile_index
    def increase_thickness(self):
        if self.draw_thickness==1:
            self.draw_thickness=2
        elif self.draw_thickness==2:
            self.draw_thickness=4
        elif self.draw_thickness==4:
            self.draw_thickness=1
    def update_zoom(self):
        self.box_width=self.var.camera_zoom
        self.box_height=self.var.camera_zoom
    
    
    def get_sprite_sheet(self,size,file,pos=(0,0)):
        import pygame#file is path_to_file
        #Initial Values
        pos=(0,0)
  
        len_sprt_x,len_sprt_y = size #sprite size
        
        sprt_rect_x,sprt_rect_y = pos #where to find first sprite on sheet
        sheet = pygame.image.load(file).convert_alpha() #Load the sheet
        sheet_rect = sheet.get_rect()
        
        sprites = []
        
        image_size=size
        #print("sheet rect w:",sheet_rect.w)
        #print("row")
        for i in range(0,sheet_rect.width,size[0]):#columns
            #print("column")
            #print("i:",i)    
            sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y)) #find sprite you want
            sprite = sheet.subsurface(sheet.get_clip()) #grab the sprite you want
            sprites.append(sprite)
            sprt_rect_x += len_sprt_x
        sprt_rect_y += len_sprt_y
        sprt_rect_x = 0

        #sprites=[pygame.transform.scale(i,(image_size[0],image_size[1])) for i in sprites]
        #print("sprites:",sprites)
        return sprites