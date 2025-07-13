from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.title = '큐브 마크'
window.borderless = False
window.fullscreen = True
window.exit_button.visible = True
window.fps_counter.enabled = True

# 블럭 종류
block_pick = 1
block_colors = {
    1: color.green,
    2: color.gray,
    3: color.brown,
    4: color.azure
}

# 플레이어
player = FirstPersonController()
player.gravity = 1
player.jump_height = 1.5
player.speed = 5
player.cursor.visible = True

# 블럭 클래스
class Voxel(Button):
    def __init__(self, position=(0,0,0), color=color.green):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            color=color,
            scale=1,
            collider='box'
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            elif key == 'right mouse down':
                voxel = Voxel(
                    position=self.position + mouse.normal,
                    color=block_colors[block_pick]
                )

# 기본 바닥 생성
for x in range(-8, 8):
    for z in range(-8, 8):
        Voxel(position=(x, 0, z), color=color.lime)

# 업데이트 루프: 블럭 선택
def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

app.run()
