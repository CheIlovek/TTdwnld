from moviepy.editor import VideoFileClip
from datetime import timedelta
import os
import numpy as np


class VidToFrames:
    SAVING_FRAMES_PER_SECOND = 1
    FRAMES_PATH = []

    def __init__(self, save_fps=1):
        self.SAVING_FRAMES_PER_SECOND = save_fps

    def format_timedelta(self, td):
        result = str(td)
        try:
            result, ms = result.split(".")
        except ValueError:
            return result + ".00".replace(":", "-")

        ms = round(int(ms) / 10000)
        return f"{result}.{ms:02}".replace(":", "-")

    def from_video_to_frames(self, video_file):
        self.FRAMES_PATH.clear()
        try:
            video_clip = VideoFileClip(video_file)
        except OSError:
            return ""
        changed_name = False
        fullpath = video_file
        if video_clip.duration > 20:
            changed_name = True
            video_clip = video_clip.subclip(0, 20)
            name = os.path.basename(video_file)
            name = "edtd_" + name
            fullpath = os.path.abspath(video_file)
            fullpath = fullpath.replace(os.path.basename(video_file), name)
            video_clip.write_videofile(fullpath, verbose=False, logger=None)

        filename, _ = os.path.splitext(fullpath)

        if not os.path.isdir(filename):
            os.mkdir(filename)

        saving_frames_per_second = min(video_clip.fps, self.SAVING_FRAMES_PER_SECOND)
        step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second

        for current_duration in np.arange(0, video_clip.duration, step):
            frame_duration_formatted = self.format_timedelta(timedelta(seconds=current_duration)).replace(":", "-")
            frame_filename = os.path.join(filename, f"frame{frame_duration_formatted}.jpg")
            self.FRAMES_PATH.append(frame_filename)
            try:
                video_clip.save_frame(frame_filename, current_duration)
            except OSError:
                return ""
        video_clip.close()
        if changed_name:
            os.remove(video_file)
            return fullpath
        else:
            return video_file
