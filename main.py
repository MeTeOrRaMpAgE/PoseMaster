import cv2
import mediapipe as mp
from math import atan2, pi, degrees
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(0)


# Create yoga pose "database"

treepose_sample = [
    38.46935274589811,
    13.941969932743916,
    22.55661817377735,
    28.507977391612446,
    125.20336704067765,
    97.48606388468028,
    36.78828174957272,
    177.0929928050104,
    124.95561541108796,
    179.04508919030698,
]

Upward_Salute_Pose = [
    72.26376560067679,
    76.7826033535801,
    59.12201767760001,
    57.56900857544926,
    84.08331990604727,
    93.37027308020515,
    177.365743406559,
    177.39614381067204,
    176.6252207833334,
    175.03628405077572,
]

warriorPose = [
  171, 85, 170, 80, 150, 130, 119, 179, 111, 136
]

standing = [
    144.70861752904437,
    31.696894069281313,
    136.9566854913852,
    34.38898708404743,
    89.37284225096695,
    93.81684070001228,
    179.4549537188072,
    179.08055311460194,
    167.1792071031823,
    164.7229060781326
]



def calculate_angle(A, B, C):

    Ax, Ay = A[0] - B[0], A[1] - B[1]
    Cx, Cy = C[0] - B[0], C[1] - B[1]
    a = atan2(Ay, Ax)
    c = atan2(Cy, Cx)
    if a < 0:
        a += pi * 2
    if c < 0:
        c += pi * 2
    if a > c:
        angle = pi * 2 + c - a
    else:
        angle = c - a
    angle = degrees(angle)
    if angle > 180:
        angle = 360 - angle
    return angle



def check_angle(samples):
    for i in range(len(samples)):
        if abs(samples[i] - joint_angles[i]) > 20:
            
            return False
    mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(119, 255, 0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(119, 255, 0), thickness=2, circle_radius=2),
        )

    return True

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

         # Render detections
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
        )


        # Extract landmarks
        try:
            
            landmarks = results.pose_landmarks.landmark

            Lshoulder = [
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z,
            ]
            Lelbow = [
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z,
            ]
            Lwrist = [
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z,
            ]
            Rshoulder = [
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z,
            ]
            Relbow = [
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z,
            ]
            Rwrist = [
                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z,
            ]
            Lhip = [
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z,
            ]
            Lknee = [
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z,
            ]
            Lankle = [
                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z,
            ]
            Rhip = [
                landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z,
            ]
            Rknee = [
                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z,
            ]
            Rankle = [
                landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y,
                landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z,
            ]


            joint_angles = (
                calculate_angle(
                    Lshoulder, Lelbow, Lwrist
                ),  # Calculates angle of left elbow
                calculate_angle(
                    Lhip, Lshoulder, Lelbow
                ),  # Calculates angle of left shoulder
                calculate_angle(
                    Rshoulder, Relbow, Rwrist
                ),  # Calculates angle of right elbow
                calculate_angle(
                    Rhip, Rshoulder, Relbow
                ),  # Calculates angle of right shoulder
                calculate_angle(
                    Lknee, Lhip, Rhip
                ),  # Calculates angle of left hip
                calculate_angle(
                    Rknee, Rhip, Lhip
                ),  # Calculates angle of right hip
                calculate_angle(
                    Lhip, Lknee, Lankle
                ),  # Calculates angle of left knee
                calculate_angle(
                    Rhip, Rknee, Rankle
                ),  # Calculates angle of right knee
                calculate_angle(
                    Lshoulder, Lhip, Lknee
                ),  # Calculates outer angle of left hip
                calculate_angle(
                    Rshoulder, Rhip, Rknee
                ),  # Calculates outer angle of right hip
            )

            
            check_angle(warriorPose)
            
        except:
            pass

        cv2.imshow("Mediapipe Feed", image)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
