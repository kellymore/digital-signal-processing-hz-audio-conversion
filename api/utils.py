import librosa
import soundfile as sf
import tempfile


def change_frequency(audio_path, target_sr, res_type='sinc_best'):
  """Changes the sample rate of an audio file.

  Args:
      audio_path: Path to the audio file.
      target_sr: Target sample rate (Hz).
      res_type: Resample type (string). Defaults to 'sinc_best'.

  Returns:
      Path to the modified audio file.
  """
  y, orig_sr = librosa.load(audio_path)
  y_resampled = librosa.resample(y=y, orig_sr=orig_sr, target_sr=target_sr, res_type=res_type)

  # Create a temporary file for the modified audio
  with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
      sf.write(temp_file.name, y_resampled, target_sr)
  return temp_file.name
