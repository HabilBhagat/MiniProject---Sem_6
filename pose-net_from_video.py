import torch
import cv2
import time
import argparse

import posenet

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default=101)
parser.add_argument('--cam_id', type=int, default=0)
parser.add_argument('--cam_width', type=int, default=1280)
parser.add_argument('--cam_height', type=int, default=720)
parser.add_argument('--scale_factor', type=float, default=0.7125)
args = parser.parse_args()


def main():
    #  D:\Programming-Github\Sem-6\MiniProject\posenet-pytorch-master\posenet\converter\wget.py
    #  go here and find 
    #       data = json.loads(response.content)
    #  replace with
    #       data = json.loads(response.content.decode('utf-8'))
    model = posenet.load_model(args.model)
    model = model.cuda()
    output_stride = model.output_stride

    cap = cv2.VideoCapture("C:\\Users\\habil\\Pictures\\Camera Roll\\WIN_20200329_15_03_35_Pro.mp4")
    cap.set(3, args.cam_width)
    cap.set(4, args.cam_height)

    start = time.time()
    frame_count = 0
    while True:
        

        try:
            input_image, display_image, output_scale = posenet.read_cap(
                cap, scale_factor=args.scale_factor, output_stride=output_stride)
        except OSError:
            break
        

        with torch.no_grad():
            input_image = torch.Tensor(input_image).cuda()

            heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = model(input_image)

            pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multiple_poses(
                heatmaps_result.squeeze(0),
                offsets_result.squeeze(0),
                displacement_fwd_result.squeeze(0),
                displacement_bwd_result.squeeze(0),
                output_stride=output_stride,
                max_pose_detections=10,
                min_pose_score=0.15)

        keypoint_coords *= output_scale

        
        #overlay_image = posenet.draw_skel_and_kp(
            #display_image, pose_scores, keypoint_scores, keypoint_coords,
            #min_pose_score=0.15, min_part_score=0.1)

        print(keypoint_coords)
        #overlay_image = posenet.draw_skel_and_kp(display_image,[],[],[])

        #cv2.imshow('posenet', overlay_image)
        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print('Average FPS: ', frame_count / (time.time() - start))


if __name__ == "__main__":
    main()
    print(args)