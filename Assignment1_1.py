mobile_nr = [9,3,0,9,2,7,8,5,3,0]

feature_1 = 42
feature_2 = 77

weight_1 = 0.1 * mobile_nr[-1]
weight_2 = 0.3 * mobile_nr[0]

final_score = (feature_1 * weight_1) + (feature_2 * weight_2)
print(final_score)