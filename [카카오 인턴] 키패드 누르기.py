def solution(numbers, hand):
    answer = ''
    left_finger = 10
    right_finger = 11
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 11]]

    left_finger_index = []
    right_finger_index = []
    current_number_index = []
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left_finger = i
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            right_finger = i
            answer += 'R'
        else:
            for j in range (4):
                for k in range (3):
                    if left_finger == arr[j][k]:
                        left_finger_index = [j, k]
                    if right_finger == arr[j][k]:
                        right_finger_index = [j, k]
                    if i == arr[j][k]:
                        current_number_index = [j, k]

            left_distance = abs(current_number_index[0] - left_finger_index[0]) + abs(current_number_index[1] - left_finger_index[1])
            right_distance = abs(current_number_index[0] - right_finger_index[0]) + abs(current_number_index[1] - right_finger_index[1])

            if left_distance < right_distance:
                left_finger = i
                answer += 'L'
            elif left_distance > right_distance:
                right_finger = i
                answer += 'R'
            elif left_distance == right_distance:
                answer += hand[0].upper()
                if hand[0] == 'l':
                    left_finger = i
                elif hand[0] == 'r':
                    right_finger = i

    return answer


numbers = [2, 5, 8, 0]
hand = "right"
print(solution(numbers, hand))