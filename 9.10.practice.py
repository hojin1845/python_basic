#9.10.스타크래프트 프로잭트 전반전

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 채력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격력을 증가, 자기 채릭 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소".format(self.name))
        else:
            print("{0} : 채력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# 탱크
class Tank(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        # 시즌모드 : 탱크를 지상에 고졍시켜, 더 높은 파워로 공격 가능./ 이동불가.
        seize_developed = False # 시즈모드 개발여부

        def __init__(self):
            AttackUnit.__init__(self, "탱크", 150, 1, 35)
            self.seize_mode = False

        def set_seize_mode(self):
            if Tank.seize_developed == False:
                return

            # 현재 시즈모드가 아닐때 -> 시즈모드
            if self.seize_mode == False:
                print("{0} : 시즈모드로 전환합니다.".format(self.name))
                self.damage *= 2
                self.seize_mode = True
            # 현재 시즈모드 일때 -> 시즈모드 해재  
            else:
                print("{0} : 시즈모드를 해재합니다.".format(self.name))
                self.damage /= 2
                self.seize_mode = False
    
            

# 드랍십 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
    
    def move (self, location):
        print("[공중 유닛 이동")
        self.fly(self.name, location)

        # 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)


# 레이스
class wraith(FlyableAttackUnit):

    def __init__(self):
        FlyableAttackUnit.__init__("레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해재상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해재
            print("{0} : 클로킹 모드를 해재합니다.".format(self.name))
            self.clocked = False

        else:# 클로킹 모드 해재 -> 모드해재
            print("{0} : 클로킹 모드를 설정 합니다.".format(self.name))
            self.clocked = True


  




        





        
    