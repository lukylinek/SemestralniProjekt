

def check_goal(ball_pos, pitch_left, pitch_right, goal_top, goal_bottom):
    if ball_pos[0] <= pitch_left and goal_top <= ball_pos[1] <= goal_bottom:
        return "team2"
    elif ball_pos[0] >= pitch_right - 50 and goal_top <= ball_pos[1] <= goal_bottom:
        return "team1"
    return None



