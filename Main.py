def main():

    sim = Simulator()  # 환경
    files = pd.read_csv("./data/factory_order_train.csv")  # files를 가져와서 학습데이터로 활용

    for epi in range(2):  # len(files)):  <- 2 = 배치 숫자?
        items = list(files.iloc[epi])[0]
        done = False
        i = 0
        obs = sim.reset(epi)
        actions = [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1]

        while done == False:

            i += 1
            next_obs, reward, cumul, done, goal_reward = sim.step(actions[i])

            obs = next_obs

            if (done == True) or (i == (len(actions) - 1)):
                i = 0