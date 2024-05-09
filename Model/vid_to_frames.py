from moviepy.editor import VideoFileClip
from datetime import timedelta
import os
#import numpy as np
from Controller.LimitsChecker import LimitsChecker


class VidToFrames:

    def format_timedelta(self, td):
        result = str(td)
        try:
            result, ms = result.split(".")
        except ValueError:
            return result + ".00".replace(":", "-")

        ms = round(int(ms) / 10000)
        return f"{result}.{ms:02}".replace(":", "-")



    def from_video_to_frames(self, video_file):
        result_paths = []
        try:
            video_clip = VideoFileClip(video_file)
        except OSError:
            return ""

        saving_frames_per_second = min(video_clip.fps, LimitsChecker.FRAMES_PER_SECOND)
        step = 1 / saving_frames_per_second

        for current_duration in range(0,video_clip.duration,step):
            frame_duration_formatted = self.format_timedelta(timedelta(seconds=current_duration)).replace(":", "-")
            frame_filename = os.path.join(LimitsChecker.PATH_TO_SAVE_IMAGES, f"frame{frame_duration_formatted}.jpg")
            result_paths.append(frame_filename)
            try:
                video_clip.save_frame(frame_filename, current_duration)
            except OSError:
                return ""
        video_clip.close()
        return result_paths
