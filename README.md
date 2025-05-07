# FoxGame

## Навігація
- [Мета проекта](#title1)
- [Корисність проекта](#title2)
- [Мета проекта](#title3)
- [Управління](#title0)
- [Обов'язкові модулі](#title4)
- [Структура проекта](#title5)
- [Як працює гра](#title5)
- [Висновок](#title5)

## <a id="title1">Мета проекту</a>
Мета проекту - розробка гри, яка б покращіла мої навички рішення задач. 
Та наглядна демонстрація того, що можно ррозробити за допомогою модуля Pygame

---


## <a id="title2">Чим мій проект може бути корисним для вас?</a>
Деякі інші програмісти можуть брати частинки мого коду, щоб розробити свою гру.
А прості відвідувачі можуть пограти у мою гру, та подивитись, що це за гра.

---


## <a id="title3">Як запустити цю гру?</a>
1. Завантажити проект
    - git clone https://github.com/ArtemDema/FoxGame_2d.git
2. Перейти до папки з грою
    - cd FoxGame
3. Встановлення python
    - пишемо pip install python
4. Встановлення потрібних модулів для роботи гри
    - pip install -r requirements.txt
5. Запустити гру
    - запустити скрипт через файл main.py
---

## <a id="title0">Управління</a>
### A - йти у ліву сторону
### D - йти у праву сторону
### SPACE - стрибати
### Q - підняти ящік
### R - штовхати ящік
### G - бросити ящік
### T - завдання
### ESCAPE - пауза
### SHIFT - присід
---

## <a id="title4">Модулі для роботи гри</a>
### Pygame
Головний модуль, на якому працює гра
### PyTMX
Модуль, завдяки якому переноситься карта з .tmx файла у гру

---

## <a id="title5">Структура проекта</a>
### Fonts
Daydream.ttf - шрифт, який використовується при паузі, листі задач
### Images
Папка у якій знаходиться усі зображення, які використовуються у грі
### Json
Зберігає в собі json файл, у якому знаходиться інформація про останній захід у гру 
### Level task
Зберігає в собі json файл, у якому знаходиться інформація про задачі на конкретний рівень
### Levels
Зберігає в собі .tmx файл, у якому знаходиться частина першого рівня
### Modules
1. Box
    - Зберігає в собі всі функції та можливості коробок
2. Bush
    - Зберігає в собі всі функції та можливості кустів
3. Chest
    - Зберігає в собі всі функції та можливості скринь
4. Cloud
    - Зберігає в собі всі функції та можливості хмар
5. Enemy
    - Зберігає в собі всі функції та можливості ворогів, таких як жаба, курка, курча і півень
6. Game events and checks
    - Зберігає в собі перевірки завдяки яким працюють деякі функції гри
7. Interface
    - Зберігає в собі інвертар який показується вверху ігрового вікна
8. Json
    - Зберігає в собі функції для роботи та обробки json файлів
9. Modal window
    - Зберігає в собі код для показу, що було в скрині
10. Resources
    - Зберігає в собі всі функції для обробки ресурсів, які є у ігрока
11. Screen
    - Зберігає в собі мапу, ігрока, загрузку зображень, малювання всього, що є на єкрані 
12. Tree
    - Зберігає в собі всі функції та можливості дерев
13. Water
    - Зберігає в собі всі функції та можливості води
14. Functions for main
    - Зберігає в собі функції для гравітації, штовхання ящика та стрибок
15. Main class
    - Зберігає в собі всі самі головні класи завдяки яким створена вся гра
16. Main meny
    - Зберігає в собі меню, яке показується при заході в гру
### Sounds
Зберігає в собі усі звуки, які використовуються у грі
### Main.py
Головний файл, через який гра повинна запускатись
### Requirements.txt
Зберігає в собі усі модулі, необхідні для роботи гри

---

## <a id="title6">Як працює ця гра</a>
### Move
#### Переміщення зроблено за допомогою перевірок на дотик до стін та ворогів,
#### якщо персонаж не доторкається до них, то ігрок може йти в бік.
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
if keys[pygame.K_a]:
    for enemy in list_enemy:
        answer = enemy.check_collision_right_wall(player.x, player.y + 5, 
                                                player.x + player.width, player.y + player.height)
        if answer:
            dict_return["last_side"] = 0
            return dict_return

    if answer != True:
        if move_jump == False:
            dict_return["move_left"] = True
        if push_box: dict_return["push_box"] = False
        dict_return["last_side"] = 0
        player.x -= player.speed
        player.rect.x -= player.speed
```
---
### Jump
#### Стрибок зроблено за допомогою перевірок на дотик до низу блоків,
#### якщо персонаж не доторкається до них, то ігрок виконує стрибок
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
if keys[pygame.K_SPACE]:
    if player.strength_jump != 0:
        for block in blocks:
            answer = block.check_collision_bottom_wall_p(player)
            if answer:
                return_dict["move_jump"] = False
                return_dict["player_strength_jump"] = 20
                return return_dict
        
        player.y -= player.speed * 1.5
        player.rect.y -= player.speed * 1.5
    else:
        return_dict["move_jump"] = False
        return_dict["player_strength_jump"] = 20
        return return_dict
```
---
### Crouch
#### Присідання зроблено за допомогою перевірок на стан ігрока,
#### якщо персонаж не стрибає, не йде, не падає, то ігрок може пригнутися
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
if keys[pygame.K_LSHIFT]:
    if mod.move_bottom == False and mod.move_jump == False and mod.move_right == False and mod.move_left == False and mod.player.hide == False and mod.with_box == False:
        mod.move_crouch = True
else:
    mod.move_crouch = False
```
---
### Pause
#### Паузу зроблено за допомогою перевірки на натискання клавіши Escape,
#### якщо ця клавіша натиснута, то гра замідляється і з'являються дві кнопки(віходу и продовження) 
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
if keys[pygame.K_ESCAPE]:
    pause = True
if pause:
    pygame.time.delay(120)
    exit_b = mod.Button(525, 450, 190, 100, "images/resources/exit.png")
    continue_b.show_image(mod.screen)
```
---
### Menu
#### Меню зроблено за допомогою такого ж самого циклу як і сама гра,
#### Перед початком гри запускається нескінечний цикл, вийти з якого можно натиснувши кнопку
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
menu_run = True
while menu_run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
                position_mouse = event.pos

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            menu_run = button1.check_click(position_mouse[0], position_mouse[1])
            if menu_run == False:
                return True
    pygame.display.flip()
```
---
### Map
#### Карту зроблено за допомогою модулю PyTMX(статичні блоки) та мартиці(девера, ресурси, вороги),
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
path = os.path.abspath(__file__ + "\..\..\..\levels")

level = pytmx.load_pygame(path + "/first_screen.tmx")

layer = level.get_layer_by_name("Слой тайлов 1")

for x, y, tileSurface in layer.tiles():
    tile =  TileBlock(x = x * 50, y = y * 50, width = 50, height = 50, image = tileSurface)
    blocks.append(tile)

map = [ [" ","r"," ","b"," "," "," "] ]
for idy, row in enumerate(map):
    for idx, column in enumerate(row):       
        if column == "b":
            pass
        elif column == "r":
            pass
```
---
### Frog
#### Поведінка жаби - агресивна, може стрибати. Ось кусочок с коду, с демонстраціей як це працює:
```python
#стрибок
frog.x = self.x + 10 * math.cos(self.angle * (math.pi / 180))
frog.y = self.y + 10 * math.sin(self.angle * (math.pi / 180))

#агресивність
if self.player_visibility:
            if player.hide == False:
                if self.frequency_jump == 0:
                    if self.angle == 0:
                        distance = player.x - self.x
                        if distance <= 0:
                            self.angle = -135
                            self.vector_move = 1
                        else:
                            self.angle = -45
                            self.vector_move = 0
                else:
                    self.frequency_jump -= 1

#нанесення урону гравцю
if player.hide == False:
    answer = player.check_collision_left(frog.x, frog.y, frog.x + frog.width, frog.y + frog.height)
    if answer:
        player.damage_player(sound_damage)
```
---
### Chick
#### Поведінка курча - агресивна, може бігати. Ось кусочок с коду, с демонстраціей як це працює:
```python
#біг
for block in list_of_all_blocks: #CHECK TOUCH LEFT WALL OF BLOCK
    answer = block.check_collision_left_wall(chick.x, chick.y, 
                                            chick.x + chick.width, chick.y + chick.height)
if answer != True:
    chick.x += chick.speed

#нанесення урону гравцю
if player.hide == False:
    answer = player.check_collision_left(frog.x, frog.y, frog.x + frog.width, frog.y + frog.height)
    if answer:
        player.damage_player(sound_damage)
```
---
### Chicken
#### Поведінка куриці - пуглива, може бігати. Ось кусочок с коду, с демонстраціей як це працює:
```python
#пугливість
if chicken.player_visibility:
    if chicken.random_move <= 0:
        distance = player.x - chicken.x
        if distance <= 0:
            chicken.random_move = 200
            chicken.vector_move = 1
        else:
            chicken.random_move = 200
            chicken.vector_move = 0

#біг
for block in list_of_all_blocks: #CHECK TOUCH LEFT WALL OF BLOCK
    answer = block.check_collision_left_wall(chicken.x, chicken.y, 
                                            chicken.x + chicken.width, chicken.y + chicken.height)
if answer != True:
    chick.x += chick.speed

```
---
### Rooster
#### Поведінка півня - агресивна, може бігати. Ось кусочок с коду, с демонстраціей як це працює:
```python
#біг
for block in list_of_all_blocks: #CHECK TOUCH LEFT WALL OF BLOCK
    answer = block.check_collision_left_wall(chick.x, chick.y, 
                                            chick.x + chick.width, chick.y + chick.height)
if answer != True:
    chick.x += chick.speed

#агресивність
if self.player_visibility:
            if player.hide == False:
                if self.frequency_jump == 0:
                    if self.angle == 0:
                        distance = player.x - self.x
                        if distance <= 0:
                            self.angle = -135
                            self.vector_move = 1
                        else:
                            self.angle = -45
                            self.vector_move = 0
                else:
                    self.frequency_jump -= 1

#нанесення урону гравцю
if player.hide == False:
    answer = player.check_collision_left(frog.x, frog.y, frog.x + frog.width, frog.y + frog.height)
    if answer:
        player.damage_player(sound_damage)
```
---
### Feather
#### З'являється коли півень баче ігрока. Летить в напрямок ігрока.
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
#поява
feather = Feather(rooster.x, rooster.y + (rooster.height // 2) + 3, 25, 25, "images/enemy/rooster/feather/0.png", rooster.angle)
feather.image = pygame.transform.rotate(feather.image, self.angle - 200)

#переміщення
feather.x = feather.x + 4 * math.cos(feather.angle * math.pi / 180)
feather.y = feather.y + 4 * math.sin(feather.angle * math.pi / 180)

#нанесення урону гравцю
if player.hide == False:
    answer = player.check_collision_left(feather.x, feather.y, feather.x + feather.width, feather.y + feather.height)
    if answer:
        player.damage_player(sound_damage)
        list_feather.remove(feather)
        return
```
---
### Water
#### Вода наносить урон ігроку. Ось кусочок с коду, с демонстраціей як це працює:
```python
for water in mod.list_water:
    answer = water.check_death_of_player(mod.player)
    if answer:
        mod.player.damage_player(mod.sound_damage)
        mod.player.player_in_the_water = True
```
---
### Task
#### Задачі реалізовані наступним чином:
```python
task = mod.get_info(__file__ + "/../level_task/tasks.json")
task_egg  = int(task[f'{player_level}']['1'])

if keys[pygame.K_t]:
        tasks = True
if tasks:
    for index in range(len(task["1"])):
        if index % 2 == 0:
            text_task = mod.Button(535, 200 + index * 50, 0, 0)
            text_task.text(mod.screen, f"{task['1'][f'{index}']}", 48, 0, 0, 0)
```
---
### Chest
#### Скриню можна відкрити ключом, та сховатися у ній(тількі якщо скриня відкрита)
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
#відкриття скрині
if count_key >= 1:
    self.open_chest = True
    list_return[0] = True
    if random_n == 1:
        egg = Discarded_Item(x = self.x + (self.width / 2) - 5, y = self.y + self.height + 15, width = 20, height = 30, image = "images/resources/egg.png", whatIsThis= "egg")
        droped_resources.append(egg)
        list_return[1] = "egg"
        return list_return

elif answer[0] == False: 
    return_list["player.hide"] = True
    chest.hide_in_him = True
```
---
### Throw box
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
if keys[pygame.K_g]:
    if mod.with_box == True:
        mod.with_box = False
        if last_side == 0:
            box_player.throw = True
            box_player.angle = -125
            mod.drop_box.set_volume(0.2)
            mod.drop_box.play(loops = 0)

if self.angle == -45:
    for block in list_of_all_blocks: #DOES THE PLAYER TOUCH THE BOTTOM COLLISION BLOCK
        answer = block.check_collision_bottom_wall(left_x_p = self.x, top_y_p = self.y, 
                                    right_x_p = self.x + self.width, bottom_y_p = self.y + self.height)
        if answer: 
            self.throw = False
            self.column_throw_move = 10
            boxes.append(self)
            return

if answer != True:
    if self.column_throw_move != 0:
        self.x = self.x + 17 * math.cos(self.angle * (math.pi / 180))
        self.y = self.y + 17 * math.sin(self.angle * (math.pi / 180))
        self.column_throw_move -= 1
```
---
### Push box
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
mod.push_box = mod.check_push_box(mod.player, last_side) #BOX PUSH TEST

#що в цій функції(головний кусочок)
if last_side == 1:
    for box in boxes:
        answer = box.check_collision_left_wall(player.x, player.y, 
                                                player.x + player.width, player.y + player.height)
        if answer:
            return True
return False
```
---
### Up a box
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
if keys[pygame.K_q]:
    if player.hide == False and with_box == False:
        for box in boxes: #CHECKING AN ATTEMPT TO UP A BOX 
            answer = box.check_up_the_box(player)
            if answer:
                return_list["with_box"] = True
                return_list["box_player"] = box
```
---
### Resources
#### Ресурси використовуються для проходження рівня
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
answer = self.check_collision_bottom_wall(left_x_p = player.x, top_y_p = player.y, #CHECKING IF THE PLAYER IS TOUCHING THE OBJECT BOTTOM
    right_x_p = player.x + player.width, bottom_y_p = player.y + player.height)
    if answer:
        self.x = 10000
        self.y = 10000
        if self.whatIsThis == "meat": 
            return_list["meat_count"] = meat_count + 1
            return_list["task_meat"] = task_meat - 1
```
---
### Interfaсe
#### Показується вверху ігрового вікна
#### Ось кусочок с коду, с демонстраціей як це працює:
```python
meat = Column_Meat_Egg_Hp_Key(220, 25, 55, 30, "images/resources/meat.png", 0, 32)
interface.append(meat)

#відображення тексту
f1 = pygame.font.Font(None, 32)
text1 = f1.render(f"{self.count}", 1, (255, 255, 255))
screen.blit(text1, (self.x + self.width + 10, self.number_y))
```
---
## <a id="title7">Висновок</a>
Розробивши цю гру я отримав, та удосконалив навички розробки ігор на модулі pygame. 
Озираючись назад я розумію, який шлях я пройшов, щоб закінчити цей проект.
Зараз дивлячись на свій код, я бачу в яких аспектах я удосконалив свое вміння писати код в цілому.
Також в процесі розробки гри я познайомився з TileMapEditor, який допомогаю розробити статичну частину карти.
Попрацював з Figma розробивши у ній дизайн декількох рівней.
Хоч проект ще можно доробити, наприклад розробити ще рівней, все одно він вже гідний для демонстрації,
та викладу на GitHub 