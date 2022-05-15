# 좌선(수) 알고리즘 (π*에 가까울 것으로 예측됨)
class LeftHandedRule:

    def __init__(self, cur_x, cur_y, new_x, new_y, reward): #현재 위치, 행동후 바뀐위치, 리워드
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.new_x = new_x
        self.new_y = new_y
        self.reward = reward

    def obsjudge(self, cur_x, cur_y): #현재 위치에서 상하좌우에 장애물이 있는지 확인 (환경정보를 아는게 필요? or 시행착오로 학습?)
        obslst = []
        if done:
            obslst.append(cur_x, cur_y)
        # 스텝이 끝나면 호출되어, 장애물과 부딪쳐 에피소드가 종료된 경우 해당 좌표를 obslist에 추가

    def targetjudge(self): #타겟은 장애물로 취급해서 피해가도록 일단 설계
        targetlst = []
        if reward == goal_reward:
            targetlst.append(cur_x, cur_y)

    def setorient(self, cur_x, cur_y, new_x, new_y): # 두 좌표차이로부터 에이전트가 바라보고 있는 방향을 지정
        z = (new_x - cur_x, new_y - cur_y) # 액션으로 인한 새로운 좌표 - 이전 좌표
        if z == (1, 0):
            orient = 'up'
        elif z == (-1, 0):
            orient = 'down'
        elif z == (0, 1):
            orient = 'left'
        elif z == (0, -1):
            orient = 'right'

    def exceptrule(self, cur_x, cur_y):
        #1. 이동하려는 방향 설정 후, 왼쪽에 targetlst가 있는 경우 왼쪽이동, 오른쪽이동으로 목표 task를 수행
        #2.

    def actionpolicy:
        # 방식 1, 모든 경우에 수에 따라 움직일 방향 직접 지정 (상,하,좌,우, 이동가능 or 장애물)
        # 방식 2, 이동한 방향 기준으로 지난 Action에 따라 움직일 방향 지정 (orientd -> 이전액션에 의해 결정됨)
        '''
        매 스텝 상하좌우에 장애물이나 타겟이 있는지를 확인함
        매 스텝마다 다음으로 이동할 방향을 확인해서 아래 알고리즘대로 액션 정책을 짬
        (좌측에 타겟이 있는 경우 예외적으로 좌측으로 한칸 이동했다 돌아옴)
        (좌측에 장애물이 없으면 -> 좌회전)
        (좌측에 장애물이 있으면 -> 직진)
        (좌측과 앞쪽에 장애물이 있으면 -> 우회전)
        (좌측과 앞쪽과 우측에 장애물이 있으면 -> 뒤로)
        (끝나지 않고 loop를 도는 경우? -> 어쩌지?)
        '''
        if obslit in ()

class Astar:

    def __init__(self, cur_x, cur_y):  # 현재 위치만 받아온다.
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.f = 0 # f는 지나온 길에 대한
        self.g = 0
        self.h = 0
