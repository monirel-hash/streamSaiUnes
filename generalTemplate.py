import cv2
import pyaudio
import numpy as np
import subprocess

# Configure video capture
cap = cv2.VideoCapture(0)  # Use the default camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Configure audio capture
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Configure streaming to RTMP server
rtmp_url = "rtmp://your.rtmp.server/your/stream/key"
ffmpeg_cmd = ["ffmpeg",
              "-y",
              "-f", "rawvideo",
              "-pix_fmt", "bgr24",
              "-s", "640x480",
              "-r", "30",
              "-i", "-",
              "-f", "s16le",
              "-ar", "44100",
              "-ac", "1",
              "-i", "-",
              "-c:v", "libx264",
              "-preset", "veryfast",
              "-pix_fmt", "yuv420p",
              "-g", "30",
              "-b:v", "3000k",
              "-c:a", "aac",
              "-b:a", "128k",
              "-f", "flv",
              rtmp_url]

# Start streaming loop
while True:
    # Capture video frame and audio sample
    ret, frame = cap.read()
    audio_data = stream.read(1024)

    # Send video and audio data to FFmpeg process for streaming
    ffmpeg_in = np.array(frame).astype(np.uint8).tobytes()
    ffmpeg_audio_in = np.fromstring(audio_data, dtype=np.int16).tobytes()
    ffmpeg_proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    ffmpeg_proc.stdin.write(ffmpeg_in)
    ffmpeg_proc.stdin.write(ffmpeg_audio_in)
    ffmpeg_proc.communicate()

    # Show video stream on local display
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
stream.stop_stream()
stream.close()
audio.terminate()
